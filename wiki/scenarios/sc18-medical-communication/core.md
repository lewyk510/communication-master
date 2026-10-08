---
id: sc18-medical-communication
title: Medical Communication · 就医沟通
type: scenario
lang: core
tags:
  - doctor-patient
  - shared-decision-making
  - pain-description
  - second-opinion
  - breaking-bad-news
  - caregiver
  - interpreter
  - medication-questions
  - malaysia
scenarios:
  - S1
  - S2
sources:
  - raw/sc18-medical-communication/f-ahrq-20tips.md
  - raw/sc18-medical-communication/f-patients-assoc-4q.md
  - raw/sc18-medical-communication/f-spikes-mdanderson.md
  - raw/sc18-medical-communication/f-healthify-pain.md
  - raw/sc18-medical-communication/f-nia-caregiver.md
  - raw/sc18-medical-communication/f-moh-klinik.md
  - raw/sc18-medical-communication/f-msd-second-opinion.md
  - raw/sc18-medical-communication/search-ask-doctor.json
  - raw/sc18-medical-communication/search-malaysia-hospital.json
related:
  - "[[scenarios/sc4-hard-conversations/core]]"
  - "[[scenarios/sc12-asking-help/core]]"
  - "[[scenarios/sc9-live-service/core]]"
  - "[[concepts/c3-nvc-conflict-repair/core]]"
  - "[[concepts/c4-emotional-intelligence/core]]"
  - "[[cultures/cu1-malaysia-malay/core]]"
  - "[[cultures/cu2-malaysia-chinese/core]]"
created: 2026-10-07
updated: 2026-10-07
---

# 就医沟通（Medical Communication）

本页是本主题的基准参考（zh-first，术语保留英文）。核心问题：**在信息严重不对称、时间被压缩、双方都紧张的诊室里，患者（及家属）如何把症状说清楚、把该问的问出来、把医嘱听明白、并把决定权拿回自己手里**。覆盖：症状陈述结构、疼痛描述、四问决策框架（benefits / risks / alternatives / do nothing）、检查与药物的目的性提问、费用与替代方案、second opinion 第二意见、陪诊与翻译（老人照护）、坏消息告知与接收（SPIKES）、teach-back 复述确认、马来西亚就医体系导航（klinik kesihatan / 私人 GP / hospital kerajaan / hospital swasta）、药房沟通与药物标签。

**边界声明（必读）**：本主题是**沟通指南，不是医学建议**。KB 不提供任何诊断、治疗方案或用药判断——"该不该做某个检查、吃哪种药"属于医生与你的临床决定。本页教的是**对话的形状**：如何问、如何描述、如何确认、如何求助。所有具体医疗问题请交给注册医师与药剂师。

### 本题机制：信息不对称下的高压对话

就医对话与 [[scenarios/sc8-job-interviews/core]] 恰好互为镜像：面试里你是被评分的人，诊室里双方互为评分者——你在评估医生，医生在根据你说的话做推断。它的三个结构性难点（`Practice heuristic`，综合本页来源）：

1. **信息不对称**：医学术语是医生的母语，不是你的。AHRQ（美国医疗研究与质量局，tier 1）明确指出："errors also happen when doctors and patients have problems communicating"（沟通出问题本身就是医疗差错的来源之一），并把"参与每一项医疗决定"列为患者自保的第一原则——"Research shows that patients who are more involved with their care tend to get better results"（越参与的患者结果越好）。Evidence-backed，见 [ahrq-20tips]。
2. **时间压缩**：诊室平均几分钟到十几分钟，最贵的资源是提问机会——问不出的问题等于没问。这要求**就诊前把问题写好**，进场照单执行（下文症状陈述与问题清单）。
3. **状态不利**：疼痛、焦虑、替家人担心的人恰恰是最不擅长组织语言的人。对策不是"临场发挥好一点"，而是**把语言工作前置到诊室外**完成。

一个值得记住的量级证据：AHRQ 引用的数据是 "One in seven Medicare patients in hospitals experience a medical error"（住院的 Medicare 患者中约七分之一经历过医疗差错）。Evidence-backed，见 [ahrq-20tips]。沟通不是客套，是患者侧唯一能主动控制的差错防线。

### 就诊前 10 分钟：症状陈述的压缩包

`Practice heuristic`（框架综合 [healthify-pain] 医方提问清单，倒推患者侧结构）：医生问诊有自己的固定问题序列——"多久了？多严重？什么让它变好变坏？"（Healthify NZ 捕获的三连问）。你的对策是**把答案提前写成三句话开场白**：

1. **主诉一句**：部位 + 性质 + 起病时间。"左膝内侧疼了三周，上下楼梯加重。"
2. **变化曲线一句**：更好/更坏/波动的诱因。"冰敷会缓解，久坐后起身最痛。"
3. **已做处理与背景一句**：吃过什么药、有什么旧病、对什么过敏。"自己吃过 paracetamol，效果一般；有高血压病史。"

Pitfalls：从"三个月前那次感冒"开始讲编年史（医生要的是当下主诉的时间线，不是病史回顾）；用网络自诊断结论开场（"我是不是得了 X 病"——把假设当主诉会同时误导叙述和拉低信任，见下文 Dr Google 条目）；痛点分散（一次列八个症状会稀释真正的重点，先说最影响生活的那一个）。

`constructed example`：同一位患者的两种开场——"医生，我浑身都不舒服，睡不好吃不好"（医生需要五分钟追问才能定位）vs "左膝内侧疼三周，上楼加重、冰敷缓解，走路打软腿"（两句完成定位，省下的时间可以用来问问题）。

### 疼痛怎么说：量表 + 性质词 + 功能影响

疼痛是主观的，医生只能通过你的语言校准它。Healthify NZ（新西兰卫生体系患者门户）给出的医方工具正好是患者侧的**描述词库**：医生会问 "How long have you had your pain? How bad is it? What makes your pain feel better or worse?"（疼多久了、多严重、什么让它更好更坏）；描述性质时可用 dull ache（钝痛）、burning（灼烧感）、sharp（锐痛）、throbbing（搏动性痛）、pins and needles（针刺/麻刺感）；强度用 0–10 量表，0 = 无痛、10 = 最痛、5 左右 = 中度，且建议分别在"最好的一天 / 最坏的一天 / 平均一天"打分，让医生看到波动。Evidence-backed（对捕获内容的转述），见 [healthify-pain]。

`Practice heuristic` 的补充件：**数字之外补一句功能影响**——"疼到爬不了楼梯 / 半夜疼醒两次 / 吃止痛药也没用"比单报数字传递的信息多得多。比喻是有用的压缩（"像针扎""像抽筋""像火烧"），但比喻后面跟上性质词和量表分，才构成可校准的描述。极度脸盲或儿童可用 faces pain scale 表情量表（Healthify 捕获提及 IASP 的 Faces Pain Scale – Revised）。

### 四问框架：把共享决策装进口袋

英国 Patients Association 的 shared decision-making 页面给出了最简洁的患者侧决策工具——**四个问题**：What are the benefits of each treatment?（每个治疗的好处是什么）risks 是什么？有哪些 alternatives（替代方案）？"如果我什么都不做"会怎样（do nothing 也是选项）？Evidence-backed（对四问的转述），见 [patients-assoc-4q]。NHS England 的 shared decision-making 资料也推广同一思路的 "Ask 3 Questions"（我的选项是什么？各选项的利弊？如何获得帮助做决定）。Evidence-backed（对搜索捕获摘要的转述），见 [search-ask-doctor]。

`Practice heuristic` 的落地顺序：先问选项（保证不是单方案推销），再问利弊（把风险问成具体频率——"发生率大概多少？"），然后问替代（含保守观察），最后问什么都不做的后果（很多小病自愈、很多手术不急，这问能立刻暴露"过度医疗"或"没问题"）。四个问题在任何诊室都合法，且会把对话从"服从模式"切换到"合作模式"。

### 检查与药物的目的性提问清单

AHRQ 20 Tips 里对药物那段是全页最可直接照抄的部分——它列出的药物五问原话：*What is the medicine for? How am I supposed to take it and for how long? What side effects are likely? What do I do if they occur? Is this medicine safe to take with other medicines or dietary supplements I am taking?*（这药治什么；怎么吃吃多久；可能有什么副作用、出现了怎么办；与我在吃的其他药/保健品是否冲突）。还有两条常被忽略的：标签看不懂要问（"four times daily" 是 24 小时不停每 6 小时一次，还是醒着时每 6 小时一次——AHRQ 给的原例）；取药时问一句 "Is this the medicine that my doctor prescribed?"（这是医生开的那支吗）。Evidence-backed，见 [ahrq-20tips]。

`Practice heuristic` 把它扩展成中文诊室/药房的对应清单：

- "这个检查/药的**目的是什么**？如果我不做/不吃，会怎样？"
- "**有没有更便宜的替代**？"（generic 学名药 vs 原厂药，在马来西亚 klinik kerajaan 与药房都值得问；具体换药决定仍需医生/药剂师做）
- "吃了之后**正常反应和不正常反应**分别是什么样？出现哪种情况要打电话回来？"
- "跟我现在吃的 **X 药或保健品**冲突吗？"（同时看多名医生、中药西药混吃的高危动作，AHRQ 的 "brown bagging" 建议：把所有正在吃的药装一袋带去给医生看。Evidence-backed，见 [ahrq-20tips]。）
- AHRQ 还有一条给自己留底的："Ask for written information about the side effects"——要书面副作用说明。Evidence-backed，见 [ahrq-20tips]。

### 费用与替代方案：把钱的问题问出口

钱是最难开口的问题，但它是医疗决策的真实变量。AHRQ 的框架支持直接问："Is there a generic version?"（有没有学名药版本）属于 alternatives 四问的子集。`Practice heuristic` 的马来西亚版话术：

- 在 klinik/hospital swasta：**"Boleh saya tahu anggaran kos sebelum rawatan?"（治疗前的费用预估）**"Ada penalti kalau guna panel TPA/insurans tak cover？"——先问预估再同意治疗，尤其是手术、住院、影像检查这类大项。
- 医生同时开检查时："这几项检查**哪些现在必须做，哪些可以先观察**？"——这不是拒绝治疗，是 alternatives 四问的本地化。
- 私人保险/公司 panel 用户：确认诊所是否 panel、是否需要 guarantee letter，避免付现金后再报销的纠纷。`Practice heuristic`。

社区流传的对比（医院 kerajaan 账单低廉 vs swasta 账单从几十到上万马币）来自社交媒体经验帖，anecdotal（tier 3），见 [search-malaysia-hospital]——作为背景感知可以，作为具体费用依据不行，费用请当场问。

### Second opinion 第二意见：怎么开口不得罪人

MSD Manual（默沙东家庭版手册）把逻辑说得很平：**医生之间的意见分歧本来就存在**（证据不明确时尤其如此），第二意见若相同则安心，若不同则获得更知情的选择；还可以有第三意见。操作要点：可以请现任医生推荐（多数医生欢迎）；第二医生**不要选现任医生的近亲同行**（视角会重合）；就诊前把病历与检查结果送过去，避免重复检查；把问题写下来带去；条件允许时当面看诊而非纯远程。Evidence-backed（对捕获内容的转述），见 [msd-second-opinion]。

AMA（美国医学会）的说法更抚慰人：鼓励患者寻求第二意见的医生展示的是自信与对患者的尊重。Evidence-backed（对搜索摘要的转述），见 [search-second-opinion]。

`Practice heuristic` 的话术层（中文）："我想再听一个意见再决定，**可以请您帮我写转介信/把报告给我一份吗**？"——把请求落在"帮我做足准备"上而不是"我不信任你"上。英文版："I'd like to get another opinion before deciding — could you help me with a referral and copies of my results?" 马来西亚语境下向 hospital kerajaan 专科请求转介（rujukan）是常规流程的一部分，把"要第二意见"说成"请帮我 rujuk"完全正常。`Practice heuristic`。

### 陪诊与翻译：替父母看医生的角色管理

美国国家老龄研究所 NIA（NIH 旗下，tier 1）的照护者指南给出了陪诊的角色纪律，逐条可迁移：

- **先解决授权**：想让医生之后能跟你谈家人的病情，需要本人同意/书面授权（美国是 HIPAA 授权表；马来西亚多数机构有自己的同意流程，`Practice heuristic`：首次就诊时就当面请老人向医生口头同意"可以跟我儿子/女儿讲我的情况"）。
- **带齐物件**：保险卡、其他医生的联系方式、**全部在吃药物的清单（名字、剂量、时间表，含维生素/草药/OTC）**、眼镜和助听器。Evidence-backed，见 [nia-caregiver]。
- **问题按重要性排序写下来，当面递给医生，边听边记**——笔记是给老人和其他家人看的。Evidence-backed，见 [nia-caregiver]。
- **让老人自己回答医生的问题**，除非被问到你。"别把就诊变成你与医生的双人对话，始终把被照护者包括在内。" Evidence-backed，见 [nia-caregiver]。
- 离开前**要书面材料**，问清复诊安排。Evidence-backed，见 [nia-caregiver]。

`Practice heuristic` 的马来西亚增补件：老一辈华人可能只讲方言（福建/广东/客家），公共系统里 BM 是通用工作语言——**提前安排一个会方言的家属陪诊，或在候诊时就开口请护士协助**（"我的母亲只会讲广东话，可以麻烦你们帮我翻译吗？"）；英文与 BM 的关键医嘱词（dos 剂量 / kesan sampingan 副作用 / selepas makan 饭后）值得提前教会老人辨认药袋标签。就诊后当晚把笔记用方言复述给老人听一遍，是效率最高的依从动作。

### 坏消息的告知与接收：SPIKES 六步

Baile、Buckman 等人 2000 年发表于 *The Oncologist* 的 SPIKES 协议是坏消息沟通的事实标准（MD Anderson 癌症中心官方存档 PDF，tier 1）。六步：**S**etting up（安排私密场合、请家属在场、坐下）→ **P**erception（"before you tell, ask"——先问患者已知什么，"What is your understanding of the reasons we did the MRI?"）→ **I**nvitation（确认患者想知道多少）→ **K**nowledge（分小段、避免行话、先给预告句）→ **E**mpathy（识别情绪并回应）→ **S**trategy and Summary（共同定下一步计划）。Evidence-backed，见 [spikes-mdanderson]。

患者侧与家属侧同样可以从协议里取货（`Practice heuristic`）：

1. **要求场地**："我们可以找个房间慢慢谈吗？我想叫上我太太一起。"——Setting 不是医生的专属动作，你有权要求它。
2. **校准认知**：听完结论先复述——"我听到的意思是 X，对吗？"对应协议里"check understanding"，论文明说这能防止"患者高估疗效或误解治疗目的"的已知倾向（documented tendency）。Evidence-backed，见 [spikes-mdanderson]。
3. **控制信息流**："请一步一步讲，我先听完这一步。"协议原文支持"provide information in small increments"。
4. **问下一步而不是问为什么是我**：Strategy 步骤的核心是"有明确下一步计划的患者更不容易焦虑"（论文原话：patients who have a clear plan for the future are less likely to feel anxious and uncertain）。Evidence-backed，见 [spikes-mdanderson]。

配套数据：ASCO 调查里 52% 的肿瘤医生认为协议中最难的是共情回应（E 步）——**连职业选手都难的部分，不要指望一次对话完美**；99% 的受训者认为 SPIKES 实用。Evidence-backed，见 [spikes-mdanderson]。

### 听懂医嘱：复述确认（teach-back 思路）

AHRQ 对出院场景的要求是患者主动的："ask your doctor to explain the treatment plan you will follow at home"——新药怎么吃、复诊怎么约、何时恢复日常、之前的药要不要继续吃，"getting clear instructions may help prevent an unexpected return trip to the hospital"（拿到清晰说明可以避免二次入院）。Evidence-backed，见 [ahrq-20tips]。SPIKES 论文同样强调医生应 "check to see if information was correctly received"。Evidence-backed，见 [spikes-mdanderson]。

`Practice heuristic` 的患者侧动作是**把确认责任拿回自己**：与其说"明白了"（诊室里 90% 的"明白了"事后被证明是礼貌），不如说——"我怕记错，**我复述一遍，您看对不对**：这个药早晚各一次、饭后吃，吃两周后回来验血。"复述把单向告知变成双向校验，且给了医生一个低成本纠错的机会。对老人陪诊场景，复述 + 当场写进手机备忘录 + 当晚方言复述，三件套几乎消灭"回家就忘"。

### 马来西亚就医体系导航：从 klinik kesihatan 到 hospital rujukan

马来西亚卫生部长透露的 KKM 系统数据：全国 151 所 KKM 医院按服务类型分级，Jenis 1/2 为有专科的转诊中心（anecdotal 摘自部长社媒帖，见 [search-malaysia-hospital]）。更权威的患者侧信息来自卫生部 BPKK 官方页：**Klinik Kesihatan 按日均就诊量分为 KK1–KK7 七类**（KK1 为日均 >800 人次的大型诊所），大型类型提供 OPD 门诊、A&E 小急诊、母婴保健 MCH、牙科、康复、X-Ray、Lab 化验与 Farmasi 药房服务。Evidence-backed，见 [moh-klinik]。

`Practice heuristic` 的患者侧路径图（沟通视角，非医疗建议）：

1. **小病初诊**：klinik kesihatan（政府诊所，便宜、人多、BM 环境）或私人 GP klinik（快、可挑时段、语言选择多）。两条路都合法，初次沟通时说清"我有保险/我用政府诊所"不影响医嘱质量。
2. **需要专科/影像/住院**：私人 GP 可写 referral letter（转介信）；进公立体系则经 klinik kesihatan → hospital daerah → hospital pakar 的 rujukan 链条。**转介信是沟通资产**——离开前确认信里写了主诉、已做处理与转诊原因，拿着它去下一站少讲一半话。
3. **急诊**：直接 hospital 急诊科，不用转介；沟通重点是**一句话主诉 + 时间线**（"胸口痛两小时"）——急诊的分诊护士（triage）按主诉定优先级，压缩包式开场在这里最救命。`Practice heuristic`。

私人 vs 公立的常见取舍（等待时间、费用、连续性）来自社区讨论，anecdotal，见 [search-malaysia-hospital]；本页不评判孰优，只提醒：**换体系时把病历/报告带齐**（MSD 对第二意见的要求同样适用于换医院），Evidence-backed 见 [msd-second-opinion]。

### 药房沟通与药物标签

药房是马来西亚就医闭环里被低估的沟通点（klinik kesihatan 内设 farmasi，社区药房则无处不在）。AHRQ 的药房条目已在上文清单：核对取到的是不是处方药、液体药用专用量具（家用茶匙不可靠）、要书面副作用说明、标签疑问当场问。Evidence-backed，见 [ahrq-20tips]。

`Practice heuristic` 的本地动作：拿到药后当场**对着药袋标签读一遍用法**（KKM 药袋常为 BM：sehari sekali 每天一次 / selepas makan 饭后 / sebelum tidur 睡前），有不认识的缩写直接问药剂师；同时吃多种药时请药剂师做一次用药核对（medicine review）。副作用上报体系：马来西亚国家药品监管局 NPRA 接受消费者直接上报药物不良反应（Evidence-backed：对 NPRA 页面搜索摘要的转述，见 [search-myhealth-ubat]）——"报告副作用"本身也是一种医患沟通，只是对象换成了监管体系。

### 语言、称呼与 Dr Google

`Practice heuristic`（马来西亚三语诊室的现实）：BM 是公立系统默认工作语言，私人体系 English 通用，华人聚居区常可遇中文服务。三条实用规则：

1. **跟医生的语言走，技术词全保留**：医生用 BM 开场就用 BM 回，中途切 English 跟着切；药名、器官名用原文，别硬翻译（"blood pressure" 别说成"血压力"）。
2. **称呼**："Doctor" 是诊室里安全通用的称呼（马来语环境同样叫 Doktor）；对护士/职员用 "Puan/Encik" 或 "sister"（护士的本地惯称）。礼貌开场一句 "谢谢医生麻烦您了" / "Terima kasih, doktor" 成本为零、收益为正。
3. **Dr Google 条目**：查资料不是问题，**拿查询结果当主诉**才是问题。上传用法：把网络信息降级为问题——"我在网上看到 X，这个适用于我的情况吗？"（替代：先讲自己的症状，把"我怀疑是 X"放在最后且明确标注是猜测）。SPIKES 的 Perception 步骤证明了好医生本来就会先问"你已知什么/你怎么理解"——你主动供上认知状态，正好接住这一步。`Practice heuristic`。

### 危险信号与复诊指令：把模糊变明确

`Practice heuristic`（收尾两条必问，任何场景通用）：

1. **"出现什么情况必须马上回来/去急诊？"**——把医生脑子里的红线说出口。这句话把"按时吃药、有情况复诊"这类模板句逼成具体清单（"发烧超过三天""伤口渗液发红""体重一周掉两公斤"）。AHRQ 的出院沟通建议（新药、复诊时间、恢复日常、旧药去留）正是同一清单的住院版。Evidence-backed（对清单内容的转述），见 [ahrq-20tips]。
2. **"我什么时候需要回来复诊？查的结果谁通知我？"**——检验报告的"没消息"不等于"好消息"：AHRQ 明确建议 "If you have a test, don't assume that no news is good news"（做了检查别默认没消息就是好消息），主动要结果与解读。Evidence-backed，见 [ahrq-20tips]。

把这两问写进每次就诊的最后两分钟，配合复述三件套，就医沟通的闭环就完成了：**症状说清 → 选项问全 → 医嘱复述 → 红线明确 → 结果追到**。

## Sources

- [AHRQ: 20 Tips To Help Prevent Medical Errors (Patient Fact Sheet)](https://www.ahrq.gov/questions/resources/20-tips.html) — tier 1（美国政府机构）
- [Baile, Buckman, Lenzi et al. (2000): SPIKES—A Six-Step Protocol for Delivering Bad News, The Oncologist（MD Anderson 官方存档 PDF）](https://www.mdanderson.org/documents/education-training/project-echo/10%2027%2016%20ECHO-PACA%20SPIKES.pdf) — tier 1（学术期刊论文官方存档）
- [NIA/NIH: Taking Someone to a Doctor's Appointment: Tips for Caregivers](https://www.nia.nih.gov/health/medical-care-and-appointments/taking-someone-doctors-appointment-tips-caregivers) — tier 1（美国国立卫生研究院下属研究所）
- [KKM/Ministry of Health Malaysia BPKK: Klasifikasi Klinik Kesihatan](https://hq.moh.gov.my/bpkk/index.php/klasifikasi-klinik-kesihatan) — tier 1（马来西亚卫生部官方）
- [Healthify NZ: Pain – describing your pain](https://healthify.nz/health-a-z/p/pain-describing-your-pain) — tier 1（新西兰卫生体系支持的患者信息门户）
- [MSD Manuals (Consumer Version): Getting a Second Opinion](https://www.msdmanuals.com/home/special-subjects/making-the-most-of-health-care/getting-a-second-opinion) — tier 2（既有医学参考出版物消费者版）
- [Patients Association (UK): Shared decision-making](https://www.patients-association.org.uk/shared-decision-making) — tier 2（全国性患者组织）
- [NHS England: Personalised Care — Shared Decision Making Summary Guide (PDF)](https://www.england.nhs.uk/wp-content/uploads/2019/01/shared-decision-making-summary-guide-v1.pdf) — tier 1（官方，经搜索捕获转述）
- [AMA: Second opinions are a good idea—but there are caveats](https://www.ama-assn.org/public-health/prevention-wellness/second-opinions-are-good-idea-there-are-caveats) — tier 2（经搜索捕获转述）
- [NPRA Malaysia: Pelaporan Kesan Sampingan Ubat oleh Pengguna](https://www.npra.gov.my/index.php/en/component/content/article/2-english/uncategorised/675-reporting-consumer.html?Itemid=1391) — tier 1（官方，经搜索捕获转述）
- [Serper 搜索捕获：马来西亚医院/诊所对比（社区帖，anecdotal）](https://www.lemon8-app.com/@mulawithmai/7268180965980209666?region=my) — tier 3（anecdotal）
