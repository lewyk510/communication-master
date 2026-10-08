#!/usr/bin/env bash
# Back up / migrate the communication-master KB.
#   ./tools/backup.sh push    -> push master to origin (needs a registered key/remote)
#   ./tools/backup.sh bundle  -> write a single-file git bundle (works offline)
#   ./tools/backup.sh         -> bundle, then push if origin exists
set -euo pipefail
cd "$(dirname "$0")/.."

mode="${1:-auto}"
stamp="$(date +%Y%m%d-%H%M%S)"
out_dir="${BACKUP_DIR:-$(pwd)/../communication-master-backups}"
mkdir -p "$out_dir"

bundle() {
  local f="$out_dir/communication-master-$stamp.bundle"
  git bundle create "$f" --all >/dev/null
  echo "bundle: $f"
  echo "  restore elsewhere:  git clone <that-file> communication-master"
}

push() {
  r="origin"
  if ! git remote get-url "$r" >/dev/null 2>&1 && git remote get-url private >/dev/null 2>&1; then
    r="private"
  fi
  if git remote get-url "$r" >/dev/null 2>&1; then
    git push "$r" HEAD
    git push "$r" --tags 2>/dev/null || true
    echo "pushed to '$r' ($(git remote get-url "$r"))"
  else
    echo "no backup remote — add one: git remote add private git@github.com:<you>/<repo>.git"
    return 1
  fi
}

case "$mode" in
  push) push ;;
  bundle) bundle ;;
  auto) bundle; push || true ;;
  *) echo "usage: $0 [push|bundle]"; exit 2 ;;
esac
