# Active

Current focus items and priorities.

## Focus Areas

| Priority | Area | Status | Next Step |
|----------|------|--------|-----------|
| 1 | Topic content — 46 folders | ✅ complete (all lint-green) | — |
| 2 | `wiki/synthesis/00-how-to-use.md` | ✅ present | — |
| 3 | `tools/lint_kb.py` | ✅ present | full run: 46 topics, 0 failures |
| 4 | Router (`router.json`) + `index.md` | ✅ merged/reindexed | 46 entries, 184 paths resolve |
| 5 | `QUICKSTART.md` (SC5) | ✅ written | paste-ready |
| 6 | QA dry-run transcripts (SC2/SC4) | ✅ complete | `qa/transcripts/` S1–S4 + README |
| 7 | Reviewer gate (ultrabrain) | ✅ SHIP (round 3) | 46-topic KB passed after sc16 recall + sc19 cleanup fixes |
| 8 | Recall regression gate | ✅ `qa/router-smoke.py` | 26/26 must-pass + 5 known-gap probes |
| 9 | Freshness / updatability | ✅ `tools/freshness.py` + `updating-the-kb.md` | `tools/check.sh` runs lint+smoke+freshness |
| 10 | Token cost reduction | ✅ compact index + digest cards + exact cache + one-command resolver | light ≈6.9k vs full ≈22.7k tok/query (~3.3×); `tools/ask.py` runs cache→route→card |
| 11 | GitHub backup + public repo | ✅ private + public live | `private` = full backup; `public` (no `raw/`) = lewyk510/communication-master; `tools/publish.sh` |

---

## Awaiting Content (46 topics) — ALL COMPLETE

Each `wiki/<cluster>/<id>/`: `core.md` + `zh.md` + `en.md` + `ms.md`, ≥3 `raw/<id>/` captures. All pass lint.

### concepts (18)
- [x] c1-subtext-implicature · [x] c2-persuasion-influence · [x] c3-nvc-conflict-repair · [x] c4-emotional-intelligence
- [x] c5-personality-typology · [x] c6-nonverbal-subconscious · [x] c7-demographic-differences · [x] c8-astrology-heuristics (incl. `## Skeptical evidence`)
- [x] c9-manipulation-defense · [x] c10-models-meta · [x] c11-paralanguage-prosody · [x] c12-rhetoric-storytelling
- [x] c13-visual-multimodal · [x] c14-self-talk · [x] c15-group-team-communication · [x] c16-public-speaking
- [x] c17-mass-media-pr · [x] c18-propaganda-fallacies

### scenarios (19)
- [x] sc1-workplace-power · [x] sc2-romance-intimacy · [x] sc3-family-kinship · [x] sc4-hard-conversations
- [x] sc5-networking-first-impressions · [x] sc6-friends-social · [x] sc7-digital-messaging · [x] sc8-job-interviews
- [x] sc9-live-service · [x] sc10-negotiation-deals · [x] sc11-teaching-coaching · [x] sc12-asking-help
- [x] sc13-mediation · [x] sc14-online-social · [x] sc15-calls-video · [x] sc16-condolence-grief
- [x] sc17-landlord-tenant · [x] sc18-medical-communication · [x] sc19-live-streaming

### cultures (5)
- [x] cu1-malaysia-malay · [x] cu2-malaysia-chinese · [x] cu3-malaysia-indian · [x] cu4-cross-cultural-general · [x] cu5-codeswitching

### playbooks (4)
- [x] p1-reply-engine · [x] p2-subtext-decoder · [x] p3-formal-writing · [x] p4-ai-prompting

---

## Questions to Investigate

- [x] **S2 engine wiring** — RESOLVED: `router.json.engines.S2 = wiki/playbooks/p1-reply-engine/`.
- [x] **core.md language policy** — RESOLVED: zh-first prose mixed with standard English terms (per AGENTS.md).
- [x] **`raw/smoke/`, `raw/c7/`, `tools/w-perm-test.txt`** — REMOVED (reviewer-gate hygiene: stray/orphan, off-schema).

## Known gaps (accepted, post reviewer-gate)

- [x] **Modality matrix** — RESOLVED: 直播/语音房 + 哀悼/重大变故 rows added to `wiki/synthesis/modality-matrix.md`.
- [x] **Email sub-genre** — RESOLVED: internal-email sub-genre (cc/bcc, "per my last email", follow-up cadence) added to `p3-formal-writing/` (core+zh+en+ms) with 2 tier-2 captures.
- [x] **Scenario thin spots** — RESOLVED: sc16-condolence-grief, sc17-landlord-tenant, sc18-medical-communication written (trilingual).
- [x] **Router recall** — RESOLVED (P0): 11 dead high-frequency phrasings fixed; subtext/culture/exposure triggers added. Re-run the SC2 smoke after any trigger edit — lint does NOT test recall.
- [x] **ms lane register** — RESOLVED: lanes authored natively per-topic; standard Malay (bahasa baku) with KL-register notes where relevant (cu5-codeswitching covers register mixing).
- [x] **Recall regression net** — RESOLVED: `qa/router-smoke.py` (26 must-pass query→id cases + 5 known-gap probes); run after any trigger edit. Lint still does not test recall — the smoke test does.

## Sources to Find

- [x] Per-topic sources satisfied: every wiki file has `## Sources` with ≥3 URLs; every `raw/<id>/` has ≥3 captures.

---

## Completed

| Date | Item | Notes |
|------|------|-------|
| 2026-10-07 | Schema + router seed + index scaffolding + registry entry | see log.md |
| 2026-10-07 | All 42 topics written (c1–c18, sc1–sc15, cu1–cu5, p1–p4) | lint-green, committed in waves |
| 2026-10-07 | W4 instruction slice + reindex + patches normalized + S2 wired | `commands/*`, `wiki/synthesis/*` |
| 2026-10-07 | `QUICKSTART.md` (SC5) | paste-ready load instructions |
| 2026-10-07 | P2 pass: modality rows + p3 internal-email + complain/cu1 triggers | commits `20c1388`, `98e5821` |
| 2026-10-07 | sc16/sc17/sc18 trilingual scenarios | commit `ed2681c` |
| 2026-10-07 | sc19-live-streaming trilingual scenario + router patch; lint `EXPECTED`→range(1,20) | full lint 46/46 green |
| 2026-10-07 | Reviewer gate round 2 (FIX-FIRST) → round 3 **SHIP** | sc16 condolence recall + sc19 token/trace fixes; commits `cb7e721`, `ad752ed` |
| 2026-10-07 | Recall gate + freshness scanner + update playbook | `qa/router-smoke.py`, `tools/freshness.py`, `tools/check.sh`, `wiki/synthesis/updating-the-kb.md` |
| 2026-10-07 | Token-cost tool + compact `router-index.json` | `tools/token_cost.py`, `tools/build_router_index.py`; router.json 9,346→3,263 tok |
| 2026-10-08 | Digest cards + exact-match answer cache | `tools/build_cards.py`→`sidecars/cards.json`, `tools/cache.py`; light path ≈6.6k vs full ≈22.4k tok |
| 2026-10-08 | One-command resolver + shared router scorer | `tools/ask.py`, `tools/router_match.py`; recall gate now imports the shared scorer |
| 2026-10-08 | Backup/portability tooling | `tools/backup.sh` (GitHub push + offline bundle) |
| 2026-10-08 | GitHub two-track live | private `communication-master-private` (full) + public `communication-master` (no `raw/`); `tools/publish.sh`; leak-guard clean |
