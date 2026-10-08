---
id: sc18-medical-communication
title: Medical Communication · 就医沟通
type: scenario
lang: zh
tags:
  - doctor-patient
  - symptoms
  - pain-description
  - medication-questions
  - second-opinion
  - caregiver
  - interpreter
  - malaysia
scenarios:
  - S1
  - S2
sources:
  - raw/sc18-medical-communication/f-ahrq-20tips.md
  - raw/sc18-medical-communication/f-healthify-pain.md
  - raw/sc18-medical-communication/f-nia-caregiver.md
  - raw/sc18-medical-communication/f-spikes-mdanderson.md
related:
  - "[[scenarios/sc18-medical-communication/core]]"
  - "[[scenarios/sc3-family-kinship/core]]"
created: 2026-10-07
updated: 2026-10-07
---

LANE — authored natively, NOT a translation

# 就医沟通 · 中文信号手册

从中文患者的诊室处境出发：三分钟门诊、带父母看医生、中马两边的公立与私人系统、方言翻译。每条独立成篇，不与 en/ms lane 互译。**本页是沟通指南，不构成任何诊断或用药建议。**

### 「哪里不舒服？」——三句话开场白

**Context** — 任何诊室的第一问，公立私人通用。看似随口，其实决定了这场问诊的检索方向。

**Reading**
1. 医生在等一个**可定位的主诉**：部位 + 性质 + 时间。
2. 你答得越压缩，医生追问越少，剩下的时间全归你的问题。
3. 开场散漫（"就是整个人不太舒服"）会把问诊变成大海捞针。

**Response options**
1. 主诉一句：「左膝内侧疼了三周，上下楼加重。」
2. 曲线一句：「冰敷能缓解，久坐后起身最痛。」
3. 背景一句：「自己吃过止痛药效果一般；有高血压史，对青霉素过敏。」

**Pitfalls** — 从三个月前讲起编年史；一口气报八个症状稀释重点；用网络自诊断开场（「我是不是得了绝症」）。

**Examples** — `constructed example`：患者开口「胸口闷了两天，爬楼梯时出现，休息几分钟就好；我爸六十岁做过支架」，医生当场说「讲得很清楚」，直接进入检查安排。

### 疼痛的中文词库：别只会说「疼」

**Context** — 被问「怎么个疼法」时的大面积卡壳点。中文疼痛词汇其实非常丰富，用对词能省三轮追问。

**Reading**
1. 医生在用你的描述缩小范围：刺痛/钝痛/绞痛/灼痛指向完全不同的可能性（怎么处理是医生的事，**你只负责把感觉翻译准**）。
2. 「很痛」「超级痛」是零信息词；比喻（像针扎、像抽筋）是高压缩词。
3. 数字量表 0–10 是通用货币：0 不痛、10 最痛、5 中度。

**Response options**
1. 性质词 + 量表：「刺痛，大概 6 分；最痛的时候 8 分。」
2. 诱因与波动：「晚上睡觉翻身最痛，走路反而不太痛。」（Healthify 捕获的医方三问正是：多久、多严重、什么让它变好变坏——Evidence-backed，见 [healthify-pain]。）
3. 功能影响补一句：「疼到爬不了楼梯、半夜疼醒两次。」——比数字更能传达严重度。

**Pitfalls** — 忍痛文化（「还能忍」）让医生低估严重度；夸大到 10 分导致后续校准失灵；只报数字不报场景。

**Examples** — `constructed example`：「像有根筋在拧，一阵一阵的，绞着痛，5 到 6 分，吃完饭更明显。」——一句话完成性质、节律、强度、诱因四个维度。

### 「这个检查/药的目的是什么？」

**Context** — 医生开单、开药时的标准时刻。多数人点头接过就走，这是诊室里信息密度最高的免费提问窗口。

**Reading**
1. 合法且被鼓励的问题：AHRQ 患者指南把"参与每项决定"列为第一原则（Evidence-backed，见 [ahrq-20tips]）。
2. 这问会逼出两个关键信息：检查是为了确诊还是排除；药是治症状还是治根。
3. 医生的回答长度也是信号——一句说不清目的的项目，值得再问一遍。

**Response options**
1. 直接问：「这个检查是想查什么？如果我不做，会有什么后果？」
2. 拆组合单：「这几项里，哪些现在必须做、哪些可以先观察？」
3. 关联到下一步：「查出来之后，治疗方案会有哪几种可能？」

**Pitfalls** — 怕显得「质疑医生」而全盘沉默（好的医生欢迎这问）；问了但不听答案；拿网上文章当反问依据（见 Dr Google 条）。

**Examples** — `constructed example`：「医生，这个 CT 是想排除什么？」——「主要怕肺里那个结节有变化。」——「那先观察三个月复查跟现在直接做，各有什么利弊？」医生坐下来认真讲了五分钟。

### 「有没有更便宜的替代？」

**Context** — 开药与结账环节。钱的话题最难开口，但原厂药与学名药、检查的先后顺序，都是真实决策变量。

**Reading**
1. 这问完全合规：alternatives 四问的子集（好处/风险/替代/不做——Patients Association 框架，Evidence-backed，见 [patients-assoc-4q]）。
2. 医生可能真不知道你的预算压力——不说，没人替你省。
3. 回答若是「这个不能换」，理由本身就是有用信息。

**Response options**
1. 药：「有学名药（generic）版本吗？效果差多少？」
2. 检查与治疗：「如果预算有限，您会先做哪一项？」
3. 系统：「这个在政府诊所/药房是不是也有？我两边都能配合。」

**Pitfalls** — 把省钱说成对医生能力的质疑（「你是不是想赚我钱」直接烧桥）；自己停药换药省钱（这是治疗决定，只能医生做）；只在结账时才发现价格（大项治疗前先问预估）。

**Examples** — `constructed example`：「医生，我在长期吃这个药，预算有点紧——有更便宜的等效药吗？」医生换了学名药并补了一句「效果一样的，别担心」，一个月省下两百多马币。

### 药袋上的字：用法五问

**Context** — 诊室开药后、药房取药时。马来西亚药袋多为 BM（sehari sekali / selepas makan / sebelum tidur），中文患者常半懂不懂地拿走。

**Reading**
1. AHRQ 原话把标签疑问列为正式提问项："If you have any questions about the directions on your medicine labels, ask"——连 "four times daily" 是不是半夜也要吃药都值得问（Evidence-backed，见 [ahrq-20tips]）。
2. 半懂的操作是最危险的操作：吃错时间、漏吃、加倍补吃。
3. 药房药剂师是免费的第二层把关，很多问题问药师比等下次复诊快得多。

**Response options**
1. 当场对着药袋读一遍：「这个是早晚各一次、饭后吃、吃两周——对吗？」
2. 问冲突：「我在吃 X 药和保健品，跟这个一起吃可以吗？」（AHRQ 的 brown bagging：把所有药装袋带给医生看——Evidence-backed，见 [ahrq-20tips]。）
3. 要书面：「有没有副作用说明单？出现什么情况要马上停药联系你们？」（「停药」的决定也请回到医生/药师，你先问清楚流程。）

**Pitfalls** — 拿错家人的药袋；把「症状好了就自己停」当成默认（抗生素类尤其危险，但决定权在医嘱，你只负责问清楚「吃完了是不是要回来」）；液体药用家用茶匙量。

**Examples** — `constructed example`：患者取药时问「这个capsule是一天一次还是两次？」药师发现医生手写剂量被误读，当场更正——一次 30 秒的提问避免了一周的错误剂量。

### 「我复述一遍，您看对不对？」

**Context** — 医嘱交代完毕、起身要走前的最后 60 秒。中文诊室最缺的动作：没人复述，人人说「好」。

**Reading**
1. 「明白了吗？」「好」是礼貌不是理解——诊室里九成的「好」回家就忘。
2. 复述把单向告知变双向校验，医生纠错成本极低（点一下头或补一句）。
3. 对陪老人就诊的家庭，这一句是代沟滤网：老人点头≠懂了，复述才算。

**Response options**
1. 药嘱复述：「这个药早晚一次饭后吃，两周后回来验血——对吗？」
2. 方案复述：「所以我接下来是先吃这个观察两周，没好转再做检查？」
3. 复诊锚点：「我什么时候要回来？结果是谁通知我？」（AHRQ：做了检查别默认没消息就是好消息——Evidence-backed，见 [ahrq-20tips]。）

**Pitfalls** — 复述太长变成反驳；只复述对自己有利的部分；复述后不记笔记（当场写进手机备忘录）。

**Examples** — `constructed example`：患者复述「早晚各一粒、饭后、吃完五天回来」，医生说「三粒改成早一粒晚两粒」，纸面写大数字——复述抓出了剂量歧义。

### 「出现什么情况必须马上回来？」

**Context** — 任何就诊的最后两分钟。医生脑中有红线清单，但不说你就拿不到。

**Reading**
1. 模板式叮嘱（「有情况再来」）等于零指令；这问把红线逼成具体条目。
2. 答案同时告诉你「什么情况不用慌」——反过来就是安心清单。
3. 这问在急诊、出院、术后场景价值最大。

**Response options**
1. 直接问：「出现什么症状时，我必须马上回来或去急诊？」
2. 量化边界：「发烧超过多少度、持续几天要回来？」
3. 出院版（AHRQ 建议的清单）：「出院后旧药还吃吗？什么时候复诊？什么时候能正常上班？」——Evidence-backed，见 [ahrq-20tips]。

**Pitfalls** — 问了不写下来（红线清单必须落纸/落手机）；把红线当成唯一标准（任何让你不安的变化都可以问，不用等到红线）；替老人看病时没把这问带回去。

**Examples** — `constructed example`：「如果伤口周围发红变大、渗液、或者发烧超过 38 度，当天就要回来。」患者第三天发现渗液，按红线当晚回院处理。

### 「我想再听一个意见」——第二意见开口法

**Context** - 大决定前（手术、长期用药、重要诊断）想多听一方意见，又怕得罪现任医生。

**Reading**
1. 医学上第二意见本来就正常：医生之间分歧存在， MSD 手册明说多数医生欢迎（Evidence-backed，见 [msd-second-opinion]）。
2. 对方反应紧张才是有用的信号，多数时候你会收获「好的，我帮你写转介」。
3. 把请求落在「帮我准备」上，落在流程而不是情绪上。

**Response options**
1. 「我想再听一个意见再做决定，可以请您帮我写转介信、给我一份报告吗？」
2. 政府系统版：「麻烦帮我 rujuk 去专科，我想确认一下方案。」
3. 委婉版：「这是个不小的决定，我想跟家人商量并再咨询一位专科，您看合理吗？」

**Pitfalls** — 隐瞒现任医生偷偷去问（两边信息不全会互相干扰）；第二医生选现任医生的老搭档（MSD：视角会重合——Evidence-backed，见 [msd-second-opinion]）；不带病历报告去，重做全套检查。

**Examples** — `constructed example`：「医生，手术我想再听多一个意见，报告能给我一份吗？」医生答「应该的，我把影像也刻给你」，转介信十分钟写好。

### 陪父母看病：谁说、谁问、谁记

**Context** - 替老人挂号陪诊的子女。最常见事故：全程变成「医生—我」的双人对话，老人被晾在旁边。

**Reading**
1. NIA 照护者指南原话：让老人自己回答医生的问题，别把就诊变成你与医生的双人谈——始终包括被照护者（Evidence-backed，见 [nia-caregiver]）。
2. 你的正确角色是三件套：**带清单（药单+问题单）、记笔记、事后复述**，不是抢答。
3. 老人当场说「没什么事啦」可能是怕花钱或怕麻烦子女——提前单独问一次「你最想跟医生讲什么」。

**Response options**
1. 开场交接：「医生，我妈有三个问题想问，她自己讲，我补充。」
2. 记笔记并举手：「我可以确认一下吗——刚才说的药，跟她的血压药冲突吗？」
3. 离开前要书面材料与复诊时间（NIA 建议动作——Evidence-backed，见 [nia-caregiver]）。

**Pitfalls** — 替老人回答「她就是有点累」（轻描淡写是老人最常见的防御，你的转述会放大它）；把老人的药单靠记忆报（剂量写下来或带药袋）；当晚不复述给老人听。

**Examples** — `constructed example`：儿子把写好的问题单递给医生：「她眼神不好，问题我念给她听，她自己选先问哪个。」医生看完笑说「这是今天我收到的最好清单」。

### 「我妈只会讲广东话」——方言与翻译求助

**Context** - 公立 klinik/hospital 以 BM 为工作语言，老一辈华人只讲方言；沟通断裂时 medication 与医嘱最容易丢。

**Reading**
1. 这是常规请求不是特殊请求：医护人员每天处理多语言患者，开口就有人接。
2. 断裂点常在细节：dos（剂量）、kesan sampingan（副作用）、复诊时间——恰好是最不能错的部分。
3. 子女临时翻译是可以的，但医学术语上仍应向医护确认（你翻错没人纠）。

**Response options**
1. 候诊时就开口：「我的母亲只会讲广东话，可以麻烦你们帮忙翻译或安排会方言的同事吗？」
2. 关键词双检：「用广东话跟她讲一次，我用中文确认一遍，可以吗？」
3. 教标签：把药袋上的 BM 用法（selepas makan 等）用方言教老人认，标在药袋上。

**Pitfalls** - 假设老人「听得懂英文就够」；只在出问题时才翻译；让孙辈小孩当翻译（儿童承接不了剂量与病情信息）。

**Examples** - `constructed example`：女儿候诊时请护士协助，护士找来会广东话的工友；离开前女儿把「一日两次、饭后」用粤语再讲一遍给母亲听，母亲点头并自己复述成功。

### 听到坏消息时的四个问题

**Context** - 诊断告知、复查异常、病情变化。坏消息场景里人脑会宕机，SPIKES 协议的医生侧步骤反过来用就是患者侧的抓手（Evidence-backed，见 [spikes-mdanderson]）。

**Reading**
1. 协议要求医生「分小段、先确认你想知道多少」——你可以主动配合这场节奏。
2. 坏消息当场记住的细节通常不到一半：笔记与「我复述一遍」比勇气有用。
3. 有明确下一步的患者更不易焦虑（SPIKES 原话）——所以问题要指向「接下来」而不是「为什么」。

**Response options**
1. 节奏：「请一步一步讲，我记一下笔记。」
2. 校准：「我听到的意思是 X，对吗？」（对应协议的 check understanding——Evidence-backed，见 [spikes-mdanderson]。）
3. 下一步：「下一步的检查/方案有哪几种？我什么时候能拿到它们？」

**Pitfalls** - 当场做重大决定（除非紧急，大决定约定下次带着家人来谈）；把医生理解为冷血（52% 的肿瘤医生自认共情回应最难——Evidence-backed，见 [spikes-mdanderson]）；全程沉默回去后全家猜测。

**Examples** - `constructed example`：患者听完结论后说「我先复述一遍您听对不对，然后我们谈下一步」，医生放缓语速重新分段讲解，离开时患者手里有一张写好的下一步清单。

### 「医生，我在网上查了……」——Dr Google 的降级用法

**Context** - 诊室里最易翻车的开场。查资料本身没错，错的是把查询结果当主诉。

**Reading**
1. 医生听到「网上说我是 X」时，评估对象从症状变成了你的信息来源——双输。
2. SPIKES 的 Perception 步骤显示医生本来就要问「你怎么理解自己的情况」——你主动交认知，反而接得住（Evidence-backed，见 [spikes-mdanderson]）。
3. 网络资料的正确输出是一句问题，不是一段论证。

**Response options**
1. 症状先行：「我左腹疼三天……另外我在网上看到可能是阑尾的问题，这个方向对吗？」
2. 焦虑显性化：「我有点担心是不是严重的东西，所以才来。」
3. 来源降权：「我知道网上信息不准，所以想听您的判断。」

**Pitfalls** - 拿文章跟医生辩论；先说诊断再说症状（顺序反了问诊全乱）；用网络信息吓自己后把焦虑包装成愤怒。

**Examples** - `constructed example`：「我查到我的症状像 X 也像 Y，越查越怕——您帮我判断一下该往哪边看？」医生直接说「这样问很好，我来给你排序」。

## Sources

- [AHRQ: 20 Tips To Help Prevent Medical Errors](https://www.ahrq.gov/questions/resources/20-tips.html) — tier 1
- [Healthify NZ: Pain – describing your pain](https://healthify.nz/health-a-z/p/pain-describing-your-pain) — tier 1
- [NIA/NIH: Taking Someone to a Doctor's Appointment: Tips for Caregivers](https://www.nia.nih.gov/health/medical-care-and-appointments/taking-someone-doctors-appointment-tips-caregivers) — tier 1
- [Baile et al. (2000): SPIKES, The Oncologist（MD Anderson 官方存档 PDF）](https://www.mdanderson.org/documents/education-training/project-echo/10%2027%2016%20ECHO-PACA%20SPIKES.pdf) — tier 1
- [KKM BPKK: Klasifikasi Klinik Kesihatan](https://hq.moh.gov.my/bpkk/index.php/klasifikasi-klinik-kesihatan) — tier 1
- [MSD Manuals: Getting a Second Opinion](https://www.msdmanuals.com/home/special-subjects/making-the-most-of-health-care/getting-a-second-opinion) — tier 2
- [Patients Association (UK): Shared decision-making](https://www.patients-association.org.uk/shared-decision-making) — tier 2
