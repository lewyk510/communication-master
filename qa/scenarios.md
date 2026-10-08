# QA Scenarios — FROZEN SPEC (v1, 2026-10-07)

**STATUS: FROZEN.** The inputs in this file are frozen verbatim and MUST NOT be
reworded, softened, translated, shortened, or "improved" by any future session.
If an input needs to change, write a NEW spec version file; never edit this one.

Transcripts produced against these scenarios go to `qa/transcripts/`. A
scenario PASSES or FAILS — there is no partial credit. Every pass criterion
below is binary and machine-checkable by a reader.

---

## System checks (SC1–SC5)

Each is binary. The dry-run session passes SC1–SC5 only if all five hold.

| ID | Check | Pass criterion (binary) |
|----|-------|-------------------------|
| SC1 | Skill loads | The `communication-master` skill loads without error: `SKILL.md`, `AGENTS.md`, `router.json` (if present) and `index.md` (if present) are all readable, and `python3 tools/lint_kb.py` runs to completion. |
| SC2 | Router resolves a concrete message | Given one concrete incoming message (any non-trivial message, e.g. the S1 input), the router path (router.json `always_load` + `triggers`/`scenarios` matching) resolves it to at least one entry, and the resolved entry's `paths`/lane files exist on disk. |
| SC3 | Topic coverage | At least **24** of the 25 topic folders under `wiki/` contain cited sources (`## Sources` with ≥ 3 URLs) and all three trilingual lanes (`zh.md`, `en.md`, `ms.md`) plus `core.md`. |
| SC4 | Transcripts use ONLY the KB | Each of the 3 transcripts (S1, S3, S4) is produced with the knowledge base as the only permitted reference: no external web search, no model priors presented as evidence. Every factual/claim citation inside the transcript traces to a KB file path under `wiki/` or `raw/`. |
| SC5 | Paste-ready quickstart | A paste-ready quickstart exists (a copy-pasteable block that tells a fresh session how to use the KB: load router → resolve → read lane → answer with citations), and it contains no placeholders. |

---

## S1 — Subtext decode

**Scenario code:** S1 (Decode). **Engine:** `wiki/playbooks/p2-subtext-decoder/`.

**FROZEN INPUT** (message from a superior, verbatim):

```
你要加班吗？如果不想也没关系，你开心就好。
```

**Pass criterion (binary — all must hold):**

1. The answer names **>= 2 plausible readings** of the message (e.g. at minimum:
   a genuine soft opt-out, and a face-preserving pressure to comply) — fewer
   than 2 readings = FAIL.
2. The answer gives **exactly 3 reply options** — more or fewer = FAIL.
3. Each of the 3 reply options cites **at least one KB file path** (a path
   under `wiki/` that exists). Zero citations on any option = FAIL.

---

## S3 — Complaint / appeal letter

**Scenario code:** S3 (Compose). **Engine:** `wiki/playbooks/p3-formal-writing/`.

**FROZEN INPUT** (verbatim):

```
我在马来西亚买了一张预付电话卡，未被告知有效期，充值后仍无法使用，我要求退款但被拒绝。请写一封正式的投诉/申诉信。
```

**Pass criterion (binary — all must hold):**

1. The output is an **end-to-end formal letter** containing all of: sender,
   recipient, date, subject, body, and a concrete demand (refund). Any missing
   element = FAIL.
2. The output includes an **escalation ladder** with at least the two rungs:
   provider first, then regulator (e.g. Malaysian regulator / consumer
   tribunal tier). A letter with no escalation path = FAIL.
3. The answer cites **KB files** (paths under `wiki/` that exist) supporting
   the letter's structure or phrasing. No citations = FAIL.

---

## S4 — AI prompting

**Scenario code:** S4 (Prompt). **Engine:** `wiki/playbooks/p4-ai-prompting/`.

**FROZEN INPUT** (verbatim):

```
我需要让一个客服聊天机器人真正帮我处理退款，而不是绕圈子。给我一个有效的提示词。
```

**Pass criterion (binary — all must hold):**

1. The output contains a **concrete, reusable prompt pattern** (copy-pasteable
   text with slots/variables where appropriate) — advice without the pattern
   itself = FAIL.
2. The output explains the **rationale** for why the pattern works (mechanism,
   not just assertion). No rationale = FAIL.
3. The output cites **at least one KB file path** (under `wiki/` that exists).
   No citation = FAIL.

---

## Dry-run protocol

1. Load the skill (SC1).
2. Resolve each frozen input through the router (SC2).
3. Answer S1, S3, S4 using ONLY the KB (SC4), saving each transcript to
   `qa/transcripts/`.
4. Verify coverage and quickstart (SC3, SC5).
5. A dry-run PASSES only if SC1–SC5 all hold AND all three scenarios pass
   their binary criteria above.
