#!/usr/bin/env bash
set -euo pipefail

# research_loop.sh — Outer loop: topic select → agent select → pipeline → score update
# Single command to run the entire research system.

BASE="/data/.openclaw/workspace/finance_research"
LOG="$BASE/logs/research.log"
HEARTBEAT="/data/.openclaw/workspace/logs/research_heartbeat.json"
PIPELINE="$BASE/pipeline/run_iteration.sh"
TOPIC_SELECT="$BASE/topic_registry/select_topic.py"
AGENT_SELECT="$BASE/agent_selection/select_agents.py"
TOPIC_REGISTRY="$BASE/topic_registry/topic_registry.json"
AGENT_POOL="$BASE/agents/agent_pool.json"
AGENT_SCORES="$BASE/scoring/agent_scores.json"

# Create required directories
mkdir -p "$BASE"/{outputs,logs,knowledge_base/{concepts,relationships,frameworks,evidence}}

# Persistent iteration counter (survives restarts)
COUNTER_FILE="$BASE/logs/.iteration_counter"
if [ -f "$COUNTER_FILE" ]; then
    ITERATION=$(cat "$COUNTER_FILE")
else
    ITERATION=0
fi

SESSION_ID="loop_$$_$(date +%s)"

write_heartbeat() {
    local phase="$1" topic="${2:-}" status="${3:-running}" iter="${4:-$ITERATION}"
    python3 -c "
import json, time
from datetime import datetime, timezone
hb = {
    'timestamp': datetime.now(timezone.utc).isoformat(),
    'epoch': int(time.time()),
    'pid': $$,
    'session': '$SESSION_ID',
    'iteration': $iter,
    'phase': '$phase',
    'topic': '$topic',
    'status': '$status',
    'mode': 'ucb_curriculum_v4'
}
with open('$HEARTBEAT', 'w') as f:
    json.dump(hb, f, indent=2)
" 2>/dev/null || true
}

log_msg() {
    echo "$(date -Iseconds) | loop | $1" >> "$LOG"
}

# Signal handling for clean shutdown
RUNNING=true
trap 'RUNNING=false; log_msg "shutdown signal received"; exit 0' SIGTERM SIGINT

log_msg "=== Research Loop v4 Started | PID=$$ | session=$SESSION_ID ==="
echo $$ > "$BASE/logs/.loop_pid"
write_heartbeat "startup" "" "starting"

while $RUNNING; do
    ITERATION=$((ITERATION + 1))
    echo "$ITERATION" > "$COUNTER_FILE"
    ITERATION_ID="iter_$(printf '%04d' $ITERATION)"

    # ── 1. Select topic (curriculum-based) ──
    log_msg "iter=$ITERATION_ID | phase=topic_selection"
    write_heartbeat "topic_selection" "" "running" "$ITERATION"

    TOPIC_JSON=$(python3 "$TOPIC_SELECT" "$TOPIC_REGISTRY" 2>>"$LOG")
    TOPIC=$(echo "$TOPIC_JSON" | python3 -c "import sys,json; print(json.load(sys.stdin)['selected_topic'])" 2>/dev/null)
    TOPIC_CATEGORY=$(echo "$TOPIC_JSON" | python3 -c "import sys,json; print(json.load(sys.stdin)['category'])" 2>/dev/null)
    MODE=$(echo "$TOPIC_JSON" | python3 -c "import sys,json; print(json.load(sys.stdin)['mode'])" 2>/dev/null)
    DISPLAY_NAME=$(echo "$TOPIC_JSON" | python3 -c "import sys,json; print(json.load(sys.stdin)['display_name'])" 2>/dev/null)

    log_msg "iter=$ITERATION_ID | topic=$TOPIC | category=$TOPIC_CATEGORY | mode=$MODE"

    # Save selection context for the pipeline
    SELECTION_FILE="$BASE/outputs/${ITERATION_ID}_topic_selection.json"
    echo "$TOPIC_JSON" > "$SELECTION_FILE"

    # ── 2. Select agent roster (UCB-based) ──
    log_msg "iter=$ITERATION_ID | phase=agent_selection"
    write_heartbeat "agent_selection" "$TOPIC" "running" "$ITERATION"

    AGENTS_FILE="$BASE/outputs/${ITERATION_ID}_agents.json"
    python3 "$AGENT_SELECT" \
        --topic-category "$TOPIC_CATEGORY" \
        --pool "$AGENT_POOL" \
        --scores "$AGENT_SCORES" \
        > "$AGENTS_FILE" 2>>"$LOG"

    AGENT_NAMES=$(python3 -c "import json; d=json.load(open('$AGENTS_FILE')); print(', '.join(a['role_id'] for a in d['selected']))" 2>/dev/null || echo "unknown")
    log_msg "iter=$ITERATION_ID | agents=$AGENT_NAMES"

    # ── 3. Run pipeline ──
    log_msg "iter=$ITERATION_ID | phase=pipeline_start"
    write_heartbeat "pipeline_running" "$TOPIC" "running" "$ITERATION"

    PIPELINE_OK=true
    if TOPIC="$TOPIC" \
       TOPIC_CATEGORY="$TOPIC_CATEGORY" \
       MODE="$MODE" \
       AGENTS_JSON="$AGENTS_FILE" \
       ITERATION_ID="$ITERATION_ID" \
       BASE_DIR="$BASE" \
       LOG_FILE="$LOG" \
       HEARTBEAT_FILE="$HEARTBEAT" \
       bash "$PIPELINE" 2>>"$LOG"; then
        log_msg "iter=$ITERATION_ID | phase=pipeline_complete | status=success"
        write_heartbeat "iteration_complete" "$TOPIC" "running" "$ITERATION"
    else
        PIPELINE_OK=false
        log_msg "iter=$ITERATION_ID | phase=pipeline_complete | status=FAILED"
        write_heartbeat "iteration_failed" "$TOPIC" "error" "$ITERATION"
    fi

    # ── 4. Log summary ──
    KB_CONCEPTS=$(find "$BASE/knowledge_base/concepts" -name "*.json" -type f 2>/dev/null | wc -l)
    KB_RELS=$(find "$BASE/knowledge_base/relationships" -name "*.json" -type f 2>/dev/null | wc -l)
    log_msg "iter=$ITERATION_ID | kb_concepts=$KB_CONCEPTS | kb_relationships=$KB_RELS | pipeline=$PIPELINE_OK"

    # ── 5. Push to GitHub ──
    log_msg "iter=$ITERATION_ID | phase=git_push"
    (
        cd "$BASE"
        git add -A
        git commit -m "${ITERATION_ID}: ${DISPLAY_NAME} (${MODE})" \
            -m "topic=${TOPIC} category=${TOPIC_CATEGORY}" \
            -m "kb_concepts=${KB_CONCEPTS} kb_relationships=${KB_RELS} pipeline_ok=${PIPELINE_OK}" \
            2>>"$LOG" || true
        git push origin main 2>>"$LOG" || log_msg "iter=$ITERATION_ID | git push failed"
    )
    log_msg "iter=$ITERATION_ID | phase=git_push_complete"

    # ── 6. Sleep ──
    SLEEP_TIME=$(( RANDOM % 61 + 30 ))
    log_msg "iter=$ITERATION_ID | sleeping ${SLEEP_TIME}s"
    sleep "$SLEEP_TIME" || true
done
