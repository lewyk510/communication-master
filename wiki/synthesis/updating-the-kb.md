---
id: updating-the-kb
title: Updating & Freshness · 更新与保鲜
type: synthesis
lang: core
tags:
  - maintenance
  - freshness
  - ingest
  - meta
scenarios: []
sources:
  - https://en.wikipedia.org/wiki/Knowledge_management
  - https://en.wikipedia.org/wiki/Evidence-based_practice
  - https://en.wikipedia.org/wiki/Software_documentation
related:
  - "[[synthesis/00-how-to-use]]"
  - "[[synthesis/modality-matrix]]"
created: 2026-10-07
updated: 2026-10-07
---

# Updating & Freshness · 更新与保鲜

本页回答「这个库怎么更新、内容会不会过时、需要新理论/新话术时怎么办」。它是维护者的操作手册，不是使用者读的查询页。

## (a) 数据模型：线下为主，线上为辅（offline-first, online-enrich）

- **查询时 100% 线下**：`router.json` + `wiki/` 全在本地，不联网、不调用任何 API。技能被加载后即可离线运行。
- **只有 Ingest（收录）时才联网**：`tools/s.sh`（搜索：Serper/Exa/Jina/NewsAPI）与 `tools/f.sh`（抓取单链接）。
- 三层分工：`raw/<topic-id>/` = **不可变证据快照**（永远只读）；`wiki/` = 综合后的可读内容；`router.json` / `index.md` / `log.md` = 索引与历史。
- 结论：**线下资料库 + 按需线上补料**。不是每次回答都上网，而是定期（或遇到缺口时）上线抓新证据、落盘进 `raw/`，再综合进 `wiki/`。

## (b) 什么时候该更新

1. **过时** — `python3 tools/freshness.py` 报告有 capture 超过保鲜窗口（默认 18 个月）；平台机制、AI 提示词等快变主题建议收到 6 个月。
2. **新理论 / 新话术** — 出现更好的"这样说更友善 / 更有说服力 / 更不易被操控"的实证或成熟做法，来源可追溯（tier 1–2 优先）。
3. **缺口** — `qa/router-smoke.py` 的 known-gaps 列表，或真实提问命中不了主题（走 `router.json.fallback` 兜底提问）。

## (c) Ingest 工作流（与 AGENTS.md 一致）

1. **抓取** — 存进 `raw/<topic-id>/`，文件名带日期、文件头写 `capture date:` + `source tier:`；不改旧捕获。
2. **撰写** — 更新 `wiki/<cluster>/<id>/` 的 `core.md` 与受影响车道；遵守车道契约（原生撰写，非翻译）、深度下限、防编造标签。
3. **路由** — 写 `router-patch.json` 片段（不手改 `router.json`），见 §f。
4. **索引** — 运行 `reindex`，`index.md` 状态 `pending → seeded → complete`。
5. **日志** — `log.md` 追加 `## [YYYY-MM-DD] ingest | <title>`。
6. **自检** — `bash tools/check.sh`（结构 lint + 召回 smoke + 保鲜）。

## (d) 保鲜策略（freshness policy）

- 每条捕获头部必须写 **`capture date:` 与 `source tier:`**（1 官方/学术，2 成熟媒体/出版物，3 社区/轶事）。
- `tools/freshness.py` 汇总：捕获总数、tier 分布、最旧/最新、以及**超窗的 re-crawl 候选**。JSON 搜索快照无头部时会回退用文件 mtime，并计入 `unknown` tier（提示可补 tier）。
- **周期**：每月跑一次 `freshness.py`；tier 1–2 的慢变理论 18 个月复查一次，快变主题（直播平台规则、AI 提示词、聊天软件机制）6 个月一次。
- **替代而非删除**：来源被更新版本取代时，**新增**一条捕获并在 `## Sources` 注明 supersedes，绝不编辑既有 `raw/`。
- 目标不是"永远最新"，而是**知道哪一条该重抓**——把时间花在该更新的证据上。

## (e) 新增一个主题

1. 建 `wiki/<cluster>/<id>/`：`core.md`（≥10 结构条目 且 ≥1000 词）+ `zh.md`（≥10）+ `en.md`（≥8）+ `ms.md`（≥8），每条末尾 `## Sources` ≥3 URL。
2. 建 `raw/<id>/`，放 ≥3 条带日期的捕获。
3. 写 `router-patch.json`（id/title/type/paths/scenarios/triggers/see_also）。
4. 把 `tools/lint_kb.py` 的 `EXPECTED` 对应 cluster 列表扩一位。
5. `python3 tools/lint_kb.py reindex` → `bash tools/check.sh` → 在 `qa/router-smoke.py` 里加一条该主题的召回用例。

## (f) 路由补丁与召回门（recall gate）

- 补丁片段：`{"op":"update","id":"...","set":{"triggers":[...],"scenarios":[...]}}`，`reindex` 合并后 `router.json` 必须仍是合法 JSON。
- **lint 不测召回**：改任何 trigger 后必须跑 `python3 qa/router-smoke.py`。每当修好一个真实漏检，就在其 `CASES` 里补一条用例，防止回归。
- 计分口径见 `router.json.matcher`：命中触发词按长度累加；媒介/渠道词（`medium_tokens`）只计 +1，避免"WhatsApp"之类压过主题词；全程大小写不敏感；同分取 `entries[]` 靠前者。

## (g) 版本与可追溯

- 一切变更走 git 提交，`log.md` 只增不改；每个主题的 `updated:` 日期随内容更新。
- 状态口径（`index.md`）：`pending` / `seeded` / `complete`。

## (h) 加载分层与查询缓存（省 token）

回答一个问题的代价 = **固定开销** + **按需加载**。实测（`tools/token_cost.py`）：

| 层 | 内容 | 大致 token |
|----|------|-----------|
| L0 固定 | `SKILL.md` + `00-how-to-use.md` | — |
| L1 路由 | `router-index.json`（compact） | 固定 ~6.2k |
| L1.5 卡片 | `sidecars/cards.json` 里 1 张卡片 | ~0.4k |
| L2 全量 | 命中的 `core.md` + 一条语言车道 | ~10k |

- **light 路径**（L0+L1+1 张卡片）≈ **6.6k**；**full 路径**（L0+L1+core+lane）≈ **22.4k**——同一次查询差 ~3.4 倍。所以**先卡片，不够再上全量**。
- `sidecars/cards.json` 由 `tools/build_cards.py` 生成（每主题：标题 + 首段 TL;DR + 条目小标题），内容变更后必须重新生成；`tools/build_cards.py --check` 会因漂移而失败，`tools/check.sh` 已接入。
- **精确缓存**：`tools/cache.py` 对**原样问题**存取答案（`get` / `put` / `stats` / `gc`）。命中即零主题加载。缓存按 **KB 内容指纹**失效（`wiki/**/*.md` + `router-index.json` + `cards.json` 的哈希）——内容一变，旧条目自动变 STALE/MISS，**不需要 TTL，也不会有陈旧答案**。`cache/` 已在 `.gitignore`（本机派生数据，可随时重建）。
- 只做**精确**匹配缓存，不做语义缓存：不同问题的相似问法可能答案不同，语义缓存有答错风险（见 Active.md 的调研结论）。
- **一条命令走完**：`python3 tools/ask.py "<问题>"`（缓存 → 路由 → 卡片；`--full` 再展开 `core`+lane，`--json` 结构化，`--save "<答案>"` 回存缓存）。`tools/router_match.py` 是路由计分的**唯一实现**，召回门 `qa/router-smoke.py` 与 `ask.py` 共用它——门禁校验的就是运行时用的逻辑。
- **CJK 计费提醒**：同一段中文在 cl100k 上约是英文的 1.85 倍 token，在 o200k 上约 1.35 倍。内容仍以 zh 为基准（正确性优先），成本靠卡片分层与缓存抵消。

## (i) 备份与发布（私有 + 公开双轨）

本库用「双轨」：一个**私有**仓库做完整备份，一个**公开**仓库供他人使用、fork、提 PR 来促进进化。

- **私有（完整备份，含 `raw/`）**：`https://github.com/lewyk510/communication-master-private`
  - git 远端名 `private`；`git push private main` 即备份。
  - 换机恢复：`git clone https://github.com/lewyk510/communication-master-private ~/.agents/skills/communication-master`。
- **公开（社区开发，不含 `raw/`）**：`https://github.com/lewyk510/communication-master`
  - git 远端名 `public`。**不含** `raw/`——那是第三方网页抓取，公开再分发有版权风险；来源 URL 已在各页 `## Sources` 保留。
  - 发布/更新：`./tools/publish.sh`（把工作区已跟踪文件覆盖到公开仓库的克隆并推送，保留历史与社区提交；自动跳过 `raw/`）。
  - 他人用法：`npx skills add lewyk510/communication-master`；改进走 fork → PR。
- **离线备份（无网络）**：`./tools/backup.sh bundle` 生成单文件 `.bundle`，任意机器 `git clone <文件> communication-master` 还原。
- 进 git：`wiki/`、`router*.json`、`sidecars/cards.json`、工具与文档。不进 git：`cache/`（本机派生）；公开库不含 `raw/`。
- 公开库 CI（`.github/workflows/ci.yml`）跑 `bash tools/check.sh`；公开库无 `raw/` 时 lint 自动跳过抓取检查。
- 注意：社区在公开库新增的内容不会被 `publish.sh` 删除（覆盖式、不删除），但本地私有副本不会自动获得——合并 PR 后按需把改动同步回本地。

## Sources

本页是维护流程说明，非事实主张。背景性参考（概念导航，不作为本页具体论断的依据）：

- https://en.wikipedia.org/wiki/Knowledge_management
- https://en.wikipedia.org/wiki/Evidence-based_practice
- https://en.wikipedia.org/wiki/Software_documentation
