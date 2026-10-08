# communication-master — KB Schema

Instructions for the LLM on how to maintain this trilingual (zh / en / ms) communication knowledge base.

## Purpose

A knowledge base about reading, understanding, and responding to people: subtext, persuasion, conflict repair, nonverbal signals, culture (Malaysia-first), and practical playbooks. The user is Chinese-first and Malaysia-based — **zh and ms lanes matter as much as en**. The LLM reads raw captures, writes wiki content, keeps lanes natively authored, and maintains the router/index/log.

## Structure

```
communication-master/
├── AGENTS.md              ← this file: schema + workflows
├── README.md / LICENSE / CONTRIBUTING.md / .github/   ← public-repo publishing kit
├── router.json            ← full source of truth (query resolution, patches, lint)
├── router-index.json      ← compact matching index (generated; what the resolver loads)
├── sidecars/cards.json    ← per-topic digest cards (generated; L1.5 light-load path)
├── cache/                 ← local exact-match answer cache (git-ignored, derived)
├── index.md               ← human catalog. START HERE.
├── log.md                 ← append-only change history
├── Active.md              ← current focus / open questions / gaps
├── raw/<topic-id>/        ← immutable source captures (≥3 per topic)
├── wiki/
│   ├── concepts/<id>/     ← c1–c18
│   ├── scenarios/<id>/    ← sc1–sc19
│   ├── cultures/<id>/     ← cu1–cu5
│   ├── playbooks/<id>/    ← p1–p4
│   └── synthesis/         ← cross-topic pages; 00-how-to-use.md is router always_load
├── tools/                 ← lint_kb.py, build_router_index.py, build_cards.py, router_match.py, ask.py, cache.py, backup.sh, publish.sh
├── commands/              ← slash commands
├── sidecars/              ← machine-readable sidecar data
└── qa/transcripts/        ← QA transcripts
```

`raw/` mirrors the topic ids under `wiki/`. Raw captures are immutable: read from them, never edit them.

## Topic Folders and Files

Every topic folder `wiki/<cluster>/<id>/` MUST contain exactly these four files:

| File | Role | Floor |
|------|------|-------|
| `core.md` | Canonical deep reference: mechanisms, models, evidence, cross-lane comparison. Written zh-first, mixed with English terms where standard. | ≥ 10 structured entries AND ≥ 1000 words |
| `zh.md` | Native zh lane (signals/phrases in Chinese) | ≥ 10 entries |
| `en.md` | Native en lane (signals/phrases in English) | ≥ 8 entries |
| `ms.md` | Native ms lane (signals/phrases in Malay) | ≥ 8 entries |

`raw/<topic-id>/` MUST contain ≥ 3 captures (md/html/txt/json snapshots). Prefix each capture's filename with a capture date and add a small header inside: source URL, capture date, source tier.

## Frontmatter Schema

Every wiki file (`core.md`, `zh.md`, `en.md`, `ms.md`, and synthesis pages) starts with this YAML frontmatter:

```yaml
---
id: c1-subtext-implicature      # topic id; synthesis pages use their file stem (e.g. 00-how-to-use)
title: Subtext & Implicature    # display title
type: concept                   # concept | scenario | culture | playbook | synthesis
lang: core                      # core | zh | en | ms
tags:                           # free-form lowercase tags
  - pragmatics
scenarios:                      # subset of S1|S2|S3|S4 (see Scenario Codes)
  - S1
  - S2
sources:                        # paths under raw/ (preferred) or URLs
  - raw/c1-subtext-implicature/grice-implicature-2026-10-07.md
related:                        # [[wikilinks]] to other wiki pages
  - "[[concepts/c9-manipulation-defense/core]]"
created: 2026-10-07
updated: 2026-10-07
---
```

All fields are required. `scenarios` may be empty only for synthesis pages.

## Scenario Codes (S1–S4)

| Code | Meaning | Seeded engine |
|------|---------|---------------|
| S1 | **Decode** — interpret an incoming message or behavior | `wiki/playbooks/p2-subtext-decoder/` |
| S2 | **Respond** — craft a reply in a relationship context | `wiki/playbooks/p1-reply-engine/` |
| S3 | **Compose** — formal writing (email, letters, reports) | `wiki/playbooks/p3-formal-writing/` |
| S4 | **Prompt** — draft with AI assistance (prompt engineering) | `wiki/playbooks/p4-ai-prompting/` |

## Lane Contract

`zh.md` / `en.md` / `ms.md` are **NATIVELY authored lanes, NOT translations**. Never translate one lane into another: each lane is written from scratch in its own language, with examples and phrasing natural to that language's speakers. A lane may *mention* equivalents from other lanes, but its entries stay in its own language.

Each lane file must carry this header line, verbatim, right after the frontmatter:

```
LANE — authored natively, NOT a translation
```

Per-entry shape (a lane file is a sequence of such entries):

```markdown
### <signal/phrase>

**Context** — when/where this signal typically occurs (relationship, channel, stakes).

**Reading** — what it plausibly means; give 1–3 candidate readings when ambiguous.

**Response options**
1. ...
2. ...
3. ...

**Pitfalls** — common misreads or mistakes.

**Examples** — real or constructed exchanges. Label `constructed example` unless captured in raw/.
```

- Response options: exactly 2–3 per entry.
- The `### <signal/phrase>` heading is the entry's identity and its lint unit; keep it short and quotable.
- `core.md` entries are freer in shape (definitions, models, evidence sections) but must be clearly structured with `##`/`###` headings so the entry count is countable.

## Depth Floors

Per topic folder (lint checks all of these):

- `core.md`: ≥ 10 structured entries AND ≥ 1000 words.
- `zh.md`: ≥ 10 entries. `en.md`: ≥ 8 entries. `ms.md`: ≥ 8 entries.
- Every wiki file ends with a `## Sources` section containing **≥ 3 URL citations** (tiered, see below).
- `raw/<topic-id>/` contains **≥ 3 captures**.

A topic's status is `complete` only when all floors pass (see index statuses below).

## Anti-Fabrication Rules

1. **Named studies, statistics, quotes, and specific cultural rules MUST trace** to a `raw/` capture or a `## Sources` URL. If you cannot trace it, do not state it as fact.
2. Practice advice may be uncited but MUST be labelled `Practice heuristic`.
3. Evidence-backed claims MUST be labelled `Evidence-backed` (with the trace in `## Sources`).
4. Invented dialogues/exchanges MUST be labelled `constructed example`.
5. Source tiers: **1** = official/academic; **2** = established media/book; **3** = community/anecdote. Tier-3-sourced claims MUST be marked `anecdotal`.
6. `c8-astrology-heuristics` MUST contain a `## Skeptical evidence` section stating that **astrology has no demonstrated predictive validity**. Its content is framed as heuristics people actually use to read others — never as valid prediction.

## Workflows

### Ingest (capture raw → write wiki → append log)

1. **Capture** the source into `raw/<topic-id>/` (dated filename + header: URL, date, tier). Never modify existing captures.
2. **Write** the wiki files in `wiki/<cluster>/<id>/`: update `core.md` and the affected lanes, respecting the lane contract, depth floors, and anti-fabrication rules. Update `updated:` in frontmatter.
3. **Router**: update the topic's entry in `router.json` (triggers / scenarios / see_also) — prefer emitting a `router-patch.json` fragment and merging (see Router patches).
4. **Index**: flip the topic's `index.md` row status (`pending` → `seeded` → `complete`).
5. **Log**: append `## [YYYY-MM-DD] ingest | <topic-id or source title>` to `log.md`.

A single source may touch several files across a topic folder; it rarely touches other topics.

### Query (router resolution)

Fast path: `python3 tools/ask.py "<question>"` runs steps 2–5 below in one offline command
(`--full` escalates to core+lane, `--json` is structured, `--save "<answer>"` caches).

1. Load `always_load` from `router.json` (`wiki/synthesis/00-how-to-use.md`).
2. **Cache first** — for a recurring question, try the exact-match cache: `python3 tools/cache.py get "<question>"` (hit → serve, zero topic-load). After answering, `python3 tools/cache.py put "<question>" "<answer>" --source <wiki/path>`.
3. **Language**: `lang_default` is `"auto"` — match the user's language to a lane (`zh` / `en` / `ms`); on ambiguity fall back to `core.md`.
4. **Intent**: match the user's request against entry `triggers` (and `scenarios` codes); direct S1/S3/S4 dispatch goes through `engines`. Best-scoring entry wins.
5. **Escalate cheaply** — read the topic's `sidecars/cards.json` card first (~400 tok); load `core.md` + the lane only when the card is not enough. Then anything in `see_also`.
6. **Answer** with citations into the KB (`[[...]]` paths). Good answers can be filed back as synthesis pages — queries compound knowledge too.

### Router patches

Writers do not hand-edit `router.json` wholesale. They emit `router-patch.json` fragments that get merged:

```json
{"op": "update", "id": "c1-subtext-implicature", "set": {"triggers": ["潜台词", "subtext"], "scenarios": ["S1", "S2"]}}
```

`op` is one of `update` | `add` | `remove`. After every merge, `router.json` must remain valid JSON (validate with `python3 -c "import json;json.load(open('router.json'))"`).

**After any `triggers`/entry change, regenerate the compact index**: `python3 tools/build_router_index.py`. The resolver loads `router-index.json` (≈1/3 the tokens of `router.json`); `tools/build_router_index.py --check` fails if it drifts, and `tools/check.sh` runs that check. `router.json` stays the source of truth for patches and lint.

### Lint

Run `python3 tools/lint_kb.py` from the skill root. It checks:

- Frontmatter: all fields present and valid (`id`/`title`/`type`/`lang`/`tags`/`scenarios`/`sources`/`related`/`created`/`updated`).
- Lane header `LANE — authored natively, NOT a translation` present in every `zh.md`/`en.md`/`ms.md`.
- Entry counts and `core.md` word count against the depth floors.
- `## Sources` with ≥ 3 URLs in every wiki file; ≥ 3 captures in every `raw/<topic-id>/`.
- Label hygiene: unlabelled statistics/studies/quotes; tier-3 claims missing `anecdotal`; `c8-astrology-heuristics` missing `## Skeptical evidence`.
- Consistency: `router.json` entries ↔ `index.md` rows ↔ wiki folders.

Fix failures before marking a topic `complete` in `index.md`.

**Lint does NOT test recall.** It verifies structure only — a topic can pass lint yet be unreachable from a natural phrasing. After any `triggers` change (and before marking work done), run the recall gate `python3 qa/router-smoke.py` (curated query → expected topic id; exit 1 on regression). Add a case whenever a real miss is fixed.

### Index regeneration

`index.md` is regenerated from `wiki/` + `router.json`: walk `wiki/<cluster>/<id>/`, read frontmatter, and emit one row per topic in the matching section table (Concepts / Scenarios / Cultures / Playbooks / Synthesis). Status per row: `pending` (folder empty) → `seeded` (files exist but below floor or lint-failing) → `complete` (all floors pass). Never delete the section tables themselves.

## Conventions

- **Wikilinks**: `[[concepts/c1-subtext-implicature/core]]` path-style, `[[Page#Section]]` deep links, `[[Page|alias]]` aliases.
- **Dates**: `YYYY-MM-DD` everywhere (frontmatter, log, raw capture headers).
- **File naming**: lowercase with hyphens; raw captures `<slug>-<YYYY-MM-DD>.<ext>`.
- **Status values** (`index.md`): `pending` | `seeded` | `complete`.

### Log Format

Append-only. Each entry: `## [YYYY-MM-DD] <type> | <title>`; types: `schema`, `ingest`, `query`, `lint`, `gap`. Parseable via `grep "^## \[" log.md | tail -5`.

## Content freshness

The KB is an offline snapshot; it does not self-update. Currency is managed explicitly:

- Every `raw/` capture header must carry `capture date:` (YYYY-MM-DD) and `source tier:` (1–3).
- Run `python3 tools/freshness.py` to list captures past the staleness window (default 18 months) as re-crawl candidates, plus the per-tier coverage. `--strict` exits non-zero; `--months N` tightens the window; `--all` lists every stale capture.
- Cadence: run monthly. Re-crawl tier-1/2 theory sources at ~18 months; fast-moving topics (platform mechanics, AI prompting, chat-app behaviour) at ~6 months.
- Supersede, don't edit: when a source changes, add a **new** dated capture and note `supersedes …` in `## Sources`; never mutate existing `raw/` files.
- Full procedure (offline-first/online-enrich model, adding topics, the ingest workflow): `wiki/synthesis/updating-the-kb.md`.

## Maintenance

After each session: update `log.md`, `index.md`, and `Active.md` (open questions, gaps, priorities). Whenever you touch content, run the full health check `bash tools/check.sh` (**lint + router-smoke + freshness**). Periodically: review synthesis pages and resolve one `Active.md` question at a time.
