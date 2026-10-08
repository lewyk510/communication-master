#!/bin/bash
# Jina reader fetch wrapper for communication-master.
# usage: tools/f.sh <topic-id> <slug> <url>
#
# Fetches <url> as markdown via https://r.jina.ai and saves it to
# raw/<topic-id>/f-<slug>.md, then prints:
#   === <slug> | <lines> lines | <bytes> bytes ===
set -euo pipefail

if [ $# -ne 3 ]; then
  echo "usage: f.sh <topic-id> <slug> <url>" >&2
  exit 2
fi

topic_id="$1"
slug="$2"
url="$3"

: "${JINA_API_KEY:?JINA_API_KEY is not set}"

root="/root/.agents/skills/communication-master"
outfile="$root/raw/$topic_id/f-$slug.md"
mkdir -p "$root/raw/$topic_id"

curl -s "https://r.jina.ai/$url" \
  -H "Authorization: Bearer $JINA_API_KEY" \
  -H "X-Return-Format: markdown" \
  -o "$outfile" \
  --max-time 90

echo "=== $slug | $(wc -l < "$outfile") lines | $(wc -c < "$outfile") bytes ==="
