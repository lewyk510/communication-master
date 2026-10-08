#!/usr/bin/env bash
# One command for the full health check of the communication-master KB:
#   lint      -> structure: frontmatter, entry floors, sources, raw counts
#   smoke     -> recall: curated phrasings resolve to the right topics
#   freshness -> currency: capture dates / tiers, what is due for a re-crawl
set -euo pipefail
cd "$(dirname "$0")/.."

echo "== lint =="
python3 tools/lint_kb.py

echo "== router-index (compact matching index in sync) =="
python3 tools/build_router_index.py --check

echo "== cards (digest cards in sync) =="
python3 tools/build_cards.py --check

echo "== router-smoke =="
python3 qa/router-smoke.py

echo "== resolver (ask.py end-to-end) =="
python3 tools/ask.py --json --no-cache "潜台词是什么意思" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); assert d.get('id')=='p2-subtext-decoder', d; print('resolver: OK ->', d['id'])"

echo "== freshness =="
python3 tools/freshness.py

echo "== token cost (advisory) =="
python3 tools/token_cost.py

echo "== all checks passed =="
