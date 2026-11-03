#!/usr/bin/env python3
"""Semantic agreement check for the router (Round 13).

A topic-level BM25 index over each entry's triggers (x3) plus its digest card
(tldr x2 + signals). It never picks the route — ``router_match.rank`` does that.
It provides the second opinion ``router_match.assess`` compares against, so a
weak or disputed keyword route is flagged low-confidence instead of silently
returning a wrong topic. Pure stdlib, ~6 ms to build for 46 topics.

Measured on the Round 8 bombardment gold set (qa/eval/bombard-adjudicated.json,
118 adjudicated questions): keyword routing alone is 48.3% correct on free-form
text; when this index disagrees with the keyword winner (or the keyword score is
weak), the route is wrong ~2 out of 3 times — which is exactly what the
low-confidence flag needs to catch. See qa/eval/CONFIDENCE-REPORT.md.
"""
from __future__ import annotations

import json
import math
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent

K1 = 1.5
B = 0.6
TRIGGER_WEIGHT = 3
TLDR_WEIGHT = 2


def _tok(text: str) -> list[str]:
    """Lowercased latin words + CJK character bigrams (no segmenter needed)."""
    out: list[str] = re.findall(r"[a-z0-9']+", text.lower())
    for run in re.findall(r"[\u3400-\u9fff\uf900-\ufaff]+", text):
        if len(run) == 1:
            out.append(run)
        else:
            out += [run[i:i + 2] for i in range(len(run) - 1)]
    return out


class SemIndex:
    def __init__(self, index: dict[str, Any], cards: dict[str, Any] | None = None):
        cards = cards or {}
        self.order: list[str] = []
        self.tf: dict[str, dict[str, int]] = {}
        self.len: dict[str, int] = {}
        df: defaultdict[str, int] = defaultdict(int)
        for e in index.get("entries", []):
            tid = e["id"]
            tl: list[str] = []
            for t in e.get("triggers", []):
                tl += _tok(t) * TRIGGER_WEIGHT
            card = cards.get(tid, {})
            tl += _tok(card.get("tldr", "")) * TLDR_WEIGHT
            tl += _tok(" ".join(card.get("signals", [])))
            self.order.append(tid)
            counts: dict[str, int] = defaultdict(int)
            for t in tl:
                counts[t] += 1
            self.tf[tid] = dict(counts)
            self.len[tid] = len(tl)
            for t in counts:
                df[t] += 1
        n = max(len(self.order), 1)
        self.idf = {t: math.log((n - d + 0.5) / (d + 0.5) + 1) for t, d in df.items()}
        self.avg = (sum(self.len.values()) / n) if n else 1.0

    def rank(self, query: str) -> list[tuple[str, float]]:
        qt = _tok(query)
        pos = {tid: i for i, tid in enumerate(self.order)}
        out: list[tuple[str, float]] = []
        for tid in self.order:
            s = 0.0
            for t in qt:
                f = self.tf[tid].get(t, 0)
                if not f:
                    continue
                s += self.idf[t] * f * (K1 + 1) / (f + K1 * (1 - B + B * self.len[tid] / self.avg))
            out.append((tid, s))
        out.sort(key=lambda x: (-x[1], pos[x[0]]))
        return out

    def top(self, query: str) -> tuple[str | None, float]:
        r = self.rank(query)
        if not r or r[0][1] <= 0:
            return (None, 0.0)
        return (r[0][0], r[0][1])


def load_cards() -> dict[str, Any]:
    p = ROOT / "sidecars" / "cards.json"
    if not p.exists():
        return {}
    return json.loads(p.read_text(encoding="utf-8")).get("cards", {})


_cache: dict[int, tuple[dict[str, Any], "SemIndex"]] = {}


def for_index(index: dict[str, Any]) -> SemIndex:
    """Semantic index for a router index dict, cached by object identity, so
    ``assess(router_dict, q)`` scores semantics against the same entries it
    ranked (not whatever a singleton happened to load first). The dict itself
    is held in the cache so its id() can never be reused by a new dict."""
    held, cached = _cache.get(id(index), (None, None))
    if held is not index or cached is None:
        cached = SemIndex(index, load_cards())
        _cache[id(index)] = (index, cached)
    return cached
