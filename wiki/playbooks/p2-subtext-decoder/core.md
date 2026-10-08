---
id: p2-subtext-decoder
title: Subtext Decoder · 潜台词解码器
type: playbook
lang: core
tags:
  - pragmatics
  - decode
  - s1
scenarios:
  - S1
sources:
  - raw/p2-subtext-decoder/f-grice-implicature-2026-10-07.md
  - raw/p2-subtext-decoder/f-searle-indirect-speech-acts-2026-10-07.md
  - raw/p2-subtext-decoder/f-direct-indirect-communication-2026-10-07.md
  - raw/p2-subtext-decoder/f-malay-indirect-communication-2026-10-07.md
  - raw/p2-subtext-decoder/f-culturally-dependent-no-2026-10-07.md
  - raw/p2-subtext-decoder/f-decode-his-text-2026-10-07.md
related:
  - "[[concepts/c1-subtext-implicature/core]]"
  - "[[concepts/c6-nonverbal/core]]"
  - "[[concepts/c11-paralanguage/core]]"
  - "[[concepts/c13-visual-semiotics/core]]"
  - "[[concepts/c9-manipulation-defense/core]]"
created: 2026-10-07
updated: 2026-10-07
---

# 潜台词解码器 · Subtext Decoder

可执行的 S1 引擎：收到一条消息或行为，按下面七个步骤产出一份**多假设解读 + 恰好 3 个回复选项**的结构化输出。它是程序，不是描述性文章——每一步都要真实执行。

理论根基：会话含义（conversational implicature，Grice；见 [[concepts/c1-subtext-implicature/core]]）解释了"说的怪 → 意思在别处"为什么可推断；间接言语行为（indirect speech acts，Searle）解释了"问题的形式请求的内容"（*Can you pass the salt?* 字面是疑问句，实际是指令）。Evidence-backed：两者的原始论证见 raw captures（SEP implicature 条目；Searle 1979 章）。

### 引擎总流程

七步：复述字面 → 收集语境 → 列候选解读 → 称证据重量 → 置信度 → S1 输出 → 决定是否该提问。任何一步缺失，输出就不合格。全程假设：**先给最无聊的解释（boring wins most of the time，Practice heuristic，trace: f-decode-his-text）**。

### Step 1 — 复述字面

把消息按三个层拆开（Evidence-backed）：Layer 1 = 实际打出来的字；Layer 2 = 结合对方模式与最近 48 小时的"大概率意思"；Layer 3 = 你自己的神经系统加的戏。第一步只写 Layer 1：逐字复述，不解释。这步的作用是防止把 Layer 3 伪装成解读。

### Step 2 — 收集语境

五个槽位，缺一条就降低最终置信度：

1. **Channel**（文字 / 电话 / 面对面 / 第三人转述）
2. **关系与权力差**（上级↔下级 / 客户↔供应商 / 平辈 / 家人）
3. **文化底色**（直接文化 vs 高语境文化；见下文「文化层与高语境」）
4. **历史模式**（对方过去 48 小时 / 过去 3 次同样说法之后发生了什么）
5. **Tone 与副语言**（标点、延迟、省略词；线上则看 emoji/withdraw 模式）— 详见 [[concepts/c11-paralanguage/core]]、[[concepts/c6-nonverbal/core]]、[[concepts/c13-visual-semiotics/core]]。

### Step 3 — 列 ≥2 候选解读

最少两条，推荐三条：

- **R-literal**：字面（或最无聊）解读。
- **R-subtext**：结合语境最可能的潜台词（例如 S1 例句里"面子上放你走、实际希望你留下加班"的压力式读法）。
- **R-worst**：最坏情况解读（操纵、试探、逐客、警告），写入但常给低置信。

先列后称重，顺序不可反——先称重会锚定第一条情报。

### Step 4 — 逐条称证据

对每个候选回答三问（Practice heuristic）：**支持它的证据有什么？反对它的证据有什么？哪个证据是关键判别点（discriminator）？** Searle 式方法：如果字面句式（疑问）与其语力（请求/命令）方向一致则记为支持 R-subtext；文化准则也参与称重——高语境="不直接说不"会抬高潜台词化解读的先验（见下文「文化层与高语境」）。

### Step 5 — 置信度

每条候选给高 / 中 / 低（够用就行，不做伪精度）。规则：字面 + 文化先验同向 → 高；诉求与权力差相悖（如上级发）而字面极好 → 中；仅靠 Layer 3 的感受支撑 → 低并标注[Past pattern only, unverified]。

### S1 输出格式（硬性）

S1 场景的最终产出**必须**是以下结构，缺一即失效：

```
【解读】
- Reading A（literal）: <句子> — confidence <高/中/低>
- Reading B（subtext）: <句子> — confidence <高/中/低>
- Reading C（worst case）: <句子> — confidence <高/中/低>

【三个回复选项】（恰好 3 条，每条至少引 1 个 KB 路径）
1. <直球式回复 + 理由> — cites [[…]]
2. <条件式回复（接受其一解读并留退路）> — cites [[…]]
3. <澄清式回复（把损失面最小的试探丢回去）> — cites [[…]]

【是否该提问代替猜测】 YES/NO + 一句触发理由
```

### Step 6 — 输出执行

三个选项的策略分工固定：选项 1 用字面层接住（安全资产）；选项 2 兼容最可能的潜台词（答复遣句交给 [[playbooks/p1-reply-engine/core]]）；选项 3 是试探或澄清。**不是让你三选一部署，而是把三态摊给用户**。

### Step 7 — 提问代替猜测

满足任一条 → 输出【是否该提问】= YES：① 两候选置信差 ≤2 档，无法分出主次；② 后果不对称（猜错代价大：合同、辞退、感情决断）；③ 对方是不可逆的人脉节点。否则声明"已给出 best-effort 解读，默认采纳字面+低置信标注"。

### 高信号短语库（zh 侧节选）

zh 完整库在 [[playbooks/p2-subtext-decoder/zh]]；en 在 [[playbooks/p2-subtext-decoder/en]]；ms 在 [[playbooks/p2-subtext-decoder/ms]]。此处只放跨语言通用的 4 条：

| 短语 | 首选读法 | 家族 |
|---|---|---|
| 你要加班吗？…你开心就好 | 面子留出口、压力留给你 | 官方退路=压力试探 |
| 随便 / 都行 | 当着上级说 = 别擅自决定 | 表面放权 |
| "Would be great if someone could…" | 有人=是你 | Searle 指令式 |
| "nanti kita fikirkan dulu" / "回头再议" | 多半 = 礼貌的不 | 悬置式婉拒（Evidence-backed：malay capture） |

### Tone-dropping channels（文字 vs 电话对照表）

字面丢 tone 是 channel 降维的产物。Practice heuristic 对照：

| 维度 | 文字消息 | 电话 / 面对面 |
|---|---|---|
| 副语言信号 | 全部丢失（除 emoji） | 音质 / 语速 / 停顿全在 |
| 时延 | 延迟本身成为信号 | 无 |
| 危险区域 | 短句被读成冷漠 | 语气被现场放大 |
| 补偿策略 | 假设最无聊解释；延迟 ≤ 对方 baseline 才计入信号 | 优先信 paralanguage 而非措辞 |

claim `Most misreads in text channel come from tone loss` — Practice heuristic，anecdotal 级（tier-3 source: f-decode-his-text）。暗号类误读（"可以聊一下吗"在文字里被读成坏消息）请配套 [[concepts/c9-manipulation-defense/core]] 里的台面识别检查（对方是否利用模糊制造焦虑）。

### 文化层与高语境

Evidence-backed（f-direct-indirect-communication，引用 Peace Corps 资料）：间接交际文化的首要目标是 harmony 与 saving face；因此在这些文化里"没说不"≠"说是"。证据（f-malay-indirect-communication）：马来交际以"语言有 lapik（衬里/礼护）"为常态，样例如 *nanti kita fikirkan dulu*（回头再议）、*"barangkali elok juga kalau begini"* 通常不是犹豫，而是保住社会体面的"不"。中文同构："回头联系"、"再说"、"我考虑一下" 常是软拒。所以 Step 2 的文化槽位在高语境一侧时，把 R-subtext（软拒类）默认上调一档；反过来在直接文化（如美式员工来信）不要过度把礼貌句读成压力。

### 何时此引擎会让位给其他引擎

1. 对方明显在布局操纵（反复制造模糊、拖延消息）→ 交给 [[concepts/c9-manipulation-defense/core]] 检查是否 Fog / 间歇性强化，解码结果改标 "strategic ambiguity suspected"。
2. 信号在非语言层（表情、站位姿态、语调）→ [[concepts/c6-nonverbal/core]]、[[concepts/c11-paralanguage/core]]、[[concepts/c13-visual-semiotics/core]] 各自承担，本引擎只收其输出作 Step 2 的 tone 输入。
3. 需要遣句而不是解码 → 下一步交给 [[playbooks/p1-reply-engine/core]] 展开遣句。

### 反 Failsafe

- 不是所有消息都要三候选：某些讯息永远只有字面一条读法（如收据、纯故障报备）， engine 允许输出单读法 +【不需要解码】标记，不算失败。
- 不给心理病史：Step 2 的历史槽位只用**发生在对话里的**过去事件，不做人品断言。

## Sources

Tier 1 (academic/official):
1. Implicature — Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/implicature/ （src capture: raw/p2-subtext-decoder/f-grice-implicature-2026-10-07.md）
2. Searle, *Indirect Speech Acts* (chapter PDF). https://www.flf.vu.lt/dokumentai/Searle_indirect_speech_acts.pdf （capture: raw/p2-subtext-decoder/f-searle-indirect-speech-acts-2026-10-07.md）
3. Joyce, C., *The Impact of Direct and Indirect Communication* (Univ. of Iowa Conflict Management, citing Peace Corps). https://conflictmanagement.org.uiowa.edu/sites/conflictmanagement.org.uiowa.edu/files/2020-01/Direct%20and%20Indirect%20Communication.pdf （capture: raw/p2-subtext-decoder/f-direct-indirect-communication-2026-10-07.md）
4. *Komunikasi berlapik dalam budaya Melayu* (Nusantara: J. for Southeast Asian Islamic Studies, UIN Suska, 2025). https://ejournal.uin-suska.ac.id/index.php/nusantara/article/download/38451/13120 （capture: raw/p2-subtext-decoder/f-malay-indirect-communication-2026-10-07.md）

Tier 2 (established practitioner media):
5. Culture Coach, *Cultural No in Cross-Cultural Business*. https://www.culturecoach.biz/post/the-culturally-dependent-no-in-cross-cultural-business-interactions-learn-to-decipher-all-the-way （capture: raw/p2-subtext-decoder/f-culturally-dependent-no-2026-10-07.md）

Tier 3 (community/anecdote — treat as `anecdotal`):
6. Olively, *Decode His Text*. https://www.olively.app/learn/decode-his-text （capture: raw/p2-subtext-decoder/f-decode-his-text-2026-10-07.md；三层模型与 "48 小时 / 最无聊解释" 启发式引自此文，标注 anecdotal-adjacent practice）
