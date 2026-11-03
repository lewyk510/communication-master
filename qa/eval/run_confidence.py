#!/usr/bin/env python3
"""Round 13 confidence-calibration runner.

Replays the Round 8 bombardment gold set (qa/eval/bombard-adjudicated.json —
118 questions, each adjudicated by blind judges) through router_match.assess
and reports:

  1. routing hit@1 — MUST equal keyword-only rank() (assess never reroutes;
     any drift is a hard failure, exit 1)
  2. high-tier precision — accuracy inside the 'high' confidence tier
  3. wrong-route coverage — share of wrong keyword routes flagged 'low'
  4. out-of-scope coverage — share of no-topic questions flagged 'low'

Advisory report otherwise; exit 1 only on routing drift or missing data.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from router_match import assess, rank  # noqa: E402


def main() -> int:
    router = json.loads((ROOT / "router.json").read_text(encoding="utf-8"))
    adj_path = ROOT / "qa/eval/bombard-adjudicated.json"
    if not adj_path.exists():
        print("run_confidence: bombard-adjudicated.json missing")
        return 1
    adj = json.loads(adj_path.read_text(encoding="utf-8"))

    gold = []
    for c in adj["cases"]:
        v = c["verdict"]
        g = c["router"] if v in ("clean", "router_ok_label_noise") else c["judge"]["best"]
        gold.append({"q": c["q"], "gold": g})

    drift = kw_hit = 0
    hi_n = hi_ok = 0
    wrong_total = wrong_flagged = 0
    oos_total = oos_flagged = 0
    by_reason: dict[str, int] = {"weak-keyword": 0, "semantic-disagrees": 0,
                                 "typo-fuzzy-match": 0, "agree": 0}
    for g in gold:
        r = rank(router, g["q"])
        kw_pick = r[0]["id"] if r else None
        a = assess(router, g["q"])
        pick = a["ranked"][0]["id"] if a["ranked"] else None
        if pick != kw_pick or [x["id"] for x in a["ranked"]] != [x["id"] for x in r]:
            drift += 1
        if kw_pick == g["gold"]:
            kw_hit += 1
        if a["confidence"] == "low":
            by_reason[a["reason"]] = by_reason.get(a["reason"], 0) + 1
        if g["gold"] is None:
            oos_total += 1
            if a["confidence"] in ("low", "none"):
                oos_flagged += 1
            continue
        if a["confidence"] == "high":
            hi_n += 1
            if pick == g["gold"]:
                hi_ok += 1
        if kw_pick != g["gold"]:
            wrong_total += 1
            if a["confidence"] == "low":
                wrong_flagged += 1

    print("== Round 13 confidence calibration (bombard gold, n=%d) ==" % len(gold))
    print(f"routing hit@1: {kw_hit}/{len(gold)} = {kw_hit/len(gold):.1%}  "
          f"(must equal keyword-only; drift cases: {drift})")
    if drift:
        print(f"run_confidence: FAIL — assess changed routing for {drift} case(s)")
        return 1
    print(f"high tier:      n={hi_n}  precision={hi_ok}/{hi_n}"
          + (f" = {hi_ok/hi_n:.0%}" if hi_n else ""))
    print(f"wrong routes flagged low: {wrong_flagged}/{wrong_total}"
          + (f" = {wrong_flagged/wrong_total:.0%}" if wrong_total else ""))
    print(f"out-of-scope flagged low/none: {oos_flagged}/{oos_total}"
          + (f" = {oos_flagged/oos_total:.0%}" if oos_total else ""))
    print(f"low-tier reasons: weak-keyword {by_reason['weak-keyword']}, "
          f"semantic-disagrees {by_reason['semantic-disagrees']}, "
          f"typo-fuzzy-match {by_reason['typo-fuzzy-match']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
