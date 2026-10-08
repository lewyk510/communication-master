#!/usr/bin/env python3
"""Source freshness scan for the communication-master KB.

The KB is an offline snapshot; nothing currently tells you when its evidence
is getting old. This scanner walks raw/<topic>/ captures, reads the
`capture date:` and `source tier:` lines from each capture header, and reports
what is due for a re-crawl. Advisory by default (exit 0); pass --strict to make
stale captures a non-zero exit.

Usage (from the skill root):
    python3 tools/freshness.py                 # summary; stale = older than 18 months
    python3 tools/freshness.py --months 12     # tighten the window
    python3 tools/freshness.py --strict        # exit 1 if anything is stale
    python3 tools/freshness.py --all           # list every stale capture
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
EXTS = {".md", ".html", ".txt", ".json"}
DATE_RE = re.compile(r"capture date:\s*(\d{4}-\d{2}-\d{2})", re.IGNORECASE)
TIER_RE = re.compile(r"source tier:\s*([123])", re.IGNORECASE)


def read_header(path: Path) -> str:
    # headers are at the top; JSON snapshots have no header, so only peek a bit
    try:
        return path.read_text(encoding="utf-8", errors="ignore")[:2000]
    except OSError:
        return ""


def capture_date(path: Path) -> tuple[dt.date | None, str]:
    head = read_header(path)
    m = DATE_RE.search(head)
    if m:
        try:
            return dt.date.fromisoformat(m.group(1)), "header"
        except ValueError:
            pass
    # fallback: file mtime (JSON search snapshots generally lack a header)
    try:
        ts = path.stat().st_mtime
        return dt.date.fromtimestamp(ts), "mtime"
    except OSError:
        return None, "unknown"


def capture_tier(path: Path) -> str:
    m = TIER_RE.search(read_header(path))
    return m.group(1) if m else "?"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--months", type=int, default=18, help="staleness window in months (default 18)")
    ap.add_argument("--strict", action="store_true", help="exit 1 if any capture is stale")
    ap.add_argument("--all", action="store_true", help="list every stale capture")
    args = ap.parse_args()

    if not RAW.is_dir():
        print(f"freshness: no raw/ directory at {RAW}")
        return 0

    cutoff = dt.date.today() - dt.timedelta(days=args.months * 31)
    files = sorted(p for p in RAW.rglob("*") if p.is_file() and p.suffix.lower() in EXTS)

    tiers = {"1": 0, "2": 0, "3": 0, "?": 0}
    dated: list[tuple[dt.date, str, Path, str]] = []
    for p in files:
        d, _how = capture_date(p)
        tiers[capture_tier(p)] += 1
        if d:
            dated.append((d, capture_tier(p), p, _how))

    print(f"freshness: {len(files)} captures under raw/, "
          f"{len(dated)} dated, window = {args.months} months (cutoff {cutoff})")
    print(f"  tiers: 1={tiers['1']} 2={tiers['2']} 3={tiers['3']} unknown={tiers['?']}")

    if dated:
        dated.sort()
        print(f"  oldest: {dated[0][0]} ({dated[0][2].relative_to(ROOT)})")
        print(f"  newest: {dated[-1][0]} ({dated[-1][2].relative_to(ROOT)})")

    stale = [row for row in dated if row[0] < cutoff]
    if not stale:
        print("  stale: none")
        return 0

    # group stale captures by topic folder
    by_topic: dict[str, int] = {}
    for _d, _t, p, _how in stale:
        topic = p.relative_to(RAW).parts[0] if len(p.relative_to(RAW).parts) > 1 else "(loose)"
        by_topic[topic] = by_topic.get(topic, 0) + 1

    print(f"  stale: {len(stale)} capture(s) across {len(by_topic)} topic(s) — re-crawl candidates")
    shown = stale if args.all else stale[:15]
    for d, t, p, how in shown:
        print(f"    {d}  tier {t}  {p.relative_to(ROOT)}  [{how}]")
    if not args.all and len(stale) > len(shown):
        print(f"    … and {len(stale) - len(shown)} more (use --all)")

    if args.strict:
        print("freshness: STRICT — stale captures present")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
