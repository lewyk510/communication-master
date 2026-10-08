---
id: 00-how-to-use
title: How to Use This KB · 使用指南
type: synthesis
lang: core
tags:
  - router
  - howto
  - meta
scenarios: []
sources:
  - https://en.wikipedia.org/wiki/Implicature
  - https://en.wikipedia.org/wiki/High-context_and_low-context_cultures
  - https://www.cnvc.org/
related:
  - "[[concepts/c10-models-meta/]]"
  - "[[cultures/cu4-cross-cultural-general/]]"
  - "[[playbooks/p1-reply-engine/]]"
  - "[[playbooks/p2-subtext-decoder/]]"
  - "[[playbooks/p3-formal-writing/]]"
  - "[[playbooks/p4-ai-prompting/]]"
created: 2026-10-07
updated: 2026-10-07
---

# How to Use This KB · 使用指南

本页是 router 的 `always_load`。任何一次查询都从这里开始。

## (a) What this KB is · 这个知识库是什么

一个三语（中文 / English / Bahasa Malaysia）沟通知识库，用于**读懂人**和**写好回应**。覆盖潜台词、说服、冲突修复、非语言信号、文化语境（马来西亚优先）、正式写作与 AI 提示词。

- 三条语言车道 **zh / en / ms** 是各自原生撰写的，**不是互译**。
- 42 个主题，分五个簇：concepts（c1-c18）、scenarios（sc1-sc15）、cultures（cu1-cu5）、playbooks（p1-p4）、synthesis（本页与 modality-matrix）。
- 四个引擎（playbooks）+ 四个命令（commands/）对应四类任务（S1-S4，见 c 节）。
- 机器入口：`router-index.json`（紧凑匹配索引，日常加载）＋ `router.json`（全量真源，供补丁/lint）；人类目录 `index.md`；逐主题速查见 f 节与 `index.md`。

## (b) Resolution procedure · 解析流程

每次查询按序执行：

1. **加载本页**（router.json `always_load`）。
2. **定语言车道**：`lang_default: auto`。用户写中文走 zh 车道，英文走 en，马来文走 ms；无法判定时回退 `core.md`。车道文件是原生表达，读取时不要做翻译式理解。
3. **匹配条目**：把用户请求对上 `router-index.json`（紧凑匹配索引；字段同 `router.json` 的 id/dir/scenarios/triggers）各 entry 的 `triggers`（三语关键词）与 `scenarios` 代码；S1/S3/S4 有直达引擎（`engines` 字段）；得分最高的 entry 胜出（计分与匹配口径见 `router-index.json.matcher`（即 `router.json.matcher`）：拉丁字母按词边界、大小写不敏感，中文按子串）。**计分**：命中 trigger 按长度累加；但**媒介/渠道类词**（`router-index.json.matcher.medium_tokens`：whatsapp/微信/消息/email/群/电话/评论 等）只按 +1 弱计——渠道词不得压过主题词（例：「父亲过世了，WhatsApp 慰问消息怎么发」应归 `sc16-condolence-grief`，不是 `sc7-digital-messaging`）；匹配全程**大小写不敏感**（拉丁 trigger 与 `medium_tokens` 比较前统一转小写）；同分取 `entries[]` 靠前者。S2 走 `wiki/playbooks/p1-reply-engine/` 加 `commands/reply.md`。
   **零命中兜底**（`router.json.fallback`）：若无任何 trigger 命中，**不要凭空作答**——加载 `index.md` 与本节，向用户提**一个**澄清问题再继续。
4. **读取**：胜出 entry 的 `paths`（core + 对应车道）+ `see_also`。
5. **作答**：结论挂 KB 引用（`wiki/...` 路径）。有歧义或跨文化时，先执行 d 节的提问规则再作答。
6. 好的答案可回填为 synthesis 页：查询也在积累知识。

## (c) Scenario codes S1-S4 · 任务类型与引擎

| 代码 | 含义 | 引擎 | 命令 |
|------|------|------|------|
| **S1** | Decode：解读收到的消息或行为 | `wiki/playbooks/p2-subtext-decoder/` | `commands/decode.md` |
| **S2** | Respond：在关系语境中起草回复 | `wiki/playbooks/p1-reply-engine/` | `commands/reply.md` |
| **S3** | Compose：正式写作（投诉/申诉/申请/婉拒/谈判邮件） | `wiki/playbooks/p3-formal-writing/` | `commands/draft.md` |
| **S4** | Prompt：让 AI 与工具办成事（提示词工程） | `wiki/playbooks/p4-ai-prompting/` | `commands/prompt.md` |

混合请求拆开处理：先 S1 解码，再 S2/S3 回应。渠道路由见 `wiki/synthesis/modality-matrix.md`。

## (d) Confidence & uncertainty · 置信与不确定规则

- **Evidence-backed**：主张可追溯到 `raw/` 捕获或主题文件的 `## Sources`（tier 1-2）。引用时保留标签。
- **Practice heuristic**：实践建议，允许不引来源，但必须显式标注，不得冒充事实。
- **anecdotal**：tier-3 来源（社区/个人经验）的主张，必须标注。
- 构造的对话一律标注 constructed example。
- **歧义规则**：一条消息存在 >= 2 个合理解读时，输出全部候选并给置信度，不强行收敛为一种。
- **跨文化规则**：涉及 cu1-cu5 而背景信息不足时，**先提问再作答**。提问用 `wiki/cultures/cu4-cross-cultural-general/` 的针对性问题清单（文化背景、过往互动模式、前因、对方惯常风格）。宁可多问一句，不可编一个文化解释。

## (e) Ethics · 伦理边界

- **说服 vs 操纵**：说服（`wiki/concepts/c2-persuasion-influence/`）目标透明、尊重对方的选择权；操纵（`wiki/concepts/c9-manipulation-defense/`）隐藏意图、利用偏差、剥夺选择。本库帮用户说服，不帮用户操纵。
- **拒绝协助**：欺骗、胁迫、煤气灯（gaslighting）、伪装身份、批量话术轰炸。识别出这类请求时，说明原因并转向正当目标（如把「让她回心转意的话术」转为「如何坦诚沟通」）。
- **公开信息**：写公关、演讲、社媒内容时守 c17 的边界；识别与抵制宣传手法是 c18 的正当用途。
- **c8 占星**：只作为「人们实际用来读人的文化启发式」呈现，其预测效力无实证支持，任何输出不得把它当作事实依据。

## (f) Quick links · 簇速查

| 簇 | 路径 | 内容 | 主要服务 |
|----|------|------|----------|
| Concepts | `wiki/concepts/` | c1-c18，机制与框架 | S1 解码的依据库 |
| Scenarios | `wiki/scenarios/` | sc1-sc15，生活情境 | S1/S2 的情境库 |
| Cultures | `wiki/cultures/` | cu1-cu5，文化语境（马来西亚优先） | 三类任务的文化校准 |
| Playbooks | `wiki/playbooks/` | p1-p4，四个引擎 | S1-S4 的执行流程 |
| Synthesis | `wiki/synthesis/` | 本页 + modality-matrix | 横向路由与规则 |

逐主题的 46 行目录（含标题、车道、scenario 标签、状态）见 `index.md`。

## Paste-ready quickstart（SC5）

```text
1. Load wiki/synthesis/00-how-to-use.md (router always_load).
2. Detect the user's language lane: zh / en / ms (lang_default auto; fall back to core.md).
3. Match the request against router-index.json entries (id/dir/scenarios/triggers);
   score = sum of matched trigger lengths, but medium/channel tokens
   (router-index.json.matcher.medium_tokens: whatsapp/微信/消息/email/群/电话/评论 …)
   count as +1 only, so a channel word never outranks a subject word;
   matching (trigger match and medium-membership lookup) is case-insensitive;
   dispatch S1/S3/S4 to engines wiki/playbooks/p2-subtext-decoder/ ,
   wiki/playbooks/p3-formal-writing/ , wiki/playbooks/p4-ai-prompting/ ;
   S2 goes through wiki/playbooks/p1-reply-engine/ + commands/reply.md.
4. Read the resolved topic folder (core.md + the lane file) plus see_also.
5. Answer with KB citations (wiki/ paths). Label claims Evidence-backed or
   Practice heuristic. If ambiguous (>= 2 readings) or cross-cultural, ask the
   targeted questions from wiki/cultures/cu4-cross-cultural-general/ first.
```

## Sources

知识主体来源：本库全部主题文件夹（`wiki/concepts/`、`wiki/scenarios/`、`wiki/cultures/`、`wiki/playbooks/`）及其 `raw/` 捕获。一般性参考（背景概念导航，非本页具体主张的依据）：

- https://en.wikipedia.org/wiki/Implicature
- https://en.wikipedia.org/wiki/High-context_and_low-context_cultures
- https://www.cnvc.org/
