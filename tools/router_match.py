#!/usr/bin/env python3
"""Shared router scoring for the communication-master KB.

Single source of truth for the documented matcher (router.json.matcher.scoring):
latin = case-insensitive word-boundary, cjk = substring; score = sum of matched
trigger lengths; medium/channel tokens count as +1 only; highest wins, ties go
to the earlier entry.

Used by both qa/router-smoke.py (the recall gate) and tools/ask.py (the runtime
resolver), so the gate validates exactly what the resolver runs.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _latin_hit(tl: str, ql: str) -> bool:
    """Word-boundary match for ASCII triggers (router.json.matcher.latin).

    Only ASCII ``[a-z0-9]`` count as word characters, so a latin trigger still
    matches when it sits directly against CJK (e.g. ``用whatsapp聊``), while
    ``PR`` no longer matches inside ``proposal``.
    """
    return re.search(r"(?<![a-z0-9])" + re.escape(tl) + r"(?![a-z0-9])", ql) is not None


def load_index(path: str | Path | None = None) -> dict:
    p = Path(path) if path else ROOT / "router-index.json"
    return json.loads(p.read_text(encoding="utf-8"))


def rank(index: dict, query: str) -> list[dict]:
    entries = index["entries"]
    medium = {t.lower() for t in index.get("matcher", {}).get("medium_tokens", [])}
    ql = query.lower()
    out: list[dict] = []
    for i, e in enumerate(entries):
        score = 0
        matched: list[str] = []
        for trig in e.get("triggers", []):
            tl = trig.lower()
            if not tl:
                continue
            hit = _latin_hit(tl, ql) if tl.isascii() else (tl in ql)
            if hit:
                score += 1 if tl in medium else len(tl)
                matched.append(trig)
        if score:
            out.append({
                "id": e["id"],
                "dir": e.get("dir") or (e.get("paths") or {}).get("core"),
                "score": score,
                "matched": matched,
                "scenarios": e.get("scenarios", []),
                "order": i,
            })
    out.sort(key=lambda r: (-r["score"], r["order"]))
    return out


def resolve(index: dict, query: str) -> dict | None:
    ranked = rank(index, query)
    return ranked[0] if ranked else None
