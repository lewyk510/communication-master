---
id: p3-formal-writing
title: Formal Writing · 正式写作
type: playbook
lang: core
tags:
  - complaint
  - appeal
  - escalation
  - malaysia
  - templates
scenarios:
  - S3
sources:
  - raw/p3-formal-writing/f-ttpm-prosedur.md
  - raw/p3-formal-writing/f-bnm-complaint.md
  - raw/p3-formal-writing/f-cfm-faq.md
  - raw/p3-formal-writing/f-ftc-complaint-letter.md
  - raw/p3-formal-writing/ttpm.json
  - raw/p3-formal-writing/bnm.json
  - raw/p3-formal-writing/mcmc.json
  - raw/p3-formal-writing/cca.json
related:
  - "[[playbooks/p1-reply-engine/core]]"
  - "[[concepts/c3-nvc-conflict-repair/core]]"
  - "[[scenarios/sc4-hard-conversations/core]]"
created: 2026-10-07
updated: 2026-10-07
---

# p3-formal-writing — 正式写作引擎（投诉 / 申诉 / 申请 / 拒绝 / 谈判）

本 playbook 是一台**引擎**：给结构、给模板、给升级阶梯。所有信件类型共享一个骨架（sender / recipient / date / subject / body / demand / enclosures），差别只在 body 的论证顺序与 demand 的强度。rules: 所有监管机构名称与联系方式均 trace 至 `raw/p3-formal-writing/` 的 capture（见 `## Sources`）。

---

## 1. 通用骨架（Engine skeleton）

每一封正式信必须包含全部七件套，缺一即 Fail（对应 QA S3 Pass criterion #1）：

```text
1. Sender    发件人：姓名、地址、电话、邮箱（Legal recipient 要能回复你）
2. Recipient 收件人：具体到「人 + 职位 + 部门」，比 "Dear Sir/Madam" 强十倍
3. Date      日期（YYYY-MM-DD）
4. Subject   主题：〔类型〕+〔账单/交易/工单 reference number〕+〔一句话诉求〕
5. Body      背景→事实时间线→违反了什么→造成什么损失
6. Demand    诉求：一个具体动作 + 一个具体金额 + 一个具体期限
7. Enclosures 附件：发票、截图、合同、往来邮件的编号清单
```

- **Reference numbers 是正式信的灵魂。** Subject 与 body 内每一处事实都挂上单号：发票号、订单号、工单号、账号尾号、此前的投诉编号（complaint ref / ticket ID）。监管机构收信时第一件事就是找这些单号。
- **Practice heuristic**：把「时间线」写成日期列表而不是段落——最高可读性，监管人员审案主要看时间线。

## 2. Demand 写法：一个动作 + 金额 + 期限

**Evidence-backed**（FTC官方投诉信套件，`raw/p3-formal-writing/f-ftc-complaint-letter.md`）：FTC 要求投诉信明确「tell the business what you want, like a refund, repair, exchange」，并保持 polite and reasonable。

Demand 段的三段式模板：

```text
I am requesting a full refund of RM [___], paid via [method] on [date],
to be credited to [account/card ending ___].
If the refund is not processed within [14] days of this letter,
I will escalate this matter to [TTPM / BNMLINK / MCMC / NCCC] without further notice.
```

- 期限常用 7 / 14 / 30 天；「escalation ladder」预告写进信里本身就是软性压力（见 §5）。
- **Practice heuristic**：一次只提一个 primary demand（退款），repair / exchange / apology 作为 secondary 或不提——多诉求会让回信方挑最便宜的那条回你。

## 3. 六类信件的 body 差异

| 类型 | 核心结构 | Demand 钩子 |
| --- | --- | --- |
| 投诉信 complaint | 问题时间线 + 权利来源（合同/法条） | 退款/修复 + 期限 |
| 申诉信 appeal | 决定内容 → 申诉理由逐条反驳 → 请复审 | 重审决定 + 期限 |
| 退款/拒付 demand refund/chargeback | 交易单号 + 交涉记录已失败 + [银行/卡组织] 条款 | 全额退款 + 14 天 |
| 申请信 application | 资历 → 匹配点 → 请求 +所需材料清单 | 批准/面试/签发 |
| 正式拒绝 refusal | 收悉致谢 → 拒绝决定 → 理由 → 替代方案 | 无（但留门） |
| 谈判邮件 negotiation | 共同目标 → 我方筹码 → 提案 → 让步边界 | 一揽子 offer + deadline |

## 4. 语气：firm-but-polite 的操作化

**Practice heuristic**（源自 FTC 官方模板与马来西亚消费者实践）：

1. Firm 在**事实与期限**，polite 在**人称与预期**。写「the service I paid for was not delivered」而不写「你们骗子」。
2. 不加情绪形容词（disgusting / furious）、不加威胁人身的话，威胁只存在一个维度：升级到监管/法务。
3. 每段落是一个命题，一段一个主题；总长 ≤ 1 页 A4（email ≤ 250 词）——审件人 30 秒内看完诉求。
4. 结尾保持开放：`I remain open to a amicable resolution` 这句要有——但**必须排在 deadline 之后**。

三语 register 对照（同一封信三种语言）：

| 层级 | English | Bahasa Melayu | 中文 |
| --- | --- | --- | --- |
| 开头 | I refer to the above matter | Saya merujuk kepada perkara di atas | 兹函询上述事项 |
| 陈述错误 | The service was not delivered as agreed | Perkhidmatan tidak diberikan seperti yang dipersetujui | 贵方未按约定提供服务 |
| 诉求 | I hereby request… | Saya dengan ini memohon dengan rasmi… | 现正式要求…… |
| 期限 | within fourteen (14) days | dalam tempoh empat belas (14) hari | 于十四（14）日内 |
| 升级预告 | otherwise I will lodge a complaint with… | sekiranya tidak, saya akan memfailkan aduan kepada… | 否则将向……提出投诉 |
| 收尾 | Faithfully, / Yours sincerely | Yang benar, | 此致 盼复 / 顺颂商祺 |

**Practice heuristic**：马来正式信用 Saya merujuk kepada…（大宗信函开头句）；中文「兹」「贵方」「此致」标记正式度；英文 I refer to / I am constrained to… 同理。

## 5. 升级阶梯（Escalation ladders）——马来西亚路径

**Evidence-backed**：以下每一级机构与联系方式均 trace 到 capture；未列入正文引用的机构，仅作 path 提示。

马来西亚通用四级阶梯：

```
【第1级】服务商内部
         customer service / Complaints Unit → 书面投诉，拿到 complaint ref no.
   ↓ 未解决（含超过期限）
【第2级】上级/ dsp 安排
         supervisor / Head of Customer Experience（如果第1级拒绝给出 ref no.，这就是升级的理由）
   ↓
【第3级】监管机构/投诉中介（按行业分流）
         · 消费类（宽带、外卖、电商平台、预付卡等消费纠纷，TTPM 无金额下限，上限以官网为准）：TTPM
         · 电讯丶多媒体：MCMC / CFM
         · 银行 / 保险 / Takaful / e-money：BNM BNMLINK
         · 公司/经营主体合规问题：SSM
         · 民间声援与调解：NCCC / FOMCA / CAP
   ↓ 仅 TTPM 是「裁定级」；其余为调解级
【第4级】TTPM 裁定 / FMOS / 法庭
```

### 5.1 TTPM — Tribunal for Consumer Claims Malaysia

**Evidence-backed**（官方程序页 `raw/p3-formal-writing/f-ttpm-prosedur.md`，2024-08-29 更新）：

- 用 Borang 1（Pernyataan Tuntutan / Statement of Claim）提出，免费取表或从 ttpm.kpdn.gov.my 下载。
- 填 **4 份 Borang 1**，到最近的 Tribunal 登记处提交，**挂号费 RM5.00**（将获得正式收据）；也可在 https://ttpm.kpdn.gov.my/user/login 在线提交。
- Penentang（被诉方）必须在收表后 **14 天内提交 Borang 2**（答辩）。
- 热线：**1-800-88-9811**；隶属 KPDN（Kementerian Perdagangan Dalam Negeri dan Kos Sara Hidup）。
- **Practice heuristic**：写给你的第 1 级投诉信时，在结尾加 `Failing which I will file a claim at the Tribunal for Consumer Claims Malaysia` 即升级第 3 级的预告。

### 5.2 MCMC / CFM — 电讯与多媒体

**Evidence-backed**（CFM FAQ capture `raw/p3-formal-writing/f-cfm-faq.pdf 文件`）：

- 网上投诉门户：**https://aduan.mcmc.gov.my/**（MCMC Consumer Redress Portal）
- 电话：**1800-188-030**（CFM Customer Contact Centre，受 MCMC 委托运营）
- E-mail：**aduan@cfm.my**（hanya可递交或获取进度）
- Walk-in：Ground Floor, MCMC Tower 2, Jalan Impact, Cyber 6, 63000 Cyberjaya, Selangor
- **Practice heuristic**：S3 冻结输入（预付卡问题）走的正是 MCMC 路径（配套证据链：有效期告知义务属 telco/comms service dispute）。

### 5.3 BNMLINK — Bank Negara Malaysia（银行/保险/e-money）

**Evidence-backed**（官方投诉页 `raw/p3-formal-writing/f-bnm-complaint.md`）：

- **3 步规则**：先向金融机构的 **Complaints Unit**（不是 Business/Claims Unit）取得最终决定 → 未收到回复 **14 天**后，可向 **BNMLINK** 提案。
- BNMLINK 渠道：webform https://bnmlink.bnm.gov.my/；电话 **1-300-88-5465**；email bnmtelelink@bnm.gov.my；SMS 15888；邮件 BNMLINK, Bank Negara Malaysia, 50929 Kuala Lumpur。
- BNM 拒收范围：未先向 Complaints Unit 提交的、已进 FMOS / 法庭 / tribunal 的；credit companies / pawn brokers / leasing 不属 BNM 监管（属 KPDN）。
- **Practice heuristic**：给银行的信里写 `Please provide your final decision in writing within 14 days as required for BNMLINK referral`——把 regulator 的时间规则作为压力拿在手上。

### 5.4 SSM — Suruhanjaya Syarikat Malaysia

**Evidence-backed**（官网检索 capture `raw/p3-formal-writing/ssm.json`）：

- Channel：e-Complaint（ssm.com.my /Pages/Services/Other-Services/e-Complaint.aspx）；Customer Care **+603-7721 4000**；enquiry@ssm.com.my；SSMCC 8:00-5:30。
- 适用：处理公司主体、合规、 misleading representations of a registered business 的问题（显得与 TTPM 分工不同：SSM 对 business, TTPM 对 consumer-merchant relationship）。

### 5.5 消费者协会（声援与调解）

**Evidence-backed**（协会门户检索 capture `cca.json` / `consumersinternational.org`）：

- **FOMCA** — www.fomca.org.my；tel +603-78764648；fomca@fomca.org.my；其辖下 **NCCC**（National Consumer Complaints Centre，www.nccc.org.my）可直接受理投诉。
- **CAP（Consumers Association Penang）** — consumer.org.my；info@consumer.org.my；No. 10, Jln Masjid Negeri, 11600 Jelutong, Pulau Pinang；04-8299511。
- **Practice heuristic**：协会发函（第 3.5 级）的意义是「把升级至公众/媒体」预告写进信里——对本地商家非常有效。

## 6. 证据与文件编号清单（Evidence pack）

**Practice heuristic**：升级信（第 2 级及以后）随信附一张 evidence index 表：

```text
Enclosures:
  Annex A — Invoice / receipt no. ____ (RM ____, dated ____)
  Annex B — Evidence of defect / non-delivery (photos/screenshots, dated)
  Annex C — The contract / ad / promo terms relied upon (rev. ____)
  Annex D — Correspondence timeline: SMS/WhatsApp/email log, ref nos. ___
  Annex E — Provider's final decision or acknowledgement letter
```

TTPM 也要求 Statement of Claim 附 supporting documents（`raw/p3-formal-writing/ttpm.json`：richard we chambers 的实务指南亦提示 attach supporting documents 并缴纳 RM5 filing fee）。

**Practice heuristic**：所有附件在正文里都有对应参照句（Annex A: receipt no. 12345），别只 attach 不提。

## 7. Deadline 与 follow-up（节奏表）

**Practice heuristic**（结合 BNM 14 天规则与通用惯例）：

```
Day 0   发第 1 封投诉信（registered mail / email + read receipt）
Day 7   无任何确认 → follow-up email：附首通信，设 7 天最后期限
Day 14  仍无解决 → 发升级信给 supervisor（为客户升级预告的 executes tertiary rung）
Day 21–30 → 向 regulator / TTPM（Banking: BNMLINK；Telco: aduan.mcmc.gov.my）
TTPM already been filed → 听着会安排 hearing；不须要律师
```

- 每一封 follow-up 都要 paste 上一封信与 ref no.（把时间线串成一条审计链）。
- 法定或监管期限压倒一切：BNM 的 14 天、TTPM Penentang 的 14 天答辩期。

## 8. 每信类型的填空骨架（Skels）

以下 6 个骨架是引擎的交付物。{{ }} 是填空槽位。

### 8.1 Complaint letter（投诉信）

```text
From: {{name}}, {{address}}, {{tel}}, {{email}}
To: {{officer}}, {{title}}, {{company}}, {{address}}
Date: {{YYYY-MM-DD}}

Subject: Formal Complaint — {{product/service}} — Ref {{invoice/order no.}} — Demand for {{refund of RM___}}

Dear {{officer}},

1. On {{date}} I purchased {{item}} from you for RM{{amount}} (Annex A: receipt no. ___).
2. On {{date}} the following problem arose: {{facts, dated one per line}} (Annex B).
3. This breaches {{contract clause / paid service / advertised term}} (Annex C).
4. I contacted your team on {{date}} ({{ref no./agent name}}) and was told {{outcome}}.

I hereby request {{refund of RM___ / repair / replacement}} within fourteen (14) days
of this letter. Failing which, I will lodge a complaint with {{CFM/MCMC aduan.mcmc.gov.my |
TTPM | NCCC}} and pursue all available remedies without further reference to you.
I remain open to an amicable resolution within that period.

Enclosures: Annex A–D as listed.

Yours faithfully,
{{name}}  {{signature}}
```

### 8.2 Appeal letter（申诉信）

```text
Subject: Appeal against {{decision}} dated {{date}} — Ref {{case no.}} — Request for reinstatement/reassessment

Dear {{deciding officer}},

1. On {{date}}, you informed me that {{decision summary}} (copy attached).
2. I respectfully appeal against this decision on the following grounds:
   (a) {{ground 1 + evidence, Annex B}}
   (b) {{ground 2 + evidence, Annex C}}
   (c) {{procedural defect, if any}}
3. I further enclose {{new evidence not before the decision-maker}} (Annex D).

I request that the decision be reviewed/reinstated, and that I receive a written
decision within fourteen (14) days. Sections {{X}} of the {{relevant guideline}}
support this appeal.

Yours faithfully, ...
```

### 8.3 Refund / chargeback demand（退款与拒付）

```text
Subject: Refund Demand — Transaction {{txn no.}} RM{{amount}} — {{merchant}} — 14-day deadline

To {{bank/card issuer}}:
I paid {{merchant}} RM{{amount}} on {{date}} (txn ref ___). The goods/service
was {{not delivered / materially not as described}}. I have complained to the
merchant in writing on {{dates}} (Annex D) without resolution.

Under your dispute/chargeback procedure, I request a chargeback for the full
amount of RM{{amount}}. Evidence: merchant terms (Annex C), merchant
correspondence (Annex D). If you decline, please provide your final written
decision so I may refer the matter to BNMLINK / the relevant redress channel.
```

### 8.4 Application letter（job / school / government）

```text
Subject: Application for {{position/programme}} — Ref {{vacancy code}}

Dear {{officer}},

1. I apply for {{position}} advertised on {{source + date}}.
2. I hold {{highest qualification}} and have {{n}} years' experience in {{field}}
   (CV Annex A; certificates Annex B).
3. The role requires {{requirement 1}} — my {{experience}} matches this;
   {{requirement 2}} — my {{experience}} matches this.
4. I am available to commence from {{date}} and to attend {{duty stations}} as required.

I request an interview / processing of my application and am pleased to furnish
any additional documents.

Yours faithfully, ...
```

### 8.5 Formal refusal（正式拒绝）

```text
Subject: Re: {{their request}} — Ref {{their ref no.}} — Refusal with reasons

Dear {{name}},

1. Thank you for your letter of {{date}} regarding {{request}}.
2. After careful consideration, I regret to inform you that we are unable to
   {{grant the request}}, because {{reason tied to a rule/contract/policy}}.
3. {{rung}: I enclose {{alternative I CAN offer}} / the correct channel for
   reconsideration is {{X}}, within {{deadline}}.

We value your continued trust. Should you wish, I am available to discuss
the alternatives above. This letter does not constitute an admission or waiver
of any rights. 【Rejection letters: 留一句 "may be reconsidered if ..."】
```

### 8.6 Negotiation email（谈判）

```text
Subject: Proposal to resolve {{dispute}} — Ref {{file no.}} — {{party A ↔ party B}}

Dear {{counterparty}},

1. Our shared objective is {{outcome both parties want}}.
2. Our position: we hold {{leverage}} — {{evidence of strength, briefly}}.
3. Proposal: {{package — you do X (your ~% concession), we do Y (our ~% concession)}}
   within {{period}}, in full and final settlement.
4. Authority: this proposal requires sign-off from our side by {{date}}; after
   {{expiry}} it lapses. We would accept the deal on these terms only, and retain
   the right to revert to the prior (higher) position thereafter.

Kindly confirm acceptance or counter with terms that satisfy clause 3's
structure, by {{deadline}}.
```

## 9. 三语信型短语库（fill-in phrases）

**Practice heuristic**：三个 lane 里的完整信模板（投诉信 / 申诉信 / 申请信）分别在本目录的 `zh.md`、`en.md`、`ms.md`；本节只列跨信法定条件对照：

| 元素 | zh | en | ms |
| --- | --- | --- | --- |
| Subject 前缀 | 「关于：……之正式投诉」 | RE: Formal Complaint — ... | Perkara: Aduan Rasmi — ... |
| 引语 | 兹函询 | I refer to the above matter | Saya merujuk kepada perkara di atas |
| 附件 | 附件：一至四 | Enclosures: Annexes A–D | Lampiran: Lampiran A–D |
| 不给答复后果 | 否则将不再另行通知，径提交 | Failing which … without further reference | Sekiranya gagal, aduan akan difailkan tanpa notis lanjut |

## 10. 内部邮件子类（internal email）

**Practice heuristic + tier-2 来源**（`raw/p3-formal-writing/f-cnbc-passive-email.md`、`f-wtj-passive-email.md`）：内部邮件（对内汇报、跨部门、cc 上司）是"半正式"语域——语域低于对外正式信，潜台词密度却更高。三个高频信号：

- **"Per my last email" / "如前所述"** — 表面复述，实为公开记账"你没读/你漏了"；是施压而非提问。收到先补读，别对呛。
- **cc / bcc 的层数** — 抄送你的直属上司 = 抬高 stakes、留痕；密送 = 避免正面冲突但已"存档"。看 cc 名单判断对方把你放到哪一档。
- **跟进节奏** — 第一次不催、第三次升级；"Just following up" 越用越薄，第三次应改电话/当面。`Practice heuristic`

**写法骨架（三步：context → ask → close）**

```text
Subject: {{topic}} — {{action needed}} by {{date}}

Hi {{name}},
1. Context: {{one line of shared state / last email ref}}
2. Ask: {{one specific action + deadline}}
3. Close: thanks — {{what happens next if no reply by deadline}}
```

规则：一次一封、**一个** ask、**一个**期限；情绪当天不互呛，草稿箱隔夜再发。`Practice heuristic`

---

## Sources

Tier-1（官方 / 学术 / 监管）:

- Tribunal Tuntutan Pengguna Malaysia (TTPM/KPDN) — Prosedur Pemfailan (Borang 1 ×4, RM5 fee, 14-day答复期, 1-800-88-9811): https://ttpm.kpdn.gov.my/Prosedur_Pemfailan.html （captured: raw/p3-formal-writing/f-ttpm-prosedur.md）
- Bank Negara Malaysia — Lodge Complaint（3-step rule, 14-day → BNMLINK, 1-300-88-5465, bnmlink.bnm.gov.my）: https://www.bnm.gov.my/contact-us/lodge-complaint （captured: raw/p3-formal-writing/f-bnm-complaint.md）
- MCMC Consumer Redress Portal / CFM FAQ (aduan.mcmc.gov.my, 1800-188-030, aduan@cfm.my): https://cfm.my/wp-content/uploads/2025/01/Frequently-Asked-Questions-CCMD.pdf （captured: raw/p3-formal-writing/f-cfm-faq.md）
- FTC (US) — Sample Customer Complaint Letter, polite-and-reasonable structure: https://consumer.ftc.gov/articles/sample-customer-complaint-letter （captured: raw/p3-formal-writing/f-ftc-complaint-letter.md）

Tier-2（established media / 检索快照，用于交叉确认）:

- Serper search snapshot: raw/p3-formal-writing/ttpm.json （含 KPDN 官方 e-Tribunal 登录页 https://ttpm.kpdn.gov.my/user/login）
- Serper search snapshot: raw/p3-formal-writing/bnm.json
- Serper search snapshot: raw/p3-formal-writing/mcmc.json （MCMC 之 1800-188-030 等渠道确认）
- Serper search snapshot: raw/p3-formal-writing/cca.json （FOMCA +603-78764648 fomca@fomca.org.my；NCCC www.nccc.org.my；CAP consumer.org.my 04-8299511）
- Serper search snapshot: raw/p3-formal-writing/ssm.json （SSM Customer Care +603-7721 4000, enquiry@ssm.com.my, e-Complaint 页 https://www.ssm.com.my/Pages/Services/Other-Services/e-Complaint.aspx）
- Serper search snapshot: raw/p3-formal-writing/writing.json （英文模板惯例）
- CNBC (2023-11-27) — "Don't reply to that passive-aggressive email": https://www.cnbc.com/2023/11/27/dont-reply-to-passive-aggressive-emails-communication-expert.html （captured: raw/p3-formal-writing/f-cnbc-passive-email.md）
- Welcome to the Jungle — "How to avoid passive aggression in the office": https://www.welcometothejungle.com/en/articles/passive-aggressive-comments-worklife （captured: raw/p3-formal-writing/f-wtj-passive-email.md）
- Serper search snapshot: raw/p3-formal-writing/internal-email.json （"per my last email" / cc 语义交叉确认）"
