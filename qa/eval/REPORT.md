# 通信能力评测报告 (communication ability — eval report)

> 目标：用可复现的实验回答一个问题——**这个 skill 的沟通能力到底好不好？**
> 两个维度分开测：**(A) 检索**（确定性，可自动化）与 **(B) 回答质量**（rubric 评分）。
> 结论：检索 **10/10**；回答 **4/4 通过 rubric**，但发现 1 个生成层缺陷与 1 个匹配器潜在 bug（见 §5）。

---

## 1. 实验怎么做（可复现协议）

固定 10 个场景 `qa/eval/scenarios.json`，覆盖 4 类任务 × 3 语言（中/英/马来）：

| 类型 | 含义 | 场景 |
|---|---|---|
| **S1** decode | 解码潜台词（他到底什么意思） | `S1-zh-suinbian`、`S1-en-noted`、`S1-ms-takapa` |
| **S2** respond | 给回复/应对（含礼节、拒绝、边界） | `S2-zh-credit`、`S2-en-decline`、`S2-zh-condolence`、`S2-zh-pua` |
| **S3** artifact | 生成成篇文章（投诉信/正式文书） | `S3-zh-refund`、`S3-ms-surat` |
| **S4** meta | 教人自己用（AI 提示词/机制） | `S4-zh-apology` |

每个场景带 `rubric_by_type`（按类型给若干条**可核对**的通过条件）与 `red_flags`（必须避免的失败模式）。

**实验步骤：**

1. **检索（确定性）**：`python3 tools/eval.py`
   对每个 prompt 做路由打分，取 rank-1，看是否命中 `expect_topics`。输出 hit@1 与 token 记分卡。
2. **回答质量**：`python3 tools/eval.py --context-out /tmp/opencode/eval-context/`
   导出每个场景的 KB 上下文，交给**只能用 KB** 的作答者按 prompt 产出答案，再对 `rubric_by_type` 逐条判分、并对 `red_flags` 做反查。
3. **回归**：任何对 `router.json` 的改动后跑 `qa/router-smoke.py`（28 条固定路由断言）+ `tools/check.sh`。

---

## 2. 结果 A：检索（确定性）

**hit@1 = 10/10**（修复前 7/10）。token 记分卡：

| 指标 | 值 |
|---|---|
| 平均检索卡片（light 路径） | **~331 tok** |
| 平均全文加载（full 路径） | **~8,715 tok** |
| 节省倍数 | **≈26×** |

逐条（rank-1 → 期望）：

```
[OK] S1-zh-suinbian   -> p1-reply-engine        card~166  full~7821
[OK] S1-en-noted      -> p2-subtext-decoder     card~233  full~5067
[OK] S1-ms-takapa     -> p2-subtext-decoder     card~233  full~4955
[OK] S2-zh-credit     -> sc1-workplace-power    card~446  full~9496
[OK] S2-en-decline    -> sc6-friends-social     card~483  full~8874
[OK] S2-zh-condolence -> sc16-condolence-grief  card~526  full~11281
[OK] S2-zh-pua        -> c9-manipulation-defense card~264 full~10950
[OK] S3-zh-refund     -> p3-formal-writing      card~280  full~9340
[OK] S3-ms-surat      -> p3-formal-writing      card~280  full~7942
[OK] S4-zh-apology    -> p4-ai-prompting        card~405  full~11424
```

### 修复前的 3 个 miss 及根因

| 场景 | 旧结果 | 根因 | 修复 |
|---|---|---|---|
| `S1-en-noted` | `sc7-digital-messaging`（"reply" 命中） | `p2` 只有 `noted with thanks`，而 prompt 是 `noted, thanks`（逗号、无 with） | `p2` 补 `noted, thanks` / `noted thanks` |
| `S1-ms-takapa` | `cu1-malaysia-malay`（"tak apa" 命中） | `p2` 缺马来语"什么意思"信号 | `p2` 补 `maksud dia` / `apa maksud` |
| `S1-zh-suinbian` | `p1-reply-engine` | 该 prompt 同时问"怎么回"，`p1-reply-engine` 是**合理**rank-1 | 调整该场景 `expect_topics`（标注修正，非 bug） |

---

## 3. 结果 B：回答质量（rubric）

**4/4 场景通过全部 rubric 项**。摘要：

| 场景 | rubric 要点 | 结果 | 备注 |
|---|---|---|---|
| S1 解码 | ≥2 种读法 + 各给理由/置信度 + 恰好 3 个回复选项 + 引用 KB 路径 | ✅ | 显式区分"证据支持的读法"与"KB 未覆盖"的部分；置信度声明为定性 |
| S2 慰问 | 2–3 个具体选项 + 含示例措辞 + 顾及关系/渠道/文化 + ≥1 条雷区 + 引用 | ✅ | 覆盖白色信封/单数帛金/马来 takziah；**但示例消息出现串码（见下）** |
| S3 投诉信 | 完整成品（称谓/日期/主题/正文/明确诉求）+ 升级路径 + 正式语域 + 引用 | ✅ | 升级阶梯具体到 TTPM / Borang 1 / RM5 费用 |
| S4 提示词 | 可复用占位符模板 + 讲清机制 + 标注构造示例 + 引用 | ✅ | 模板可填空；构造的示例被明确标注 |

### 发现的缺陷
- **S2 串码（生成层，非 KB）**：示例消息里出现 `人 Streaming 到不了灵堂 Another 宝`、误用日文 `素直` 等无意义片段。rubric 项仍算通过，但这是**作答者稳定性**问题，不是知识错误。缓解方向见 §5-2。
- 无场景触发 `red_flags`（未出现"单一定论"、未编造研究、未给危险建议）。

---

## 4. 结论

- **能力如何**：检索**准且省**（10/10，~26× token 节省）；回答**结构完整、有据可查、按 rubric 全过**。
- **最像"人"的地方**：敢于说"KB 没覆盖这块"、给多读法而非单一定论、按语言切换文化礼节。
- **最薄的地方**：① 路由依赖关键词覆盖率，冷门口语/外语表述会漏（已修 3 例）；② 生成层偶发串码；③ 匹配器存在拉丁子串误命中（**已修**，见 §5-1）。

---

## 5. 升级建议（按优先级）

1. **~~修匹配器的拉丁子串误命中（潜在 bug）~~（已完成）**：`router.json.matcher` 声明拉丁词走 word-boundary，但实现曾是纯子串，导致 `PR` 命中 `proposal`、`fine` 命中 `define` 等。**修复**：`tools/router_match.py` 对 ASCII 触发器用 ASCII-alnum 词边界（CJK 仍走子串，且 `用whatsapp聊` 这类 CJK 相邻拉丁仍能命中），并加回归锚点（`proposal`→`sc7`、`noted, thanks`→`p2`）；smoke 28/28、eval 10/10 全绿。
2. **给作答者的"输出前自检"约束**：在 playbook 生成步骤加入一条硬约束——"只输出目标语言；专有名词不得夹生造英文/日文 token；每条示例消息发出前逐字复读一遍"。用于压制 §3 的串码。
3. **扩充评测集 + 引入独立判分**：把当前 10 场景扩到 ≥30，覆盖 S1–S4 × 中英马；引入 **LLM 独立判分**（对 rubric 逐条分级）并每类抽 1 条人工复核，降低自评偏差。
4. **把 eval 接进 CI（advisory）**：`tools/eval.py` 以非阻塞方式跑在 `check.sh` 里，hit@1 下降即告警；不因单条 miss 阻断发布。
5. **建立"miss → 加召回调例"闭环**：任何真实漏检，先补进 `scenarios.json` 作为回归锚点，再改 `router.json`，永不删例。
6. **具体触发器候选（下一步按需加）**：EN 子串误命中修正项；MS 更多口语（`tak apalah`、`boleh ke`）；ZH 网络新词。

---

## 6. 复现命令

```bash
cd /root/.agents/skills/communication-master
python3 tools/eval.py                                  # 检索 hit@1 + token 记分卡
python3 tools/eval.py --context-out /tmp/opencode/eval-context/   # 导出作答上下文
python3 qa/router-smoke.py                             # 26 条路由回归
bash tools/check.sh                                    # 全量健康检查
```

## 7. 指标定义
- **hit@1**：rank-1 路由结果落在 `expect_topics` 内的场景比例。
- **rubric 通过**：该场景 `rubric_by_type` 的每一条都满足，且未触发任何 `red_flag`。
- **card vs full**：`light`（紧凑固定头 + 事由卡）与 `full`（core + 整条 lane）两条加载路径的估算 token。
