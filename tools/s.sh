#!/bin/bash
# Serper search wrapper for communication-master.
# usage: tools/s.sh <topic-id> <name> <query...> [gl] [hl]
#
#   <topic-id>  raw folder name, e.g. c1-subtext-implicature (created if missing)
#   <name>      output basename -> raw/<topic-id>/<name>.json
#   <query...>  search query (quote it: "how to decline politely")
#   [gl] [hl]   optional trailing ge/locale codes; popped from the end only if
#               each matches ^[a-z]{2}$ AND popping never leaves an empty query.
#               Defaults: gl=my hl=en. Env override: SERPER_GL / SERPER_HL.
#
# Output: saves full Serper JSON to raw/<topic-id>/<name>.json and prints a
# digest: each organic result's title/link/first-300-chars snippet, plus
# answerBox / knowledgeGraph when present.
set -euo pipefail

if [ $# -lt 3 ]; then
  echo "usage: s.sh <topic-id> <name> <query...> [gl] [hl]" >&2
  exit 2
fi

topic_id="$1"; shift
name="$1"; shift

gl="${SERPER_GL:-my}"
hl="${SERPER_HL:-en}"

# Pop trailing [hl] then [gl] (2-letter codes); never consume the whole query.
if [ $# -gt 1 ] && [[ "${!#}" =~ ^[a-z]{2}$ ]]; then
  hl="${!#}"
  set -- "${@:1:$#-1}"
fi
if [ $# -gt 1 ] && [[ "${!#}" =~ ^[a-z]{2}$ ]]; then
  gl="${!#}"
  set -- "${@:1:$#-1}"
fi

if [ $# -lt 1 ]; then
  echo "s.sh: query must not be empty" >&2
  exit 2
fi
q="$*"

: "${SERPER_API_KEY:?SERPER_API_KEY is not set}"

root="/root/.agents/skills/communication-master"
outdir="$root/raw/$topic_id"
outfile="$outdir/$name.json"
mkdir -p "$outdir"

body="$(python3 -c 'import json,sys;print(json.dumps({"q":sys.argv[1],"num":10,"gl":sys.argv[2],"hl":sys.argv[3]}))' "$q" "$gl" "$hl")"

curl -s -X POST https://google.serper.dev/search \
  -H "X-API-KEY: $SERPER_API_KEY" -H "Content-Type: application/json" \
  -d "$body" \
  -o "$outfile"

python3 - "$outfile" "$name" <<'PY'
import json, sys
path, name = sys.argv[1], sys.argv[2]
try:
    with open(path, encoding="utf-8") as fh:
        d = json.load(fh)
except Exception as e:
    print(f"{name} PARSE_ERR {e}")
    raise SystemExit(1)
if "error" in d:
    print(f"{name} API_ERROR: {d['error']}")
    raise SystemExit(1)
print(f"### {name}")
for o in d.get("organic", []):
    print(f"- {o.get('title')}\n  {o.get('link')}\n  {o.get('snippet', '')[:300]}")
if d.get("answerBox"):
    print("ANSWERBOX:", str(d["answerBox"])[:400])
if d.get("knowledgeGraph"):
    print("KG:", str(d["knowledgeGraph"])[:300])
print()
PY
