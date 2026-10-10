#!/usr/bin/env python3
"""Shared router scoring for the communication-master KB.

Single source of truth for the documented matcher (router.json.matcher.scoring):
latin = case-insensitive word-boundary, cjk = substring; score = sum of matched
trigger lengths; medium/channel tokens count as +1 only; highest wins; ties
prefer an engine (playbook) then the earlier entry; a dead-end query (zero hits)
falls back to within-1-edit CJK matching for single-typo tolerance.

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


def _eng(e: dict) -> int:
    """Engine (playbook) flag for tie-breaks; works on router.json and the index."""
    return e.get("eng", 1 if e.get("type") == "playbook" else 0)


# Generic function phrases must not seed typo-fuzzy matching (e.g. 怎么办 ~ 怎么回).
_FUZZY_STOP = {"怎么办", "怎么回", "怎么样", "为什么", "什么时候", "什么", "怎样",
               "如何", "多少", "哪里", "哪个", "可以吗", "是不是", "有没有"}


# Question-frame triggers: an engine does NOT win a tie on these alone.
_GENERIC = {"什么意思", "啥意思", "代表什么", "what did they mean",
            "what do they mean", "interpret", "maksud dia", "apa maksud"}


def _prio(e: dict, matched: list[str]) -> int:
    """Tie-break priority: a playbook wins a tie only via a non-generic trigger."""
    return 1 if _eng(e) and any(m not in _GENERIC for m in matched) else 0


def _edit1(a: str, b: str) -> bool:
    """True if a and b are within Levenshtein distance 1 (single typo)."""
    if a == b:
        return True
    if abs(len(a) - len(b)) > 1:
        return False
    if len(a) == len(b):
        return sum(x != y for x, y in zip(a, b)) == 1
    short, long = (a, b) if len(a) < len(b) else (b, a)
    i = j = diff = 0
    while i < len(short) and j < len(long):
        if short[i] != long[j]:
            diff += 1
            if diff > 1:
                return False
            j += 1
        else:
            i += 1
            j += 1
    return True


def _fuzzy_hits(entries: list[dict], ql: str) -> list[dict]:
    """Dead-end-only typo tolerance for CJK triggers (len>=2).

    Fires ONLY when exact matching found nothing. Slides a window the length of
    each CJK trigger across the query and accepts a within-1-edit window. Latin
    triggers are skipped (word-boundary typos are handled by aliases instead).
    """
    out: list[dict] = []
    for i, e in enumerate(entries):
        score = 0
        matched: list[str] = []
        for trig in e.get("triggers", []):
            tl = trig.lower()
            if len(tl) < 2 or tl.isascii() or tl in _FUZZY_STOP:
                continue
            w = len(tl)
            for pos in range(len(ql) - w + 1):
                if _edit1(tl, ql[pos:pos + w]):
                    score += w
                    matched.append(trig)
                    break
        if score:
            out.append({
                "id": e["id"],
                "dir": e.get("dir") or (e.get("paths") or {}).get("core"),
                "score": score,
                "matched": matched,
                "scenarios": e.get("scenarios", []),
                "eng": _prio(e, matched),
                "order": i,
                "fuzzy": True,
            })
    return out


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
                "eng": _prio(e, matched),
                "order": i,
            })
    if not out:
        out = _fuzzy_hits(entries, ql)
    out.sort(key=lambda r: (-r["score"], -r.get("eng", 0), r["order"]))
    return out


def resolve(index: dict, query: str) -> dict | None:
    ranked = rank(index, query)
    return ranked[0] if ranked else None


def resolve_intent(index: dict, query: str) -> dict | None:
    """Layer-1.5 coarse-read fallback (``router.json.intents``).

    Used ONLY when ``rank`` finds no entry, so a clear-intent question that
    happens to use no exact trigger still routes to the right engine instead of
    dead-ending. ASCII patterns are regex (case-insensitive); non-ASCII patterns
    are substring matches. First matching pattern in declaration order wins.
    """
    intents = index.get("intents")
    if not isinstance(intents, dict):
        return None
    for name, spec in intents.items():
        if name == "note" or not isinstance(spec, dict):
            continue
        for pat in spec.get("patterns", []):
            if not pat:
                continue
            hit = (re.search(pat, query, re.IGNORECASE) is not None
                   if pat.isascii() else (pat in query))
            if hit:
                return {
                    "intent": name,
                    "dir": spec.get("dir"),
                    "engine": spec.get("engine"),
                    "pattern": pat,
                }
    return None
