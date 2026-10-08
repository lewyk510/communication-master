# QA transcripts — dry-run proof index

KB: `communication-master` · Date: 2026-10-07 · Reference spec: `qa/scenarios.md` (FROZEN v1)

All four transcripts were produced with the KB as the only permitted reference (no external
search). Every claim in each transcript cites a `wiki/` path with a verbatim quoted line.
Trigger strings claimed as "matched" in each transcript were verified by grep against
`router.json` before writing. No file outside `qa/transcripts/` was created or modified.

| Transcript | Evidences | Verdict | Key evidence (quoted line + file path) |
|---|---|---|---|
| `S1-decode-subtext.md` | SC2 (router resolves a concrete message) + SC4a (KB-only S1 answer) | **PASS** | Phrase-table row "`你要加班吗？…你开心就好` \| 面子留出口、压力留给你 \| 官方退路=压力试探" — `wiki/playbooks/p2-subtext-decoder/core.md`; 3 readings + exactly 3 cited reply options from `wiki/playbooks/p2-subtext-decoder/zh.md`; router hits `什么意思`/`暗示`/`解码` → `engines.S1` |
| `S2-cross-cultural-ambiguity.md` | SC4 edge case (ambiguity ⇒ ask-first, no single culture reading) | **PASS** | "**永远不要**因为对方'是某国人'就直接输出单一读法。" — `wiki/cultures/cu4-cross-cultural-general/core.md`; 3 candidate readings + 5 verbatim questions from the S2 bank; `"怎么回"` → p1-reply-engine, `"cross-cultural"` → cu4 (both grepped in router.json) |
| `S3-formal-letter.md` | SC3/SC4b (formal letter completeness + regulator coverage) | **PASS** | "填 **4 份 Borang 1** … **挂号费 RM5.00**" — `wiki/playbooks/p3-formal-writing/core.md` §5.1; letter has sender/recipient/date/subject/body/concrete refund demand; ladder = provider → MCMC/CFM (aduan.mcmc.gov.my) → TTPM; `complaint`/`refund`/`formal letter` → `engines.S3` |
| `S4-ai-prompt.md` | SC4c (concrete prompt pattern + mechanism + citation) | **PASS** | "封闭式问题把它的「生成空间」压缩到可核查的是非输出，使绕圈在结构上不可能。" — `wiki/playbooks/p4-ai-prompting/core.md` §12; slotted pattern = §17-T6 verbatim + labelled `constructed example` English rendering; `prompt` → `engines.S4` |

## Pass criteria traceability (binary, per `qa/scenarios.md`)

- **SC2** — each transcript's §2 quotes the matched trigger strings and the resulting entry
  ids; each resolved `paths`/lane file was confirmed on disk before the transcript was written.
- **SC4** — each transcript's §6 states the KB-only condition; §5 gives one quoted line per
  cited file. Where the KB had no material (S1: the leader's 48-hour history; S3: statute
 -level breach claim), the transcript says "KB silent / not claimed" instead of inventing.
- **Lane discipline** — S1 answers in the zh lane (options quoted natively from
  `p2-subtext-decoder/zh.md`); S3 letter in the en lane; S4 renders the zh-native T6 only as
  a labelled `constructed example`, per the lane contract in `AGENTS.md`.
- **Labels** — every claim in the transcripts carries the KB's own labels:
  `Evidence-backed` / `Practice heuristic` / `constructed example` (and `anecdotal` where the
  KB's tier-3 sources are involved, e.g. the 百度百科 depiction of "你开心就好").

## Known limits (honest gaps, not failures)

- S2 is an edge-case transcript: the KB's own rule converts it into a question-asking turn,
  so the deliverable is candidate readings + targeted questions, not a final reply.
- S3 sample values (RM60, receipt #A001, tickets #T-772/#T-810) reuse the KB's own
  `constructed example` values and are marked as such in the transcript.
- These dry-runs exercise SC2/SC3/SC4 evidence; SC1 (lint passes) and SC5 (quickstart) are
  verified separately — `wiki/synthesis/00-how-to-use.md` contains the paste-ready quickstart
  block ("Paste-ready quickstart（SC5）").
