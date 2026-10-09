#!/usr/bin/env python3
"""Retrieval + token eval for the communication-master skill.

For every scenario in qa/eval/scenarios.json this runs the *shipped* resolver
(tools/router_match.py), reports whether the winner is one of the expected
topics (hit@1), and measures the token cost of the light path (card) vs the
full path (core + language lane). It can also write the assembled KB context
for each scenario, which is what an answer-generation experiment consumes.

Answer quality is judged separately against `rubric_by_type` (see qa/eval/REPORT.md).

Usage (from the skill root):
    python3 tools/eval.py                       # scorecard
    python3 tools/eval.py --json
    python3 tools/eval.py --context-out DIR      # also write <id>.md KB context files
    python3 tools/eval.py --strict               # exit 1 if any scenario misses
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import router_match
from token_cost import toks

CJK = re.compile(r"[\u3000-\u9fff\uff00-\uffef]")


def load_cards() -> dict:
    p = ROOT / "sidecars" / "cards.json"
    return json.loads(p.read_text(encoding="utf-8")).get("cards", {}) if p.exists() else {}


def rank_position(ranked: list[dict], expected: list[str]) -> int | None:
    for i, r in enumerate(ranked, 1):
        if r["id"] in expected:
            return i
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description="retrieval + token eval over qa/eval/scenarios.json")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--context-out", help="write assembled KB context per scenario to this dir")
    ap.add_argument("--strict", action="store_true", help="exit 1 if any scenario misses at rank 1")
    args = ap.parse_args()

    spec = json.loads((ROOT / "qa/eval/scenarios.json").read_text(encoding="utf-8"))
    index = router_match.load_index()
    cards = load_cards()
    ctx_dir = Path(args.context_out) if args.context_out else None
    if ctx_dir:
        ctx_dir.mkdir(parents=True, exist_ok=True)

    rows = []
    misses = 0
    for sc in spec["scenarios"]:
        ranked = router_match.rank(index, sc["prompt"])
        top = ranked[0] if ranked else None
        top_id = top["id"] if top else None
        pos = rank_position(ranked, sc["expect_topics"])
        hit1 = pos == 1
        if not hit1:
            misses += 1
        card_tok = toks(json.dumps(cards.get(top_id, {}), ensure_ascii=False)) if top_id else 0
        core_tok = lane_tok = 0
        dir_path = ROOT / top["dir"] if top else None
        if dir_path and dir_path.is_dir():
            core = dir_path / "core.md"
            lane = dir_path / f"{sc['lang']}.md"
            core_tok = toks(core.read_text(encoding="utf-8", errors="ignore")) if core.exists() else 0
            lane_tok = toks(lane.read_text(encoding="utf-8", errors="ignore")) if lane.exists() else 0
        rows.append({
            "id": sc["id"], "type": sc["type"], "lang": sc["lang"],
            "top": top_id, "expected": sc["expect_topics"], "rank": pos, "hit@1": hit1,
            "card_tok": card_tok, "full_tok": core_tok + lane_tok,
        })
        if ctx_dir and dir_path and dir_path.is_dir():
            parts = [f"# {sc['id']}  ({sc['type']}, {sc['lang']})",
                     f"\n## Prompt\n{sc['prompt']}",
                     f"\n## Resolved topic\n{top_id}  ({top['dir']})"]
            for fn in ("core.md", f"{sc['lang']}.md"):
                p = dir_path / fn
                if p.exists():
                    parts.append(f"\n## KB: {top['dir']}/{fn}\n\n{p.read_text(encoding='utf-8', errors='ignore')}")
            (ctx_dir / f"{sc['id']}.md").write_text("\n".join(parts), encoding="utf-8")

    n = len(rows)
    hit = sum(1 for r in rows if r["hit@1"])
    avg_card = sum(r["card_tok"] for r in rows) // max(1, n)
    avg_full = sum(r["full_tok"] for r in rows) // max(1, n)

    if args.json:
        print(json.dumps({"scenarios": rows, "hit@1": f"{hit}/{n}",
                          "avg_card_tok": avg_card, "avg_full_tok": avg_full}, ensure_ascii=False, indent=2))
    else:
        print(f"eval: {n} scenario(s) — retrieval hit@1 {hit}/{n}")
        for r in rows:
            flag = "OK " if r["hit@1"] else ("r%d" % r["rank"] if r["rank"] else "MISS")
            print(f"  [{flag:>4}] {r['id']:<18} -> {r['top']}  (want {r['expected']})"
                  f"  card~{r['card_tok']} full~{r['full_tok']}")
        print(f"  avg tokens: card ~{avg_card}  |  full ~{avg_full}")
        print("  answer quality: graded against qa/eval/scenarios.json rubric_by_type")

    if args.strict and misses:
        print(f"eval: STRICT — {misses} scenario(s) missed at rank 1")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
