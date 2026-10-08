---
id: c10-models-meta
title: Models & Meta · 沟通模型与元方法
type: concept
lang: core
tags:
  - communication-models
  - trust
  - attachment
  - scarf
  - transactional-analysis
  - meta
scenarios:
  - S1
  - S2
  - S3
  - S4
sources:
  - raw/c10-models-meta/f-models-of-communication.md
  - raw/c10-models-meta/f-mayer-trust-1995.md
  - raw/c10-models-meta/f-scarf-rock-2008.md
  - raw/c10-models-meta/f-love-languages-book.md
  - raw/c10-models-meta/f-transactional-analysis-wiki.md
related:
  - "[[concepts/c1-subtext-implicature/core]]"
  - "[[concepts/c2-persuasion-influence/core]]"
  - "[[concepts/c3-nvc-conflict-repair/core]]"
  - "[[concepts/c4-emotional-intelligence/core]]"
  - "[[concepts/c5-personality-typology/core]]"
  - "[[concepts/c9-manipulation-defense/core]]"
  - "[[cultures/cu4-cross-cultural-general/core]]"
  - "[[cultures/cu5-codeswitching/core]]"
  - "[[playbooks/p4-ai-prompting/core]]"
created: 2026-10-07
updated: 2026-10-07
---

# Models & Meta · 沟通模型与元方法

本页是 c10 的基准参考（zh-first，术语保留英文）。它干两件事：一，把全 KB 反复用到但不专属于任何一个专题的**底层模型**（沟通模型、信任、依恋、冲突风格、SCARF、TA）集中钉牢，别的专题直接引用不再重复论证；二，写清本 KB 自身的**元方法**（router 怎么用、confidence 标签怎么读、什么时候该问而不是假设、influence 的伦理边界、认知谦逊）。所有命名模型与研究均可溯源到 `## Sources` 中列出的 raw 捕获或 URL；无法溯源的一律标 `Practice heuristic`。

### 沟通模型三代谱系：linear → interaction → transactional

沟通研究把主流模型分成三代。Evidence-backed，见 [models-of-communication] 捕获：最早是 **linear transmission models**（线性传输模型：Aristotle、Lasswell、Shannon–Weaver、Berlo），把沟通描述成"发送者把消息单向送达接收者"，没有反馈回路，发送者不知道消息是否到达；接着 **interaction models**（如 Schramm）加入反馈与场域；1970 年代起，**transactional models**（Barnlund 等）承认发送与回应是**同时进行的**，且**意义是在沟通过程中被创造的，不是先于过程存在的**。捕获原话：transaction 模型下 "meaning is created in the process of communication and does not exist prior to it"，沟通还反过来塑造关系、身份与共同体。

`Practice heuristic`：和一个"人"对话时默认起手 transactional 心智——对方在听的同时也在用姿态、表情、语速向你"发消息"；只有邮件、群发通知这类无即时反馈的渠道，linear 模型才够用。两种常见混淆：把一次单向广播当"沟通完毕"（对方可能根本没收到），或者反过来，在根本没有双向通道的场合（已读不回的群通知）追着要 transaction 式回应。

### Shannon–Weaver：发送者、噪声与"信息 ≠ 意义"

Shannon–Weaver 的经典的链路：source → transmitter → signal（+noise）→ receiver → destination。Evidence-backed，见 [models-of-communication] 捕获（"Shannon and Weaver"一节）。工程模型的核心贡献是**把技术噪声从语义噪声剥出来**：字节丢了是一回事，听懂了但理解岔了是另一回事。

`Practice heuristic`："没收到 / 没听清"（channel 问题）与"收到但误读"（semantic 问题）分开诊断。对方没回消息，第一步排除渠道（发送失败、时区、通知设置），第二步再谈含义。`constructed example`："你怎么不回我"的抱怨，多数时候先检查是否发进了对方屏蔽的会话，而不是先怀疑"他对我有意见"。

### Transactional model 与 Barnlund：语境三件套

Barnlund 的 transactional 模型强调（Evidence-backed，见 [models-of-communication] 捕获）：(1) 发送与回应**同时**发生——听者用身体姿态、表情在你说的时候就给了反馈，这反馈又实时改变你的下一句；(2) 意义在过程中共同生成；(3) 模型必须吃进三层语境——**social**（明规则：不该打断人、问候要回）、**relational**（你们是朋友、同事还是对手，过去的共同史）、**cultural**（种族、性别、国籍、社会阶层等社会身份）。

`Practice heuristic`：解码一场对话时同时读"内容"与"语境三件套"。同一句话，relational 层不同（上司对下属 vs 老友之间）读法完全不同；cultural 层不同（见 [[cultures/cu4-cross-cultural-general/core]]、[[cultures/cu2-malaysia-chinese/core]]）则连"哪些规则算明规则"都不同。低估 linguistic context 是误读的主要来源之一，见 [[concepts/c1-subtext-implicature/core]]。

### Hall 的 Encoding/Decoding：主导、协商、对抗三种读法

Stuart Hall (1973) 的 encoding/decoding 模型：发送方**编码**时预设了一个"首选读法"（dominant/preferred reading），但接收方**解码**时不必然照单收货——可以**主导式**（dominant）照单全收、**协商式**（negotiated，大体接受但按自己的处境打折）、也可以**对抗式**（oppositional，反向解读）。Evidence-backed，见 [enc-dec-hall] URL。

`Practice heuristic`：写正式文书（S3）前，预判受众的三种读法。对抗式读者搞对抗往往不是恶意，而是他们的社会位置让那条消息天然显得可疑；最小动作不是更用力地重复主张，而是先把他们怀疑的点摆到台面上。同样适用于给 AI 的 prompt（S4）：模型解码时也会"协商"，指令与上下文冲突时它会自行折中——所以 prompt 里的约束必须显式，见 [[playbooks/p4-ai-prompting/core]]。

### Communication Accommodation Theory（CAT）：趋同与分化

Giles 的 CAT：互动中的人会调整语言、语速、方言、语体、衣着等，以求**趋同**（convergence，拉近距离、求认同）或**分化**（divergence，拉开距离、维护群体身份）。Evidence-backed，见 [cat-csic] URL；与语码转换的机制相关性见 [[cultures/cu5-codeswitching/core]]。

`Practice heuristic`：对方突然用你的母语、你的口头禅、跟你的节奏，CAT 的默认读法是**趋同即示好**；但两个修正是必要的——在权力不对称关系里，下层对上层的趋同可能只是生存策略而非亲近；持续 divergence（拒用你的话码、刻意书面化、切换第三语）通常在说"我不认你是同类"，这是 S1 解码里的强信号，要纳入 [[concepts/c1-subtext-implicature/core]] 的候选读法清单。

### 信任三维：ability / benevolence / integrity（Mayer et al. 1995）

Mayer, Davis & Schoorman (1995) 把 trust 定义为"a willingness to be vulnerable to the actions of another party"，并把它和**可预测性**区分开：可预测性不等于信任——捕获里的例子：一个总"枪打出头鸟"（shoot the messenger）的上司是可预测的，但没人会因此愿意递坏消息给他。信任的三前件全部是**感知**而非事实：**ability**（领域特定的能力感知：一个技术权威不因此获得人际领域信任）、**benevolence**（对方除利己外确实想对你好）、**integrity**（对方遵守你认可的原则、说话算数）。Mayer 等还标注了与 Aristotle《Rhetoric》ethos 三要素（智慧、品格、善意）的平行对应。Evidence-backed，见 [mayer-trust-1995] 捕获（tier 1，academic 全文）。

`Practice heuristic`：信任被"扎了一下"时，先问断了哪个维度。ability 断了最好修：换个 domain 证明自己，或在 domain 内找背书；benevolence 断了要一致性证据、要时间；integrity 断了最难修——对方会把你一句失信读成"人格问题"而不是"一次失误"。本模型在原文献中为 organization context 提出，直接外推到亲密关系属 `Practice heuristic` 范围（结构可用，参数得改）。

### 依恋风格（attachment styles）与沟通内的张力

成人依恋研究（Fraley 综述，承 Hazan & Shaver 1987 与 Bowlby）把童年形成的模板沿用为成年亲密关系里的沟通行为倾向。四种常见风格：**secure**（能直接表达需求，冲突后修复快）、**anxious-preoccupied**（把模糊信号往坏里读，需要反复确认）、**dismissive-avoidant**（亲密度上升时退缩，用"讲道理"回避情绪话）、**fearful-avoidant**（既渴望又害怕，忽近忽远）。Evidence-backed，见 [fraley-attachment] URL。

`Practice heuristic`：依恋风格的第一用途是**看自己**，不是看别人——当你需要"知道自己在高压下会贴错方向"时最有价值。anxious / avoidant 配对冲突的修复走 [[concepts/c3-nvc-conflict-repair/core]] 与 [[scenarios/sc2-romance-intimacy/core]]。风险：用"他是回避型"解释对方一切行为不是工具而是越权定论，和给 c5 人格类型贴标签的陷阱同源，见 [[concepts/c5-personality-typology/core]] 的批判条目。

### Love languages：证据缺口与仍可用之处

Chapman 1992《The Five Love Languages》（words of affirmation、quality time、gifts、acts of service、physical touch）流行度极广，但证据面薄。Evidence-backed，见 [love-languages-book] 捕获：条目直陈 "Empirical evidence does not strongly support its core claims"；2017 年一项 67 对伴侣的研究只给出有限证据；**2023 年**关系科学家的综述明确指出：研究并没有确证"个人有稳定的 preferred love language"，也没有确证"说同种语言的伴侣质量更高"。捕获里的正面结论是：lasting love 需要的是**多样的关系行为**，不是某一种语言的专攻。

`Practice heuristic`：把 love languages 当**启发式清单**而非**类型学**。问对方"最近你感觉得到的关心是怎么到手的"，收到的是一个行为倾向的快照，比锁死他属于哪一格安全；若要表达关心，宁可轮流试五一样，也别笃定答案是那一样。

### 冲突风格：Thomas–Kilmann 的五种策略

Thomas–Kilmann 的冲突模式把策略放在 **assertiveness（追求己方利益）× cooperativeness（追求对方利益）** 的二维上，分出五型：**competing**（高 assert/低 coop）、**avoiding**（低/低）、**accommodating**（低 assert/高 coop）、**compromising**（中/中）、**collaborating**（高/高）。Evidence-backed，见 [tki-wiki] URL（注意：TKI instrument 本身是商业测评工具，框架原型则来自 Blake & Mouton 管理风格网格——精确谱系见该条目）。对应修复操作见 [[concepts/c3-nvc-conflict-repair/core]]。

`Practice heuristic`：五型不是性格，是**每场冲突各选一次**的策略。常见的病态是"只会一种"：只会回避的人靠"拖"，拖到 deadline 变成 high-stakes 正面冲突；只会迁就的人用迁就换短期和平，但让交换长期失衡（对方可能读作"他心虚"而不是"他脾气好"）。分阶段的组合拳:先用迁就稳住情绪，再谋求合作解决事实层。

### SCARF：五个社会威胁/奖励域

David Rock (2008) 的 SCARF 把社会经验拆成五个域，每个域的威胁感和奖励感都足以驱动行为：**Status**（相对 importance：我在对方眼里的地位感知）、**Certainty**（能不能预测未来会怎样，含糊常常比确定的坏消息更耗人）、**Autonomy**（对环境与事态的掌控感）、**Relatedness**（对方是 friend 还是 foe 的归类，安全感来源）、**Fairness**（交换是否公平的感知）。Rock 的定义式原文在捕获里可逐字查证。Evidence-backed，见 [scarf-rock-2008] 捕获（tier 1，原文 PDF）。Rock 引用的神经证据包括"status 威胁激活与物理疼痛相联的眶额/前扣带回通路"等；这类具体脑结论在社会神经科学界的复制情况有限——`Practice heuristic`：脑机制有争议，五域作为行为注记有价值，作为神经科学定律不可引用。

`Practice heuristic`：给负面反馈（S2/S4）时分次打击——一次谈话只碰一个域。当 status 打击（"这么简单都错"）＋certainty 威胁（"我马上要你重做"）＋autonomy 剥夺（"别问为什么"）＋fairness 质疑同时交叠，人不是"变成更差情绪的听者"，而是直接退场：只给出被动反应或防御。麻烦谈话前先排好序：哪个域本轮必须保住、哪个域可以下次再处理，见 [[scenarios/sc4-hard-conversations/core]]。

### Transactional Analysis（TA）：Parent / Adult / Child

Eric Berne 的 TA 把每个人内化的心理状态拆成三 ego states：**Parent**（内化的规范与上下级口吻，"你应该"、"你别再犯"）、**Adult**（就事论事、基于当下信息做决策）、**Child**（内化的早年情绪反应：sulk、兴奋、服从或反叛）。Berne 分析的是 transactions——每一次交互里，双方各自用了哪个 state、状态流是否"合流"（complementary，同一走向，对话可继续）、还是"交叉"（crossed，state 错位，冲突瞬间升级）、还是"隐藏"（ulterior，表面一套内里另一套）。他并列出 **games**（重复出现、结果多为一方落输的 transaction 序列）与 **strokes**（一切认可他人的沟通过合单位——表扬或批评都算）。Evidence-backed，见 [ta-wiki] 捕获。**重要免责**：TA 属 psychoanalytic 传统、**不是实证体系**，ego states 是概念划分而非脑/生理结构，见 [ta-wiki]。

`Practice heuristic`：TA 最实用的产出是"**换座位**"——识别对方此刻从哪个 state 在说话，再用相匹配的口吻回应。关键的 catch：Parent⇄Child 的对撞（训话遇上顶嘴）是最常见的 crossed transaction，一交叉就锁死。`constructed example`：上司"这都第二次了吧？"（Parent 起手）。回复 A："收到，我理解。这次的问题是 X，明早前我给你一份 change list。"（ Adult 应 Adult 或 Parent，不接情绪）比回复 B："你别每次都抓住不放！"（Child 顶 Parent，交叉锁死）更稳。另注："你这句触到了我的 Child"适合对内自省，不适合当面向对方的话术。

### META：如何使用本 KB（router、confidence 标签、ask vs assume）

本节解释 KB 的使用约定，全部 `Practice heuristic`：

1. **router 的用法**：任何查询先过 [[synthesis/00-how-to-use]]，按语言分到 zh/en/ms lane；路由命中不了，才回退进相关主题的 `core.md`。c10 的定位是**兜底模型层**：别的专题没讲清机制时、或者问题已经跨专题时，才来这里读。
2. **confidence 标签的读法**：`Evidence-backed` = 命名研究/原文，可溯源到 raw/ 或 `## Sources`（Mayer 1995、Rock 2008、Hall 1973、Berne 的条目都属于这层）；`Practice heuristic` = 从这些模型推出的可执行规则，方便但**未独立验证**；`constructed example` = 编出来的对话样例；`anecdotal` = tier 3 的社区说法，只能做假设，不能下判断。
3. **when to ask vs assume**：提问便宜而误读昂贵时（评估对方情绪、涉及给钱、披露与承诺、冲突可能升一级），**问，别假设**；提问昂贵而误读可逆时（日常闲聊、非关键决策），可以按最可能读法推进然后观察反馈，快速修正。模型是给你排出多种读法的，不是替你做最终决定。提问本身的方法集合见 [[scenarios/sc12-asking-help/core]]。
4. **专题层级**：c10 把模型集中在这，但它们的证据强度不同——c5（人格类型）里 MBTI 一类偏商业框架，成人依恋的科研基础较稳，c8（astrology）则只是"人在读人"的**民间启发**（其专题内已有精确告示）。**读到的内容按证据强度取用，不按"好用"取用**。

### META：influence 的伦理边界（对 c2/c9 的元约定）

全 KB 里所有"影响"专题（[[concepts/c2-persuasion-influence/core|c2]]、[[concepts/c9-manipulation-defense/core|c9]]）共用的伦理约定，`Practice heuristic`：

1. **红线：未经知情同意的影响**。任何显著仰赖对方**无法或不便评估**的事实缺口（隐瞒关键代价、伪造稀缺、利用依恋恐惧或权力差配：上司对可能被解雇的人、医生对病人、债主对急难的借款人）属于操纵，不属于 influence——这条是 [[concepts/c9-manipulation-defense/core]] 的判别主线，c10 把它提升为全 KB 通用边界。
2. **被允许的： transparent influence**。对方看过底牌、可以拒绝、决定后可回撤，Cialdini 式技巧（reciprocity、scarcity、social proof 等，见 c2 捕获）只在这个框架内使用。关键条件是**对方保留了自由与信息基础**。
3. **透明原则**：试图影响对方时，把"我打算说服你走 X 方向"放在台面上（至少在关系型通道上），而不是让它藏着。隐藏的影响意图哪怕初衷好，一旦被识破（在 [[scenarios/sc13-mediation/core]] 这类高审视场景几乎必被识破），伤害比正面表述大。

### META：认知谦逊（epistemic humility）

读人是概率不是判决；模型是地图不是领土，所有"几型几式"都只是把人压到低维平面的**临时支架**。`Practice heuristic`：

1. **解码一律存为工作假设**。候选读法（[[playbooks/p2-subtext-decoder/core]] 的流程要求至少 2–3 个 candidates）连同 confidence 一起记录；说出的是"目前最可能的读法"，不是判定。当两个候选读法无法分辨、且分辨代价大时，**承认不知道并去问**，比押注更便宜。
2. **模型防直觉偏差，但模型自身也有偏**。编好的通用模型（SCARF 五域、五冲突型、四种依恋）救你看穿单点印象，同时也会让你"看见一直在找的东西"（确认偏误）。两个对策：一次只用一个模型；换第二个模型交叉核对同一组证据，冲突时升级为需要更多观察的信号。
3. **新证据要显式改变排序**。新的话语、行为、context 变化应当重新给候选读法排序，而不是逼旧假设的墙角。`models are tools, not truth`；模型间意见相左（比如 SCARF 与 love languages 给出不同 read）不是算错，而是说明观察不够，需要补证据。

## Sources

Tier 1（academic / original papers）：

- Mayer, R. C., Davis, J. H., & Schoorman, F. D. (1995). *An Integrative Model of Organizational Trust*. Academy of Management Review 20(3): 709–734. raw 捕获: <https://www.makinggood.ac.nz/media/1270/mayeretal_1995_organizationaltrust.pdf>
- Rock, D. (2008). *SCARF: a brain-based model for collaborating with and influencing others*. NeuroLeadership Journal. raw 捕获: <https://schoolguide.casel.org/uploads/sites/2/2018/12/SCARF-NeuroleadershipArticle.pdf>
- Fraley, R. C. *A Brief Overview of Adult Attachment Theory and Research* (Univ. of Illinois): <http://labs.psychology.illinois.edu/~rcfraley/attachment/attachmentstyles.htm>

Tier 2（established encyclopedic / theory pages）：

- Models of communication (Shannon–Weaver、Barnlund、transactional models): <https://en.wikipedia.org/wiki/Models_of_communication> — raw 捕获 `raw/c10-models-meta/f-models-of-communication.md`
- Stuart Hall 的 encoding/decoding model of communication: <https://en.wikipedia.org/wiki/Encoding/decoding_model_of_communication>
- Communication Accommodation Theory: <https://en.wikipedia.org/wiki/Communication_accommodation_theory>
- Thomas–Kilmann conflict modes: <https://en.wikipedia.org/wiki/Thomas%E2%80%93Kilmann_Conflict_Mode_Instrument>
- Transactional analysis / Transactional analysis (Berne; Parent/Adult/Child): <https://en.wikipedia.org/wiki/Transactional_analysis> — raw 捕获 `raw/c10-models-meta/f-transactional-analysis-wiki.md`
- The Five Love Languages（含 2017 couple study、2023 review 的证据反观）: <https://en.wikipedia.org/wiki/The_Five_Love_Languages> — raw 捕获 `raw/c10-models-meta/f-love-languages-book.md`
