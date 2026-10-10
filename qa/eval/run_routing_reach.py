#!/usr/bin/env python3
"""Round 7 routing reachability runner.

Replays qa/eval/routing-reach.json through the SAME scorer the resolver uses
(tools/router_match.rank) and reports hit-rate overall and per category, plus
misses and (none)-case false positives. Advisory: prints a report, always exit 0
unless the data file is missing.
"""
from __future__ import annotations
import json, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from router_match import rank  # noqa: E402


def main() -> int:
    router = json.loads((ROOT / "router.json").read_text(encoding="utf-8"))
    data = json.loads((ROOT / "qa/eval/routing-reach.json").read_text(encoding="utf-8"))
    cases = data["cases"]

    hit = defaultdict(int)
    tot = defaultdict(int)
    misses = []
    fps = []
    for c in cases:
        q, exp, cat = c["q"], c["expect"], c["cat"]
        ranked = rank(router, q)
        got = ranked[0]["id"] if ranked else None
        score = ranked[0]["score"] if ranked else 0
        if exp == "(none)":
            if got is None:
                hit[cat] += 1
            else:
                fps.append((q, got, score))
            tot[cat] += 1
            continue
        tot[cat] += 1
        if got == exp:
            hit[cat] += 1
        else:
            misses.append((q, exp, got, score, cat))

    def pct(a, b):
        return f"{100*a//b}% ({a}/{b})" if b else "n/a"

    print("== Round 7 routing reachability ==")
    print(f"overall: {pct(sum(hit.values()), sum(tot.values()))}")
    print("\n-- per category --")
    order = data["meta"].get("categories") or sorted(tot)
    for cat in order:
        if cat in tot:
            print(f"  {cat:12} {pct(hit[cat], tot[cat])}")

    if misses:
        print(f"\n-- misses ({len(misses)}) --")
        for q, exp, got, score, cat in misses:
            print(f"  [{cat}] {q!r}\n        want {exp}, got {got} (score {score})")
    if fps:
        print(f"\n-- (none)-case false positives ({len(fps)}) --")
        for q, got, score in fps:
            print(f"  {q!r} -> {got} (score {score})")
    if not misses and not fps:
        print("\nall reach cases resolved as expected.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
