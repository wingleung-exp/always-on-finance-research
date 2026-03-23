#!/usr/bin/env bash
set -euo pipefail

# Recovery script: run missing phases for failed iterations
# iter_0006, 0007, 0008, 0018: have valid phase4, need phases 5-6
# iter_0019: has valid phase3, needs phases 4-6

BASE="/data/.openclaw/workspace/finance_research"
SCRIPT_DIR="$BASE/pipeline"
KB_DIR="$BASE/knowledge_base"
LOG="$BASE/logs/research.log"
HEARTBEAT="/data/.openclaw/workspace/logs/research_heartbeat.json"

log() {
    local ts
    ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
    printf '[%s] [RECOVERY:%s] %s\n' "$ts" "$1" "$2" >> "$LOG"
    printf '[%s] [RECOVERY:%s] %s\n' "$ts" "$1" "$2"
}

run_phase5() {
    local iter_id="$1" topic="$2" category="$3"
    local iter_dir="$BASE/outputs/iteration_${iter_id}"
    log "$iter_id" "Running phase 5 (KB write)..."
    python3 "${SCRIPT_DIR}/phase5_kb_write.py" \
        --phase4-dir "${iter_dir}/phase4" \
        --kb-dir "$KB_DIR" \
        --iteration-id "$iter_id" \
        --topic "$topic" \
        --topic-category "$category"
    log "$iter_id" "Phase 5 complete."
}

run_phase6() {
    local iter_id="$1" topic="$2" category="$3"
    local iter_dir="$BASE/outputs/iteration_${iter_id}"
    log "$iter_id" "Running phase 6 (score update)..."
    python3 "${SCRIPT_DIR}/phase6_score_update.py" \
        --phase4-dir "${iter_dir}/phase4" \
        --base-dir "$BASE" \
        --topic "$topic" \
        --topic-category "$category" \
        --iteration-id "$iter_id"
    log "$iter_id" "Phase 6 complete."
}

run_phase4() {
    local iter_id="$1" topic="$2" category="$3"
    local iter_dir="$BASE/outputs/iteration_${iter_id}"
    log "$iter_id" "Running phase 4 (knowledge extraction)..."
    python3 "${SCRIPT_DIR}/phase4_knowledge_extraction.py" \
        --iter-dir "$iter_dir" \
        --topic "$topic" \
        --topic-category "$category" \
        --iteration-id "$iter_id"
    log "$iter_id" "Phase 4 complete."
}

echo "=== Recovery: fixing failed iterations ==="

# Iterations with valid phase4, need phases 5-6
for iter_id in iter_0006 iter_0007 iter_0008 iter_0018; do
    topic=$(python3 -c "import json; d=json.load(open('$BASE/outputs/${iter_id}_topic_selection.json')); print(d['selected_topic'])")
    category=$(python3 -c "import json; d=json.load(open('$BASE/outputs/${iter_id}_topic_selection.json')); print(d['category'])")

    echo "--- Recovering $iter_id ($topic / $category): phases 5-6 ---"
    log "$iter_id" "Starting recovery (phases 5-6)"

    run_phase5 "$iter_id" "$topic" "$category"
    run_phase6 "$iter_id" "$topic" "$category"

    log "$iter_id" "Recovery complete."
    echo "--- $iter_id recovered ---"
done

# iter_0019: needs phases 4-6
iter_id="iter_0019"
topic=$(python3 -c "import json; d=json.load(open('$BASE/outputs/${iter_id}_topic_selection.json')); print(d['selected_topic'])")
category=$(python3 -c "import json; d=json.load(open('$BASE/outputs/${iter_id}_topic_selection.json')); print(d['category'])")

echo "--- Recovering $iter_id ($topic / $category): phases 4-6 ---"
log "$iter_id" "Starting recovery (phases 4-6)"

run_phase4 "$iter_id" "$topic" "$category"
run_phase5 "$iter_id" "$topic" "$category"
run_phase6 "$iter_id" "$topic" "$category"

log "$iter_id" "Recovery complete."
echo "--- $iter_id recovered ---"

echo "=== All recoveries complete ==="
