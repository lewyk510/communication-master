# QA dry-run — S4 ai-prompt (SC4) | KB: communication-master | 2026-10-07

## 1. User message (verbatim, en lane)

> I need to get a customer service chatbot to actually process my refund instead of
> giving me the runaround. Give me a prompt that works.

## 2. Router resolution (per `wiki/synthesis/00-how-to-use.md` §b–§c)

- `always_load`: `wiki/synthesis/00-how-to-use.md`. Language: English → en lane (`lang_default: "auto"`).
- Trigger matches (verified by grep against `router.json`):
  - `"prompt"` → entry **p4-ai-prompting** (triggers include `"AI"`, `"提示词"`, `"让AI帮我"`, `"prompt"`, `"prompting"`, `"ChatGPT"`, `"LLM"`, `"arahan AI"`)
  - `"customer service"` → entry **sc9-live-service** (triggers include `"客服"`, `"投诉"`, `"退货"`, `"customer service"`, `"complaint"`, `"khidmat pelanggan"`)
- Best-scoring entry: **p4-ai-prompting** + direct engine dispatch: `router.json` `"engines": {"S4": "wiki/playbooks/p4-ai-prompting/"}`. sc9 is the consumer-side context (what to demand), p4 is the how-to-prompt engine.

## 3. Files loaded

| # | Path | Role |
|---|------|------|
| 1 | `wiki/synthesis/00-how-to-use.md` | always_load |
| 2 | `wiki/playbooks/p4-ai-prompting/core.md` | S4 engine: §12 chatbot playbook, §17-T6 template, §14 failure modes |
| 3 | `wiki/playbooks/p4-ai-prompting/en.md` | en lane: closed-question + hallucination entries |
| 4 | `wiki/scenarios/sc9-live-service/core.md` | co-matched; Fact–Impact–Ask feeding the prompt's demand line |

## 4. Answer (en lane)

### 4.1 The prompt (concrete, reusable, slotted)

Base pattern — `p4-ai-prompting/core.md` §17-T6 「让客服机器人办事（S4 核心模板）」, quoted verbatim (its native lane is zh; template labelled `constructed example` in the KB):

```text
我的问题只需要一个结果，请直接处理，不要用模板话术：
- 账户/订单：{订单号}
- 事实：{日期}购买了{商品}，{发生了什么}，我已尝试{……}未解决。
- 我的唯一诉求：{退款 RM89 到原支付卡}
请按顺序回答：
1. 能办理 / 不能办理（二选一，明确说）；
2. 如能：具体步骤和时限；
3. 如不能：我需要输入什么关键词才能转人工。
禁止：说「我们会尽快处理」；重复我提供过的信息；道歉超过一次。
回答前先用一行复述我的订单号与问题，确认你读对了。
```

English instantiation for your case (`constructed example` — adaptation labelled per KB rules; slots `{}` to fill):

```text
My issue needs exactly one outcome — process it directly, no template talk:
- Account/order: {order number}
- Facts: on {date} I bought {prepaid SIM, RM60}; {top-up succeeded but service
  was never activated}; I already tried {live chat on 12 Sep, ticket #T-772} unresolved.
- My single demand: {refund RM60 to the original payment card}.
Answer in this order:
1. CAN PROCESS / CANNOT PROCESS — pick exactly one;
2. If CAN: the concrete steps and the timeline;
3. If CANNOT: the exact keyword I must type to reach a human agent.
Forbidden: saying "we will look into it as soon as possible"; repeating
information I already gave; apologising more than once.
Before answering, restate my order number and issue in one line to confirm
you read it correctly.
```

### 4.2 Why it works (mechanism, not assertion)

`p4-ai-prompting/core.md` §12 gives the rationale: "机器人（无论规则脚本还是 LLM 驱动）都服从提示中的显式约束；模板腔是它阻力最小的默认路径，除非被禁令点名；封闭式问题把它的「生成空间」压缩到可核查的是非输出，使绕圈在结构上不可能。" The en lane compresses the same point: "The bot's lowest-effort path is the canned deflection script; open-ended questions … just feed it more room to loop. You beat it by removing generation space." The five moves map to the KB's named techniques: single demand + number + deadline (constraints), closed question (output contract), ban list ("禁令比要求更有效"), forced readback (catch misreads in round one), human-exit probe ("很多 bot 只有被明确问到时才暴露转人工路径"). `Practice heuristic` (pattern), with official-guidance traces for the underlying techniques (`Evidence-backed`: Anthropic role/context and OpenAI constraint guidance in `core.md` Sources).

### 4.3 Two variations (when the base pattern stalls)

1. **Evidence-locked variation** — for when the bot starts quoting refund policy at you: paste the operator's actual terms and lock the source: "Answer only from the document I paste below; quote the exact line for every claim; say 'not found' where absent." (`p4-ai-prompting/en.md`, "It cited a policy that doesn't exist" — option 1.) Pitfall from the same entry: the most dangerous hallucinations are the most detailed ones; verify every citation it gives. `Practice heuristic`
2. **System-layer variation** — for long back-and-forths where the bot drifts: put the unchanging rules (language, ban list, output contract) in the system prompt or first paragraph, and send the volatile facts per message. Basis: `core.md` §4 — instructions at the system level "will take priority over a prompt in the input parameter" (`Evidence-backed`, OpenAI capture), and the drift fix: "重申系统层设定 / 开新会话并粘贴摘要" (`Practice heuristic`).

### 4.4 Failure modes to watch (from `core.md` §14, relevant rows)

| Failure mode | Symptom | Fix (KB) |
|---|---|---|
| 模板腔 / 过度道歉 | "非常抱歉给您带来不便……" loops | 负面清单 + 字数上限（§9、§12） |
| 一次塞太多任务 | only half the long prompt executed | 拆成多轮，一轮一个任务 |
| 幻觉 | invented policy clauses/dates | "只基于我给的材料；不知道就说不知道" + 人工抽查 |
| 输出失控 | prose where yes/no was contracted | 输出契约写死（格式、字段、字数），必要时给一个示例 |

En-lane pitfalls for this exact scenario: "Venting anger at the bot buys more apology, not action; stacking three demands lets it hop between them; if its readback of your order number is wrong, correct it immediately — everything downstream inherits the error." (`p4-ai-prompting/en.md`, "It keeps apologising and does nothing".)

## 5. Citation block

| KB file | Quoted line (verbatim) | Supports | Label |
|---|---|---|---|
| `wiki/synthesis/00-how-to-use.md` | "S4 \| Prompt：让 AI 与工具办成事（提示词工程）\| `wiki/playbooks/p4-ai-prompting/`" | engine routing | Evidence-backed (KB rule) |
| `wiki/playbooks/p4-ai-prompting/core.md` | "封闭式问题把它的「生成空间」压缩到可核查的是非输出，使绕圈在结构上不可能。" | rationale | Practice heuristic (§12 机制) |
| `wiki/playbooks/p4-ai-prompting/core.md` | "我的唯一诉求：{退款 RM89 到原支付卡}" (T6 line) | base pattern | constructed example |
| `wiki/playbooks/p4-ai-prompting/en.md` | "Reply with exactly one of: CAN PROCESS / CANNOT PROCESS." | closed question move | constructed example entry |
| `wiki/playbooks/p4-ai-prompting/en.md` | "Answer only from the document I paste below; quote the exact line for every claim; say 'not found' where absent." | variation 1 | constructed example entry |
| `wiki/playbooks/p4-ai-prompting/core.md` | "instructions 参数里的指令「will take priority over a prompt in the input parameter」" | variation 2 | Evidence-backed (OpenAI capture) |
| `wiki/scenarios/sc9-live-service/core.md` | "Ask 要给出数字和期限，才可能被记录进系统。" | demand-line wording | Practice heuristic |

## 6. SC4 statement

No external search; the pattern (T6), the mechanism paragraph, both variations and the failure-mode table all trace to the `wiki/playbooks/p4-ai-prompting/` files quoted above, whose official-guidance claims (OpenAI/Anthropic/Google, Wei 2022, Kojima 2022) are traced in those files' `## Sources` to `raw/p4-ai-prompting/` captures. The English rendering of T6 is explicitly labelled `constructed example` — the KB's lane contract (`AGENTS.md`: lanes are "NATIVELY authored lanes, NOT translations") forbids passing it off as quoted en-lane material.

**Verdict: PASS** — copy-pasteable slotted pattern ✓；mechanism rationale quoted from §12 ✓；KB path citations ✓；plus 2 variations and failure modes, all KB-grounded ✓。
