#!/usr/bin/env bash
# Bootstrap: runs the popular GitHub frameworks prompt in batches until all
# candidates have been processed (ingested or rejected).
#
# Each hermes chat run handles --limit 20 candidates. This script loops until a
# full run produces no new source files and no new rejections, which means
# the filter returned an empty list.
#
# Usage: ./scripts/ingest_all.sh [prompt_file]
#   Default prompt: prompts/github_frameworks_popular.md

set -euo pipefail

PROMPT="${1:-/home/simon/documents/ai-researcher/prompts/github_frameworks_popular.md}"
SOURCES="/home/simon/documents/ai-researcher/sources"
REJECTED="/home/simon/documents/ai-researcher/scripts/github_rejected.json"

rejected_count() {
  python3 -c "import json; print(len(json.load(open('$REJECTED'))))" 2>/dev/null || echo 0
}

batch=1
while true; do
  echo "=== Batch $batch ==="
  before_files=$(ls "$SOURCES"/github-*.md 2>/dev/null | wc -l)
  before_rejected=$(rejected_count)

  hermes chat --cli -Q --yolo -q "$(cat "$PROMPT")"

  after_files=$(ls "$SOURCES"/github-*.md 2>/dev/null | wc -l)
  after_rejected=$(rejected_count)

  new_files=$(( after_files - before_files ))
  new_rejected=$(( after_rejected - before_rejected ))
  echo "  +$new_files file(s), +$new_rejected rejection(s)"

  if [ "$new_files" -eq 0 ] && [ "$new_rejected" -eq 0 ]; then
    echo "No progress — filter returned empty. Ingestion complete."
    break
  fi

  batch=$(( batch + 1 ))
done
