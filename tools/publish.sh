#!/usr/bin/env bash
# Publish the public/development repo from this working tree.
#
# The public repo is the same skill WITHOUT raw/ — that directory holds
# third-party web captures whose redistribution is not licensed. Files are
# overlaid onto a persistent clone of the public repo so its history (and any
# community commits/PRs) is preserved rather than force-pushed away.
#
# Usage:
#   ./tools/publish.sh [remote]     # default remote: public
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"

remote="${1:-public}"
work="${PUBLISH_DIR:-/tmp/communication-master-public}"
puburl="$(git remote get-url "$remote" 2>/dev/null || true)"
[ -n "$puburl" ] || { echo "publish: no '$remote' remote — add it: git remote add $remote <url>"; exit 1; }

if [ -d "$work/.git" ]; then
  git -C "$work" pull --ff-only -q origin main 2>/dev/null || true
else
  rm -rf "$work"
  git clone -q "$puburl" "$work" 2>/dev/null || { mkdir -p "$work"; git -C "$work" init -q -b main; git -C "$work" remote add origin "$puburl"; }
fi

n=0
while IFS= read -r -d '' f; do
  case "$f" in raw/*) continue ;; esac
  mkdir -p "$work/$(dirname "$f")"
  cp -p "$f" "$work/$f"
  n=$((n + 1))
done < <(git ls-files -z)

cd "$work"
if git rev-parse -q --verify HEAD >/dev/null 2>&1 && [ -z "$(git status --porcelain)" ]; then
  echo "publish: no changes to publish"
  exit 0
fi
git add -A
git -c user.name=lewyk510 -c user.email=lewyk510@users.noreply.github.com \
    commit -q -m "publish: sync public snapshot ($(date +%Y-%m-%d))"
git push -q origin main
echo "publish: pushed $n file(s) -> $puburl"
