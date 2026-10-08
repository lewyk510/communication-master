---
description: Decode an incoming message or behaviour (S1). Produces >= 2 candidate readings with confidence labels, confirm/deny tests, and targeted questions when ambiguous. Engine: wiki/playbooks/p2-subtext-decoder/
---

# /decode · 潜台词解码（Subtext Decoder）

**用途**：用户收到一条消息、一个行为或一种态度，想知道「这到底是什么意思」。
**引擎**：`wiki/playbooks/p2-subtext-decoder/`
**配套**：`wiki/synthesis/modality-matrix.md`（选渠道相关主题）

## 输入

用户给出的原文（尽量逐字）+ 谁说的 + 对谁说的 + 大致情境。缺哪项就先问哪项，不要替用户编造上下文。

## 流程（按序执行）

### 1. 固定原文与渠道
逐字引用原话/原行为，不改写、不翻译。判定渠道属于哪一类（口头 / 书面 / 文字 / 语音 / 视频 / 视觉 / 非语言 / 公开），按 `wiki/synthesis/modality-matrix.md` 找到该渠道的解码主题。渠道本身改变含义：同一句话，语音里的停顿（c11）和文字里的标点/表情（c13）走的是不同信号系统。

### 2. 定位关系与权力
回答三个问题：双方谁更依赖谁？这次互动谁承担更大风险？之前有没有未结的恩怨或请求？
- 职场上下级 → `wiki/scenarios/sc1-workplace-power/`
- 亲密关系 → `wiki/scenarios/sc2-romance-intimacy/`
- 家庭亲戚 → `wiki/scenarios/sc3-family-kinship/`
- 服务/买卖 → `wiki/scenarios/sc9-live-service/`、`wiki/scenarios/sc10-negotiation-deals/`
- 群体/公开 → `wiki/concepts/c15-group-team-communication/`、`wiki/scenarios/sc14-online-social/`

权力不对称是读法分歧的最大来源：同一句「你决定就好」，上司说是授权，施加压力者说可能是测试。

### 3. 文化检查（不确定就停）
马来西亚语境优先：马来文化 `wiki/cultures/cu1-malaysia-malay/`、华人文化 `wiki/cultures/cu2-malaysia-chinese/`（面子、人情）、印度文化 `wiki/cultures/cu3-malaysia-indian/`、语码转换 `wiki/cultures/cu5-codeswitching/`。
高/低语境、直接/间接的通则在 `wiki/cultures/cu4-cross-cultural-general/`。
**规则**：如果发送方的文化背景未知，或消息刚好卡在两种规范之间，不要猜。先用第 7 步的问题清单向用户提问，拿到答案再继续解码。

### 4. 生成候选读法（至少 2 个）
按引擎 `wiki/playbooks/p2-subtext-decoder/` 的步骤拆解，读法必须有机制依据，不许凭空发挥：
- 字面说了什么 vs 实际推什么（会话含义）→ `wiki/concepts/c1-subtext-implicature/`
- 有肢体/表情/姿态信息时 → `wiki/concepts/c6-nonverbal-subconscious/`
- 有语音信息时：语调、停顿、语速 → `wiki/concepts/c11-paralanguage-prosody/`
- 有 emoji/表情包/图片时 → `wiki/concepts/c13-visual-multimodal/`
- 出现施压、愧疚绑架、忽冷忽热模式时 → `wiki/concepts/c9-manipulation-defense/`
- 公开文本、媒体稿、带节奏的内容 → `wiki/concepts/c18-propaganda-fallacies/`

### 5. 给每个读法标置信度
- **Evidence-backed**：线索就在原文/原行为里，且该线索的定义能在上面对应的主题文件中找到。
- **Practice heuristic**：基于常见情境的模式匹配，原文本身不足以确证。必须显式标注，不得当结论卖。

### 6. 写确认/否证清单
每个读法各列：什么后续观察会**支持**它、什么会**否证**它。可观察项举例：对方下一句怎么接、直接问一句后对方的反应、未来几天的行为一致性。没有可观察检验项的读法要降级为 heuristic。

### 7. 标注不确定性并提问
仍有歧义时，从 `wiki/cultures/cu4-cross-cultural-general/` 的问题清单里挑针对性问题问用户（典型维度：双方文化背景、过往互动模式、这次互动的前因、发送方的惯常风格）。**禁止**在歧义未消时强行输出单一读法。

### 8. 交接
用户还想知道「那我怎么回」→ 转 `/reply`。用户想写正式信件回应 → 转 `/draft`。

## 输出模板

```markdown
## 原文
（逐字引用）

## 渠道 / 关系 / 文化
- 渠道：（8 类之一，引用 modality-matrix 对应行）
- 关系与权力：（谁依赖谁，风险谁担）
- 文化语境：（cu1-cu5 中相关者；未知则标注「未确认」）

## 读法 A：【一句话概括】（置信度：高/中/低）
- 依据：（原文线索 + 引用的 KB 路径）
- 支持：… ｜ 否证：…

## 读法 B：【一句话概括】（置信度：高/中/低）
- 依据：（原文线索 + 引用的 KB 路径）
- 支持：… ｜ 否证：…

## 待确认问题（如有）
1. …（来自 cu4 的问题维度）

## 下一步
（/reply 或 /draft，或直接向对方求证的方式）
```

## 硬规则

1. 候选读法 **>= 2** 个，永不允许只给一种。
2. 每个读法必须带置信度标签（Evidence-backed 或 Practice heuristic）。
3. 每个读法的依据必须引用至少一个存在的 KB 路径。
4. 跨文化或高度歧义时：先问（cu4 问题清单），后解码。
5. 指控「操纵」需要 c9 的模式证据，不是凭一句重话；不足时只说「有施压迹象，需更多样本」。

## 引用

- 引擎：`wiki/playbooks/p2-subtext-decoder/`
- 核心机制：`wiki/concepts/c1-subtext-implicature/`、`wiki/concepts/c6-nonverbal-subconscious/`、`wiki/concepts/c11-paralanguage-prosody/`、`wiki/concepts/c13-visual-multimodal/`
- 风险识别：`wiki/concepts/c9-manipulation-defense/`、`wiki/concepts/c18-propaganda-fallacies/`
- 文化：`wiki/cultures/cu1-malaysia-malay/`、`wiki/cultures/cu2-malaysia-chinese/`、`wiki/cultures/cu3-malaysia-indian/`、`wiki/cultures/cu4-cross-cultural-general/`、`wiki/cultures/cu5-codeswitching/`
- 渠道路由：`wiki/synthesis/modality-matrix.md`
