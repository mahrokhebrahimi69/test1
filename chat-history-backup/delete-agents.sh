#!/usr/bin/env bash
# Permanently delete backed-up Cloud Agents from the Cursor account.
# Requires CURSOR_API_KEY from https://cursor.com/dashboard/api
# Usage:
#   export CURSOR_API_KEY=...
#   ./chat-history-backup/delete-agents.sh
# Optional:
#   SKIP_CURRENT=1  # skip this backup chat (default: 1)
#   DRY_RUN=1       # print requests only

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CATALOG="$SCRIPT_DIR/2026-08-02/catalog.json"
CURRENT_BC_ID="bc-c6224a15-ac68-4eeb-8d95-b0ff9a16fc1f"
SKIP_CURRENT="${SKIP_CURRENT:-1}"
DRY_RUN="${DRY_RUN:-0}"

if [[ -z "${CURSOR_API_KEY:-}" ]]; then
  echo "ERROR: set CURSOR_API_KEY first (https://cursor.com/dashboard/api)" >&2
  exit 1
fi

if [[ ! -f "$CATALOG" ]]; then
  echo "ERROR: catalog not found: $CATALOG" >&2
  exit 1
fi

mapfile -t BC_IDS < <(python3 -c 'import json,sys; from pathlib import Path; data=json.loads(Path(sys.argv[1]).read_text());
[print(a["bcId"]) for a in data["agents"]]' "$CATALOG")

deleted=0
skipped=0
failed=0

for bc in "${BC_IDS[@]}"; do
  if [[ "$SKIP_CURRENT" == "1" && "$bc" == "$CURRENT_BC_ID" ]]; then
    echo "SKIP (current chat): $bc"
    skipped=$((skipped + 1))
    continue
  fi

  url="https://api.cursor.com/v1/agents/$bc"
  if [[ "$DRY_RUN" == "1" ]]; then
    echo "DRY_RUN DELETE $url"
    continue
  fi

  code=$(curl -sS -o /tmp/cursor-delete-agent.out -w "%{http_code}" \
    -X DELETE "$url" -u "${CURSOR_API_KEY}:") || true
  if [[ "$code" == "200" || "$code" == "204" || "$code" == "404" ]]; then
    echo "OK ($code): $bc"
    deleted=$((deleted + 1))
  else
    echo "FAIL ($code): $bc" >&2
    cat /tmp/cursor-delete-agent.out >&2 || true
    echo >&2
    failed=$((failed + 1))
  fi
done

echo
echo "done. deleted/ok=$deleted skipped=$skipped failed=$failed"
if [[ "$failed" -gt 0 ]]; then
  exit 2
fi
