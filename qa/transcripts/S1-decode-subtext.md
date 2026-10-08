# QA dry-run — S1 decode-subtext (SC4) | KB: communication-master | 2026-10-07

## 1. User message (verbatim, zh lane)

> 老板刚在微信上给我发：「你要加班吗？如果不想也没关系，你开心就好。」
> 这话什么意思？是不是在暗示什么？帮我解码一下。

## 2. Router resolution (per `wiki/synthesis/00-how-to-use.md` §b)

- `always_load` loaded first: `wiki/synthesis/00-how-to-use.md` (router.json `"always_load": ["wiki/synthesis/00-how-to-use.md"]`).
- Language: user writes 中文 → zh lane (`lang_default: "auto"`).
- Trigger matching against `router.json` `entries[].triggers` — every match below was verified by grep in `router.json`:
  - `"什么意思"` → entry **p2-subtext-decoder** (triggers include `"解码"`, `"他什么意思"`, `"什么意思"`, `"暗示"`)
  - `"暗示"` → entries **c1-subtext-implicature** AND **p2-subtext-decoder** (both list `"暗示"`)
  - `"解码"` → **p2-subtext-decoder**
  - `"老板"` → **sc1-workplace-power**
  - `"微信"` → **sc7-digital-messaging**
- Best-scoring entry: **p2-subtext-decoder** (3 trigger hits) + direct engine dispatch: `router.json` `"engines": {"S1": "wiki/playbooks/p2-subtext-decoder/"}`.
- Resolved paths exist on disk (SC2: `paths.core` + lane `zh` verified with `ls`).

## 3. Files loaded

| # | Path | Role |
|---|------|------|
| 1 | `wiki/synthesis/00-how-to-use.md` | always_load: resolution + confidence rules |
| 2 | `wiki/playbooks/p2-subtext-decoder/core.md` | S1 engine: 7-step procedure + S1 output format |
| 3 | `wiki/playbooks/p2-subtext-decoder/zh.md` | zh lane: signal phrase entries |
| 4 | `wiki/concepts/c1-subtext-implicature/core.md` | theory base (implicature, face, FTA) |
| 5 | `wiki/concepts/c1-subtext-implicature/zh.md` | zh lane: 「你开心就好」entry |
| 6 | `wiki/scenarios/sc1-workplace-power/zh.md` | router-matched (老板); context only, no claim drawn |
| 7 | `wiki/scenarios/sc7-digital-messaging/core.md` | router-matched (微信); context only, no claim drawn |

## 4. Answer (zh lane, per `p2-subtext-decoder/core.md` 「S1 输出格式（硬性）」)

**Step 1 复述字面（Layer 1 only）** — 上级在微信文字渠道发来一句问句：是否愿意加班，并附"不想也没关系、你开心就好"的免责表述。未加解释。

**Step 2 语境槽位（缺项如实标注）** — Channel=微信文字（tone 全丢）；关系与权力差=上级↔下级（P 高）；历史模式=**KB 不持有你领导过去 48 小时的行为记录，此槽位必须由你补充，本解读不编造**；tone=文字渠道无副语言，见下方 cues。

【解读】（≥2 候选，全部列出并给置信度，不强行收敛）

- **Reading A（literal，真诚的软性退出）**：他真的随你——不想加就不加，没有后续含义。 — confidence **中**（字面成立，但 p2 core Step 5 规则："诉求与权力差相悖（如上级发）而字面极好 → 中"）
- **Reading B（subtext，面子保全式压力）**：面子留给你、压力留给你——他其实希望你答"加"，"你开心就好"是官方退路；你若答"不加"，等于自己上不了道。 — confidence **中**（p2 core 高信号短语库原行："你要加班吗？…你开心就好 | 面子留出口、压力留给你 | 官方退路=压力试探"）
- **Reading C（中性试探工作量预期）**：他在探你对工作量的态度，为后续排期收集信息，非逼站队。 — confidence **低**（来自 c1 core 对本句的 constructed example 演示，仅作候选）
- R-worst（操纵/试探记录态度）核查：p2 core 要求最坏解读"写入但常给低置信"；c9 的操纵信号（反复制造模糊、拖延消息）在本条**无证据可称重**，故不展开——KB 无本领导个人历史的素材，不做人品断言（p2 core 反 Failsafe："不做人品断言"）。

**判别 cues（来自 KB，可自查）**
- 真诚版的语言标记：c1 core 指出"'你开心就好'……真诚版会补一句'因为你开心我就开心'"——本条无此补充。`Evidence-backed`（tier-3 源，anecdotal）
- 语气判别依赖现场，而文字渠道恰恰没有语气：c1 core："同一句'行，你开心就好'，配上笑意是宠溺，配上长叹是失望，配上冷笑是反话"；c1 zh（同短语条目）："文字渠道没有语气，风险更高"。
- 判别点（discriminator）是你领导的 baseline 与近期事件（过去 48 小时 / 过去 3 次同样说法后发生了什么）——p2 core Step 2 第 4 槽位。此信息在消息里不存在，只能由你补。

【三个回复选项】（恰好 3 条，每条至少引 1 个 KB 路径；条文出自 `p2-subtext-decoder/zh.md` 「你要加班吗？……你开心就好」条目）

1. **直接问标准**："这次工作量上是否需要我排进去？我可以加。" — cites `wiki/playbooks/p2-subtext-decoder/core.md`
2. **条件式（兼容两种读法，留退路）**："手头 A 完成后我可以加 B，不冲突就排。" — cites `wiki/concepts/c1-subtext-implicature/core.md`
3. **澄清式（把损失面最小的试探丢回去）**："想确认下进度优先级：B 是必须本周还是可以缓？" — cites `wiki/playbooks/p2-subtext-decoder/core.md`

选项策略分工依据 p2 core Step 6："选项 1 用字面层接住（安全资产）；选项 2 兼容最可能的潜台词；选项 3 是试探或澄清。不是让你三选一部署，而是把三态摊给用户。"

【是否该提问代替猜测】**YES** — 触发理由：Reading A 与 B 置信同为"中"，两候选置信差 ≤2 档、无法分出主次（p2 core Step 7 条件①）；判别所需的历史模式槽位（48 小时 / 前 3 次同类说法的后续）为空，KB 不允许编造填充。`Practice heuristic`

**Pitfalls**（p2 zh 原文）：把 Reading B 当 Reading A，直接答"不加班"而失去信用；反过来反复追问则显得不敢表态。

## 5. Citation block（每条引用均给出 KB 内实际存在的一行原文）

| KB file | Quoted line (verbatim) | Supports | Label |
|---|---|---|---|
| `wiki/synthesis/00-how-to-use.md` | "歧义规则：一条消息存在 >= 2 个合理解读时，输出全部候选并给置信度，不强行收敛为一种。" | multi-reading output | Evidence-backed (KB rule) |
| `wiki/playbooks/p2-subtext-decoder/core.md` | "你要加班吗？…你开心就好 \| 面子留出口、压力留给你 \| 官方退路=压力试探" | Reading B | Evidence-backed entry in phrase table (pattern claim = Practice heuristic) |
| `wiki/playbooks/p2-subtext-decoder/zh.md` | "1) 真心的软性退出：确实随你；2) 面子留给你、压力留给你的合规试探：他其实希望你说'加'。" | Readings A/B | constructed example (entry's own example) |
| `wiki/concepts/c1-subtext-implicature/core.md` | "(a) 真诚 opt-out，(b) 面子保全式压力——先给拒绝的台阶再看你会不会上道，(c) 中性试探工作量预期" | Reading C + discriminator logic | constructed example |
| `wiki/concepts/c1-subtext-implicature/zh.md` | "文字渠道没有语气，风险更高。" | tone-loss cue | constructed example entry (Baidu usage note = anecdotal) |
| `wiki/scenarios/sc1-workplace-power/zh.md` | loaded via router (trigger `"老板"`); no claim drawn in this answer | — | — |
| `wiki/scenarios/sc7-digital-messaging/core.md` | loaded via router (trigger `"微信"`); no claim drawn in this answer | — | — |

## 6. SC4 statement

No external search was performed; every claim above traces to a `wiki/` path quoted in §5. Where the KB holds no data (leader's personal 48-hour history), the transcript says so instead of inventing content — as required by `AGENTS.md` Anti-Fabrication Rules ("If you cannot trace it, do not state it as fact").

**Verdict: PASS** — 3 readings ≥ 2 ✓；exactly 3 reply options ✓；every option cites an existing `wiki/` path ✓；zh lane used natively (options quoted from `p2-subtext-decoder/zh.md`, not translated from en) ✓。
