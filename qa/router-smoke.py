#!/usr/bin/env python3
"""Router recall smoke-test for the communication-master KB.

lint_kb.py checks *structure* but never checks that a real user phrasing
resolves to the right topic. This script is the recall gate: it replays a
curated set of phrasings (zh / en / ms) through the documented router
scoring and asserts the winner.

Documented scoring (router.json.matcher.scoring):
  - trigger match: latin = case-insensitive word-boundary; cjk = substring
  - score      = sum of matched trigger lengths
  - medium/channel tokens (matcher.medium_tokens) count as +1 only
  - matching   = case-insensitive everywhere (normalise latin to lowercase)
  - highest wins; ties -> earlier entry in entries[]

Run from the skill root:  python3 qa/router-smoke.py
Exit code 0 = all must-pass cases green; 1 = a regression.
KNOWN_GAPS are reported as warnings (not regressions) so they stay visible
without breaking the build.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROUTER = ROOT / "router.json"

sys.path.insert(0, str(ROOT / "tools"))
from router_match import rank, resolve_intent  # noqa: E402  (shared scorer)

# (query, expected topic id)  — must resolve exactly. Covers every cluster and
# all three lanes; includes the reviewer round-2 regressions.
CASES: list[tuple[str, str]] = [
    # --- S1 decode / subtext engine + concept
    ("潜台词是什么意思", "p2-subtext-decoder"),
    ("你开心就好是什么意思", "p2-subtext-decoder"),
    ("他说'我没事'是什么意思", "p2-subtext-decoder"),
    ("他是不是在PUA我", "c9-manipulation-defense"),
    # --- workplace / power
    ("怎么跟老板谈加薪", "sc1-workplace-power"),
    ("同事抢我功劳怎么办", "sc1-workplace-power"),
    # --- new scenarios (reviewer round-2 recall regressions) ---
    ("房东不退押金怎么办", "sc17-landlord-tenant"),
    ("朋友父亲过世了，怎么发慰问消息", "sc16-condolence-grief"),
    ("奶奶过世了怎么安慰我妈", "sc16-condolence-grief"),
    ("uncle passed away what do I text", "sc16-condolence-grief"),
    ("takziah 怎么跟马来同事说", "sc16-condolence-grief"),
    ("macam mana nak cakap takziah", "sc16-condolence-grief"),
    ("帛金要包多少钱", "sc16-condolence-grief"),
    ("医生说我需要手术，要不要问第二意见", "sc18-medical-communication"),
    ("抖音直播弹幕有人骂我怎么办", "sc19-live-streaming"),
    # --- digital messaging / formal writing / interviews / AI ---
    ("微信上他突然已读不回怎么办", "sc7-digital-messaging"),
    ("商家不退款我要写投诉信", "p3-formal-writing"),
    ("cara tulis surat rasmi", "p3-formal-writing"),
    ("面试被问缺点怎么答", "sc8-job-interviews"),
    ("怎么让 ChatGPT 帮我写周报", "p4-ai-prompting"),
    # --- culture / mediation / friends / hard conversations / public speaking ---
    ("马来西亚华人过年送礼有什么讲究", "cu2-malaysia-chinese"),
    ("邻居噪音纠纷找谁调解", "sc13-mediation"),
    ("朋友借钱不还怎么开口", "sc6-friends-social"),
    ("how to say no politely", "sc4-hard-conversations"),
    ("怎么拒绝推销电话", "sc4-hard-conversations"),
    ("public speaking 紧张怎么办", "c16-public-speaking"),
    # --- matcher regressions: latin = word-boundary (not substring), CJK-adjacent still matches ---
    ("用whatsapp 发这份 proposal 给客户", "sc7-digital-messaging"),
    ("My coworker replied 'noted, thanks'. What do I reply?", "p2-subtext-decoder"),
    # --- Manglish / codeswitching lexicon (round-6) ---
    ("can lah 什么意思", "cu5-codeswitching"),
    ("他说 where got 是什么意思", "cu5-codeswitching"),
    ("paiseh 是什么意思", "cu5-codeswitching"),
    ("what does walao eh mean", "cu5-codeswitching"),
]

# Known recall gaps: currently miss or misroute. Reported as warnings so the
# suite stays green while the gaps are visible for future trigger work.
KNOWN_GAPS: list[tuple[str, str]] = [
    ("how to write a cover letter", "(none)"),
    ("怎么跟爸妈说我辞职了", "(none)"),
    ("和伴侣吵架了怎么和好", "(none)"),
    ("怎么判断一个人在撒谎", "(none)"),
    ("谈判时怎么让步", "sc10-negotiation-deals"),
]

# Layer-1.5 coarse-read fallback (router.json.intents): a CLEAR-intent query that
# uses no exact entry trigger must still route to an ENGINE. (query, engine code)
INTENT_CASES: list[tuple[str, str]] = [
    ("他昨天突然这么说是什么意思", "S1"),
    ("how should I interpret her long silence", "S1"),
    ("收到这种话我该怎么回复", "S2"),
]


def build_scorer(router: dict):
    def resolve(query: str) -> tuple[str | None, int, list[str]]:
        ranked = rank(router, query)
        if not ranked:
            return None, 0, []
        top = ranked[0]
        return top["id"], top["score"], top["matched"]

    return resolve


def main() -> int:
    router = json.loads(ROUTER.read_text(encoding="utf-8"))
    resolve = build_scorer(router)

    failures = 0
    print(f"router-smoke: {len(CASES)} must-pass, {len(KNOWN_GAPS)} known-gap probes")
    for query, expected in CASES:
        got, score, matched = resolve(query)
        if got == expected:
            print(f"  [PASS] {query} -> {got} ({score})")
        else:
            failures += 1
            print(f"  [FAIL] {query} -> {got} (expected {expected}, score {score}, matched {matched})")

    if KNOWN_GAPS:
        print("known gaps (not failures):")
        for query, expected in KNOWN_GAPS:
            got, score, _ = resolve(query)
            tag = "STILL-GAP" if got != expected else "NOW-OK "
            print(f"  [{tag}] {query} -> {got} (want {expected}, score {score})")

    intent_failures = 0
    if INTENT_CASES:
        print("intent-fallback (engine routing when keywords yield nothing):")
        for query, expected_engine in INTENT_CASES:
            got = resolve_intent(router, query)
            ge = got.get("engine") if got else None
            if ge == expected_engine:
                print(f"  [PASS] {query} -> engine {ge} (intent {got['intent']})")
            else:
                intent_failures += 1
                print(f"  [FAIL] {query} -> {got} (expected engine {expected_engine})")

    if failures or intent_failures:
        print(f"router-smoke: FAIL — {failures} recall + {intent_failures} intent regression(s)")
        return 1
    print(f"router-smoke: OK — {len(CASES)}/{len(CASES)} passed, "
          f"{len(INTENT_CASES)}/{len(INTENT_CASES)} intent-fallback passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
