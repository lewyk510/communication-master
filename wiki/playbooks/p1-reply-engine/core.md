---
id: p1-reply-engine
title: Reply Engine · 回复引擎
type: playbook
lang: core
tags:
  - reply
  - decision-procedure
  - assertiveness
  - conflict-styles
  - de-escalation
  - boundaries
scenarios:
  - S2
sources:
  - raw/p1-reply-engine/f-mayoclinic-assertive.md
  - raw/p1-reply-engine/f-pon-conflict-styles.md
  - raw/p1-reply-engine/f-therapistaid-passive-assertive.md
  - raw/p1-reply-engine/f-umatter-styles.md
related:
  - "[[concepts/c1-subtext-implicature/core]]"
  - "[[concepts/c3-nvc-conflict-repair/core]]"
  - "[[concepts/c2-persuasion-influence/core]]"
  - "[[concepts/c9-manipulation-defense/core]]"
  - "[[cultures/cu1-malaysia-malay/core]]"
  - "[[cultures/cu2-malaysia-chinese/core]]"
  - "[[cultures/cu3-malaysia-indian/core]]"
  - "[[cultures/cu4-cross-cultural-general/core]]"
  - "[[cultures/cu5-codeswitching/core]]"
created: 2026-10-07
updated: 2026-10-07
---

# Reply Engine · 回复引擎

Take an incoming message plus context, run the procedure, output three replies. This page is
an engine: every section is a step the responder (or an assistant acting for the responder)
executes in order. Sections 1–8 are the procedure; sections 9–11 are calibration and fail-safes.

## 1. What the engine does (specification)

**Input tuple:**

| Slot | Example |
|---|---|
| A. Incoming message (verbatim) | 你要加班吗？如果不想也没关系，你开心就好。 |
| B. Relationship × power (self → other) | peer / subordinate→boss / service-provider→client |
| C. Goal for this exchange | protect time / repair trust / buy information / preserve face |
| D. Culture frame (link [[cultures/cu4-cross-cultural-general/core]]) | high-context zh family; low-context en boss |
| E. Channel | face-to-face / WeChat text / formal email / voice note |

**Output contract:** exactly **three** labelled reply options —
**Safe** (lowest relationship risk), **Assertive** (clear stance, respectful), **Warm**
(relationship-first, still honest). One sentence each is acceptable; a short paragraph each is
better; anything more than two sentences per option means the exchange belongs to a full
letter engine ([[playbooks/p3-formal-writing/core]]).

The procedure: **Decode intent → read power → check culture & channel → pick strategy → draft
3 options → run exit tests.**

## 2. Step 1 — Intent detection (what does the other person want?)

### 2.1 The two questions
Before choosing words, answer two questions from the message plus context:

1. **Surface ask** — what are they literally requesting or saying?
2. **Underlying need** — which of these sits beneath the surface ask?

### 2.2 The underlying-need menu
- *Approval/permission* ("can I get your blessing on this?")
- *Assurance/reassurance* ("tell me the relationship is fine")
- *Information* ("what actually happened?")
- *Action* ("I need you to do X by Y")
- *Release* ("I need to vent; I do not need you to fix it")
- *Pressure dressed as choice* — a soft ask where "no" was not priced in (the classic
  「不想也没关系，你开心就好」 pattern; links [[playbooks/p2-subtext-decoder/core]])

`Practice heuristic`: if two readings collide and stakes are real, do not guess between them —
**Probe** (Strategy P below) is the default move. Citation for the two-readings discipline:
[[concepts/c1-subtext-implicature/core]].

## 3. Step 2 — Power & relationship read

### 3.1 Axis set
Three axes, decided before drafting:

### 3.2 The three axes in detail
- **Who bears the cost of a bad reply?** If the other side holds your appraisal, contract, or
  livelihood (boss, client, landlord), the Safe option must still be relationship-safe even
  when the Assertive option carries the real stance.
- **One-off vs repeat.** A one-off with a stranger tolerates hard refusal; a five-year
  colleague relationship amortises a softer "no, but".
- **Precedent risk.** Consenting once to a request you resent trains the requester ("Practice
  heuristic", drawn from boundary literature below).

## 4. Step 3 — Response taxonomy (ten strategies)

### 4.1 Strategy table
Turnkey map from strategy → when to use → one-line shape. Composed by the engine;
style definitions below are `Evidence-backed` (see §4 note and Sources).

| # | Strategy | Use when | One-line shape |
|---|---|---|---|
| 1 | **De-escalate** | Emotion is the message; getting facts through will fail | Name the heat, slow the pace, no accusation |
| 2 | **Validate** | Person is venting / needs release, not solutions | "That sounds genuinely frustrating" — empathy before content |
| 3 | **Boundary-set** | Repeat ask you must cap once and for all | Stated rule + one sentence, no list of justifications |
| 4 | **Refuse** | Clear no; relationship survives it | Direct, brief, one offer of what *can* be done |
| 5 | **Deflect / postpone** | Need time, info, or to cool off | Fixed promise of return ("I'll reply by X") — never silence |
| 6 | **Probe / clarify** | Two readings collide; stakes real | One question that separates the readings |
| 7 | **Humour** | Tension is real but small; both sides read irony | Light, self-inclusive, never at their expense |
| 8 | **Silence / time** | Message is bait, provocation, or a guilt-trip volley | Do nothing now; reply later, coolly, on your topic |
| 9 | **Comply** | Cheap, legitimate, and you actually agree | Give it fast and fully — half-compliance reads as resentment |
| 10 | **Negotiate** | Both interests are real and conditionally compatible | Trade: "If I take this, I need that" |

### 4.2 Trace notes
When-to-use notes `Evidence-backed` against the Thomas–Kilmann five modes
(competing / collaborating / compromising / avoiding / accommodating, with situational
caveats for each) traced to the Harvard PON capture
(`raw/p1-reply-engine/f-pon-conflict-styles.md`): strategic avoidance is endorsed when
emotions run high or issues are trivial; accommodating is prudent for immediate de-escalation
with an upset superior. The passive/aggressive/passive-aggressive/assertive contrast is
`Evidence-backed` via Mayo Clinic and Therapist Aid captures. Strategy 1–2 mechanics draw on
NVC: observation before evaluation, feeling, need, request
([[concepts/c3-nvc-conflict-repair/core]]). Use Strategy 8 or 3 whenever the message pattern is
gaslighting, guilt-tripping, or foot-in-the-door escalation — then pair with
[[concepts/c9-manipulation-defense/core]]. Use Strategy 10 openly when you want
*them* to say yes — see [[concepts/c2-persuasion-influence/core]] for interest-based framing.

## 5. Step 4 — Decision tree (executable)

### 5.1 The tree
Run top-down; first hit wins.

```
INPUT: message M, power P, goal G, culture C, channel E

0. If M is provocation / bait / gaslighting        → S8 (silence now, S1 decode first)
1. If emotions of either side are hot              → S1 de-escalate → S2 validate
   (only after they are warmer)
2. If two readings of M diverge AND stakes ≠ trivial → S6 probe
   (or first reply = probe framed inside a warm option)
3. If the ask is one you must say no to:
     P = "they hold power over me"                 → S4 refuse, face-softer, give a counteroffer
     repeated ask you were never OK with           → S3 boundary-set
     trivial / one-off                             → S4 refuse plain
4. If goal = relationship repair above the ask     → S2 validate + comply partially
5. If interests are compatible with trading        → S10 negotiate
6. If ask is cheap and legitimate                  → S9 comply fast
7. If you need time/coverage                       → S5 postpone with a fixed return time
8. If tension is low and irony is mutual           → S7 humour
DEFAULT (nothing matched, or you are unsure)     → probe: ask one clarifying question
```

### 5.2 Rule for the "no" branch
For the "no" branch, the escalation-free wording rule comes from the captured guidance:
**"No is a complete sentence"; keep any explanation brief**
(`raw/p1-reply-engine/f-mayoclinic-assertive.md`, §"Practice saying no").

## 6. Step 5 — The 3-options output format

### 6.1 The fixed triad
Always output exactly three, in this order, each labelled with its chosen strategy number:

- **🛡 Safe** — lowest relationship risk; usually softens or moves the ask sideways. Even
  when you refuse inside it, it gives the other person a face-preserving path (face logic:
  [[cultures/cu2-malaysia-chinese/core]], [[cultures/cu1-malaysia-malay/core]]).
- **⚔ Assertive** — your actual stance, stated once, cleanly, without over-justifying. The
  default register for boundary/refuse goals by choice of the engine: over-explaining is the
  #1 observed failure (see §9).
- **💛 Warm** — relationship-first: more accommodation than you'd give a stranger, but it
  still names the real need ("I can't this weekend, I miss talking properly — lunch Sunday?").

### 6.2 Risk-honesty rule
`Practice heuristic`: the three options must *differ in risk, not in honesty*. Never make the
Safe option a lie and the Assertive option the truth — that bifurcation is how people-pleasing
hides.

## 7. Register matching: channel × culture

### 7.1 Channel notes
- **Face-to-face / call: tone carries half the message — pacing, prosody
  ([[concepts/c11-paralanguage-prosody/core]]); refuse with a steady mid-pace, not a rush.
- **Text (WeChat/WhatsApp):** no prosody, so punctuation and emoji substitute for tone; a bare
  "好。" reads cold, "好呀👍" reads fine — `Practice heuristic`, consistent with
  [[scenarios/sc7-digital-messaging/core]] and cue substitution
  ([[concepts/c13-visual-multimodal/core]]).
- **Email/formal:** use [[playbooks/p3-formal-writing/core]]; this engine only picks the stance
  (e.g. Refuse-soft) and hands off.
- **High-context (zh family, Malay budi bahasa):** pack the refusal inside relationship
  material; indirect refusals are the local standard, not evasiveness
  ([[cultures/cu2-malaysia-chinese/core]], [[cultures/cu1-malaysia-malay/core]]).
  `Evidence-backed` for high-context cultures, per the cross-culture capture set in cu4.
- **Low-context (en corporate, global clients):** state the decision in sentence one; warmth
  is a closing line, not a wrapper around the no.
- **Codeswitching contexts (Manglish, mixed-language chat):** match their code for solidarity,
  keep the *stance-sentence* in whichever language both read unambiguously
  ([[cultures/cu5-codeswitching/core]]).

## 8. Composing the sentence (micro-templates)

For each strategy, one fill-in template. `Practice heuristic` throughout; NVC shape for 1–2 is
traced to c3 captures.

- De-escalate: "先别急——我们一件一件来。" / "Let's take this one thing at a time."
- Validate: "这件事确实挺气人的。" / "That does sound genuinely annoying."
- Boundary-set: "这个我一直没换过：______ 不做，理由不展开。" / "House rule for me: I don't
  take calls after 21:00."
- Refuse: "这个我做不了，但 ______ 我可以。" / "I can't do that — what I can do is X."
- Postpone: "今天下班前答复你。" / "You'll have my answer by 6pm today."
- Probe: "你希望我做的是 A 还是 B？" / "Do you want me to fix it, or just to hear it?"
- Humour: self-inclusive only ("是我手滑没跟上进度，不是你的安排有问题——我会改"). Never punch down.
- Comply: no conditional clauses; just do it, confirm it.

## 9. Pitfalls (fail-safes)

1. **Over-apologising.** Multiple sorry's turn a position into a plea. One apology per reply
   max; loops back to the assertive/passive evidence in the Mayo capture.
2. **Escalating in kind.** Matching heat with heat. De-escalate first even when you are
   right — rightness delivered hot is received as attack.
3. **People-pleasing ("say yes, resent, withdraw").** The passive pattern that
   `Evidence-backed` sources list as leading to being taken advantage of and to suppressed
   resentment; the engine's fix is the Assertive slot existing at all.
4. **Half-answers.** "Maybe, later, let's see" where the real answer is no → produces repeat
   asks. This is the passive-aggressive path described in both captures; repay with Strategy 3.
5. **Explaining the no with five reasons.** Five reasons are five hooks for the other side to
   rebut. One reason or none.
6. **Joke on a serious ask.** When stakes are real, humour undercuts your own credibility —
   save Strategy 7 for low-stakes tension only.
7. **Warm option that's actually evasive.** Warm is honest-but-toned; if the stance disappears
   from the sentence, it is a Silent No, and Silent Nos are the fuel of hint culture.
8. **Replying in the heat of the message.** Default to S5 postpone (with a return time)
   rather than an instant reply you cannot unsay.

## 10. Worked example (constructed example)

Input: 「不想也没关系，你开心就好」加班邀请；subordinate → boss; goal = protect the weekend;
WeChat text; zh high-context office.

1. Surface ask: a question. Underlying: pressure with a face-saving wrapper (two readings
   kept open — S1 decode discipline).
2. Power: boss holds appraisal; reply must not corner them.
3. Pick: Probe inside a Warm frame; Assertive as a real no.
4. Options:
   - 🛡 Safe: 「这周项目交付前我怕会分心，如果后面人手紧我第一时间顶上。」
   - ⚔ Assertive: 「这周末我有安排，加班去不了，下周一正常到。」
   - 💛 Warm: 「我真的很想把这个项目做好，周末家里有点事走不开，这周我每天提前一小时到，把活儿赶齐。」

Exit tests (§11) pass: no apology used, one reason each, no defensible promise broken.

## 11. Exit tests (machine-checkable)

Before delivering output, verify:

1. Exactly three options, each labelled 🛡/⚔/💛 with its strategy number.
2. No option contains more than one countable reason or one apology.
3. Every option's stance (yes/no/maybe) is identifiable from its text alone.
4. The Safe option never contradicts the truth of the Assertive option.
5. Any "no" has either zero or one justification sentence.
6. If S8 (silence) was chosen, it is stated as *implied action*, not silence in the reply.

## Sources

- Mayo Clinic — *Being assertive: Reduce stress, communicate better* (tier 2, established media):
  https://www.mayoclinic.org/healthy-lifestyle/stress-management/in-depth/assertive/art-20044644 — captured
  at `raw/p1-reply-engine/f-mayoclinic-assertive.md`.
- Harvard Program on Negotiation — *Conflict-Management Styles: Pitfalls and Best Practices*
  (tier 1, academic/program): https://www.pon.harvard.edu/daily/conflict-resolution/conflict-management-styles-pitfalls-and-best-practices/
  — captured at `raw/p1-reply-engine/f-pon-conflict-styles.md`.
- Therapist Aid — *Passive, Aggressive, and Assertive Communication* (tier 2, professional practice):
  https://www.therapistaid.com/worksheets/passive-aggressive-and-assertive-communication — captured at
  `raw/p1-reply-engine/f-therapistaid-passive-assertive.md`.
- Princeton UMatter — *Understanding Your Communication Style* (tier 2, university educational):
  https://umatter.princeton.edu/respect/tools/communication-styles — captured at
  `raw/p1-reply-engine/f-umatter-styles.md`.
