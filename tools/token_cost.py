#!/usr/bin/env python3
"""Token-cost report for the communication-master KB.

Estimates the token footprint of the artifacts an agent loads, so optimisations
(compact router, digests, caches) can be measured instead of guessed.

Heuristic: CJK chars counted as 1 token each; other chars as ~4 chars/token.
Good enough for relative comparisons; not a real tokenizer.

Usage (from the skill root):
    python3 tools/token_cost.py
    python3 tools/token_cost.py --json
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CJK = re.compile(r"[\u3000-\u9fff\uff00-\uffef]")


def toks(text: str) -> int:
    cjk = len(CJK.findall(text))
    return cjk + (len(text) - cjk) // 4


def ftoks(path: str | Path) -> int:
    try:
        return toks(Path(path).read_text(encoding="utf-8", errors="ignore"))
    except OSError:
        return 0


def main() -> int:
    as_json = "--json" in sys.argv

    wiki = glob.glob(str(ROOT / "wiki/**/*.md"), recursive=True)
    raw = [f for f in glob.glob(str(ROOT / "raw/**/*"), recursive=True) if os.path.isfile(f)]
    cores = glob.glob(str(ROOT / "wiki/*/*/core.md"))
    lanes = glob.glob(str(ROOT / "wiki/*/*/zh.md"))

    fixed = ftoks(ROOT / "SKILL.md") + ftoks(ROOT / "router.json") + ftoks(ROOT / "wiki/synthesis/00-how-to-use.md")
    fixed_compact = (
        ftoks(ROOT / "SKILL.md")
        + ftoks(ROOT / "router-index.json")
        + ftoks(ROOT / "wiki/synthesis/00-how-to-use.md")
    )
    avg_core = sum(ftoks(f) for f in cores) // max(1, len(cores))
    avg_lane = sum(ftoks(f) for f in lanes) // max(1, len(lanes))

    cards_tok = ftoks(ROOT / "sidecars/cards.json")
    n_cards = 0
    if (ROOT / "sidecars/cards.json").exists():
        try:
            n_cards = len(json.loads((ROOT / "sidecars/cards.json").read_text(encoding="utf-8")).get("cards", {}))
        except (json.JSONDecodeError, OSError):
            n_cards = 0
    avg_card = cards_tok // max(1, n_cards)

    report = {
        "router_json": ftoks(ROOT / "router.json"),
        "router_index_json": ftoks(ROOT / "router-index.json") if (ROOT / "router-index.json").exists() else None,
        "skill_md": ftoks(ROOT / "SKILL.md"),
        "how_to_use": ftoks(ROOT / "wiki/synthesis/00-how-to-use.md"),
        "index_md": ftoks(ROOT / "index.md"),
        "avg_core_md": avg_core,
        "avg_one_lane": avg_lane,
        "cards_json_total": cards_tok,
        "cards_count": n_cards,
        "avg_card": avg_card,
        "fixed_overhead_router": fixed,
        "fixed_overhead_compact": fixed_compact,
        "per_query_card_light": fixed_compact + avg_card,
        "per_query_full_router": fixed + avg_core + avg_lane,
        "whole_wiki": sum(ftoks(f) for f in wiki),
        "whole_raw": sum(ftoks(f) for f in raw),
    }

    if as_json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return 0

    print("token-cost (heuristic: CJK=1 tok/char, latin~4 char/tok)")
    print(f"  router.json                 {report['router_json']:>8}")
    if report["router_index_json"] is not None:
        print(f"  router-index.json (compact) {report['router_index_json']:>8}")
    print(f"  SKILL.md                    {report['skill_md']:>8}")
    print(f"  00-how-to-use.md            {report['how_to_use']:>8}")
    print(f"  index.md                    {report['index_md']:>8}")
    print(f"  avg core.md                 {report['avg_core_md']:>8}")
    print(f"  avg one lane                {report['avg_one_lane']:>8}")
    if report["cards_count"]:
        print(f"  cards.json ({report['cards_count']} cards)  {report['cards_json_total']:>8}")
        print(f"  avg card (light load)       {report['avg_card']:>8}")
    print(f"  ---- per query ----")
    print(f"  fixed (SKILL+router+how-to) {report['fixed_overhead_router']:>8}")
    print(f"  compact fixed (SKILL+idx)   {report['fixed_overhead_compact']:>8}")
    print(f"  light: compact fixed + card {report['per_query_card_light']:>8}")
    print(f"  full:  + avg resolved topic {report['per_query_full_router']:>8}")
    print(f"  ---- totals (should NOT be loaded) ----")
    print(f"  whole wiki/                 {report['whole_wiki']:>8}")
    print(f"  whole raw/                  {report['whole_raw']:>8}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
