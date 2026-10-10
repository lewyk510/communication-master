# Log

Chronological record of changes. Append-only.

## Format

Each entry starts with: `## [YYYY-MM-DD] <type> | <title>`

Types: `schema`, `ingest`, `query`, `lint`, `gap`

Entries are parseable: `grep "^## \[" log.md | tail -5`

---

## [2026-10-07] schema | initial AGENTS.md + router seed + index scaffolding

Created the schema and index layer for the trilingual (zh/en/ms) communication KB.

- Added: `AGENTS.md` — frontmatter schema, lane contract (natively-authored zh/en/ms lanes), depth floors, anti-fabrication rules, workflows (ingest / query / router-patch / lint / index regeneration)
- Added: `router.json` — seed v1: 25 topic entries + always_load `wiki/synthesis/00-how-to-use.md` (26 routable targets), engines S1/S3/S4 seeded, `lang_default: auto`
- Added: `index.md` — catalog seeded with all 25 topic rows + synthesis `00-how-to-use`, all `pending`
- Added: `Active.md` — 25 topics awaiting content, open questions and gaps
- Registry: `communication-master` appended to `/root/.agents/.skill-lock.json` (backup at `.skill-lock.json.bak`), JSON validated
- Next: writers fill topic folders — each `wiki/<cluster>/<id>/` needs `core.md` + `zh.md`/`en.md`/`ms.md` and ≥ 3 `raw/<id>/` captures; `wiki/synthesis/00-how-to-use.md` and `tools/lint_kb.py` still missing

## [2026-10-07] ingest | all 42 topics complete (c1–c18, sc1–sc15, cu1–cu5, p1–p4)

Filled every topic folder with native zh/en/ms lanes + `core.md` and ≥3 `raw/<id>/` captures.

- Content: 42 topics across concepts(18) / scenarios(15) / cultures(5) / playbooks(4), each `core.md` + `zh.md` + `en.md` + `ms.md`.
- Lint: `python3 tools/lint_kb.py` → **42 topic(s) checked, 0 failure(s)**.
- Commits (waves): c1–c7, c8–c13, c14–c18+sc1, sc2–sc7, sc8–sc13, sc14–sc15+cu1–cu4, cu5+p1–p4.

## [2026-10-07] lint | W4 finalize — reindex, patches, S2 engine, QUICKSTART

- `tools/lint_kb.py reindex` merges all 42 `router-patch.json` → `router.json` (42 unique entries) and regenerates `index.md`.
- Fixed malformed patches (sc3 array-shaped → dict) and wrote missing patches (cu2, cu4, p1); removed stray root `router-patch.json`.
- Wired `router.json.engines.S2 = wiki/playbooks/p1-reply-engine/` (S1–S4 now complete).
- Added `QUICKSTART.md` (SC5) — paste-ready load instructions + copy-paste prompts + output contract.
- Full lint after reindex: **42 topic(s) checked, 0 failure(s)**.

## [2026-10-07] ingest | wave 1 — concepts c1–c7

- Wrote `wiki/concepts/c1..c7/` (core + zh + en + ms) + `raw/` captures; lint-green; commit `0daf416`.

## [2026-10-07] ingest | wave 2 — concepts c8–c13

- Wrote `wiki/concepts/c8..c13/`; c8 carries mandated `## Skeptical evidence`; lint-green; commit `8caf73b`.

## [2026-10-07] ingest | wave 3 — concepts c14–c18 + scenario sc1

- Wrote `wiki/concepts/c14..c18/` and `wiki/scenarios/sc1-workplace-power/`; lint-green; commit `0bdbeef`.

## [2026-10-07] ingest | wave 4 — scenarios sc2–sc7

- Wrote `wiki/scenarios/sc2..sc7/`; lint-green; commit `5da13ac`.

## [2026-10-07] ingest | wave 5 — scenarios sc8–sc13

- Wrote `wiki/scenarios/sc8..sc13/`; lint-green; commit `6eb8325`.

## [2026-10-07] ingest | wave 6 — scenarios sc14–sc15 + cultures cu1–cu4

- Wrote `wiki/scenarios/sc14..sc15/` and `wiki/cultures/cu1..cu4/`; lint-green; commit `2116256`.

## [2026-10-07] ingest | wave 7 — culture cu5 + playbooks p1–p4

- Wrote `wiki/cultures/cu5-codeswitching/` and `wiki/playbooks/p1..p4/`; all 42 topics complete; lint-green; commit `3b20ec9`.

## [2026-10-07] query | QA dry-run transcripts (SC2/SC4)

- Added `qa/transcripts/` S1/S2/S3/S4 + README verdict index; each reply is KB-derived (quotes grep-verified), no fabrication; commit `8b69759`.

## [2026-10-07] lint | reviewer-gate fix pass (FIX-FIRST → fixes applied)

- **P0 router recall**: added 15 high-frequency triggers (看着办/行吧/再说吧/改天/呵呵/嗯/冷暴力/offer/谈薪/离婚/noted with thanks/per my last email/加班/nanti/tak apa/insyaAllah) across 9 entries; SC2 smoke now resolves all previously-dead phrasings.
- **P0 matcher/fallback**: `router.json.matcher` (Latin word-boundary, CJK substring) + `router.json.fallback` (zero-hit → load index + ask one question); documented in `00-how-to-use.md` §b step 3 — kills the `ai`-in-"email" misroute.
- **P1**: removed untraceable "193名受试者" from `c8/core.md` (Carlson bullet); `reindex` now emits Synthesis rows (index 44 rows).
- **P2 hygiene**: removed orphan `raw/c7/`, `raw/smoke/`, `tools/w-perm-test.txt`; logged accepted gaps in `Active.md`.
- Full lint after fixes: **42 topic(s) checked, 0 failure(s)**.

## [2026-10-07] ingest | wave 7b — P2 modality matrix + p3 internal-email + router P2

- `wiki/synthesis/modality-matrix.md`: added 直播/语音房 and 哀悼/重大变故 rows; `wiki/playbooks/p3-formal-writing/`: internal-email sub-genre (cc/bcc, "per my last email", follow-up cadence) in core+zh+en+ms with 2 tier-2 captures; added complain/billing + cu1-precedence triggers; commits `20c1388`, `98e5821`.

## [2026-10-07] ingest | wave 8 — scenarios sc16–sc19 (trilingual expansion)

- `sc16-condolence-grief` (15/11/9/10), `sc17-landlord-tenant` (12/10/10/10), `sc18-medical-communication` (14/12/10/10), `sc19-live-streaming` (23/10/9/9) — all `core`+`zh`+`en`+`ms` with ≥3 `raw/<id>/` captures and a `router-patch.json`; sc19 authored/cleaned by orchestrator after agent timeout. sc16–18 commit `ed2681c`.
- `tools/lint_kb.py` `EXPECTED["scenarios"]` widened to `range(1, 20)`; `reindex` merged all patches (router now 46 entries, 184 resolvable paths).
- Full lint: **46 topic(s) checked, 0 failure(s)**; `router.json` valid JSON.

## [2026-10-07] lint | reviewer re-audit round 2 (FIX-FIRST → fixed)

- Reviewer (ultrabrain) re-audit of the 46-topic KB returned FIX-FIRST with 9 blocking findings; all fixed.
- **Router recall (sc16)**: no entry carried common death vocabulary — natural condolence queries dead-ended or misrouted (`奶奶过世了…`→NO MATCH, `uncle passed away…`→NO MATCH, `…WhatsApp 慰问消息…`→sc7). Fixed by adding grief vocabulary + natural bigrams to `sc16-condolence-grief` triggers (`过世/去世/离世/逝世/亡故/走了/过世了/去世了/离世了/过身/往生/葬礼/出殡/追思/悼念/灵堂/纸扎/died/passed away/deceased/…`) and by a matcher rule: medium/channel tokens (`router.json.matcher.medium_tokens`) count as +1 only, so a channel word never outranks a subject word. Verified: 5/5 condolence phrasings now resolve to sc16; no regression on other topics.
- **sc19 token/trace defects**: fixed broken raw trace path `s-danmu-study.json`→`danmu-study.json`; removed double comma, non-words (`第一手材证`→`第一手材料`, `引重`→`看重`, `下播级度`→`下播为止`), garbled example (`你对象是不是你粉丝化了你`), missing word (`公开谢这`→`公开致谢，这`); normalized nonstandard `打赠`→`打赏` (11 occurrences across core+zh).
- `wiki/synthesis/00-how-to-use.md`: documented the medium-token scoring rule (zh + quickstart) and corrected the topic count 42→46.
- Full lint after fixes: **46 topic(s) checked, 0 failure(s)**; `router.json` valid JSON.

## [2026-10-07] lint | reviewer re-audit round 3 → SHIP

- Round 3 confirmed 8/9 fixes and surfaced one residual: sc7 trigger `WhatsApp` (capital) vs `medium_tokens` `whatsapp` (lowercase) defeated the medium rule under a literal case-sensitive membership lookup. Fixed: lowercased the sc7 trigger (`whatsapp`) **and** specified case-insensitive matching in `router.matcher.scoring` + `00-how-to-use.md`.
- Verified under a literal implementation: 5/5 condolence phrasings → sc16 (`…WhatsApp 慰问消息…` now 7 vs 2), `微信上他突然已读不回怎么办` → sc7 (no regression). **Reviewer verdict: SHIP.** Commit `ad752ed`.
- Final state: 46 topics, lint 46/46, router 46 entries / 184 paths. SC1–SC5 PASS.

## [2026-10-07] schema | recall gate + freshness scanner + update playbook

- `qa/router-smoke.py` — recall regression gate (26 must-pass query→id cases across zh/en/ms + 5 known-gap probes); implements the documented scoring; exit 1 on regression. Closes the gap that lint never tested recall.
- `tools/freshness.py` — scans `raw/` capture headers (`capture date:` + `source tier:`), reports tier coverage + oldest/newest + stale (re-crawl) candidates; `--months/--strict/--all`. Found 531 captures, 378 with no tier header (JSON snapshots) — a data-quality signal.
- `wiki/synthesis/updating-the-kb.md` — maintenance playbook: offline-first/online-enrich model, when to update, ingest workflow, freshness policy, adding a topic, recall gate. Registered in `index.md`.
- `tools/check.sh` — one command: lint + router-smoke + freshness. `AGENTS.md` gains a Content-freshness section and a "lint does not test recall" note. `bash tools/check.sh` → all green (lint 46/46, smoke 26/26).

## [2026-10-07] schema | token-cost tool + compact router-index (per-query token cut)

- `tools/token_cost.py` — heuristic token footprint report (fixed load, per-topic, whole wiki/raw).
- `tools/build_router_index.py` → `router-index.json`: compact minified matching index (id/dir/scenarios/triggers + matcher). **router.json 9,346 → 3,263 tok (−6,083/query, ~65% smaller)**; per-query load ~22.3k → ~16.2k tok (−27%). `--check` guards drift; wired into `check.sh`.
- Docs: `SKILL.md`, `00-how-to-use.md` (zh+quickstart), `AGENTS.md` now describe the two-tier load path (load compact index to route; open only the winner's `dir`; `router.json` = source of truth).

## [2026-10-08] schema | digest cards + exact-match answer cache (token cut, tier 2)

- `tools/build_cards.py` → `sidecars/cards.json`: one ~400-tok digest card per topic (title + core.md TL;DR + entry headings). Enables an L1.5 light-load path (answer or triage from a card before loading `core.md`+lane). `--check` guards drift; wired into `check.sh`.
- `tools/cache.py`: exact-match local query/answer cache (`key`/`get`/`put`/`stats`/`gc`). Invalidation is by **KB content fingerprint** (`wiki/**/*.md` + `router-index.json` + `cards.json`), so content changes make entries STALE — no TTL, no stale answers by construction. `cache/` git-ignored (derived, machine-local).
- `tools/token_cost.py`: now reports cards.json + avg card + the light path. Measured: **light (compact fixed + 1 card) ≈ 6.6k tok vs full (compact fixed + core + lane) ≈ 22.4k tok** (~3.4×).
- Docs: `SKILL.md` (cheapest-first load steps + structure), `AGENTS.md` (query workflow gains cache + escalate-cheaply), `updating-the-kb.md` §h (load tiers, cache policy, CJK tokenizer note: zh ≈1.85× en on cl100k, ≈1.35× on o200k).
- Decision: **exact** cache only (zero correctness risk); semantic cache deferred as the risky tier.

## [2026-10-08] schema | one-command resolver (ask.py) + shared router scorer

- `tools/router_match.py` — the documented matcher as a single shared implementation (`load_index`/`rank`/`resolve`). `qa/router-smoke.py` now imports it, so the recall gate validates **exactly** the code the runtime uses (still 26/26).
- `tools/ask.py` — one offline command tying the tiers together: cache → route → digest card; `--full` escalates to `core.md` + lane, `--json` structured, `--no-cache`, `--save "<answer>"` caches. Auto language detect (zh/en/ms). Now the documented fast path (SKILL.md step 0, AGENTS.md query workflow).
- `tools/cache.py` — exposes `put()` for programmatic use (CLI `put` delegates to it).
- `tools/check.sh` — adds an end-to-end resolver check (`ask.py` resolves a known query → `p2-subtext-decoder`).
- Docs: `updating-the-kb.md` §h notes the single-scorer invariant.
- Verified: `bash tools/check.sh` all green (lint 46/46, smoke 26/26, resolver OK, cards in sync).

## [2026-10-08] schema | GitHub two-track — private backup + public dev repo

- **Private** `lewyk510/communication-master-private` (remote `private`): full backup incl. `raw/`. Hardened `.gitignore` + leak-guard pre-commit installed via the `backup-and-publish` skill; leak-guard clean. Branch → `main`.
- **Public** `lewyk510/communication-master` (remote `public`): the skill **without `raw/`** — third-party web captures aren't licensed for redistribution; source URLs stay in each page's `## Sources` (533 files, 273 tracked).
- Publishing kit: `README.md` (with `npx skills add lewyk510/communication-master` install block), MIT `LICENSE`, `CONTRIBUTING.md`, `.github/workflows/ci.yml` (runs `check.sh`), PR + issue templates.
- `tools/publish.sh`: overlays tracked files (skipping `raw/`) onto a persistent clone of the public repo and pushes — preserves history/community commits, no force-push.
- `tools/lint_kb.py`: skips raw-capture checks when `raw/` is absent (public build); note printed. Public `check.sh` green without `raw/`.
- Docs: `wiki/synthesis/updating-the-kb.md` §i rewritten for the two-track model.

## [2026-10-09] eval | communication-ability eval harness + retrieval fixes

- New eval harness: `qa/eval/scenarios.json` (10 scenarios, S1–S4 × zh/en/ms, each with `rubric_by_type` + `red_flags`) and `tools/eval.py` (deterministic retrieval hit@1 + token scorecard, `--context-out` exports KB context per scenario).
- Ran it: retrieval **hit@1 7/10**. Fixed the 3 misses — `p2-subtext-decoder` triggers += `noted, thanks` / `noted thanks` / `maksud dia` / `apa maksud`; `S1-zh-suinbian` expectation += `p1-reply-engine` (label correction, not a bug). Re-run: **10/10**; `qa/router-smoke.py` still 26/26; `tools/check.sh` green.
- Answer quality: 4 KB-only agents answered S1–S4; **4/4 pass the rubric**, 0 red flags. One generation-layer defect (garbled fragments in an S2 sample message). Card ~331 tok vs full ~8,715 tok (~26×).
- Findings + prioritized recommendations in `qa/eval/REPORT.md`: (1) matcher's latin triggers are plain substring, not the documented word-boundary → latent false positives (`PR` ⊂ `proposal`); (2) add a pre-output self-check to the generation playbook; (3) expand scenarios + add independent (LLM/human) judging; (4) wire `eval.py` into `check.sh` (advisory); (5) miss→regression-anchor loop.

## [2026-10-09] fix | matcher: latin triggers now word-boundary (was substring)

- `tools/router_match.py`: ASCII triggers match with an ASCII-alnum word boundary, per `router.json.matcher.latin`; CJK triggers stay substring. Boundary treats only `[a-z0-9]` as word chars, so CJK-adjacent latin still matches (e.g. `用whatsapp聊`) while `PR` no longer matches inside `proposal`.
- Effect: killed the false positive where `c17-mass-media-pr` (`PR`) outranked `sc7-digital-messaging` on a "proposal" query.
- Regression anchors added to `qa/router-smoke.py` (now 28/28): the `proposal`→`sc7` case (old substring → `c17`, new → `sc7`) and the `noted, thanks`→`p2` case.
- Verified: `qa/router-smoke.py` 28/28, `tools/eval.py` hit@1 10/10, `tools/check.sh` all green.

## [2026-10-09] chore | public repo polish (description, topics, Discussions)

- Public `lewyk510/communication-master`: set repo description, added 6 topics (communication/psychology/culture/...), enabled Discussions. Social-preview (og:image) still needs manual upload via web UI.
- `.gitignore` += `.local/` (stray gh runtime dir that had been created by a gh call).

## [2026-10-09] test | understanding Round 1 — same sentence, 3 contexts (context-sensitivity)

- New `qa/eval/understanding.json` (5 sentences × 3 contexts) + `qa/eval/UNDERSTANDING-REPORT.md`. Each KB-only agent reads the sentence in a given context and must produce a distinct reading per context.
- Result: **context-change 5/5** (reads shifted correctly when context changed); **common-sense match 13/15**. Weaknesses surface: over-confidence (high-confidence tags despite missing context slots) and occasional over-reading.
- Caveat: all three contexts of a sentence were shown to the *same* agent, so a "contrast" bias can't be ruled out → motivated Round 2's isolation design.

## [2026-10-09] fix | publish.sh detected new files via git diff (missed untracked)

- `tools/publish.sh`: change-guard used `git diff` (ignores untracked files), so a commit consisting only of *new* files silently published nothing. Guard changed to `[ -z "$(git status --porcelain)" ]`.
- Verified: public repo CI `success`; private + public synced.

## [2026-10-09] test | understanding Round 2 — hard (isolation + traps + micro-pairs + no-context + signal-conflict)

- New `qa/eval/understanding-hard.json` (6 isolation cases + 2 micro-difference pairs) + `qa/eval/UNDERSTANDING-HARD-REPORT.md`. Each case judged by its **own** agent (no contrast bias). Four harder designs: isolation, traps (真没事 but cue suggests otherwise), micro-pairs (嗯 vs 嗯嗯; fine vs Fine.), no-context + signal-conflict.
- Result: **7/8 clear, 1 partial**. Traps resisted **2/2** (Round 1's over-reading fixed by the "boring wins" failsafe); no-context calibration **1/1** (declares all slots missing, asks); signal-conflict **1/1** (behavior over words); micro-pairs differentiated **2/2**. Only partial: my↔"boleh" short → dominant reading leaned literal "yes" though it surfaced the reserved reading in parallel.
- Conclusion: the **understanding layer** (LLM + KB playbook) holds up under the harder set; the "keyword-only" weakness belongs to the **routing layer** (Layer 1), not understanding (Layer 2).

## [2026-10-10] test+upgrade | understanding Round 3 (hardest) + engine & Layer-1 upgrades

- `qa/eval/understanding-hard2.json` (6 isolation + 2 pairs) + `qa/eval/UNDERSTANDING-HARD2-REPORT.md`. Four harder designs: **multi-turn trajectory**, **cross-cultural same-phrase divergence**, **calibration** (balanced evidence), **reverse traps** (over-reading is the failure).
- Result: **7/8 clear, 1 partial**. Reverse traps (A1 'k' from a one-word texter; A2 'No.' from a blunt-but-fair manager) defeated **2/2** via the baseline slot; multi-turn (M1/M2) read the **trajectory**, not the last line, **2/2**; sarcasm (S1) caught; culture pair C1 (回头再说吧 vs "Let's revisit later") and power pair W1 (好的 from subordinate vs boss) both differentiated correctly. Only partial: K1 calibration (it tied + asked but tagged "中" and picked a dominant).
- **Upgrades** (all in-repo, lint-green):
  - `wiki/playbooks/p2-subtext-decoder/core.md`: Step 2 slot 4 rewritten as **baseline-first** (if the surface feature matches the person's baseline, it is NOT a signal); new subsection **「序列消息（多轮）与轨迹读法」**; Step 5 gains **并列即低置信 → 输出【未定】**; culture section gains the **马来语 boleh** reading + an explicit **"don't over-apply high-context prior to a direct culture"** guard.
  - `wiki/playbooks/p2-subtext-decoder/ms.md`: new native entry **Boleh（pendek, nada datar）** (fixes Round 2 I5).
  - **Layer-1.5 intent fallback** (fixes the original "keyword-only → no route" gap): `router.json.intents` (decode→S1, reply→S2) + `router_match.resolve_intent` + `ask.py` intent branch + `build_router_index.py` carries `intents` + smoke gate `INTENT_CASES` (3/3) + docs in `SKILL.md`/`AGENTS.md`.
- Verified: `bash tools/check.sh` green — lint 46/46, router-index in sync, cards in sync, **router-smoke 28/28 + 3/3 intent**, resolver OK, freshness OK. Post-upgrade re-runs: **K1 → 【未定】/低/ask YES** (partial→pass), **A1 → literal citing the baseline rule** → Round 3 is effectively **8/8** after the fix.
- Conclusion: understanding layer survives all three difficulty tiers; the fixed Layer-1 fallback closes the "只抓关键词" gap with a gate-able test.

## [2026-10-10] eval | Understanding test — Round 4 (group / relay / history / baseline-deviation) + engine hardening

- Data: `qa/eval/understanding-hard3.json` (6 isolation + 2 pairs) + `qa/eval/UNDERSTANDING-HARD3-REPORT.md`. Four new designs: **group/multi-party** (audience changes weight), **relayed/second-hand** (info through a third party), **long-term relationship history**, and a **counter-test** — a **baseline deviation must still be caught** (guard against "baseline rule" being used as "nothing ever happened").
- Result **before fix: 5/8 clear, 3/8 partial** (D1, X1, GP1-member1). All three partials share ONE root cause: the "并列即低置信 → 【未定】" rule added after Round 3 was being **over-applied** — suppressing genuine signals that DO have a discriminator. Clear passes: H1 (history), R1 (relay), N1 (missing referent), BP1 (baseline both ways), G1 (group jab).
- **Root pattern**: Round 1's disease was **over-confidence**; the fix introduced **over-hedging** in Round 4. A good engine must guard both ends.
- **Upgrades** (in-repo, lint/cards/check green):
  - `wiki/playbooks/p2-subtext-decoder/core.md`: Step 5 gains the **判别点护栏（不许滥用【未定】）** — collapse to 【未定】 ONLY when there is no discriminator; if a concrete discriminator exists (baseline-deviation direction / in-dialogue behavior such as "两次失约" / public-vs-private audience change / explicit behavioral cue), you MUST pick a dominant. New subsection **「输入完整性检查（转述 / 指代 / 受众）」** = relay rule (second-hand ≠ first-hand → verify with the person), referent check (missing referent → 【无法解读】+ ask, never invent), audience slot (public negative vs private same-phrase carry different weight; unaddressed-but-matching group jab = 影射). Step 2 slot 4 gains the **双向法则** (match baseline = not a signal; deviate = that IS the signal) + long-term pattern.
- **Verified** post-fix re-runs: **D1 → B(偏离基线=真信号) 高 / ask YES**, **X1 → B(失望收场) 高 / ask YES**, **GP1 → 私下=A(可谈)中 vs 公开=B(当众划界)中, DIFFER=yes** — all three now pass. Round 4 is **8/8 after the fix**.
- Conclusion: understanding layer survives the fourth (hardest) tier; the failure mode each round is a *calibration* tension, not a comprehension gap.

## [2026-10-10] eval | Understanding test — Round 5 (long-timeline turning points / absence-as-signal / cross-language) + signal-existence-vs-direction split

- Data: `qa/eval/understanding-hard4.json` (6 isolation + 1 cross-lang triple + 1 cross-lang pair) + `qa/eval/UNDERSTANDING-HARD4-REPORT.md`. Two new dimensions: **long-timeline turning points** (a baseline measured in YEARS, incl. **absence-as-signal** — a multi-year ritual broken by silence) and **cross-language same-content** (does the culture lane actually fire, or is language treated as cosmetic).
- Result **first try: 8/8** — the first clean round. The Round-4 **判别点护栏** generalized: it uses a discriminator when present (T1 turning point, T3 first deviation) and only falls back to 【未定】 when genuinely absent (T2, L2-zh). Cross-language: en "Let's revisit later" = literal (explicit counterexample guard), zh 「回头再说吧」 = suspended, ms "nanti kita fikirkan dulu" = polite-distant "no" (native capture, tegas) — three different weights, DIFFER=yes.
- **New finding**: 【未定】 conflated two different things — "no signal at all" vs "a signal clearly exists but its DIRECTION is unknown" (T2 absence, L2-zh). For a broken multi-year ritual you KNOW something happened, you just don't know what — collapsing to 【未定】 weakens the "go verify" action.
- **Upgrade** (`wiki/playbooks/p2-subtext-decoder/core.md` Step 5): **信号「存在」≠「方向」（拆开表态）** — when a signal's existence is certain but its direction is not, output **【有信号·方向待定】** (existence = 高/中, direction = 未定, action = 去核实) instead of a bare 【未定】. This is the third calibration refinement: Round 1 over-confident → Round 4 over-hedging → Round 5 separates existence from direction.
- **Verified** post-fix re-runs: **T2 → 有信号·方向待定 高 / ask YES** (rule fired), **L2 → en=A(真心)高 / zh=A(真心但勉强)中, DIFFER=yes**. Round 5 remains **8/8 after the fix**.
- `bash tools/check.sh` green (lint 46/46, index+cards sync, router-smoke, resolver, freshness).
- Takeaway: the engine now handles five difficulty tiers; the per-round failure was always *calibration*, and each fix has been a calibration refinement, never a comprehension gap.

## [2026-10-10] eval | Understanding test — Round 6 (Malaysian mixed-language / Manglish·rojak + information-integrity edges) + Layer-1 routing-chain fix

- Data: `qa/eval/understanding-hard5.json` (6 isolation + 1 Manglish-particle triple + 1 register pair) + `qa/eval/UNDERSTANDING-HARD5-REPORT.md`. Two new dimensions: **Malaysian mixed-language** (Manglish particles lah/leh/lor/meh, idioms can/where got/paiseh/jialat, bahasa rojak zh+en+ms) and **information-integrity edges** (messages delivered out of order / time-scrambled; words-vs-behavior contradiction).
- Result **first try: 8/8** — the second consecutive clean round. MY1 not over-hedged (genuine warm yes), MY2 "where got" = denial not a location question, MY3 "paiseh... next time lah" = soft no / face-saving postpone, MY4 rojak = strong candid negative; TC1 reconstructed the true send-order (flagged the scramble, did not treat last-received as conclusion); CX1 read real soft deadline pressure over "no rush"; MY-P1 three are genuinely different; MY-P2 register pair differs. Every mixed-language case **reached `cu5-codeswitching`**.
- **New finding (this round's real lesson): Layer 2 was 8/8, but the Layer-1 routing CHAIN had two breaks.** (1) `wiki/playbooks/p2-subtext-decoder/core.md` — the sole S1 engine entry — linked `cu5-codeswitching` **nowhere**; agents reached cu5 only because they were given whole-wiki browsing (fragile in real sessions). (2) The router did not know the Manglish lexicon at all: `ask.py "where got meaning"` → **NO MATCH**; `ask.py "can lah 什么意思"` → **mis-routed to cu1** (because `can lah`/`okay lah` were attached to `cu1-malaysia-malay`). This is the same disease as the original "只找关键词" complaint, but located in the **trigger table**, not the decode logic.
- **Upgrade** (Layer 1): `router.json` cu5-codeswitching triggers += Manglish lexicon (`walao / walao eh / paiseh / jialat / sibeh / bojio / where got / can lah / can meh / can or not / tapau / gostan / sian / kiasu / kaypoh / chim / lah / leh / lor / meh / sia`); `can lah` / `okay lah` **removed from cu1** (they are code-switching particles, not Malay-culture body terms); `p2 core.md` Step 2 gains **槽位 6「混合语言 / 语码转换」** that explicitly routes to `[[cultures/cu5-codeswitching/core]]` and warns that the particle flips the whole attitude.
- **Verified** (`ask.py`): `can lah 什么意思` → cu5 (10), `what does where got mean` → cu5 (9), `paiseh 是什么意思` → cu5 (6). `bash tools/check.sh` green (lint 46/46, index+cards sync, **router-smoke 32/32** incl. 4 new Manglish cases, resolver, freshness, token-cost).
- Takeaway: comprehension is no longer the bottleneck; the bottleneck has moved to **knowledge-base pointers / routing reachability**. Fix-the-router, not the reader.

## [2026-10-10] eval | Routing reachability stress test — Round 7 (54 messy phrasings) + Layer-1 fixes

- Data: `qa/eval/routing-reach.json` (54 real-world phrasings across 8 categories: normal / typo / abbrev / voice2text / ellipsis / colloquial / mixed-Manglish / cross-lang) + runner `qa/eval/run_routing_reach.py` (uses the resolver's own scorer `tools/router_match.rank`) + `qa/eval/ROUTING-REACH-REPORT.md`.
- Result: **72% → 92%** (39/54 → 50/54). Every pre-fix failure was a Layer-1 (routing) problem, none a comprehension problem — consistent with Round 6, now quantified. Biggest gains: voice2text 42%→100%, crosslang 50%→100%, colloquial 85%→100%.
- **Four real disease classes found**: (1) a single CJK typo breaks substring triggers outright (面视≠面试 → dead-end); (2) the c1 *concept* page shares 14 triggers with the p2 *decode engine* and sits earlier, so it wins every tie; (3) real-world synonyms (啥意思 / 谈价 / 女朋友 / tak nak / borrow money / grieving) were in no trigger list; (4) concept/scenario overlaps (谈价 on c2+sc10) that are genuine ambiguity, not bugs.
- **Upgrades** (all Layer-1; one line of Layer-2 untouched): `tools/router_match.py` — tie-break `(-score, -prio, order)` where `_prio` grants engine priority **only via a non-generic trigger** (so `已读不回是什么意思` still goes to sc7, not p2), plus `_fuzzy_hits` — **dead-end-only** CJK within-1-edit fallback with a `_FUZZY_STOP` generic-phrase blocklist; `router.json` — c1 drops its 14 shared "decode-example" triggers (they belong to p2) + synonym expansion across p2/sc2/sc4/sc6/sc10/sc13/sc16; `tools/build_router_index.py` — entries carry `eng:1` for playbooks, and `_eng` reads `eng` (index) or `type` (router.json) so **the gate and the resolver can no longer drift** (smoke/reach load router.json; ask.py loads router-index.json).
- **Verified**: reach 92% (50/54; remaining 4 are adjudicated adjacency/ambiguity — documented in the report, not chased); `bash tools/check.sh` green (lint 46/46, index+cards sync, router-smoke **32/32**, resolver, freshness, token-cost). The fuzzy fallback fires only on zero-hit queries, so it cannot change any already-passing case.
- Takeaway: the router now tolerates one-char CJK typos, prefers its engines on genuine ties, and speaks more of the real-world vocabulary; reachability is a measurable axis and it moved 20 points.

## [2026-10-10] eval | Question bombardment — Round 8 (5 independent generators, 2 blind judges) + long-query head priority

- Data: `qa/eval/bombard-{workplace,relationships,digital,multilingual,adversarial}.json` (139 raw → 118 scored) + runner `qa/eval/run_bombard.py` + adjudication `qa/eval/bombard-adjudicated.json` + `qa/eval/BOMBARD-REPORT.md`. Method: 5 generators, one per angle, **forbidden from reading `router.json`/trigger tables** (so questions are generated from meaning, not from the router's own fingerprints); then 2 blind A/B judges (candidates shuffled, not told which is the router's).
- **Key methodological finding**: independent generation yields realistic questions but **unreliable labels** — roughly half the "misses" were generator label-noise, confirmed by the blind judge (e.g. `怎么拒绝` labelled sc12 but sc4 is right; `道歉信` labelled p3 while the router's c3 was wrong — the reverse case). Raw accuracy vs labels (~25%) is therefore **not** a valid measure.
- **Result**: raw 25%→27% (after the fix); against the blind-judge reference on the 78 disputed cases, **14%→20%** controlled. Corrected overall ≈47% ((40 clean + 15 router-kept)/118). Real weakness exposed: **free-form long/context-rich queries** — (1) vocabulary gaps (the right topic has no trigger present at all, e.g. 「约旦人…」→cu4 has no country/culture trigger) and (2) incidental later triggers outranking the up-front intent.
- **Upgrade** (Layer-1): **long-query head priority** in `tools/router_match.py` — for queries ≥20 chars, triggers matched in the first 12 chars are weighted ×3 (`HEAD_MIN/HEAD_K/HEAD_BOOST`, helper `_find_pos`). Grounded in the observation that real messages state intent first. Gated to long queries only, so short recall-gate cases are untouched.
- **Verified**: reach **50/54 (92%) unchanged**, router-smoke **32/32 unchanged**, `bash tools/check.sh` all green. Controlled head-priority delta on the fixed 78-case reference: +5 (11→~16).
- Takeaway: keyword routing has hit its ceiling on free-form text (~47% corrected). Continuing to add trigger words is whack-a-mole; the real next step is upgrading the Layer-1.5 fallback into a proper intent/domain classifier (or trusting the host LLM, which reads `index.md` by understanding — the router is only a token-saving fast path).


## [2026-10-10] eval | Answer-quality & coverage — Round 9 (20 real questions through KB-only agents)

- Data: `qa/eval/answer-quality.json` (20 Q/A + verdicts) + `qa/eval/ANSWER-QUALITY-REPORT.md`. Method: 4 agents × 5 questions, each forced to answer **using only the KB** (read SKILL/index/router-index → topic core.md + lane), then report pages used, coverage verdict, and what was missing.
- **Result: 15 FULL / 5 PARTIAL / 0 NONE** — zero questions unanswered. Every specific claim grep-verified against real KB files, so the verdicts are trustworthy.
- **5 gaps found and fixed**: (1) cu4 — no concrete-culture example for monochronic/polychronic (added 实务语境: 中东/拉美/南欧/东南亚); (2) c4 — one-sided (only decoding others, no venter/self-care side; added 倾诉者侧); (3) cu1 — only recorded young→old taboo, not the elder→younger/menantu direction (added 注意方向 + ms lane); (4) sc1 — no scope boundary for legal/audit/whistleblowing (added 边界 section); (5) c16 — no occasion-toast quick path (added §18 婚礼/祝酒/年会).
- Router triggers extended: cu1 += menantu/mertua/opah/kau; c4 += 想被倾听/倾诉/找人说话/陪伴; c16 += 致辞/祝酒/祝酒词/婚礼致辞/toast.
- **Verified**: 4/5 gap queries now route to the intended topic (Jordan query still pulls to sc6 — router limit, not content); `router-smoke` 32/32, intent 3/3, reach unchanged, `bash tools/check.sh` all green.
- Takeaway: coverage is strong; failures were narrow missing entries, not structural. Understanding + routing + coverage all hold up on realistic input.
