#!/usr/bin/env bash
set -euo pipefail

###############################################################################
# run_iteration.sh — Main pipeline orchestrator for a single research iteration
#
# Required env vars:
#   TOPIC              — The topic slug (e.g. "monetary_policy")
#   TOPIC_CATEGORY     — Category (e.g. "macro_frameworks")
#   MODE               — "overview" or "deep_dive"
#   AGENTS_JSON        — Path to selected agents JSON file
#   ITERATION_ID       — Unique iteration ID (e.g. "iteration_42")
#   BASE_DIR           — Root of finance_research workspace
#   LOG_FILE           — Path to the log file
#   HEARTBEAT_FILE     — Path to the heartbeat JSON file
###############################################################################

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

log() {
    local ts
    ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
    printf '[%s] [%s] %s\n' "$ts" "$ITERATION_ID" "$1" >> "$LOG_FILE"
}

write_heartbeat() {
    local phase="$1"
    local status="${2:-running}"
    local ts epoch
    ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
    epoch="$(date +%s)"
    local tmp_hb
    tmp_hb="$(mktemp)"
    printf '{"timestamp": "%s", "epoch": %s, "pid": %s, "phase": "%s", "topic": "%s", "status": "%s"}\n' \
        "$ts" "$epoch" "$$" "$phase" "$TOPIC" "$status" > "$tmp_hb"
    cat "$tmp_hb" > "$HEARTBEAT_FILE"
    rm -f "$tmp_hb"
}

# Background heartbeat: writes every HEARTBEAT_INTERVAL seconds while running.
# Call start_heartbeat "phase_name" before a long stage, stop_heartbeat after.
HEARTBEAT_PID=""

start_heartbeat() {
    local phase="$1"
    stop_heartbeat  # ensure no leftover
    (
        while true; do
            write_heartbeat "$phase" "running"
            sleep "${HEARTBEAT_INTERVAL:-30}"
        done
    ) &
    HEARTBEAT_PID=$!
}

stop_heartbeat() {
    if [[ -n "${HEARTBEAT_PID:-}" ]] && kill -0 "$HEARTBEAT_PID" 2>/dev/null; then
        kill "$HEARTBEAT_PID" 2>/dev/null || true
        wait "$HEARTBEAT_PID" 2>/dev/null || true
    fi
    HEARTBEAT_PID=""
}

# Cleanup on exit
cleanup() {
    stop_heartbeat
}
trap cleanup EXIT

# ---------------------------------------------------------------------------
# Load config values from pipeline_config.yaml (simple grep, no parser)
# ---------------------------------------------------------------------------

CONFIG_FILE="${BASE_DIR}/config/pipeline_config.yaml"

grep_config() {
    local key="$1"
    local default="$2"
    local val
    val="$(grep -E "^\s*${key}:" "$CONFIG_FILE" 2>/dev/null | head -1 | sed 's/^[^:]*:\s*//' | sed 's/\s*#.*//' | tr -d '[:space:]')" || true
    if [[ -z "$val" ]]; then
        printf '%s' "$default"
    else
        printf '%s' "$val"
    fi
}

TIMEOUT_PHASE1="$(grep_config 'agent_research' '300')"
TIMEOUT_PHASE2="$(grep_config 'pairwise_debate' '300')"
TIMEOUT_PHASE3="$(grep_config 'panel_synthesis' '360')"
MIN_AGENTS="$(grep_config 'min_agents_for_downstream' '5')"
HEARTBEAT_INTERVAL="$(grep_config 'heartbeat_interval' '30')"

export HEARTBEAT_INTERVAL

# ---------------------------------------------------------------------------
# 1. Create output directories
# ---------------------------------------------------------------------------

ITER_DIR="${BASE_DIR}/outputs/iteration_${ITERATION_ID}"
mkdir -p "${ITER_DIR}/phase1" "${ITER_DIR}/phase2" "${ITER_DIR}/phase3" "${ITER_DIR}/phase4"

KB_DIR="${BASE_DIR}/knowledge_base"

log "=== Starting iteration ${ITERATION_ID} ==="
log "Topic: ${TOPIC} | Category: ${TOPIC_CATEGORY} | Mode: ${MODE}"
log "Output dir: ${ITER_DIR}"

write_heartbeat "init" "running"

# ---------------------------------------------------------------------------
# 2. Phase 1 — Parallel Agent Research
# ---------------------------------------------------------------------------

log "--- Phase 1: Parallel agent research ---"
write_heartbeat "phase1_parallel_research"
start_heartbeat "phase1_parallel_research"

export AGENTS_JSON TOPIC MODE ITERATION_ID ITER_DIR KB_DIR LOG_FILE
export TIMEOUT="$TIMEOUT_PHASE1"

bash "${SCRIPT_DIR}/phase1_parallel_research.sh"

stop_heartbeat
write_heartbeat "phase1_complete"
log "Phase 1 complete."

# ---------------------------------------------------------------------------
# 3. Quality gate — count successful agent outputs
# ---------------------------------------------------------------------------

log "--- Quality gate: checking Phase 1 outputs ---"

success_count=0
for f in "${ITER_DIR}/phase1/"*.md; do
    [[ -f "$f" ]] || continue
    # Stub files contain "AGENT_FAILURE" marker
    if ! grep -q "AGENT_FAILURE" "$f" 2>/dev/null; then
        success_count=$((success_count + 1))
    fi
done

log "Successful agents: ${success_count} / required minimum: ${MIN_AGENTS}"

if [[ "$success_count" -lt "$MIN_AGENTS" ]]; then
    log "GATE FAILED: only ${success_count} agents succeeded (need ${MIN_AGENTS}). Aborting downstream phases."
    write_heartbeat "gate_failed" "failed"
    exit 1
fi

write_heartbeat "gate_passed"

# ---------------------------------------------------------------------------
# 4. Phase 2 — Pairwise Debate
# ---------------------------------------------------------------------------

log "--- Phase 2: Pairwise debate ---"
write_heartbeat "phase2_pairwise_debate"
start_heartbeat "phase2_pairwise_debate"

export TIMEOUT="$TIMEOUT_PHASE2"

bash "${SCRIPT_DIR}/phase2_pairwise_debate.sh"

stop_heartbeat
write_heartbeat "phase2_complete"
log "Phase 2 complete."

# ---------------------------------------------------------------------------
# 5. Phase 3 — Panel Synthesis
# ---------------------------------------------------------------------------

log "--- Phase 3: Panel synthesis ---"
write_heartbeat "phase3_panel_synthesis"
start_heartbeat "phase3_panel_synthesis"

export TOPIC_CATEGORY TIMEOUT="$TIMEOUT_PHASE3"

bash "${SCRIPT_DIR}/phase3_panel_synthesis.sh"

stop_heartbeat
write_heartbeat "phase3_complete"
log "Phase 3 complete."

# ---------------------------------------------------------------------------
# 6. Phase 4 — Knowledge Extraction (Python)
# ---------------------------------------------------------------------------

log "--- Phase 4: Knowledge extraction ---"
write_heartbeat "phase4_knowledge_extraction"
start_heartbeat "phase4_knowledge_extraction"

if python3 "${SCRIPT_DIR}/phase4_knowledge_extraction.py" \
    --iter-dir "$ITER_DIR" \
    --topic "$TOPIC" \
    --topic-category "$TOPIC_CATEGORY" \
    --iteration-id "$ITERATION_ID"; then
    stop_heartbeat
    write_heartbeat "phase4_complete"
    log "Phase 4 complete."
else
    stop_heartbeat
    log "Phase 4 FAILED (exit $?) — retrying once..."
    write_heartbeat "phase4_retry"
    start_heartbeat "phase4_retry"
    if python3 "${SCRIPT_DIR}/phase4_knowledge_extraction.py" \
        --iter-dir "$ITER_DIR" \
        --topic "$TOPIC" \
        --topic-category "$TOPIC_CATEGORY" \
        --iteration-id "$ITERATION_ID"; then
        stop_heartbeat
        write_heartbeat "phase4_complete"
        log "Phase 4 complete (retry succeeded)."
    else
        stop_heartbeat
        log "Phase 4 FAILED on retry — skipping phases 5-6 for this iteration."
        write_heartbeat "phase4_failed"
        return 1 2>/dev/null || exit 1
    fi
fi

# ---------------------------------------------------------------------------
# 7. Phase 5 — KB Write (Python)
# ---------------------------------------------------------------------------

log "--- Phase 5: KB write ---"
write_heartbeat "phase5_kb_write"
start_heartbeat "phase5_kb_write"

if python3 "${SCRIPT_DIR}/phase5_kb_write.py" \
    --phase4-dir "${ITER_DIR}/phase4" \
    --kb-dir "$KB_DIR" \
    --iteration-id "$ITERATION_ID" \
    --topic "$TOPIC" \
    --topic-category "$TOPIC_CATEGORY"; then
    stop_heartbeat
    write_heartbeat "phase5_complete"
    log "Phase 5 complete."
else
    stop_heartbeat
    log "Phase 5 FAILED (exit $?) — skipping phase 6."
    write_heartbeat "phase5_failed"
    return 1 2>/dev/null || exit 1
fi

# ---------------------------------------------------------------------------
# 8. Phase 6 — Score Update (Python)
# ---------------------------------------------------------------------------

log "--- Phase 6: Score update ---"
write_heartbeat "phase6_score_update"
start_heartbeat "phase6_score_update"

if python3 "${SCRIPT_DIR}/phase6_score_update.py" \
    --phase4-dir "${ITER_DIR}/phase4" \
    --base-dir "$BASE_DIR" \
    --topic "$TOPIC" \
    --topic-category "$TOPIC_CATEGORY" \
    --iteration-id "$ITERATION_ID"; then
    stop_heartbeat
    write_heartbeat "phase6_complete"
    log "Phase 6 complete."
else
    stop_heartbeat
    log "Phase 6 FAILED (exit $?) — continuing anyway."
    write_heartbeat "phase6_failed"
fi

# ---------------------------------------------------------------------------
# 9. Done
# ---------------------------------------------------------------------------

log "=== Iteration ${ITERATION_ID} complete ==="
write_heartbeat "complete" "complete"
