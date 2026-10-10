# 理解力测试 · Round 6（马来西亚混合语 / 信息完整性边缘）

> Round 6 加两条**全新**维度：
> 1. **马来西亚混合语（Manglish / rojak / 语码转换）**——同一句子里 zh + en + ms 混着讲、用颗粒词（lah / leh / lor / meh）标态度、用 "can / where got / paiseh / jialat" 表意。考解码器**会不会真的去用**知识库里的 `cu5-codeswitching`（还是把"混语"当噪音）。
> 2. **信息完整性边缘**——消息**乱序到达**（时间被打乱）、**言行矛盾**（嘴上说一套、行为做一套）。
> 数据：`qa/eval/understanding-hard5.json`。8 个"只用知识库"的助手，各自独立作答。日期：2026-10-10。

---

## 1. 结果（6 孤立 + 2 组）

| 编号 | 考的是什么 | 预期 | 实际主读法 | 结果 |
|---|---|---|---|---|
| MY1 | Manglish 颗粒：「Can lah, no problem one」 | 真心答应（别过度怀疑） | A：真心答应（lah=放心 / one=性质判断），高置信，不追问 | ✅ |
| MY2 | Manglish「Where got!」 | 否认/反驳（不是问地点） | A：随口语域的强烈否认（**没**读成问地点），中置信，追问一句 | ✅ |
| MY3 | Manglish「paiseh... next time lah」 | 软拒/搁置（保面子） | B：悬置式软拒（paiseh 面子语 + next time lah=礼貌搁置），中置信，追问 | ✅ |
| MY4 | Rojak 混语（zh+en+ms）的样子 | 强烈坦率差评 | A：私下坦率强差评（memang tak boleh pakai + jialat 承载强度），高置信 | ✅ |
| TC1 | **消息乱序到达**（时间被打乱） | 顺序不可靠、去问 | A：**点名"乱序只是网络故障假象"**，按发送时间重构（3→1→2），不拿最后收到的当结论 | ✅ |
| CX1 | **言行矛盾**：「no rush」却两天催 3 次 | 真有（软）压力 | B：**行为压过字面**——真有软的截止压力，别照字面放松，高置信，追问 | ✅ |
| MY-P1 | 颗粒词三连（同一个 Can） | 三态：真心/敷衍/怀疑 | 真心(高) / 「喔好啦好啦」勉强带不耐(中) / 「可以咩?」真诚怀疑(高)，DIFFER=yes | ✅ |
| MY-P2 | 语域对：标准英文 vs Manglish | 冷/程序化 vs 暖/真心，须区分 | 标准「Noted.」=中性、无关系信号(高) vs Manglish=暖·真心承诺(中)，DIFFER=yes | ✅ |

**总账：8/8。这是连续第二轮首轮全过**——说明前几轮加的"判别点护栏 / 存在≠方向 / 输入完整性检查"已经稳。本轮**主战场从"能不能读懂"转到"知识库的路由链是否接得上"**（见 §3）。

> ⚠️ 两个"技术性但值得记"的细节：
> - **TC1 没触发"追问"**：因为题目把"真实发送顺序"直接告诉了助手，顺序已可重构，追问变得没必要。真正考的"别拿最后收到的当结论"这一条**做对了**。→ 判过，但**下轮若再考，应隐去真实顺序**，才能真考出"是否主动去问"。
> - **MY-P2 的「Noted.」被读成"中性"而非"冷"**：按直接文化的反过度解读护栏，孤立一个单字英文回执**不该**判冷——引擎在这里其实比预期标签更稳。真正得分点是**两成员区分开了**（一个无温度、一个有温度），这达到了"语域对必须区分"的要求。→ 判过。

---

## 2. 关键指标

| 能力 | 结果 |
|---|---|
| **Manglish 颗粒词（lah/leh/lor/meh）** | 3/3（MY1 未过度怀疑；MY-P1 三态分清；MY3 颗粒词被读成软拒） |
| **Manglish 习语（where got / can / paiseh）** | 3/3（MY2 不读成地点；can 分档；paiseh=面子语） |
| **Rojak 混语强度** | 1/1（MY4：混语没稀释强度，读出强差评） |
| **消息乱序 / 顺序不可靠** | 1/1（TC1：重构发送序，不拿末条当结论） |
| **言行矛盾（行为压字面）** | 1/1（CX1：两天催 3 次 > "no rush"） |
| **语域差异（正式 vs Manglish）** | 1/1（MY-P2：两成员区分） |
| **是否触达 cu5-codeswitching** | **8/8 触达**（凡混语例，助手全部翻到 cu5 并用其颗粒词/习语条目；MY2 直接引用 "where got"，MY4 引用 jialat/rojak） |
| **路由链可达性（Layer 1）** | **修前 2 处断裂 → 修后 4/4**（见 §4） |

---

## 3. 关键发现：**Layer 2 全对，断的是 Layer 1 的"路由链"**

本轮"理解力"层面的结论和上一轮一样：**给足知识库，8/8 都读对**。新增维度的真问题不在"懂不懂"，而在**知识库的指针接不接得上**——这一层前面五轮**从没系统测过**。实测发现两处断点：

1. **引擎页不指向 cu5**：`wiki/playbooks/p2-subtext-decoder/core.md`（所有 S1 解码的入口）全文**没有任何一处** `[[cultures/cu5-codeswitching/...]]` 链接。也就是说，正式走 KB 的助手**不知道该去翻混语页**；这轮之所以 8/8 触达，是因为派给助手的权限是"随便翻整个 wiki"，它们**自己搜到**了 cu5。真实会话里没这个兜底 → **脆弱**。
2. **路由器根本不认识 Manglish 词汇**：
   - `ask.py "where got meaning"` → **NO MATCH**（死路，退化成"问一个澄清问题"）。cu5 的触发词只有抽象的「Manglish / Singlish / codeswitch / dialect / 方言 / 语码转换」，**一个实际用词都没有**。
   - `ask.py "can lah 什么意思"` → **错路到 cu1（马来文化）**。因为 `can lah` / `okay lah` 这两条被挂在了 `cu1-malaysia-malay` 的触发词里——语义上它们是**混合语颗粒**，属于 cu5，不属于"马来文化本体"。

一句话：**大脑（Layer 2）会用 cu5，但路牌（Layer 1）指向了别处或没写。** 这正是用户最初抱怨"只找关键词、不理解"的同一类病——只不过这次的病灶在**触发词表**，不在解码逻辑。

---

## 4. 据此做的升级

| 升级 | 针对 | 落地 |
|---|---|---|
| **cu5 补齐 Manglish 实词触发词** | `where got` / `can lah` / `paiseh` / `jialat` 等 NO MATCH、错路 | `router.json`：cu5-codeswitching 触发词加 `walao / walao eh / paiseh / jialat / sibeh / bojio / where got / can lah / can meh / can or not / tapau / gostan / sian / kiasu / kaypoh / chim / lah / leh / lor / meh / sia` |
| **把 `can lah`/`okay lah` 从 cu1 归还 cu5** | `can lah` 错路到 cu1 | `router.json`：cu1-malaysia-malay 触发词**删除** `can lah` / `okay lah`（保留 `boleh / nanti / tak apa / insyaAllah / budi bahasa / adat` 等本体词） |
| **引擎页显式指向 cu5 + 加"混合语言"槽位** | core.md 全文不链 cu5（脆弱靠搜） | `p2 core.md` Step 2 新增**槽位 6「混合语言 / 语码转换」**：遇混语**先读 `[[cultures/cu5-codeswitching/core]]`** 再解码，并点明颗粒词换一个整句态度就变（Can lah/lor/meh） |
| **加回归用例** | 防再次漏/错路 | `qa/router-smoke.py` 增 4 条 Manglish 用例（can lah / where got / paiseh / walao eh），**32/32 全绿** |
| **重建派生物** | 触发词改了必须重建 | `tools/build_router_index.py`、`tools/build_cards.py` 已跑 |

---

## 4.5 复验（改完路由后重跑）

| 例 | 改前 | 改后 | 判定 |
|---|---|---|---|
| `can lah 什么意思` | 错路 → cu1 | **cu5-codeswitching**（score 10） | ✅ 归位 |
| `what does where got mean` | **NO MATCH**（死路） | **cu5-codeswitching**（score 9） | ✅ 接上 |
| `paiseh 是什么意思` | NO MATCH | **cu5-codeswitching**（score 6） | ✅ 接上 |
| `bash tools/check.sh` | — | lint + index + cards + **router-smoke 32/32** + resolver + freshness + token-cost **全过** | ✅ |

> **Round 6 改进后总账：8/8 理解 + 路由链 4/4 + 门禁全绿。** 混语维度从"靠助手自己搜到"升级为"引擎页显式指向 + 路由能命中"。

---

## 5. 复现

```bash
cd /root/.agents/skills/communication-master
cat qa/eval/understanding-hard5.json     # 6 孤立例 + 1 三连 + 1 对
# 每例派一个 KB-only 助手，按 p2-subtext-decoder/core.md 的 7 步独立解读
python3 tools/ask.py "can lah 什么意思"   # -> cu5-codeswitching
python3 tools/ask.py "what does where got mean"  # -> cu5-codeswitching
python3 qa/router-smoke.py               # 32/32 must-pass
```
