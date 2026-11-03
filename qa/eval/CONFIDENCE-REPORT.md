# 路由置信度校准 · Round 13（意图/领域分类器实测 + 置信度层落地）

> Round 8 的结论说：关键词路由在自由文本长句上到顶（修正口径 ~47%），下一步要么做「意图/领域分类器」，要么信任宿主 LLM。本轮把第一条路**实测到底**：纯离线、零依赖的词汇语义分类器（TF-IDF / BM25 / 条目级聚合）全部**跑输**关键词路由；但同一批实验产出了一个**可校准的置信度信号**——落地为 `router_match.assess()` 的 high/low 分档 + Layer-2 显式交接，**路由行为零改动、零回归**。日期：2026-11-03。
> 数据：`qa/eval/bombard-adjudicated.json`（Round 8 的 118 题盲审金标准）；运行器：`qa/eval/run_confidence.py`。

---

## 1. 问题：分类器能不能取代关键词路由？

Round 8 诊断的两个根因：**词汇缺口**（正确主题的触发词不在句子里）和**后段杂词压过开头意图**。词汇分类器（把每个主题的触发词+卡片建成文档，查询算相似度）理论上正好补词汇缺口——不需要句中出现过完整触发词，词袋重叠即可命中。

## 2. 方法（四个变体，全部离线 stdlib）

| 变体 | 文档构成 | 查询/文档分词 |
|---|---|---|
| TF-IDF 余弦（trig+card） | 触发词×3 + 卡片 TL;DR×2 + signals | 拉丁词 + CJK 二元组 |
| TF-IDF（core） | 上者 + core.md 全文（去 URL/代码块） | 同上 |
| BM25（trig+card） | 同 TF-IDF trig+card | 同上 |
| BM25 条目级 | 每主题拆成「触发词包 + 各 lane 的 `###` 条目标题」多文档，主题分 = max | 同上 |

评测集：Round 8 金标准 118 题（`clean`/`router_ok_label_noise` 取路由器答案，`router_wrong`/`both_wrong` 取盲审答案；其中 10 题为 out-of-scope，金标准 = 不路由）。基线 = 现网 `router_match.rank`（含 Round 8 的长句开头优先）。

## 3. 结果：负结果（诚实数字）

| 方案 | 118 题命中 | out-of-scope 误路由 |
|---|---|---|
| 关键词路由（现网，基线） | **57/118 = 48.3%** | 0/10 |
| TF-IDF trig+card（纯语义） | 44/108*（37.3%） | — |
| BM25 trig+card（纯语义） | 43/108*（39.8%） | — |
| TF-IDF core 全文 | 37/108*（31.4%） | — |
| BM25 条目级 max | 14/108*（13.0%） | — |
| **混合：关键词弱分(<5)时语义接管** | 最好 52/118 = 44.1% | **8-9/10** |

\* 纯语义变体在 108 题子集上计（10 题 out-of-scope 无法计入）；混合策略在全 118 题上计。

**混合策略全口径跑输基线**（44.1% < 48.3%），且把 8-9 成 out-of-scope 问题硬路由进主题（直接违反 Round 12 的安全结论）；在守门集上也有回归（reach 4→6 miss、smoke 破 1：`怎么拒绝推销电话`→sc15）。**结论：词汇方法不能当接管者。** 失败案例的共同点是需要世界知识的桥接：「约旦人开会不看表」→cu4（跨文化时间观）、「被裁员当天还帮我搬家 是不是圣母」→c4（同理心判断）、「突然被cue上台」→c16——句中没有任何一个主题词，词袋永远够不着。这正是 Round 8 说的「天花板在关键词匹配本身」的另一面：**天花板也在词汇语义本身**。

## 4. 转折：同一批实验产出可用的置信度信号

分桶分析发现关键词得分本身就是置信度信号（1-5 分桶正确率 33%，6-10 分桶 43%，11+ 分桶 60%），而 BM25(trig+card) 的首选与关键词首选**是否一致**是更强的错误探测器。两者合成 `assess()` 的分档规则：

- **high**：关键词得分 ≥5 **且** 语义校验选同一主题
- **low**：关键词得分 <5（weak-keyword），或语义校验 prefers 别的主题
- **none**：零命中（走既有 Layer-1.5 意图兜底/澄清问题）

| 校准指标（118 题） | 数值 |
|---|---|
| 路由命中（与关键词-only 完全一致，drift = 0） | 57/118 = 48.3% |
| **high 档精度**（整体才 48.3%） | **20/31 = 65%** |
| **错误路由被 low 拦下** | **49/60 = 82%** |
| **out-of-scope 被 low/none 拦下** | **9/10 = 90%** |
| low 档构成 | typo-fuzzy-match 31 · weak-keyword 21 · semantic-disagrees 25 |

含义：宿主 LLM 拿到 `conf high` 时可以放心走快速通道（省 token）；拿到 `conf low` 时**别信快速通道**，读 `index.md` 按理解选页（Layer 2）——这正是 Round 8 指出的正确架构路径的可执行落地。out-of-scope 题不再被硬塞进错误主题（Round 12 安全轴的补强）。注：仅靠错别字兜底（编辑距离≤1）命中的路由一律 low（`typo-fuzzy-match`）——容错匹配可以救回候选，但不该获得高信任。

阈值取舍：CONF_MIN=5 vs 8——T=8 的 high 档精度 70%（n=20）、拦错 90%，T=5 精度 65%（n=31）、拦错 82%。取 **T=5**：快速通道保留更多可用题量，拦截率损失可忽略（都是「多读一个 index.md」的代价，不是答错的代价）。

## 5. 落地（本轮 diff）

| 变更 | 位置 | 回归防护 |
|---|---|---|
| BM25 语义校验模块（触发词×3 + 卡片，~6ms 构建，纯 stdlib） | `tools/router_semantic.py`（新） | — |
| `assess()`：rank() + 置信分档，**不改路由** | `tools/router_match.py` | drift 检查（run_confidence 出错即 exit 1） |
| `conf` 字段 + low 时的 Layer-2 指引 | `tools/ask.py`（文本 + `--json`） | check.sh 的 resolver 断言照旧 |
| 置信度用例进 recall 门禁（4 例必须过） | `qa/router-smoke.py` CONF_CASES | 32/32 + 3/3 + 4/4 |
| 校准报告运行器（含 drift 硬门） | `qa/eval/run_confidence.py`（新），进 `tools/check.sh` | — |
| 路由置信度规则（何时别信快速通道） | `wiki/synthesis/00-how-to-use.md` §(d) + quickstart、`SKILL.md` 步骤 2、`AGENTS.md` 查询流程步骤 4 | lint（always_load 页保持结构） |

## 6. 复现

```bash
cd /root/communication-master
python3 qa/eval/run_confidence.py     # 校准报告 + drift 硬门
python3 qa/router-smoke.py            # 32 recall + 3 intent + 4 confidence
python3 tools/ask.py "约旦人开会都不看表 我朋友说他们没礼貌 你觉得呢"
                                      # -> conf low (semantic-disagrees) + Layer-2 指引
bash tools/check.sh                   # 全量健康检查（已含 run_confidence）
```

> **Round 13 结论：词汇语义分类器作为路由接管者被数据否决（最好 44.1% < 基线 48.3%，且 out-of-scope 误路由）；但「关键词分强度 + 语义一致性校验」构成可靠的置信度信号——high 档精度 65%（整体 48.3%）、82% 错误路由与 9/10 out-of-scope 被 low 拦下。路由零改动落地为 `assess()` + Layer-2 显式交接，把「答错」变成「知道自己不确定」。**
