#!/usr/bin/env python3
"""One-command local resolver for the communication-master KB.

Ties the load tiers together so the agent (or a human) does not load them all:
  1. exact cache  -> a recurring question answers with zero topic-load
  2. router match -> resolve the question to a topic (shared scorer)
  3. digest card  -> print that topic's ~400-tok card (triage / light answer)
  4. --full       -> escalate to core.md + a language lane

No network, no API. Exit code is 0 even on "NO MATCH" (that is an answer:
load 00-how-to-use.md and ask one clarifying question).

Usage (from the skill root):
    python3 tools/ask.py "<question>" [--lang auto|zh|en|ms] [--full]
                                       [--json] [--no-cache] [--save "<answer>"]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import cache as answer_cache
import router_match

CJK = re.compile(r"[\u3000-\u9fff\uff00-\uffef]")
MS_HINTS = (
    "macam", "nak", "tak", "boleh", "apa", "saya", "jangan", "bagaimana", "kenapa",
    "minta", "maaf", "sila", "awak", "tidak", "yang", "untuk", "dengan", "mahu",
    "sudah", "belum", "terima", "kasih", "bila", "mana", "siapa",
)
LANGS = ("zh", "en", "ms")


def detect_lang(query: str, want: str) -> str:
    if want != "auto":
        return want if want in LANGS else "zh"
    if CJK.search(query):
        return "zh"
    low = query.lower()
    if sum(1 for w in MS_HINTS if re.search(rf"\b{w}\b", low)) >= 2:
        return "ms"
    return "en"


def load_cards() -> dict:
    p = ROOT / "sidecars" / "cards.json"
    if not p.exists():
        return {}
    return json.loads(p.read_text(encoding="utf-8")).get("cards", {})


def emit(result: dict, as_json: bool) -> None:
    if as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return
    src = result["source"]
    if src == "cache":
        print(f"[cache hit] {result['question']}")
        print(result["answer"])
        return
    if src == "intent":
        print(f"[intent->engine] {result['question']}")
        print(f"  intent   {result['intent']} (matched '{result['pattern']}')")
        print(f"  engine   {result['engine']}  {result['dir']}")
        card = result.get("card") or {}
        if card.get("tldr"):
            print(f"  TL;DR    {card['tldr']}")
        print("  -> keyword routing found nothing; coarse-read intent matched. Follow the engine in that dir.")
        return
    if src == "no-match":
        print(f"[NO MATCH] {result['question']}")
        print(f"  fallback: {result.get('fallback', '')}")
        print("  -> load wiki/synthesis/00-how-to-use.md and ask ONE clarifying question.")
        return
    print(f"[resolved] {result['id']}  (score {result['score']}, lang {result['lang']})")
    print(f"  dir      {result['dir']}")
    if result.get("title"):
        print(f"  title    {result['title']}")
    if result.get("matched"):
        print(f"  matched  {', '.join(result['matched'][:8])}")
    if result.get("runners_up"):
        print(f"  also     {', '.join(result['runners_up'])}")
    card = result.get("card") or {}
    if card.get("tldr"):
        print(f"\n  TL;DR    {card['tldr']}")
    if card.get("signals"):
        print("  signals  " + "; ".join(card["signals"][:10]))
    if result.get("lane"):
        print(f"\n  card may be enough; --full loads {result['core']} + {result['lane']}")
    if result.get("full"):
        print("\n" + "=" * 60 + "\n" + result["full"])
    if result.get("saved"):
        print(f"\n[saved] cached answer under key {result['saved']}")


def main() -> int:
    ap = argparse.ArgumentParser(description="resolve a question (cache -> route -> card -> full)")
    ap.add_argument("question")
    ap.add_argument("--lang", default="auto", help="auto|zh|en|ms (default auto)")
    ap.add_argument("--full", action="store_true", help="also print core.md + the language lane")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-cache", action="store_true")
    ap.add_argument("--save", metavar="ANSWER", help="store ANSWER for this question in the exact cache")
    args = ap.parse_args()

    q = args.question
    lang = detect_lang(q, args.lang)
    result: dict = {"question": q, "lang": lang}

    if not args.no_cache:
        rev = answer_cache.fingerprint()
        entry = answer_cache.load().get(answer_cache.key(q))
        if entry and entry.get("rev") == rev:
            result.update({"source": "cache", "answer": entry["answer"],
                           "sources": entry.get("sources", []), "rev": rev})
            emit(result, args.json)
            return 0
        if entry:
            result["cache"] = "stale (KB changed since cached) — re-answered"

    index = router_match.load_index()
    ranked = router_match.rank(index, q)
    if not ranked:
        intent = router_match.resolve_intent(index, q)
        if intent:
            key = (intent.get("dir") or "").rstrip("/").split("/")[-1]
            result.update({
                "source": "intent",
                "intent": intent["intent"],
                "engine": intent["engine"],
                "dir": intent["dir"],
                "pattern": intent["pattern"],
                "card": load_cards().get(key, {}),
            })
            emit(result, args.json)
            return 0
        result.update({"source": "no-match", "fallback": index.get("fallback", "")})
        emit(result, args.json)
        return 0

    top = ranked[0]
    card = load_cards().get(top["id"], {})
    dir_path = ROOT / top["dir"]
    core = dir_path / "core.md"
    lane = dir_path / f"{lang}.md"
    result.update({
        "source": "kb",
        "id": top["id"],
        "title": card.get("title", ""),
        "score": top["score"],
        "matched": top["matched"],
        "dir": top["dir"],
        "scenarios": top["scenarios"],
        "card": card,
        "runners_up": [r["id"] for r in ranked[1:4]],
        "core": str(core.relative_to(ROOT)) if core.exists() else None,
        "lane": str(lane.relative_to(ROOT)) if lane.exists() else None,
    })

    if args.full:
        parts = []
        for p in (core, lane):
            if p.exists():
                parts.append(p.read_text(encoding="utf-8"))
        result["full"] = "\n\n".join(parts)

    if args.save:
        result["saved"] = answer_cache.put(q, args.save, [result.get("core"), result.get("lane")])

    emit(result, args.json)
    return 0


if __name__ == "__main__":
    sys.exit(main())
