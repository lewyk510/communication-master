---
id: c13-visual-multimodal
title: Visual & Multimodal
type: concept
lang: core
tags:
  - emoji
  - stickers
  - memes
  - biaoqingbao
  - multimodal
  - visual-subtext
scenarios:
  - S1
  - S2
sources:
  - raw/c13-visual-multimodal/f-emoji-misinterpretation-npr.md
  - raw/c13-visual-multimodal/f-emoji-systematic-review.md
  - raw/c13-visual-multimodal/f-emoji-crosscultural-eurekalert.md
  - raw/c13-visual-multimodal/f-genz-emoji-conversation.md
  - raw/c13-visual-multimodal/f-genz-emoji-cnn.md
  - raw/c13-visual-multimodal/f-biaoqing-uhpressbooks.md
  - raw/c13-visual-multimodal/f-biaoqing-chinosity-panda.md
related:
  - "[[concepts/c1-subtext-implicature/core]]"
  - "[[concepts/c11-paralanguage-prosody/core]]"
  - "[[concepts/c7-demographic-differences/core]]"
  - "[[scenarios/sc7-digital-messaging/core]]"
  - "[[playbooks/p2-subtext-decoder/core]]"
created: 2026-10-07
updated: 2026-10-07
---

# 视觉与多模态（Visual & Multimodal）

本页是本主题的基准参考（zh-first，术语保留英文）。核心问题只有一个：**当一条消息不是纯文字，而是 emoji、表情包、梗图、截图、GIF 的组合时，视觉层到底传达了什么，又怎样被误读？** 阅读顺序：理论骨架 → 高风险 emoji → 表情包与梗图文化 → 多模态组合 → 解码与回应对策。所有命名研究、统计与引文均溯源到 `## Sources` 中的 raw 捕获或 URL；无法溯源的实践建议一律标 `Practice heuristic`。

emoji 不是装饰。研究者的原话是：使用者以为用 emoji 风险很低，实际上它处于"高误沟通风险"中（Hannah Miller，转引自 NPR 报道，Evidence-backed）。下面每一节都在回答同一件事：这个风险来自哪里，怎么管理。

### Emoji 的三层含义模型：字符义、渲染义、语用义

一个 emoji 的"意思"至少分三层。第一层是字符义（Unicode 官方定义，如 U+1F600 是 grinning face）。第二层是渲染义（同一字符在 Apple、Samsung、WeChat 平台上画法不同，观感不同）。第三层是语用义（发的人此刻想用它做什么：示好、敷衍、讽刺、收尾）。

Miller 等人的 GroupLens 研究给第二、三层画了红线：在他们检验的 emoji 中，只有 4.5% 的符号具有"持续低方差"的情绪解读，也就是大家看法一致；反过来，在 25% 的情况下，受试者对同一渲染图的情绪极性（正/中/负）都无法达成一致（Evidence-backed，NPR 报道原始研究）。这意味着 emoji 的默认状态是歧义，不是共识。

实践推论：读 emoji 时不要问"这个符号是什么意思"，要问"这个人、在这个平台、在这个语境下，用这个符号在做什么"。三层都对上，才算读懂。`Practice heuristic`

### 平台渲染差异：同一个字符，不同的脸

Emoji 的第二层歧义来自平台。NPR 报道里最直观的例子是 grinning face with smiling eyes：同一字符在 iPhone、Samsung 等平台的渲染不同，受试者给出的平均情绪分也不同，某些平台上的版本被整体读成偏负面（Evidence-backed）。

这在混合平台聊天（iOS 用户 vs 安卓用户、微信原生表情 vs 系统表情）里是结构性风险。你发出去的😊和对方屏幕上的😊可能根本不是一张脸。`Practice heuristic`：跨平台的重要消息，情绪信息不要只押在一个 emoji 上，用文字把态度钉死，emoji 只做补充。

### 被动攻击谱系：🙃 😅 👌 👍 与"微笑脸问题"

有一批 emoji 正处在代际与场景的断裂带上，同一符号在两群人眼里是两个东西：

- 🙂（slightly smiling face / 微信微笑）：官方义是"礼貌微笑"，但在年轻用户与中文网络语境里，高频被读作"皮笑肉不笑"、敷衍、阴阳怪气，甚至"我忍着"。PLOS ONE 2024 的中英对照研究提供了跨文化证据：被归类为 happy 的 smile emoji，在中国参与者中并不总是表示开心（Evidence-backed，EurekAlert 摘录）。
- 🙃（upside-down face）：字面是颠倒的笑脸，语用上通常是"表面没事、内里翻腾"：无奈、自嘲、"行吧你赢了"。讽刺读法占比高。`Practice heuristic`
- 😅（smiling face with sweat）：不是"尴尬出汗"的字面义，而是缓和剂——用来软化拒绝、承认小失误、给冷场找台阶。`Practice heuristic`
- 👌（OK hand）：多数场合是"好、没问题"，但在部分网络亚文化里被挪用为挑衅符号；国际语境下偶发歧义。`Practice heuristic`
- 👍（thumbs up）：老一代读作"收到、认可"，很多年轻用户读作冷漠或 passive-aggressive（见 The Conversation，Evidence-backed）。

这批符号的共性：**字符义中性，语用义分裂**。解码时优先看发送者的代际与你们的关系史，其次才是字符义。

### 代际断层：😂 vs 💀 vs 🤣

😂（face with tears of joy，2015 年牛津词典年度词汇）在 millennial 手里是标准笑声；Gen Z 已把它标记为"过时"，改用 💀（skull）表达"I'm dead"（笑死了）。CNN 2021 年报道了 TikTok 上两代人的emoji冲突，💀 是"visual version of the slang phrase 'I'm dead'"，指某东西非常好笑（Evidence-backed）。The Conversation 的作者（悉尼大学）自述只有在"被逼无奈"时才用 😂，年轻一代偏好 💀（Evidence-backed）。🤣（rolling on the floor laughing）则介于两者之间：比 😂 程度更重，但还没有背上"过时"的包袱。`Practice heuristic`

回应对策：对 Gen Z 回笑，用 💀 或文字"lmao"；对长辈或上级，😂 反而是最安全的，因为上一代读它没有任何负面包袱。同一个"笑"的表意，选哪个符号本身就是一条年龄信号。

### 跨文化解读：UK vs China 的实证差异

Chen、Yang、Howman、Filik（2024，PLOS ONE）招募了 523 名成年人（253 名中国、270 名英国，18 到 84 岁），让他们解读 24 个 emoji（涵盖 Apple、Windows、Android、WeChat 四种渲染，代表 happy、sad、angry、surprised、fearful、disgusted 六种情绪）。结论：性别、年龄、文化都对解读有显著影响；且部分差异可由"对该 emoji 的熟悉度"中介（Evidence-backed）。

对中英沟通的直接含义：(1) 同一个 emoji 在中国参与者那里不总按官方义使用，典型如 smile 脸；(2) 熟悉度决定解读——不熟悉某个 emoji 的人更容易按字符义硬读；(3) 跨文化聊天时，"在对方常用平台上常用得多的符号"才是安全区。`Practice heuristic`：给跨文化对象发 emoji 前，先看对方平时用哪些——模仿对方的词表，比猜 Unicode 定义可靠。

### 表情包（biaoqingbao）：带文本的反应图

表情包（biaoqingbao，"expression package"）指中文互联网流行的 stickers、emoji、GIF 与自制图片的统称，通常是可下载的主题套装，图文结合，文字从几个字到整句话不等（UH pressbooks，Evidence-backed for 定义）。它的独特之处在文本容量：一张表情包可以承载一整句潜台词，这是单个 emoji 做不到的。

最有辨识度的一支是熊猫头（panda head）：黑白熊猫配上真人表情脸。其表情多取自中国网络的病毒素材，最著名的一张来自韩国演员 Choi Sung-kook 电影截图；这一风格由 Wang Nima 于 2008 年借西方 rage comics 之形在 baozou.com 发扬（Chinosity，tier 3，anecdotal）。熊猫头至今是中文梗图的主力模板。

读表情包的三步：先读图上文字（表层信息），再读图与文字的落差（讽刺、自嘲、示弱、示威），最后读"为什么此刻发这张"（对话中的站位）。第三步是潜台词所在。`Practice heuristic`

### 斗图（dou tu）：视觉对话的回合制

斗图即"用表情包打架"：双方以表情包来回对轰，比拼存货与接梗速度，2015 年前后开始流行，可发生在群聊也可私聊，由此形成了围绕表情包的社群文化（UH pressbooks，Evidence-backed for 现象描述）。

它的社交功能大于内容：斗图不是真的在"吵"，而是用视觉回合确认"我们共享同一套梗字典"。对方接得住你的图，说明你们在同一个文化圈层；对方发一张官方微笑脸回你的熊猫头，说明频道没对上。`Practice heuristic`

### Sticker / GIF：语义放大器与节奏器

从形态学上，sticker 与 emoji 的差别是：更大、有静态与动图形态、可增删（emoji 依赖 Unicode，不可编辑），但只能单独发送、不能插入文字中间（Zhou et al. 2017，转引自 Bai et al. 2019 综述，Evidence-backed）。"只能单独发送"这一点决定了它的语位：sticker 常常占据一整条消息，相当于一个"视觉回合"。

因此 sticker 有两种读法：(1) 情绪放大——内容本身说"谢谢"，配一张夸张的 sticker 是把音量调大；(2) 回合替代——整条消息只有一张 sticker，等于对方用视觉回应替代了文字回应。后者要看关系基线：本来话多的人突然只发图，是降温信号。`Practice heuristic`

### 截图与图片回复：图作为证据与作为回避

发一张截图（screenshot）当回复，至少有三种语义：出示证据（"这是你上次说的"）、出示现场（"事情就是这样"）、回避重新表述（懒得打字，但也不打算展开）。聊天软件把图片和文字并排陈列，图片回复的"不解释"本身也是信息。

`Practice heuristic`：收到纯截图回复时，先判断它属于哪一种；若你期待的是态度而对方只给了现场记录，说明对方在推迟表态，追问要轻（"你倾向哪边？"），不要替对方补态度。发截图给别人看之前，检查截图里有没有第三方隐私——截图的传播力远超当事人预期。

### 颜色与字体语气（typography tone）：弱信号，带保留

纯文字渠道里，颜色、字体、大小写、标点密度也构成"视觉语气"：全大写读作喊叫，句号结尾在即时通讯里读作冷淡，长段小字读作郑重。这类信号成立的前提是双方都有同样的读写习惯，且平台允许排版（邮件、Slack vs 微信语音转文字）。

保留（caveat）：颜色与字体的语气证据基础薄弱，属于民俗学范畴，不同平台、不同年龄的默认设置也不同（有人用大字号只是因为视力）。**读的时候当弱信号参考，写的时候优先保证可读性。** `Practice heuristic`

### 视觉礼貌与层级：sticker 对老板 vs 对同侪

视觉元素的正式度梯度大致是：纯文字（正式）> emoji（半正式）> sticker/GIF（非正式）> 斗图梗图（玩乐场）。The Conversation 提供了层级如何改变接受的例证：老板发的 👍 在职场语境里显得可以接受、较少引发焦虑；同样一个 👍 若来自刚发完暧昧消息的对象，解读空间骤然变大（Evidence-backed）。也就是说，符号引发的焦虑度取决于关系的赌注，不取决于符号本身。

`Practice heuristic`：向上（对上级、长辈、客户）默认只用官方义无争议的 emoji（👍 只作为收尾确认、🙏 致谢），不发梗图、不斗图；同级可逐步升级视觉玩闹，升级节奏跟着对方走——对方先发梗图，你才回梗图。关系不明时，视觉正式度取上限而不是下限。

### 多模态组合：文字 + 图片 + sticker 的排序语法

一条多模态消息（text + image + sticker）内部有排序语法。`Practice heuristic` 总结如下：

1. **文字在前的组合**（文字+补一张图/sticker）：图是语气注释，软化或夸张文字。读法：以文字为准。
2. **图在前、文字收尾**（图+一句话）：图开场定调，文字给出真正的信息。常见于熟人间的"表情包开场、正事殿后"。
3. **只有一张 sticker**：如上节所述，是回合替代，优先读关系信号而非内容。
4. **连发数图（斗图式）**：玩乐回合，除非上下文是冲突，否则不要读出敌意。

平台差异：微信的表情包文化最重（自带斗图生态），WhatsApp 上 GIF 与 sticker 混用但梗密度低，Telegram 的 sticker 生态最发达、大量社群自制包。给不同平台的人发图，密度要跟着平台的日常水位走。`Practice heuristic`

### 什么时候一张图胜过千言：图像的不可替代位

三类场景图片优于文字：**出示现场**（截图、照片、白板照片——文字描述永远不如原图可信）；**共享反应**（对一条消息的最佳回应有时就是一张"我的表情"图，它传达"我看到了，而且我和你站在同一边"）；**打破僵局**（冷场后一张轻松的图比硬找话题摩擦小）。

反过来，三类场景必须弃图用字：道歉与修复冲突（梗图会稀释诚意，见 [[concepts/c3-nvc-conflict-repair/core]]）；敏感拒绝（视觉玩闹会让"不"变得含糊）；正式请求。`Practice heuristic`

### 梗图作为社会评论：读 meme 的三个层级

梗图（meme / 表情包）常被当作纯玩笑，但它经常是社会评论的压缩包。读法分三层：表层是笑点；中层是"这张图在替谁说话"——熊猫头里嵌入的名人脸与病毒事件截图，本身就是对热点事件的再加工（Chinosity 对来源的梳理，anecdotal）；深层是"为什么此刻这张图会流行"——流行即舆情，一个梗在群里的传播速度与变体，比任何人公开表态都诚实。

`Practice heuristic`：在群里看到一张带有事件影子的梗图被反复转发，不要只回 haha；它往往是群成员对某件事的间接表态，是讨论的邀请函。接不接、怎么接，取决于你想不想在公开频道表这个态。

### 视觉潜台词清单：解码顺序小结

把全篇压缩成一个解码流程（S1 decode）：(1) 识别模态——这是字符、渲染图、sticker 还是截图；(2) 代际与文化校准——发送者属于哪套符号词表（💀 vs 😂，smile 脸的中文读法）；(3) 关系与赌注——同侪玩闹还是向上沟通（👍 的焦虑度来自关系赌注）；(4) 消息内部排序——文字主导还是图主导；(5) 与基线的偏差——对方平时的视觉风格是什么，此刻偏离了没有。回应侧（S2 respond）：正式度取上限、模仿对方词表、 emoji 只补不押、图先于字或字先于图按关系定。`Practice heuristic`

## Sources

- NPR — "Lost In Translation: Study Finds Interpretation Of Emojis Can Vary Widely" (tier 2, 报道 Miller et al. ICWSM 2016 tier 1 原始研究): https://www.npr.org/sections/thetwo-way/2016/04/12/473965971/lost-in-translation-study-finds-interpretation-of-emojis-can-vary-widely
- Miller et al., "'Blissfully happy' or 'ready to fight': Varying Interpretations of Emoji" (tier 1, ICWSM 2016, GroupLens): https://grouplens.org/site-content/uploads/ICWSM16_Emoji-Final_Version.pdf
- Bai et al. 2019, "A Systematic Review of Emoji: Current Research and Future Opportunities" (tier 1, Frontiers in Psychology): https://pmc.ncbi.nlm.nih.gov/articles/PMC6803511/
- Chen, Yang, Howman & Filik 2024, "Individual differences in emoji comprehension: Gender, age, and culture" (tier 1, PLOS ONE 19(2): e0297379): https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0297379
- EurekAlert release for the PLOS ONE study (tier 2): https://www.eurekalert.org/news-releases/1033787
- The Conversation — "Thumbs up: good or passive aggressive? How emojis became the most confusing kind of online language" (tier 2): https://theconversation.com/thumbs-up-good-or-passive-aggressive-how-emojis-became-the-most-confusing-kind-of-online-language-259151
- CNN — "Sorry, millennials. The 😂 emoji isn't cool anymore" (tier 2): https://www.cnn.com/2021/02/14/tech/crying-laughing-emoji-gen-z
- University of Houston CHIN 3343 open textbook — "Emoticon · 表情包 (biǎoqíng bāo)" (tier 2): https://uhlibraries.pressbooks.pub/chin3343sp23/chapter/expressionpackage/
- Chinosity — "What's The Deal With That Famous Chinese Panda Meme?" (tier 3, anecdotal): https://www.chinosity.com/2020/07/01/whats-the-deal-with-that-famous-chinese-panda-meme/
