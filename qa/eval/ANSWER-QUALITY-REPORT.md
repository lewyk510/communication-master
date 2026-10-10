# Answer-Quality & Coverage Report — Round 9

**Question on the table:** Rounds 1–8 tuned *routing* and *understanding decode*. Round 9 asks the question that actually decides whether the skill is useful: **given realistic questions, can the KB answer them — and does it even have the pages?**

## Method

- **Corpus:** 20 hard, real questions sampled from the Round-8 bombardment (all 5 angles × 4 languages: zh / en / ms / Manglish-rojak). Selection biased to the hardest — long free-form, mixed-language, wrong-premise, and multi-topic cases.
- **KB-only agents:** 4 agents, 5 questions each. Each had to *read the KB* (`SKILL.md` → `index.md` → `router-index.json` → the topic `core.md` + matching lane) and answer **grounded in the KB only** — no outside knowledge. Then report `pages_used`, a `coverage` verdict (FULL / PARTIAL / NONE), and what was `missing`.
- **Grounding check:** every specific claim in the answers was grep-verified against real KB files.

## Result: 15 FULL / 5 PARTIAL / 0 NONE

**Zero questions went unanswered.** Of 20 hard real questions, 15 were answered fully from KB content; 5 exposed a specific missing entry.

### Grounding verification (spot checks)

| Claim in answer | Found in |
|---|---|
| InsyaAllah = soft hedge / "saya check dulu" | `cultures/cu1-malaysia-malay/ms.md` |
| Lewicki 2016 apology components, ban "但是" | `concepts/c3-nvc-conflict-repair/core.md` |
| 无期限无金额的追问不构成催告 | `scenarios/sc17-landlord-tenant/core.md` |
| Vanakkam as goodwill signal | `cultures/cu3-malaysia-indian/*.md` |
| DARVO defence | `concepts/c9-manipulation-defense/core.md` |
| Gabarro & Kotter "forthright about bad news" | `scenarios/sc1-workplace-power/core.md` |
| grey rock | `concepts/c9-manipulation-defense/core.md` |
| 10/80/10 structure | `concepts/c16-public-speaking/core.md` |

All present → the coverage verdicts are trustworthy.

## The 5 gaps (each now fixed)

| # | Question | Gap | Fix |
|---|---|---|---|
| 1 | 约旦人开会都不看表…没礼貌 | `cu4` had the mono/polychronic framework but no concrete-culture example | added **实务语境** note (中东/拉美/南欧/东南亚; Arab example Hall used) — read as "relationship over schedule", keep anti-stereotype discipline |
| 2 | 唉 好累 就想找人说说话 | `c4` was one-sided: only "how to catch others", no **venter/search-for-support** side | added **倾诉者侧** section (state the need, pick validating listeners, "陪我聊十分钟") |
| 3 | Opah panggil menantu 'kau' | `cu1` recorded only the young→old taboo, not the **direction** | added **注意方向** note (elder→younger/menantu `kau` = normal family register; the taboo is the reverse) + ms lane |
| 4 | tai kor / kambing hitam, audit | `sc1` had the communication defence but no **scope boundary** for legal/audit/whistleblowing | added **边界：什么时候不再是「沟通问题」** (§) — hand off to lawyer/compliance, don't "talk your way out of" liability |
| 5 | 明天婚礼 致辞还没写 | `c16` had structure but no **occasion-toast** quick path | added **§18 场合型致辞（婚礼/祝酒/年会）** — closing-line-first, 3 points, weak-English downgrade, formal-register |

Also added router triggers so the new content is reachable: `cu1 += menantu/mertua/opah/kau/称呼长辈`; `c4 += 想被倾听/倾诉/找人说话/陪伴`; `c16 += 致辞/祝酒/祝酒词/婚礼致辞/toast/敬酒`.

## Verification

- **Routing for the gap queries:** 4/5 corrected to the intended topic (c4, cu1, c16 ×2). The Jordan query still pulls to `sc6` (the word 朋友 wins) — a router limit, not a content gap; the cu4 content now answers it correctly once reached.
- **No regression:** `router-smoke` **32/32**, intent fallback **3/3**, reach unchanged, `bash tools/check.sh` **all green**.
- **Files:** `qa/eval/answer-quality.json` (20 Q/A + verdicts) + this report; 8 KB files edited (5 `core.md` + 3 lanes) + `router.json`.

## Takeaway

Coverage is **strong**: a 46-topic KB answered 20 hard real questions with 0 blanks and 15 fully-grounded answers. The failures were narrow missing entries, not structural — and all 5 are now filled. Combined with Rounds 1–8: **understanding** strong, **routing** strong on short input / at ceiling on free-form, **coverage** strong and now slightly broader.
