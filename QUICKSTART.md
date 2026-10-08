# Quickstart — invoke Communication Master in a new conversation

Paste-ready load instructions. No setup, no network, no code to run.

## 1. Load the skill (one line)

```
Load the skill `communication-master` (at /root/.agents/skills/communication-master/).
Use it for any "what does this person really mean?" or "how should I reply?" question.
```

If your agent has no skill loader, paste this instead:

```
Read /root/.agents/skills/communication-master/SKILL.md, then read
/root/.agents/skills/communication-master/wiki/synthesis/00-how-to-use.md.
Treat the second file as your resolution procedure for the rest of this conversation.
```

## 2. How the agent resolves your message (the router)

1. Load `wiki/synthesis/00-how-to-use.md` (always-load: procedure, confidence rules, ethics).
2. Match your message text against `router.json` → `entries[].triggers` (zh / en / ms keywords).
3. Load the top-matching topic folder: its `core.md` + **your** language lane (`zh.md` / `en.md` / `ms.md`).
4. If a structured task, use the matching engine:
   - **S1 · decode subtext** → `wiki/playbooks/p2-subtext-decoder/`
   - **S2 · draft a reply** → `wiki/playbooks/p1-reply-engine/`
   - **S3 · formal letter (complaint/appeal/application)** → `wiki/playbooks/p3-formal-writing/`
   - **S4 · AI / tool-website prompt** → `wiki/playbooks/p4-ai-prompting/`
5. If cross-cultural and ambiguous → **ask** the targeted questions in
   `wiki/cultures/cu4-cross-cultural-general/` before answering. Do not guess.

## 3. Copy-paste prompts that work

**Decode subtext (S1)**
```
Using communication-master, someone sent me: "你开心就好 😊"
Context: my manager, after I pushed back on a deadline.
What might they really mean? Give likely readings (ranked), the cues, and 3 reply options
in 中文. Cite the KB files you used.
```

**Draft a reply (S2)**
```
Using communication-master, help me reply. Situation: [who / relationship / power / goal].
Their message: "[paste]". My language: English.
Give 3 reply options (safe / warm / assertive) + what each risks. Cite the KB files used.
```

**Complaint / appeal letter (S3)**
```
Using communication-master, draft a formal complaint letter in English.
To: [company]. Issue: [facts]. Outcome I want: [remedy]. Tone: firm but civil.
Return a paste-ready letter + a short note on the structure you used. Cite the KB files used.
```

**AI / tool prompt (S4)**
```
Using communication-master, write a prompt that makes [AI tool / customer-service bot /
AI website] do [task]. Give the prompt + 2 variations + the failure modes to watch for.
Cite the KB files used.
```

## 4. Output contract (what a good answer looks like)

- **Names the readings / options**, ranked, with the cues or reasoning that produced them.
- **Cites KB files** (`wiki/...`) it used — so you can go deeper.
- **Respects confidence**: labels `Evidence-backed` vs `Practice heuristic` vs `constructed example`;
  says "I don't know" instead of inventing when the KB is silent.
- **Asks** in cross-cultural / ambiguous cases (S2) rather than stereotyping.
- Answers in **your** language lane (zh / en / ms), natively — not translated.

## 5. Sanity check (SC1 load test)

```
Load communication-master and tell me which file answers: "my Malay colleague said
' boleh, boleh' but didn't commit — what does that mean?" Then quote one line, with its path.
```

Expected: agent routes to a culture/scenario file (e.g. `wiki/cultures/cu1-malaysia-malay/`)
and quotes from it — proving the skill loads and the router locates a domain file.
