#!/usr/bin/env bash
set -euo pipefail

SOLUTIONS_DIR="Solutions"
REPO_ROOT="$(pwd)"

mapfile -t day_dirs < <(
    find "$SOLUTIONS_DIR" -maxdepth 1 -type d -name "Day*" \
    | sed 's/.*Day \([0-9]*\)/\1 &/' \
    | sort -n \
    | cut -d' ' -f2-
)

for day_dir in "${day_dirs[@]}"; do
    day_name=$(basename "$day_dir")
    echo "=== $day_name ==="

    cd "$REPO_ROOT/$day_dir"
    for script in *.py; do
        [ -e "$script" ] || continue
        echo "--- Running $script ---"
        python3 "$script"
        echo
    done
    cd "$REPO_ROOT"
done
