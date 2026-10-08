#!/usr/bin/env python3
"""Build sidecars/cards.json — a compact per-topic digest ("digest cards").

RAPTOR-style summary level made cheap: for each topic, a card with the title, a
short TL;DR (the core.md overview paragraph) and the list of entry headings
(the topic's table of contents). The agent can answer light questions or decide
"do I need this?" from a ~150-300 token card instead of loading the ~5.8k-token
core.md plus a language lane. Escalate to the topic folder when the card is not
enough. Regenerate whenever content changes (check.sh --check guards drift).

Usage (from the skill root):
    python3 tools/build_cards.py           # write sidecars/cards.json
    python3 tools/build_cards.py --check    # exit 1 if stale
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "router.json"
OUT = ROOT / "sidecars" / "cards.json"

FM = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
H1 = re.compile(r"^#\s+(.*)$", re.MULTILINE)
H3 = re.compile(r"^###\s+(.+)$", re.MULTILINE)
URL = re.compile(r"https?://[^\s)\]>\"']+")


def first_paragraph(text: str) -> str:
    # drop frontmatter + H1, then the first non-empty block before any heading
    body = FM.sub("", text, count=1)
    lines = body.splitlines()
    # skip to after the first H1
    i = 0
    while i < len(lines) and not lines[i].startswith("# "):
        i += 1
    i += 1
    para: list[str] = []
    while i < len(lines):
        ln = lines[i].strip()
        if ln.startswith("#") or (ln == "" and para):
            break
        if ln:
            para.append(ln)
        i += 1
    return " ".join(para).strip()


def card_for(topic_dir: Path) -> dict:
    core = topic_dir / "core.md"
    text = core.read_text(encoding="utf-8", errors="ignore") if core.exists() else ""
    title = ""
    m = FM.search(text)
    if m:
        for line in m.group(1).splitlines():
            if line.startswith("title:"):
                title = line.split(":", 1)[1].strip().strip("'\"")
                break
    if not title:
        h = H1.search(text)
        title = h.group(1).strip() if h else topic_dir.name
    signals = [s.strip() for s in H3.findall(text)][:15]
    n_sources = len(set(URL.findall(text)))
    tldr = first_paragraph(text)
    if len(tldr) > 280:
        tldr = tldr[:277].rstrip() + "…"
    return {"title": title, "dir": str(topic_dir.relative_to(ROOT)),
            "tldr": tldr, "signals": signals, "sources": n_sources}


def build() -> dict:
    src = json.loads(SRC.read_text(encoding="utf-8"))
    cards = {}
    for e in src.get("entries", []):
        d = e.get("paths", {}).get("core")
        if not d:
            continue
        cards[e["id"]] = card_for((ROOT / d).parent)
    return {"version": 1, "cards": cards}


def render(obj: dict) -> str:
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))


def main() -> int:
    text = render(build())
    if "--check" in sys.argv:
        cur = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if cur != text:
            print("cards: STALE — run python3 tools/build_cards.py")
            return 1
        print("cards: in sync")
        return 0
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(text, encoding="utf-8")
    n = len(build()["cards"])
    print(f"cards: wrote {OUT.relative_to(ROOT)} ({len(text):,} bytes, {n} cards)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
