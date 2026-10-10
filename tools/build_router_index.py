#!/usr/bin/env python3
"""Build router-index.json — a compact, minified matching index.

router.json is the source of truth but is big to load every query (pretty
printed, and it carries paths/title/see_also that matching does not need).
router-index.json keeps only what matching needs (id + dir + scenarios +
triggers) plus the matcher config, minified — roughly 1/3 the tokens.

The resolver: match against router-index.json -> open the winner's `dir`.
The full router.json is still the source of truth for patches/lint.

Usage (from the skill root):
    python3 tools/build_router_index.py           # write router-index.json
    python3 tools/build_router_index.py --check    # exit 1 if stale (CI)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "router.json"
OUT = ROOT / "router-index.json"


def build(src: dict) -> dict:
    m = src.get("matcher", {})
    index = {
        "version": src.get("version", 1),
        "lang_default": src.get("lang_default", "auto"),
        "always_load": src.get("always_load", []),
        "engines": src.get("engines", {}),
        "intents": src.get("intents", {}),
        "matcher": {
            "latin": m.get("latin", "case-insensitive word-boundary match"),
            "cjk": m.get("cjk", "substring match"),
            "scoring": ("sum of matched trigger lengths; medium_tokens count +1; "
                        "case-insensitive; highest wins; ties -> earlier entry"),
            "medium_tokens": m.get("medium_tokens", []),
        },
        "fallback": "zero trigger hits -> load index.md + 00-how-to-use.md, ask ONE clarifying question",
        "entries": [
            {
                "id": e["id"],
                "dir": str(Path(e["paths"]["core"]).parent) if e.get("paths", {}).get("core") else "",
                "scenarios": e.get("scenarios", []),
                "triggers": e.get("triggers", []),
            }
            for e in src.get("entries", [])
        ],
    }
    return index


def render(index: dict) -> str:
    # minified: no indentation, tight separators
    return json.dumps(index, ensure_ascii=False, separators=(",", ":"))


def main() -> int:
    src = json.loads(SRC.read_text(encoding="utf-8"))
    text = render(build(src))

    if "--check" in sys.argv:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != text:
            print("router-index: STALE — run python3 tools/build_router_index.py")
            return 1
        print("router-index: in sync")
        return 0

    OUT.write_text(text, encoding="utf-8")
    print(f"router-index: wrote {OUT.name} ({len(text):,} bytes, "
          f"{len(build(src)['entries'])} entries)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
