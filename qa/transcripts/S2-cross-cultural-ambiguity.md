# QA dry-run — S2 cross-cultural-ambiguity (SC4) | KB: communication-master | 2026-10-07

## 1. User message (verbatim, mixed zh/en)

> My Malay colleague in the KL office replied to my leave request with
> "nanti kita fikirkan dulu" — 他这是答应了还是委婉拒绝？怎么回比较好？
> Is this a cross-cultural thing I'm misreading?

## 2. Router resolution (per `wiki/synthesis/00-how-to-use.md` §b + §d)

- `always_load`: `wiki/synthesis/00-how-to-use.md`. Language: mixed zh/en → resolve zh segments on the zh lane, English segments on the en lane; ambiguity falls back to `core.md` (`lang_default: "auto"`).
- Trigger matches (each verified by grep against `router.json`):
  - `"怎么回"` → entry **p1-reply-engine** (triggers include `"怎么回"`, `"回复"`, `"回消息"`, `"帮我想个回复"`, `"reply"`, `"respond"`, `"draft a reply"`, `"balas"`, `"cara membalas"`)
  - `"cross-cultural"` → entry **cu4-cross-cultural-general** (triggers include `"跨文化"`, `"文化差异"`, `"高语境"`, `"cross-cultural"`, `"culture shock"`, `"high-context"`, `"low-context"`, ...)
- Best-scoring entry: **p1-reply-engine** (S2 engine: `router.json` `"engines": {"S2": "wiki/playbooks/p1-reply-engine/"}`), with **cu4-cross-cultural-general** co-resolved because the request is explicitly cross-cultural.
- Escalation rule applied instead of a single answer: `00-how-to-use.md` §d — "涉及 cu1-cu5 而背景信息不足时，**先提问再作答**。提问用 `wiki/cultures/cu4-cross-cultural-general/` 的针对性问题清单"。Same rule in `SKILL.md` step 5: "If the situation is ambiguous or cross-cultural, DO NOT guess — ask the targeted questions".

## 3. Files loaded

| # | Path | Role |
|---|------|------|
| 1 | `wiki/synthesis/00-how-to-use.md` | always_load; cross-cultural ask-first rule |
| 2 | `wiki/playbooks/p1-reply-engine/core.md` | S2 engine: decision tree, probe strategy |
| 3 | `wiki/cultures/cu4-cross-cultural-general/core.md` | S2 targeted-question bank (5 axes, 15 questions) |
| 4 | `wiki/cultures/cu4-cross-cultural-general/en.md` | en lane: ambiguous-signal entries |
| 5 | `wiki/cultures/cu1-malaysia-malay/core.md` | cu4 see_also; Malaysia time/indirectness calibration |
| 6 | `wiki/playbooks/p2-subtext-decoder/core.md` | p1 core §2.2 cross-link; phrase-bank row for "nanti kita fikirkan dulu" |

## 4. Answer (mixed lane: zh for the user's zh questions, en material quoted from en lane)

**Explicit uncertainty first.** Per `cu4-cross-cultural-general/core.md` §S2 提问库: "与其拿'某国人就是那样'来猜，不如**先问用户拿到情境参数，再套框架**"，and its Pitfall line: "**永远不要**因为对方'是某国人'就直接输出单一读法。" I cannot tell you whether this is a yes or a no from the message alone — `Knowledge 只提供候选，证据只能来自这个人`（cu4 core §ambiguous 情境的操作纪律）。`Practice heuristic`

**Candidate readings (2–3, with confidence, per cu4 core 三步法 step 2):**

1. **Polite no / soft rejection** — `p2-subtext-decoder/core.md` phrase table row: "`nanti kita fikirkan dulu` / `回头再议` | 多半 = 礼貌的不 | 悬置式婉拒（Evidence-backed：malay capture）"。Confidence: 中-高 as a prior, pending your answers below. `Evidence-backed` (malay capture trace in p2 Sources)
2. **Genuine deferral to consult others / real scheduling constraint** — `cu4-cross-cultural-general/en.md` "Let me check and get back to you" entry: "Three candidates: a genuine check; a polite no …; a request for time to consult others, which indirect cultures expect before saying yes." Confidence: 中。`constructed example` entry carrying an Evidence-backed framework
3. **Face-buffer before conditions** — `cu4-cross-cultural-general/core.md` §直接 vs 间接表达: 把间接拒绝"当**三种候选之一**：① 真要再看 ② 礼貌性拒绝 ③ 需要先给面子/再铺垫"。Confidence: 低-中。`Practice heuristic`

Related calibration (not a verdict on this person): `cu1-malaysia-malay/core.md` notes Malaysia's loose time norms and that hedged answers are often non-commitments — "*boleh*（可以）是高频模糊肯定：它能表示「可以、能办」，也能只是「好吧、再说」的社交润滑"，and prescribes "收到模糊应答后用 WhatsApp 文字确认，给双方留修改余地，别当场逼承诺。" `Evidence-backed` (Cultural Atlas capture) for the time norm; `Practice heuristic` for the confirmation move; the "InsyaAllah 缓冲" reading is `anecdotal`.

**Targeted questions before any single interpretation** (selected from `cu4-cross-cultural-general/core.md` §S2 针对性提问库, verbatim items; cu4 en.md "Ambiguous cross-cultural signal" prescribes "Ask the user 3–5 targeted questions first, per core.md's S2 bank"):

1. 关系轴 Q1: "你认识对方多久了？第一层（同事/同学/客户）还是第二层（朋友/亲属/导师）？"
2. 权力轴 Q4: "对方在年龄、职位、资历上比你高、平、还是低？"
3. 利害轴 Q7: "这事对你是可以重来的，还是一次性的高风险（offer、合同、婚嫁）？"
4. 文化轴 Q10: "双方的第一语言/工作语言分别是什么？"（ELF 会话里很多"直"不是文化是词汇不够）
5. 文化轴 Q12: "对方是否常常表现出和你预期不符？之前有没有过例外？"

**Provisional reply while waiting for your answers** (low-commitment, from the KB; both `constructed example`-labelled entries):

- Checkpoint, not pressure — `cu4 en.md` "Let me check and get back to you", option 1: "Add a checkpoint rather than press: 'Shall I check back with you on Friday?'"
- Offer an out — same entry, option 2: "If it's not going to work, no worries, just let me know. This often converts a polite no into an honest one."
- Then follow cu1's move: confirm in writing on WhatsApp with 日期 + 交付物, without forcing an on-the-spot promise.

If your answers show the stakes are high (e.g. non-refundable travel), `p1-reply-engine/core.md` decision tree routes this to Strategy 6 Probe: "If two readings of M diverge AND stakes ≠ trivial → S6 probe" — one question that separates the readings.

**Out-of-bounds output** (refused, per cu4 core 硬纪律): "X 国人就是…… / people from X are always …" — 国家均值 ≠ 个人预测；刻板印象在个人证据面前让位。

## 5. Citation block

| KB file | Quoted line (verbatim) | Supports | Label |
|---|---|---|---|
| `wiki/synthesis/00-how-to-use.md` | "涉及 cu1-cu5 而背景信息不足时，**先提问再作答**" | ask-first protocol | Evidence-backed (KB rule) |
| `wiki/playbooks/p1-reply-engine/core.md` | "If two readings of M diverge AND stakes ≠ trivial → S6 probe" | probe routing | Evidence-backed (engine spec; styles = Mayo/PON captures) |
| `wiki/cultures/cu4-cross-cultural-general/core.md` | "**永远不要**因为对方'是某国人'就直接输出单一读法。" | uncertainty discipline | Practice heuristic |
| `wiki/cultures/cu4-cross-cultural-general/core.md` | "① 真要再看 ② 礼貌性拒绝 ③ 需要先给面子/再铺垫" | candidate readings | Practice heuristic |
| `wiki/cultures/cu4-cross-cultural-general/en.md` | "a genuine check; a polite no …; a request for time to consult others" | reading #2 | constructed example entry |
| `wiki/playbooks/p2-subtext-decoder/core.md` | "`nanti kita fikirkan dulu` / `回头再议` | 多半 = 礼貌的不 | 悬置式婉拒（Evidence-backed：malay capture）" | reading #1 | Evidence-backed |
| `wiki/cultures/cu1-malaysia-malay/core.md` | "收到模糊应答后用 WhatsApp 文字确认，给双方留修改余地，别当场逼承诺。" | provisional move | Practice heuristic (time norm = Evidence-backed; InsyaAllah = anecdotal) |

## 6. SC4 statement

No external search; every interpretation trace is a `wiki/` path quoted above. KB holds nothing about this specific colleague — stated as such, not filled in.

**Verdict: PASS (edge case)** — the KB correctly refuses a single reading, emits 3 candidate readings with confidence labels, and asks 5 bank questions verbatim from `cu4-cross-cultural-general/core.md`; the stereotype-ban rule was applied and surfaced to the user。
