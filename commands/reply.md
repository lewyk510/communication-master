---
description: Draft a reply in a relationship context (S2). Clarifies goal and relationship, picks a strategy from the reply engine, outputs exactly 3 options (safe/assertive/warm) in the user's language lane. Engine: wiki/playbooks/p1-reply-engine/
---

# /reply · 回复引擎（Reply Engine）

**用途**：用户收到一条消息或处于一个对话节点，想知道「我该怎么回」。
**引擎**：`wiki/playbooks/p1-reply-engine/`
**前置**： incoming message 有歧义时，先跑 `/decode`，拿着解码结果再回。

## 流程（按序执行）

### 1. 明确目标与关系
先问清（或从上下文推断）三件事，缺一不可：
- **目标**：这次回复要达成什么？让事推进、保住关系、设边界、争取时间、婉拒？
- **关系**：回复之后，你想和对方处在什么关系？（关系是产出的一部分，不是背景）
- **约束**：哪些话不能说、哪些承诺不能给、什么时间内必须回。
关系与权力定位沿用 `/decode` 第 2 步的框架：`wiki/scenarios/sc1-workplace-power/`（职场）、`wiki/scenarios/sc3-family-kinship/`（家庭）、`wiki/scenarios/sc2-romance-intimacy/`（亲密）、`wiki/scenarios/sc6-friends-social/`（朋友）。

### 2. 选策略
打开引擎 `wiki/playbooks/p1-reply-engine/`，按「目标 × 关系 × 权力」选主策略，按需叠加：
- 有冲突、要道歉、要修复 → NVC 四步（观察、感受、需要、请求）：`wiki/concepts/c3-nvc-conflict-repair/`
- 要说服对方做某事（伦理范围内）→ 说服与影响：`wiki/concepts/c2-persuasion-influence/`
- 对方在施压、愧疚绑架、PUA → 先防御再回复：`wiki/concepts/c9-manipulation-defense/`
- 用户自己情绪上头、内心戏过多 → 先理内心再落笔：`wiki/concepts/c14-self-talk/`
- 要拒绝或谈难事 → `wiki/scenarios/sc4-hard-conversations/`
- 谈钱谈条件 → `wiki/scenarios/sc10-negotiation-deals/`
- 求人办事 → `wiki/scenarios/sc12-asking-help/`

### 3. 产出恰好 3 个选项
固定输出三个选项，让用户挑或混搭。**不多不少**：

| 选项 | 定位 | 什么时候用 |
|------|------|-----------|
| **Safe 稳妥** | 低风险、留余地、不承诺 | 关系敏感、信息不足、需要时间 |
| **Assertive 坚定** | 直接表达立场与诉求 | 界限被踩、诉求明确、事实在手 |
| **Warm 温度** | 优先维护关系与情绪 | 对方脆弱、关系长期、小事化了 |

每个选项都要：能直接复制发送；长度贴合原渠道（微信短句、邮件成段）；承接对方上一句的落点。

### 4. 语言车道（lane）
用用户的语言写（zh / en / ms），**本地化表达，不是翻译腔**。文化语域参考：
- 马来语车道：budi bahasa 礼节层级 → `wiki/cultures/cu1-malaysia-malay/`
- 中文车道：面子与人情的分寸 → `wiki/cultures/cu2-malaysia-chinese/`
- 语码转换（Manglish、中英混说）→ `wiki/cultures/cu5-codeswitching/`
- 通用直接/间接维度 → `wiki/cultures/cu4-cross-cultural-general/`

### 5. 语气与坑（每个选项一行）
从所选主题文件的条目里取该场景的常见误读与禁忌，每个选项标注：
- 语气：一句话描述（如「 firm but respectful」）
- 坑：这个选项最容易翻车的地方（如 assertive 对长辈可能读作顶撞，参考 cu2）

### 6. 引用
每个选项至少引用一个存在的 KB 路径，说明该选项的形状来自哪里（引擎的哪个策略、哪个概念文件、哪个车道条目）。

## 输出模板

```markdown
## 目标 / 关系 / 约束
- 目标：…
- 回复后的关系：…
- 约束：…

## 所选策略
（来自 p1-reply-engine 的策略名 + 引用路径；叠加 c3/c2/c9 时注明）

## 选项 1 · Safe 稳妥
> （可直接发送的原文）

- 语气：…
- 坑：…
- 依据：`wiki/playbooks/p1-reply-engine/`、`wiki/...`

## 选项 2 · Assertive 坚定
（同上结构）

## 选项 3 · Warm 温度
（同上结构）

## 建议与提醒
（三选一还是混搭；发出前最后检查什么；若对方反应 X 则转 Y）
```

## 硬规则

1. **恰好 3 个选项**（safe / assertive / warm），除非用户明确只要一种。
2. 每个选项 **可复制直接发送**，且至少引用 1 个存在的 KB 路径。
3. 选项写在用户的语言车道，本地化表达；不确定车道就问。
4. 不替用户撒谎、不写操纵性话术（见 ethics：`wiki/synthesis/00-how-to-use.md` 第 e 节）。
5. Practice heuristic 性质的建议必须标注，不冒充事实。

## 引用

- 引擎：`wiki/playbooks/p1-reply-engine/`
- 策略库：`wiki/concepts/c3-nvc-conflict-repair/`、`wiki/concepts/c2-persuasion-influence/`、`wiki/concepts/c9-manipulation-defense/`、`wiki/concepts/c14-self-talk/`
- 情境：`wiki/scenarios/sc4-hard-conversations/`、`wiki/scenarios/sc10-negotiation-deals/`、`wiki/scenarios/sc12-asking-help/`
- 车道与文化：`wiki/cultures/cu1-malaysia-malay/`、`wiki/cultures/cu2-malaysia-chinese/`、`wiki/cultures/cu4-cross-cultural-general/`、`wiki/cultures/cu5-codeswitching/`
- 前置解码：`commands/decode.md`、`wiki/synthesis/modality-matrix.md`
