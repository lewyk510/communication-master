---
id: sc17-landlord-tenant
title: Landlord & Tenant · 租客与房东
type: scenario
lang: core
tags:
  - rental
  - landlord
  - tenant
  - deposit
  - tenancy-agreement
  - repair
  - eviction
  - malaysia
scenarios:
  - S2
  - S3
sources:
  - raw/sc17-landlord-tenant/f-bar-tenancy.md
  - raw/sc17-landlord-tenant/f-tenant-rights.md
  - raw/sc17-landlord-tenant/f-ttpm-jurisdiction.md
  - raw/sc17-landlord-tenant/s-deposit-dispute.json
  - raw/sc17-landlord-tenant/s-eviction-agreement.json
related:
  - "[[scenarios/sc9-live-service/core]]"
  - "[[scenarios/sc10-negotiation-deals/core]]"
  - "[[scenarios/sc4-hard-conversations/core]]"
created: 2026-10-07
updated: 2026-10-07
---

本页覆盖马来西亚语境下 landlord/tenant 的双向沟通：租客侧（要维修、要退押金、应对涨租、防止被赶）与房东侧（催租、通知搬离、谈续约）。押金、协议、维修与通知是四条最高频的冲突线。双语话术见 [[scenarios/sc17-landlord-tenant/zh]] / [[scenarios/sc17-landlord-tenant/en]] / [[scenarios/sc17-landlord-tenant/ms]]。

### 1. 关系的结构性错位：短期契约，长期共处

Practice heuristic：房东租客与客服投诉不同——不是一次性交易，而是把"陌生人契约"装进"长期共同生活"的容器里。每次沟通都要同时维护两样东西：契约上的钱（rent、deposit）和共处上的余地（噪音、维修、续约）。所以租客场景的默认策略是**先修关系再谈钱**，与 sc9 投诉场景（sc1/sc9 的 Fact–Impact–Ask 单刀直入）恰好相反。Practice heuristic：只有在关系已经破裂或对方不作为时，才切换到投诉式打法——那是最后一段阶梯，不是第一句开场。

### 2. 押金结构：2+1 及其含义

Evidence-backed：马来西亚通行押金结构是 **2+1**——两个月 gross rental 作 security deposit，加一个月（或半个月）作 utility deposit（水电按账单结算后再退还）。租约签定时通常另付首月租金；Malaysian Bar 的范例是 RM500 租金、签约时付 RM2,000（首月 + 2 个月押金 + 1 个月 utility）（来源：f-bar-tenancy.md）。同一标准结构也见于 propcashflow 与 superhomes 的指南（s-rental-guide.json、f-tenant-rights.md）。

Practice heuristic：押金数字三倍于月租是常态，租客谈租金时往往漏了谈押金——半个月的 utility deposit、可分期支付的押金、或"押金上限封顶"都值得在签约前开口，签约后没有任何谈判空间。

### 3. Tenancy agreement：盖章比签字更重要

Evidence-backed：马来西亚租约（tenancy agreement）要经 LHDN 盖章（stamp duty）才能在法庭作为证据；未盖章的租约不能作为呈堂证据，显著削弱任何一方立场（来源：f-tenant-rights.md）。Practice heuristic：把 stamp duty 分摊写进谈判（常见做法各付一半或房东承担）；拿到盖章原本的照片存档。口头协议对三年以下的租期按 NLC（国家土地法典）可构成租约，但"verify 起来几乎不可能"。

Practice heuristic：给房东转账首月押金前，先把完整 tenancy agreement 发到自己邮箱并确认盖章安排。尚未盖章的空白期是你证据链上最脆弱的一段。

### 4. Wear and tear vs damage：押金战的核心分界

Evidence-backed：押金只能为**超出正常磨损的损坏**（damage beyond normal wear and tear）扣减。正常磨损包括阳光褪色的油漆、地板浅划痕、挂画钉孔、浴室填缝轻微变色——房东不能为此收费；超出项是大洞、破窗、烧痕/污渍地毯、误用损坏的电器、搬家时缺失的 fixtures（来源：f-tenant-rights.md，speedhome.com 同义口径见 s-deposit-dispute.json）。Bar 的租约条款表述一致：租客交还房屋须"good and tenantable repair, fair wear and tear excepted"，对因租客行为或疏忽造成的损坏自费修补（f-bar-tenancy.md）。

Practice heuristic：move-in 当天全屋带时间戳的照片/视频是这场战役唯一可靠的武器；没有入住照片，任何"是你弄的"指控都难以反驳。同理，move-out 当天再拍一轮，与入住照片配对。

### 5. 押金退还：时限、扣减清单与不当扣减

Evidence-backed：租约没有法定退还期限；通行预期是搬离后 14–30 天，以租约写明为准；若有扣减，租客有权获得逐项列明（itemised list）的扣减清单（来源：f-tenant-rights.md）。房东**不能**扣的项目：除非合约明文要求，租客不需要为整屋重新粉刷付费；除非合约明文要求专业清洁而你没做到；以及一切你入住前已存在的损坏（pre-existing damage）。Practice heuristic：搬离交钥匙时当面写一份"钥匙移交 + 电表读数 + 现状说明"的简短书面记录，双方签字或 WhatsApp 确认——这是启动"押金应退"叙事的起点。

constructed example（租客侧写法）："Hi Mr Tan，以下是我明早搬离的交还清单：钥匙 2 把、水表读数 2381、电表读数 56402、全屋照片 46 张已上传 Google Drive（链接）。请按 TA 第 6 条于搬离后 14 天内退回押金 RM3,300 至Attached 账户，如有扣减请一并列明明细。谢谢。"

### 6. TTPM 的大反转：租赁争议一般**不在** TTPM

Evidence-backed（重要纠偏）：一个广泛流传的说法是押金纠纷去 TTPM（消费人仲裁庭）。官方页面显示 TTPM 无权受理"为追回土地或土地上的任何权益"的索赔（f-ttpm-jurisdiction.md："bagi mendapatkan kembali tanah atau apa-apa estet atau kepentingan mengenai tanah"）；CPA 1999 s.99 的排除清单通常使租赁纠纷（a tenancy is an interest in land）落在 TTPM 之外。正确的正式轨道是**民事法院**（Evidence-backed：f-tenant-rights.md）：

| 途径 | 金额上限 | 律师 | 用途 |
|---|---|---|---|
| 书面催告函 demand letter | 无 | 不需要 | 每类纠纷的第一步，也是"已有催告"的证据 |
| 推事庭小额索赔程序（Order 93, Rules of Court 2012） | RM5,000 | 禁止律师 | 大多数押金退还与小额损坏索赔：自填 Form 198，无需律师 |
| 推事庭 Magistrates' Court | RM100,000 | 自选建议 | 更大的押金、租金或损坏索赔 |
| 高等地方法庭 Sessions Court | RM1,000,000 | 建议聘请 | 大额金钱索赔 |

Practice heuristic：正因为 RM5,000 以下小额程序免律师、无需讼费太高，押金扣减争议的精确金额（扣多少、为什么扣）沟通要把它对齐到 RM5,000 以内——诉求清晰、金额可分项，才保留小额通道。RM5000 以上再评估成本。

### 7. 维修分工：谁修屋顶、谁修灯泡

Evidence-backed：马来西亚通行条款——**房东**承担 quit rate & assessment（地税/门牌税），并负责维持与维修 roof、main structure、external walls、main drains and pipes（屋顶、主体结构、外墙、主管道）；**租客**交还时保持合理良好状态（fair wear and tear excepted），并对自身行为或疏忽造成的损坏自费修复（来源：f-bar-tenancy.md）。

Practice heuristic：报修消息按这三层心里先归位再开口：(1) 结构类（漏水、热水器爆、电线老化）→ 房东责且可能紧急；(2) 耗材类（灯泡、水龙头垫圈、门吸）→ 默认租客自付、自可更换；(3) 毁损类（自己弄坏的）→ 承认并可安排更换。报修模板三句走：事实（哪里、何时、什么现象）＋影响（无法做饭/无法入睡/水位上涨）＋行动的组合（"我可以周六在家等水电工，也附上跑腿选择"）。第一条消息里只报事实，不飞指控。

constructed example（报修）："Mr Tan 早安。昨晚 11 点起厨房水槽下的排水管接缝处持续滴水，地上已经积了一小滩水（附照片 2 张）。这属于主管道问题，麻烦今晚或明天安排水管工；我随时在家方便维修。谢谢。"

### 8. 通知期与提前退租 Notice Period

Evidence-backed：终止通知或搬离通知须按租约写明的期限提前发出（f-bar-tenancy.md）。续约惯例：租客有优先续租权，且须在到期前三个月提出续租意向（f-bar-tenancy.md）。提前退租若租约有 penalty 条款：常见是提前 1–2 个月书面通知 + 没收部分或全部押金；但 s.75 Contracts Act 1950 将违约金封顶在"合理补偿"，联邦法院 Cubic Electronics v Mars Telecommunications (2019) 确认该原则适用于押金——过度的没收可以被挑战（Evidence-backed：f-tenant-rights.md）。若租约有 diplomatic clause（外交条款/工作调动条款），通常提前 2–3 个月通知即可不没收押金退出。

Practice heuristic：租客侧的提前退租话术是"补偿包谈判"：主动 forfeit 一个月而非两个月、帮忙找接替租客、承担中介费房东侧成本——用压低房东的实际换租成本来换减免。房东侧一律把折扣的条件写进书面回复。

### 9. 涨租：只能发生在续约时

Evidence-backed：租期之内除非合约本身有 rent review / escalation 条款，房东不能涨租；涨租只能作为续约提议提出，你有权接受、还价或拒绝走人（f-tenant-rights.md FAQ；s-rental-guide.json 同口径）。Practice heuristic：马来西亚 2026 年仍无 Residential Tenancy Act 或租金上限，租金保护完全来自你的条款——续约谈判里"涨 20%"的还价基准是市场可比租金（同区域同房型挂牌价），不是礼貌。还价模板："同区同户型现在挂牌 RM1,600–1,700，续约我按 RM1,600 续两年。"

### 10. 非法驱逐：房东不能做的事及唯一合法通道

Evidence-backed：Specific Relief Act 1950 s.7(2) 要求即便租期已到，房东也须走法院程序收屋。房东**不能**（f-tenant-rights.md）：换锁/挂锁大门、断水断电断网施压、反复不请自入骚扰或威胁。合法驱逐的唯一通道：书面违约通知 → 给足约定通知期（通常 1–2 个月）补救或搬迁 → 房东向法院提起占有之诉 → 法院命令由法院指派的官员执行，房东方不得亲自清屋。租客侧遇到 lockout：Practice heuristic 是立即拍照录像（锁、门、时间）、 WhatsApp 全套记录，不作肢体对抗，直接书面要求恢复通行并提及 s.7(2) 与 counterclaim；房东侧则必须绝对忌讳"今晚搬走他行李"——尽职调查成本远低于非法清屋引发的 damages 反诉。

### 11. 书面 vs 口头：把一切拉回 WhatsApp 纸面

Practice heuristic：本场景沟通的一条主规则——**口头共识一律落回书面**。三个动作：每次电话后跟发一条总结（"确认刚才通话：你方同意 X，期限 Y"）；任何"口头答应"当场追问一句"麻烦发个 WhatsApp 确认下"；(3) 每月一封轻量记录（水表读数、任何维修承诺）。WhatsApp 截图在马来西亚小额程序中是标准证据形态：导出全部聊天记录别只截对自己有利的段落，法院看的是连续性。Evidence-backed 支撑：superhomes 明示 cases with strong documentation resolve faster and more favourably（f-tenant-rights.md）。

### 12. 房东侧：催租、拒租与留证

Practice heuristic（房东侧镜像）：催租第一步不是涨嗓门而是"礼貌 + 明确期限 + 留痕"——从转账备注催到 WhatsApp 到 formal notice，每一步都提前说下一步。房东侧同理必需的书面习惯：每次看房、每次维修安排、每次费用分摊都用 WhatsApp 图片确认；契约条款里的 early-termination penalty 与 notice period 在签约时就当面解释一遍——签约时省的解释时间，日后会加倍在扯皮里还回来。Practice heuristic：拒收"经理不在"式拖延的方法与 sc9 相同：给截止日，预告下一步（小额程序 Form 198），然后停止任何分期承诺式的口头协调。

## Sources

1. Malaysian Bar — LAW & REALTY: Tenancy Agreement（律师公会portal文章，practice notes，tier 1–2）：https://www.malaysianbar.org.my/conveyancing_practice/law_realty_tenancy_agreement.html
2. TTPM/KPDN — Bidang Kuasa Tribunal（官方，tier 1）：https://ttpm.kpdn.gov.my/Bidang_Kuasa_Tribunal.html
3. Superhomes — Tenant Rights Malaysia 2026: Deposit, Entry & Moving Out（马来西亚法律引证指南，tier 2）：https://www.superhomes.my/resources/tenant-rights-malaysia
4. Speedhome — Wear and Tear vs Damage Malaysia: What's Deductible（tier 2–3，媒体指南）：https://speedhome.com/blog/wear-and-tear-malaysia-landlord-guide/
5. PropCashFlow — Rental Deposit Refund Malaysia: Not Returned?（tier 2–3，媒体指南）：https://propcashflow.my/blog/rental-deposit-refund-malaysia-law/
