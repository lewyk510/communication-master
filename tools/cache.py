#!/usr/bin/env python3
"""Exact-match local query/answer cache for the communication-master KB.

Why: this KB answers *recurring scenarios*. The cheapest query is the one you
already answered. An EXACT-key cache (normalised query) has zero correctness
risk — unlike a semantic cache, it never returns a wrong answer for a
different-but-similar question (see wiki/synthesis/updating-the-kb.md, and
Redis LangCache / GPTCache findings).

Correctness is scoped by a KB revision: the cache stores a content
*fingerprint* of the KB (wiki/**/*.md + router-index.json + cards). If any of
that content changes, `rev` differs and the entry is treated as a MISS
(and `gc` removes it) — staleness is impossible by construction, no TTL needed.

The agent loop:
    key = cache.key(q);  if cache hit -> serve with zero topic-load
    else -> resolve + answer as usual, then `put` the answer + its sources.

Usage (from the skill root):
    python3 tools/cache.py key  "他说'随便'是什么意思"
    python3 tools/cache.py get  "他说'随便'是什么意思" [--allow-stale]
    python3 tools/cache.py put  "他说'随便'是什么意思" "<answer>" --source wiki/concepts/c1-subtext-implicature/core.md
    python3 tools/cache.py stats
    python3 tools/cache.py gc
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "cache"
STORE = CACHE / "answers.json"
PUNCT = re.compile(r"[\s，。！？、；：\"'“”‘’（）()\[\]{}<>《》!?.,;:]+")


def normalize(query: str) -> str:
    return PUNCT.sub("", query.strip().lower())


def fingerprint() -> str:
    """Content hash of the KB surface that a cached answer depends on."""
    h = hashlib.sha256()
    files = sorted(ROOT.glob("wiki/**/*.md")) + [ROOT / "router-index.json", ROOT / "sidecars/cards.json"]
    for p in files:
        if p.is_file():
            h.update(str(p.relative_to(ROOT)).encode())
            h.update(p.read_bytes())
    return h.hexdigest()[:16]


def key(query: str) -> str:
    return hashlib.sha256(normalize(query).encode("utf-8")).hexdigest()[:16]


def load() -> dict:
    if STORE.exists():
        try:
            return json.loads(STORE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def save(db: dict) -> None:
    CACHE.mkdir(exist_ok=True)
    STORE.write_text(json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8")


def put(query: str, answer: str, sources: list[str] | None = None) -> str:
    db = load()
    k = key(query)
    db[k] = {
        "query": query,
        "normalized": normalize(query),
        "answer": answer,
        "sources": sources or [],
        "rev": fingerprint(),
        "created": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    save(db)
    return k


def cmd_key(args):
    print(json.dumps({"key": key(args.query), "rev": fingerprint(),
                      "normalized": normalize(args.query)}, ensure_ascii=False))
    return 0


def cmd_get(args):
    rev = fingerprint()
    entry = load().get(key(args.query))
    if not entry:
        print("MISS (no entry)")
        return 1
    if entry.get("rev") != rev and not args.allow_stale:
        print(f"STALE (entry rev {entry.get('rev')} != current {rev}) — re-answer")
        return 1
    if args.json:
        print(json.dumps(entry, ensure_ascii=False, indent=2))
    else:
        print(entry.get("answer", ""))
        srcs = entry.get("sources", [])
        if srcs:
            print("\n-- sources --")
            for s in srcs:
                print(s)
    return 0


def cmd_put(args):
    k = put(args.query, args.answer, args.source)
    print(f"PUT {k} ({len(load())} entries)")
    return 0


def cmd_stats(args):
    db = load()
    rev = fingerprint()
    fresh = sum(1 for e in db.values() if e.get("rev") == rev)
    print(json.dumps({
        "entries": len(db), "fresh": fresh, "stale": len(db) - fresh,
        "current_rev": rev, "store": str(STORE.relative_to(ROOT)),
    }, ensure_ascii=False, indent=2))
    return 0


def cmd_gc(args):
    db = load()
    rev = fingerprint()
    keep = {k: e for k, e in db.items() if e.get("rev") == rev}
    dropped = len(db) - len(keep)
    save(keep)
    print(f"gc: dropped {dropped} stale, kept {len(keep)}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="exact-match local query/answer cache")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("key"); p.add_argument("query"); p.set_defaults(fn=cmd_key)
    p = sub.add_parser("get"); p.add_argument("query")
    p.add_argument("--allow-stale", action="store_true"); p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_get)
    p = sub.add_parser("put"); p.add_argument("query"); p.add_argument("answer")
    p.add_argument("--source", action="append"); p.set_defaults(fn=cmd_put)
    p = sub.add_parser("stats"); p.set_defaults(fn=cmd_stats)
    p = sub.add_parser("gc"); p.set_defaults(fn=cmd_gc)

    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
