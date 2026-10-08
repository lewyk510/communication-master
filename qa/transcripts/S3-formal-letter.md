# QA dry-run — S3 formal-letter (SC4) | KB: communication-master | 2026-10-07

## 1. User message (verbatim, en lane)

> I bought a prepaid SIM card in Malaysia. The shop never told me about any validity
> period. I topped it up but the line still doesn't work, and when I asked for a refund
> the telco refused. Please write me a formal complaint/appeal letter I can actually send.

## 2. Router resolution (per `wiki/synthesis/00-how-to-use.md` §b–§c)

- `always_load`: `wiki/synthesis/00-how-to-use.md`. Language: English → en lane (`lang_default: "auto"`).
- Trigger matches (verified by grep against `router.json`):
  - `"complaint"` → entries **p3-formal-writing** (triggers include `"投诉"`, `"申诉"`, `"申请信"`, `"邮件"`, `"正式信"`, `"complaint"`, `"appeal"`, `"formal letter"`, `"refund"`, `"surat rasmi"`) AND **sc9-live-service** (triggers include `"客服"`, `"投诉"`, `"退货"`, `"customer service"`, `"complaint"`, ...)
  - `"refund"` → **p3-formal-writing**
  - `"formal letter"` → **p3-formal-writing**
- Best-scoring entry: **p3-formal-writing** (3 trigger hits) + direct engine dispatch: `router.json` `"engines": {"S3": "wiki/playbooks/p3-formal-writing/"}`.
- Sector routing note resolved from KB: prepaid SIM = telco/comms dispute → MCMC/CFM rung (`p3-formal-writing/core.md` §5.2 explicitly states "S3 冻结输入（预付卡问题）走的正是 MCMC 路径").

## 3. Files loaded

| # | Path | Role |
|---|------|------|
| 1 | `wiki/synthesis/00-how-to-use.md` | always_load |
| 2 | `wiki/playbooks/p3-formal-writing/core.md` | S3 engine: skeleton, demand template, escalation ladder, §8.1 complaint skel |
| 3 | `wiki/playbooks/p3-formal-writing/en.md` | en lane: register + full-skeleton entries |
| 4 | `wiki/scenarios/sc9-live-service/core.md` | co-matched; Fact–Impact–Ask + regulator map + TTPM details |

## 4. Answer — paste-ready letter (en lane)

> Sample values (RM60, receipt #A001, ticket #T-772) are the KB's own `constructed example` values (`p3-formal-writing/en.md`, "Complaint letter — full skeleton"). Replace them with your real data before sending.

```text
From: {{Your Name}}, {{address}}, {{phone}}, {{email}}
To: Customer Experience Manager, {{Telco}} Sdn Bhd, {{company address}}
Date: 2026-10-07

Subject: Formal Complaint — Prepaid SIM RM60 unusable — Receipt #A001 — Refund demanded

Dear Customer Experience Manager,

1. On 2026-09-01 I purchased a prepaid SIM from your dealer for RM60
   (Annex A: receipt #A001). Validity was never disclosed at sale or top-up.
2. On 2026-09-10 a RM60 top-up failed to deliver service; the line remained
   unusable (Annex B: screenshots, dated).
3. The service I paid for was not delivered as agreed (Annex C: purchase terms).
4. I contacted your team on 2026-09-12 (ticket #T-772) and again on 2026-09-24
   (ticket #T-810); on 2026-09-28 your agent refused the refund by phone. Neither
   ticket has received a written answer.

I am requesting a full refund of RM60, paid via cash/top-up on 2026-09-10,
within fourteen (14) days of this letter. Failing which, I will lodge a complaint
via the MCMC Consumer Redress Portal (aduan.mcmc.gov.my, 1800-188-030) and, if
necessary, file a claim at the Tribunal for Consumer Claims Malaysia (TTPM)
without further reference to you.
I remain open to an amicable resolution within that period.

Enclosures:
  Annex A — Receipt #A001 (RM60, dated 2026-09-01)
  Annex B — Evidence of non-delivery (screenshots, dated)
  Annex C — Purchased terms / starter-pack insert
  Annex D — Correspondence timeline: tickets #T-772, #T-810, phone log 2026-09-28

Yours faithfully,
{{Your Name}}
```

### Structure note (why the letter is built this way — all from the KB)

- **Seven-element skeleton**: sender / recipient / date / subject / body / demand / enclosures — "`Reference numbers 是正式信的灵魂`" (`p3-formal-writing/core.md` §1); forgetting the reference in the Subject line is "the #1 cause of 'we cannot locate your file'" (`p3-formal-writing/en.md`, "The seven-element skeleton"). `Practice heuristic` + `constructed example`
- **Demand = one action + amount + deadline**: template "I am requesting a full refund of RM [___] … If the refund is not processed within [14] days …" (`core.md` §2), grounded `Evidence-backed` in the FTC sample-letter capture ("tell the business what you want, like a refund … polite and reasonable"). One primary demand only — a second ask lets the provider "挑最便宜的那条回你". `Practice heuristic`
- **Firm-but-polite register**: neutral verb "The service was not delivered as agreed" (`core.md` §4 register table), no emotional adjectives; the only threat dimension is escalation. Closing line "I remain open to an amicable resolution" placed **after** the deadline, as `core.md` §4.4 requires. `Practice heuristic` (FTC-aligned)
- **Escalation ladder (Malaysia), ≥2 rungs** — provider first, then regulator, then tribunal:
  1. Provider complaints unit, in writing, obtain complaint ref (rung 1) — `sc9-live-service/core.md` §2.
  2. **MCMC / CFM** (telco sector): aduan.mcmc.gov.my, 1800-188-030, aduan@cfm.my — `p3-formal-writing/core.md` §5.2, `Evidence-backed` (CFM FAQ capture).
  3. **TTPM** (Tribunal for Consumer Claims, KPDN): Borang 1 ×4 copies, RM5.00 filing fee, respondent files Borang 2 within 14 days, hotline 1-800-88-9811 — `core.md` §5.1, `Evidence-backed` (TTPM procedure capture); eligibility note from `sc9-live-service/core.md` §8: consumer claims under Akta 599 up to RM50,000, within 3 years.
  - Timing rhythm (Day 0 / 7 / 14 / 21–30 follow-up table): `core.md` §7. `Practice heuristic`
- **What the KB is silent on**: it does not state which statute makes non-disclosure of validity unlawful, so the letter asserts breach only at the contract/service level ("not delivered as agreed") — do not cite a legal section the KB cannot trace.

## 5. Citation block

| KB file | Quoted line (verbatim) | Supports | Label |
|---|---|---|---|
| `wiki/synthesis/00-how-to-use.md` | "S3 \| Compose：正式写作（投诉/申诉/申请/婉拒/谈判邮件）\| `wiki/playbooks/p3-formal-writing/`" | engine routing | Evidence-backed (KB rule) |
| `wiki/playbooks/p3-formal-writing/core.md` | "Demand 诉求：一个具体动作 + 一个具体金额 + 一个具体期限" | demand block | Evidence-backed (KB spec; FTC trace) |
| `wiki/playbooks/p3-formal-writing/core.md` | "网上投诉门户：**https://aduan.mcmc.gov.my/**（MCMC Consumer Redress Portal）" | escalation rung 2 | Evidence-backed (CFM capture) |
| `wiki/playbooks/p3-formal-writing/core.md` | "填 **4 份 Borang 1** … **挂号费 RM5.00**" | escalation rung 3 | Evidence-backed (TTPM capture) |
| `wiki/playbooks/p3-formal-writing/en.md` | "Subject: Formal Complaint — Prepaid SIM RM60 unusable — Receipt #A001 — Refund demanded" | subject line + sample values | constructed example |
| `wiki/playbooks/p3-formal-writing/en.md` | "Validity was never disclosed at sale or top-up." | body fact sentence | constructed example |
| `wiki/scenarios/sc9-live-service/core.md` | "3. **书面正式投诉**（email/信函）——S3 场景：给期限（通常 7–14 天），声明"若逾期未解决，我将向 regulator 投诉"。" | ladder rung 1 | Practice heuristic |
| `wiki/scenarios/sc9-live-service/core.md` | "金额不超过 **RM50,000**；事由发生在索赔前 **3 年内**。" | TTPM eligibility | Evidence-backed |

## 6. SC4 statement

No external search; regulator names, fees, deadlines, subject lines and body sentences all trace to the `wiki/` paths quoted in §5 (raw captures: `raw/p3-formal-writing/f-ttpm-prosedur.md`, `f-bnm-complaint.md`, `f-cfm-faq.md`, `f-ftc-complaint-letter.md`, referenced through the topic files).

**Verdict: PASS** — end-to-end letter with sender/recipient/date/subject/body/concrete refund demand ✓；escalation ladder with provider → MCMC/CFM → TTPM rungs ✓；structure and phrasing citations to existing `wiki/` paths ✓；letter composed in the en lane (natively authored, per `p3-formal-writing/en.md` lane header) ✓。
