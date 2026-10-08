---
id: p3-formal-writing
title: Formal Writing · 正式写作
type: playbook
lang: zh
tags:
  - complaint
  - appeal
  - templates
scenarios:
  - S3
sources:
  - raw/p3-formal-writing/f-ttpm-prosedur.md
  - raw/p3-formal-writing/f-bnm-complaint.md
  - raw/p3-formal-writing/f-cfm-faq.md
related:
  - "[[playbooks/p3-formal-writing/core]]"
created: 2026-10-07
updated: 2026-10-07
---

LANE — authored natively, NOT a translation

### 兹函询 / 兹就……事宜函告

**Context** — 中文正式信（尤其给机构、公司、政府部门）的开头定调用语；メール或纸质信均可，投诉、申诉、申请皆常见。

**Reading** — 「兹」＝现在/特此，暗示以下内容是正式记录；收件方秘书处会按公函归档而非普通咨询处理。

**Response options**
1. 回信也保持同 register：「来函收悉」开头，走对等公文式回复。
2. 如果对方是客服语气，可降半格用「您好，就……事宜咨询如下」。
3. 律师函级别则用「受〔姓名〕之委托，函告如下」。

**Pitfalls** — 对私人小商家滥用「兹函」反而显得恐吓化；先判断对方是法人还是个人。

**Examples** — constructed example：检视 S3 冻结输入（预付卡退款）时，投诉信首段即可写「兹就本人在贵司购买的预付电话卡之充值及使用问题函告如下」。

### 时间线写法（日期列表而非叙事段）

**Context** — 投诉/申诉信的 body 核心：客服、监管员核案时只按日期对证据。

**Reading** — 每行「〔日期〕+〔动作/事实〕+〔附件编号〕」是格式合同层最优。

**Response options**
1. 全文用编号时间线，例如「2026-09-01 购卡；同日充值；2026-09-03 无法使用」。
2. 复杂纠纷可做成 Annex 表，正文只引 Annex 位。
3. 无实测日期就写「约」，并说明来源（银行账单/截图）。

**Pitfalls** — 把日期埋进长句里（"大约去年十月，可能是月底"）会让监管机构要求补充，延误一个月。

**Examples** — constructed example： Buyer 写「2026-09-01：购 RM30 预付卡（Annex A：收据 #A001）；2026-09-10：充值 RM30 失败（Annex B：截图）」。

### 诉求段模板（金额 + 期限 + 升级预告）

**Context** — 信的 demand 段；对方只精读这一段。

**Reading** — 一个具体动作 + 具体金额 + 来源渠道——三者齐备才算有效 demand。

**Response options**
1. 「现正式要求于本函发出之日起十四（14）日内退还全额 RM{{__}} 至〔尾号〕」，「否则本人将不再另行通知，径向 TTPM（消费者申诉法庭）提出索赔」。
2. 冷却版：「希望贵司在上述期限内提出可行方案；届时本人将考虑向 {{MCMC/T}} 反映」。
3. 拒付版：直接寄给发卡行，「请求依据您的争议/chargeback 程序，对 RM{{__}} 交易全数冲正」。

**Pitfalls** — 金额必须含小数与币种（RM30.00）；只写「要求退款」不给期限=没有 demand；同时要多个诉求会被挑最便宜回你。

**Examples** — 对 S3 冻结输入（未告知有效期），退全款 RM{{充值+购卡}} 是合理 demand。

### 「否则将升级至」预告句法

**Context** — 写给供应商第一封信的總結段前一句；是 firm-but-polite 的核心机关。

**Reading** — 表面是告知，实质是把 regulator 的程序规则当压力工具；Polite 之处在于对「您」仍留 amicable resolution 大门。

**Response options**
1. 行业分流：电讯→「径向 MCMC（aduan.mcmc.gov.my）投诉」；消费→「径向 TTPM 索赔」；银行→「径向 BNMLINK」。
2. 收件方是 BNM 监管机构时，预告下一级改为 FMOS。
3. 保留所有人情：「I remain open to an amicable resolution within that period」的作用是邮箱锁住公司信誉（不是预算）。

**Pitfalls** — 对监管机构本身预告升级（说要去另一监管机构）是浪费情绪；给出含糊威胁（「后果自负」）没有证据意义。

**Examples** — constructed example：telco 未回邮件第 14 天，升级信主题改为「HH — 往来投诉件二次升级 — 原件 Ref #A001— 转交 MCMC 已提请」。

### 收件人抬头（写职务而非 Sir/Madam）

**Context** — 所有正式信的 To 字段；中文公司信落实到「部门 + 职位 + 姓氏」。

**Reading** — 「投诉处理部经理〔姓氏〕先生/女士台启」比「敬启者」少三转发环节。

**Response options**
1. 未知姓名时用「责司客户服务部负责人员台启」。
2. 已有 ref no. 的 partner：抬头写回同一 ref，并在主题保留原时长以清时间线。
3. 政府部门：「全称 + 负责人职务」+ 官方信箱（TTPM/MCMC 均有固定门户而非个人邮箱）。

**Pitfalls** — 只留 To: customer service@ → 三次转接，工单号丢失；政府机关倾诉个人邮箱无效。

**Examples** — constructed example：「致：XX 电信 责任客户投诉部 经理 台启」（同时抄送至 aduan@cfm.my 备份，即为 MCMC 路径的预告）。

### 收尾敬词（此致 / 顺颂商祺 / 顺颂台安）

**Context** — 中文正式信收束，表明关系的正式度。

**Reading** — 对公司用「此致 敬礼」或「顺颂商祺」；对个人行政人员「顺颂台安」（中西混排时也常用）；对监管机构保留中立敬词。

**Response options**
1. 此致 + 敬礼（最高正式度，法院/学校函）。
2. 顺颂商祺（商业纠纷沟通，softening 後較自然）。
3. 敬颂钧安（政府部门强公文）。

**Pitfalls** — 署名前别用「谨启」自我降低；但多人联署投诉可用「常见联名体：恳请函复为盼」。

**Examples** — constructed example：附带四份 Annex 后「专此函达，恭候台复。」落款「投诉人：〔姓名〕（签署）」。

### 附件清单（Lampiran 一栏式）

**Context** — evidence pack 用中文写时，用「附件一」「附件二」编号，并在正文用括号回引。

**Reading** — 编号 + 文件名 + 对应事实日期；监管机构审附件时按编号对号。

**Response options**
1. 三件套：A 收据、B 瑕疵/失败截图、C 交涉记录。
2. 争议有合同/条款：另加 D 条款页（highlight 关键句）。
3. 已拿到拒绝函：始终另加 E（对升级诉求最有价值）。

**Pitfalls** — 只 attach 不 name 会丢；邮件里附件超 SJIS/兼容性问题会打不开，中文重要附件汇成单一 PDF。

**Examples** — constructed example：「附件：一、收据 #A001（2026-09-01）；二、充值失败截图（2026-09-10）；三、与客服往来记录（8–10 月共 6 封）」。

### 跟进催覆信（7 天后的第二封）

**Context** — 供应商砍件（无确认、无决定）后第 7 天。

**Reading** — 仅是「循环原信 + 新期限」，却在审计链上加一枚戳：ref no. ×2。

**Response options**
1. 「旧函 m Ref #X 于〔日期〕寄出，至今未获书面确认；今再设定七（7）日期限」。
2. 找错人时只需抬头换成 supervisor 其他不动。
3. 引用官方时限：「BNM/.ignore 可在 14 天后转向 BNMLINK」 Malaysia-specific。

**Pitfalls** — 二封信又给 30 天期限 → 自拆升级支点；漫谈情绪段落挪进第二封最伤。

**Examples** — constructed example（回信仍无）：第三封的主题「Final notice before Tribunal filing — Ref #A001 → TTPM 亥前日」。

### 三语平行段（中文信内附英文/马来段落）

**Context** — 收信方是跨国企业或双语客服，中文信量大时考虑附一版同等英文段。

**Reading** — 平行段是对抗「中文翻译件丢失」保险；Madan情形别替 AUTOMATIC 决定。

**Response options**
1. 关键 demand 段双写：中文主段 + 「English summary」三句。
2. 全马来收发时改Lane ms.md 之 Surat模板，不必混三语。
3. 上诉法庭（TTPM 表）填 BM/EN，印象更 solid。

**Pitfalls** — 一封信三语平铺只显混乱，中文主体段落最高两语言即可。

**Examples** — constructed example： 「（English: Refund of RM60.00 within 14 days; failing which TTPM claim will be filed.）」

### 投诉信全景模板（可整段复制填空）

**Context** — S3 等投诉信引擎的完整中文版骨架。

**Reading** — 七件套齐全，缺一即 FAIL。

**Response options**
1. 基础版见于 core.md §8.1（三语同骨），中文改写如下。
2. 网购/海外商家：demand 换 chargeback 路径（§8.3）。
3. 已拒绝过：升篇改「投诉升级信」结构。

**Pitfalls** — 中文日期要用公历（YYYY-MM-DD 公式）；「昨日」「上周」禁用。

**Examples** — constructed example（S3 冻结输入的中文骨架）：

```
From: 〔姓名、地址、电话、邮箱〕
To: 〔电讯公司〕 客户投诉部 经理台启
Date: 2026-10-07

Subject: 正式投诉 — 预付卡 RM60 无法使用、未告知有效期 — Ref：收据 #A001 — 要求全额退款

台鉴：
一、2026-09-01 本人从贵司购买预付电话卡一张（附件一：收据 #A001）。
二、购买及充值时贵司未告知有效期，2026-09-10 充值后仍无法使用（附件二：截图）。
三、本人于 9 月 12 至 28 日间三次联系客服（工单 #T-772、#T-810），均未获书面答复。
四、该做法违反收费服务之告知义务。

现正式要求贵司于本函发出之日起十四（14）日内退还 RM60.00 至本人原付款账户。
否则本人将就此事向 MCMC（aduan.mcmc.gov.my）投诉，并保留向消费者申诉法庭索赔之权利。
本人在上述期限内仍愿接受友好协商之任何可行方案。

附件：一、收据 #A001；二、充值失败截图；三、与客服往来记录。
此致 敬礼
投诉人：〔签名〕
```

### 内部邮件：「抄送你老板」与「如前所述」

**Context** — 跨部门或对内的半正式邮件；出现 cc 你的直属上司，或对方回「如前所述（Per my last email）」。

**Reading** — 「如前所述」= 公开记账「你没读/你漏了」，是施压而非提问；cc 上司 = 把 stakes 抬到台面、留痕。看 cc 名单判断对方把你放到哪一档（tier-2：raw/p3-formal-writing/f-cnbc-passive-email.md、f-wtj-passive-email.md）。

**Response options**
1. 先补读、只回事实：「已按你 {{日期}} 邮件第 2 点更新，见下——若我漏了某项请指出。」
2. 把冲突转私下：「关于节奏，我们电话 5 分钟对齐？我 {{时间段}} 有空。」
3. 需要留痕时，只做纪要式回复：一条 ask + 一个期限。

**Pitfalls** — 在情绪当天、且对方上司在 cc 里时回呛；把「如前所述」当人身攻击，而不是「该补读了」的提醒。

**Examples** — constructed example：对方 cc 你老板写「Per my last email，请确认」；你只补数据不辩论，事后再约电话。

## Sources

- TTPM 官方 Prosedur Pemfailan（Borang 1 ×4、RM5、14 天答辩、1-800-88-9811）: https://ttpm.kpdn.gov.my/Prosedur_Pemfailan.html
- BNM Lodge Complaint（14 天规则、BNMLINK 1-300-88-5465）: https://www.bnm.gov.my/contact-us/lodge-complaint
- MCMC Redress Portal / CFM FAQ（aduan.mcmc.gov.my、1800-188-030、aduan@cfm.my）: https://cfm.my/wp-content/uploads/2025/01/Frequently-Asked-Questions-CCMD.pdf
- CNBC (2023-11-27) — Don't reply to that passive-aggressive email: https://www.cnbc.com/2023/11/27/dont-reply-to-passive-aggressive-emails-communication-expert.html
- Welcome to the Jungle — How to avoid passive aggression in the office: https://www.welcometothejungle.com/en/articles/passive-aggressive-comments-worklife
- FTC Sample Customer Complaint Letter（polite-and-reasonable 之官方模板）: https://consumer.ftc.gov/articles/sample-customer-complaint-letter
