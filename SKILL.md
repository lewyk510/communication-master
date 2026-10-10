---
name: communication-master
description: Trilingual (中文 / English / Bahasa Malaysia) communication and reply knowledge base. Load this whenever the user needs to decode what someone really means (subtext / 弦外之音 / hint), understand a social or workplace situation, or draft a reply — including hard conversations, workplace/power dynamics, romance, family, Malaysian multi-ethnic etiquette, human-to-AI prompting, and formal complaint / appeal / application letters. Malaysia-first, with global and Chinese material.
---

# Communication Master

A trilingual knowledge base for understanding people and crafting replies. Three language
lanes (**zh** / **en** / **ms**) are authored natively — they are *lanes, not translations*.

## When to use
- "Ta 在暗示什么 / 他这话什么意思？" → decode subtext
- "我该怎么回这句话？" → draft options
- "上司/客户/家人这样说…" → situation + power/culture read
- "写一封投诉/申诉/申请信" → formal letter
- "怎么让 AI / 客服机器人 / AI 网站做我要的事" → prompt patterns

## How to use (router)
0. **One command does the whole flow** (offline, no API):
   `python3 tools/ask.py "<question>"` → cache → route → digest card; add `--full` to also
   print `core.md` + the language lane, `--json` for structured output, `--save "<answer>"` to cache.
1. Read `wiki/synthesis/00-how-to-use.md` (always load — resolution procedure, confidence rules, ethics).
2. Match the user's message against `router-index.json` (compact matching index:
   `id` / `dir` / `scenarios` / `triggers`). `router.json` is the full source of
   truth for patches; answer from the winner's `dir`. If nothing matches, run the
   **Layer-1.5 intent fallback** (`router.json.intents`: `decode`→S1, `reply`→S2)
   before falling back to a clarifying question.
3. **Cheapest first.** Resolve the topic, then escalate only as far as needed:
   - **Exact cache** — for a recurring question, check for an answer first:
     `python3 tools/cache.py get "<question>"` (hit → serve with zero topic-load; it is
     auto-invalidated when KB content changes). After answering, file good answers back
     with `python3 tools/cache.py put "<question>" "<answer>" --source <wiki/path>`.
   - **L1.5 digest card** — `sidecars/cards.json` holds one ~400-token card per topic
     (title + TL;DR + entry headings). Enough for a light question or a "do I need this?" call.
   - **Full load** — `core.md` + the user's language lane (`zh`/`en`/`ms`) when the card is not enough.
4. For engines: S1 subtext → `wiki/playbooks/p2-subtext-decoder/`; S3 letters → `p3-formal-writing/`;
   S4 AI → `p4-ai-prompting/`.
5. If the situation is ambiguous or cross-cultural, DO NOT guess — ask the targeted questions from
   `wiki/cultures/cu4-cross-cultural-general/`.

## Structure
- `router-index.json` — compact matching index (generated; load this to route)
- `router.json` — full trigger → file map / source of truth (patches, lint)
- `sidecars/cards.json` — per-topic digest cards (generated; the L1.5 light-load path)
- `cache/` — local exact-match answer cache (git-ignored; auto-invalidated by KB fingerprint)
- `index.md` — human catalog
- `wiki/{concepts,scenarios,cultures,playbooks,synthesis}/` — the knowledge body
- `raw/` — captured sources (immutable)
- `AGENTS.md` — schema, conventions, anti-fabrication rules
- `commands/` — `/decode` `/reply` `/draft` `/prompt`
- `qa/` — frozen scenarios + proof transcripts

## Rules
See `AGENTS.md`. Every specific claim is sourced; constructed examples are labelled; astrology is
framed as a cultural heuristic with skeptical evidence; practice advice is labelled as heuristic.
