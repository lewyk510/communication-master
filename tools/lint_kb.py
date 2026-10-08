#!/usr/bin/env python3
"""communication-master KB linter + reindexer. Python stdlib only."""
# allow: SIZE_OK — task contract delivers exactly one linter file; lint and
# reindex halves are independently separable if it ever grows further.
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"
ROUTER = ROOT / "router.json"
INDEX = ROOT / "index.md"

CLUSTERS = {
    "concepts": "Concepts",
    "scenarios": "Scenarios",
    "cultures": "Cultures",
    "playbooks": "Playbooks",
    "synthesis": "Synthesis",
}
LANES = ("core.md", "zh.md", "en.md", "ms.md")
FLOORS = {"core.md": 10, "zh.md": 10, "en.md": 8, "ms.md": 8}
EXPECTED = {
    "concepts": [f"c{i}" for i in range(1, 19)],
    "scenarios": [f"sc{i}" for i in range(1, 20)],
    "cultures": [f"cu{i}" for i in range(1, 6)],
    "playbooks": [f"p{i}" for i in range(1, 5)],
}
MIN_RAW_FILES = 3
MIN_SOURCE_URLS = 3
MIN_FILE_BYTES = 200
MARKERS = ("TODO", "PLACEHOLDER", "<fill", "TBD")
REQUIRED_FM_KEYS = {"id", "title", "type", "lang", "sources"}
FM_KEY = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*)\s*:(.*)$")
SOURCES_HEADING = re.compile(r"^##[ \t]+Sources", re.MULTILINE)
ENTRY_HEADING = re.compile(r"^### ", re.MULTILINE)
URL = re.compile(r"https?://[^\s)\]>\"']+")


def parse_frontmatter(text: str) -> dict[str, str] | None:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    fm: dict[str, str] = {}
    closed = False
    for line in lines[1:]:
        if line.strip() == "---":
            closed = True
            break
        m = FM_KEY.match(line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm if closed else None


def find_topics() -> dict[str, Path]:
    topics: dict[str, Path] = {}
    for cluster in CLUSTERS:
        cdir = WIKI / cluster
        if not cdir.is_dir():
            continue
        for tdir in sorted(cdir.iterdir()):
            if tdir.is_dir():
                topics[tdir.name] = tdir
    return topics


def check_expected_folders(topics: dict[str, Path]) -> int:
    fails = 0
    for cluster, shorts in EXPECTED.items():
        for short in shorts:
            if not any(t.startswith(f"{short}-") for t in topics if t.startswith(f"{short}-")):
                print(f"[FAIL] expected topic folder '{short}-*' under wiki/{cluster}/")
                fails += 1
    return fails


def check_lane_file(path: Path) -> int:
    fails = 0
    rel = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8", errors="replace")

    fm = parse_frontmatter(text)
    if fm is None:
        print(f"[FAIL] frontmatter: no closed '---' block -> {rel}")
        fails += 1
    else:
        missing = sorted(REQUIRED_FM_KEYS - set(fm))
        if missing:
            print(f"[FAIL] frontmatter: missing keys {missing} -> {rel}")
            fails += 1
        else:
            print(f"[PASS] frontmatter -> {rel}")

    m = SOURCES_HEADING.search(text)
    if m is None:
        print(f"[FAIL] sources: no '## Sources' heading -> {rel}")
        fails += 1
    else:
        n_urls = len(set(URL.findall(text[m.end():])))
        if n_urls < MIN_SOURCE_URLS:
            print(f"[FAIL] sources: {n_urls} distinct URL(s) after '## Sources', need >= {MIN_SOURCE_URLS} -> {rel}")
            fails += 1
        else:
            print(f"[PASS] sources: {n_urls} distinct URLs -> {rel}")

    n_entries = len(ENTRY_HEADING.findall(text))
    floor = FLOORS[path.name]
    if n_entries < floor:
        print(f"[FAIL] entries: {n_entries} '### ' heading(s), need >= {floor} -> {rel}")
        fails += 1
    elif path.stat().st_size < MIN_FILE_BYTES:
        print(f"[FAIL] entries: floor met but file < {MIN_FILE_BYTES} bytes (suspicious) -> {rel}")
        fails += 1
    else:
        print(f"[PASS] entries: {n_entries} -> {rel}")
    return fails


def check_topic(tid: str, tdir: Path) -> int:
    fails = 0
    rel = tdir.relative_to(ROOT).as_posix()
    for lane in LANES:
        path = tdir / lane
        if not path.is_file():
            print(f"[FAIL] files: missing {lane} -> {rel}")
            fails += 1
            continue
        fails += check_lane_file(path)

    if not RAW.is_dir():
        return fails  # public build: raw/ (third-party captures) is omitted by design
    raw_dir = RAW / tid
    if not raw_dir.is_dir():
        print(f"[FAIL] raw: folder absent -> raw/{tid}")
        fails += 1
    else:
        n = sum(1 for p in raw_dir.iterdir() if p.is_file())
        if n < MIN_RAW_FILES:
            print(f"[FAIL] raw: {n} file(s), need >= {MIN_RAW_FILES} -> raw/{tid}")
            fails += 1
        else:
            print(f"[PASS] raw: {n} file(s) -> raw/{tid}")
    return fails


def check_markers(paths: list[Path]) -> int:
    fails = 0
    for p in paths:
        text = p.read_text(encoding="utf-8", errors="replace")
        rel = p.relative_to(ROOT).as_posix()
        for marker in MARKERS:
            if marker in text:
                print(f"[FAIL] marker {marker!r} found -> {rel}")
                fails += 1
    if fails == 0 and paths:
        print(f"[PASS] markers: none of {MARKERS} in {len(paths)} wiki file(s)")
    return fails


def check_router(topic_id: str | None = None) -> int:
    if not ROUTER.is_file():
        print("[SKIP] router: router.json absent (created by parallel task; skipped gracefully)")
        return 0
    try:
        data = json.loads(ROUTER.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"[FAIL] router: invalid JSON ({exc}) -> router.json")
        return 1
    entries = data.get("entries") if isinstance(data, dict) else None
    if not isinstance(entries, list):
        print("[FAIL] router: missing entries[] list -> router.json")
        return 1
    fails = 0
    n_paths = 0
    for i, entry in enumerate(entries):
        if not isinstance(entry, dict):
            continue
        if topic_id is not None and entry.get("id") != topic_id:
            continue
        paths = entry.get("paths") or []
        if isinstance(paths, dict):
            candidates = list(paths.values())
        elif isinstance(paths, list):
            candidates = paths
        else:
            candidates = [paths]
        for p in candidates:
            if not isinstance(p, str):
                continue
            n_paths += 1
            if not (ROOT / p).exists():
                print(f"[FAIL] router: path missing on disk -> {p} (entries[{i}] id={entry.get('id')})")
                fails += 1
    if fails == 0:
        print(f"[PASS] router: {n_paths} path(s) exist on disk")
    return fails


def cmd_lint(topic_id: str | None) -> int:
    topics = find_topics()
    if topic_id is not None:
        if topic_id not in topics:
            known = ", ".join(sorted(topics)) or "none"
            print(f"lint: unknown topic '{topic_id}' (known topics: {known})")
            return 2
        selected = {topic_id: topics[topic_id]}
    else:
        selected = topics

    fails = 0
    if not RAW.is_dir():
        print("[NOTE] raw/ absent — public build; skipping raw-capture checks")
    if topic_id is None:
        fails += check_expected_folders(topics)
    for tid, tdir in selected.items():
        fails += check_topic(tid, tdir)
    md_scope = sorted({p for tdir in selected.values() for p in tdir.rglob("*.md")})
    fails += check_markers(md_scope)
    fails += check_router(topic_id)
    print(f"lint: {len(selected)} topic(s) checked, {fails} failure(s)")
    return 1 if fails else 0


def merge_router_patches() -> None:
    patches = sorted(WIKI.rglob("router-patch.json"))
    if not patches:
        print("reindex: no router-patch.json found")
        return
    if ROUTER.is_file():
        data = json.loads(ROUTER.read_text(encoding="utf-8"))
    else:
        data = {"entries": []}
        print("reindex: router.json absent, starting a fresh one")
    entries = data.get("entries") if isinstance(data, dict) else None
    if not isinstance(entries, list):
        print("reindex: router.json has no entries[] list; merge aborted")
        return

    for pp in patches:
        rel = pp.relative_to(ROOT).as_posix()
        try:
            patch = json.loads(pp.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            print(f"reindex: skip invalid patch ({exc}) -> {rel}")
            continue
        if not isinstance(patch, dict) or "id" not in patch:
            print(f"reindex: skip patch without 'id' -> {rel}")
            continue
        idx = next(
            (i for i, e in enumerate(entries) if isinstance(e, dict) and e.get("id") == patch["id"]),
            None,
        )
        if "op" in patch:
            op, fields = patch["op"], patch.get("set") or {}
            if op == "remove":
                if idx is not None:
                    entries.pop(idx)
            elif op in ("add", "update"):
                if idx is None:
                    entries.append({**fields, "id": patch["id"]})
                else:
                    entries[idx] = {**entries[idx], **fields, "id": patch["id"]}
            else:
                print(f"reindex: unknown op {op!r} -> {rel}")
                continue
        elif idx is None:
            entries.append(patch)
        else:
            entries[idx] = patch
        print(f"reindex: merged -> {rel}")

    ROUTER.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def cmd_reindex() -> int:
    sections: dict[str, list[str]] = {c: [] for c in CLUSTERS}
    for cluster in CLUSTERS:
        cdir = WIKI / cluster
        if not cdir.is_dir():
            continue
        if cluster == "synthesis":
            # synthesis pages are flat .md files, not topic folders
            for page in sorted(cdir.glob("*.md")):
                fm = parse_frontmatter(page.read_text(encoding="utf-8", errors="replace")) or {}
                tid = fm.get("id") or page.stem
                title = fm.get("title") or page.stem
                typ = fm.get("type") or "synthesis"
                rel = page.relative_to(ROOT).as_posix()
                sections[cluster].append(f"| {tid} | [{title}]({rel}) | {typ} |")
            continue
        for tdir in sorted(p for p in cdir.iterdir() if p.is_dir()):
            core = tdir / "core.md"
            if not core.is_file():
                print(f"reindex: skip (no core.md) -> wiki/{cluster}/{tdir.name}")
                continue
            fm = parse_frontmatter(core.read_text(encoding="utf-8", errors="replace")) or {}
            tid = fm.get("id") or tdir.name
            title = fm.get("title") or tdir.name
            typ = fm.get("type") or cluster.rstrip("s")
            rel = core.relative_to(ROOT).as_posix()
            sections[cluster].append(f"| {tid} | [{title}]({rel}) | {typ} |")

    lines = [
        "# communication-master — index",
        "",
        "Auto-generated by `tools/lint_kb.py reindex`. Do not hand-edit.",
        "",
    ]
    for cluster, label in CLUSTERS.items():
        lines += [f"## {label}", "", "| id | title | type |", "|---|---|---|"]
        lines += sections[cluster]
        lines.append("")
    INDEX.write_text("\n".join(lines), encoding="utf-8")
    total = sum(len(v) for v in sections.values())
    print(f"reindex: wrote index.md ({total} topics)")

    merge_router_patches()
    if ROUTER.is_file():
        try:
            json.loads(ROUTER.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            print(f"reindex: router.json INVALID after merge: {exc}")
            return 1
        print("reindex: router.json valid JSON")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="communication-master KB linter + reindexer")
    ap.add_argument("--topic", help="lint a single topic id (e.g. c1-subtext-implicature)")
    ap.add_argument("command", nargs="?", choices=["reindex"], help="reindex: regenerate index.md and merge router-patch.json files")
    args = ap.parse_args()
    if args.command == "reindex":
        return cmd_reindex()
    return cmd_lint(args.topic)


if __name__ == "__main__":
    sys.exit(main())
