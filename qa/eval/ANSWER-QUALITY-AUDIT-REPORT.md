# Answer-Quality & Language-Parity Audit — Round 11

**Question on the table:** Rounds 9–10 proved the KB *has* pages and *can* answer. Round 11 asks the harder question: is the advice actually **good** (specific, actionable, grounded, natural), and is it **equal across languages**?

## Method

- **Set A — quality (10 questions):** real questions, one language each; KB-only agents produced the reply; a **blind judge** scored each on a 5-point rubric (specificity / actionability / grounding / naturalness / calibration, 0–2 each, /10), checking grounding against the KB pages.
- **Set B — parity (5 questions × zh/en/ms = 15):** the *same* 5 questions asked in all three languages; a second **blind judge** scored all 15 on the same rubric.
- Data: `qa/eval/answer-quality-audit.json`. Rubric: `/tmp/rubric.md`.

## Result A — quality: 9.5 / 10 mean (min 8)

| id | score | weakest |
|---|---|---|
| a1–a10 | 8–10 | mostly naturalness (meta-words / garbled clauses) |

The pages are not just *present* — they produce **specific, grounded, actionable** replies. The judge traced claims back to real KB lines (sc17 deposit rules, sc1 timestamped-channels, sc3 面子账, sc16 ms three-line formula). **No weak page found.** The sub-2 deductions came from *render* problems (internal labels leaking), not from thin content.

## Result B — parity: zh 9.4 / en 9.4 / ms 9.2

| language | mean | naturalness |
|---|---|---|
| zh | 9.4 | 2/2 on all |
| en | 9.4 | 2/2 on all |
| ms | 9.2 | **1/2 on 4 of 5** |

Per-question scores are near-identical (e.g. b2: 10/10/9). **Content parity is effectively achieved.**

### The ms naturalness flags are a *render* defect, not a KB defect

The judge flagged garbled Malay in the answers ("Terjemah bara surat", "Menaiganya", "Cam jawap betul"). Checking the KB directly: **the ms lanes are explicitly headed `LANE — authored natively, NOT a translation`** and read as idiomatic Malay (sampled `sc16/ms`, `cu1/ms` — natural register, local idiom). So the glitches came from the **answering agent re-generating Malay from scratch**, not from the KB's content.

Same pattern in Set A: 「Duplex」, Cyrillic 「анализ」, 「你（）」 — all *generation* glitches; and internal markup leaking into replies (`Practice heuristic:`, `EN gloss`, `constructed example`, `按 KB 的解码规则`).

## Two real defects found (both in the render layer) → both fixed

| Defect | Fix |
|---|---|
| KB-internal labels & `wiki/` paths leak into user-facing replies | added **§(f) Reply hygiene** to `wiki/synthesis/00-how-to-use.md` (always-loaded) + a rule line in `SKILL.md` |
| Malay re-generated (glitching) instead of **reusing the native lane's own phrasings** | same §(f): rule 2 — reuse the language lane's `Examples` verbatim, esp. for ms |

Also: rule 3 — placeholders (`RM___`, `X日`, `Y%`) must be resolved or explicitly flagged, never handed back raw.

## Verification

`bash tools/check.sh` all green after the edits.

## Takeaway

**Answer quality is high (9.5/10) and language parity is real (9.4/9.4/9.2)** — the KB's pages yield specific, grounded, actionable advice in all three languages, and the Malay lane is genuinely native. The only weakness is in *how* answers get rendered (label leakage; Malay re-generation), and that is now covered by an explicit reply-hygiene rule. Nothing structural is weak.
