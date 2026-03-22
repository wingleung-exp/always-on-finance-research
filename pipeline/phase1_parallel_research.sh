#!/usr/bin/env bash
set -euo pipefail

###############################################################################
# phase1_parallel_research.sh — Run 8 agents in parallel
#
# Required env vars:
#   AGENTS_JSON    — Path to selected agents JSON file
#   TOPIC          — Topic slug
#   MODE           — "overview" or "deep_dive"
#   ITERATION_ID   — Iteration identifier
#   ITER_DIR       — Iteration output directory
#   KB_DIR         — Knowledge base directory
#   LOG_FILE       — Path to log file
#   (no forced timeout — uses Claude's own defaults)
###############################################################################

# No artificial timeout — let Claude run to completion
PHASE1_DIR="${ITER_DIR}/phase1"
mkdir -p "$PHASE1_DIR"

log() {
    local ts
    ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
    printf '[%s] [%s] [phase1] %s\n' "$ts" "$ITERATION_ID" "$1" >> "$LOG_FILE"
}

# ---------------------------------------------------------------------------
# Extract agent list from AGENTS_JSON
# We need: role_id, name, category, system_prompt (from the pool)
# AGENTS_JSON has a "selected" array with role_id/name/category.
# We also need the system_prompt which lives in the pool. The selected JSON
# might not contain it, so we look for it in the agents pool.
# ---------------------------------------------------------------------------

POOL_FILE="$(dirname "$(dirname "$AGENTS_JSON")")/agents/agent_pool.json" 2>/dev/null || true
if [[ ! -f "${POOL_FILE:-}" ]]; then
    # Try standard location relative to the pipeline
    POOL_FILE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/agents/agent_pool.json"
fi

# Use python3 to extract agent data safely — avoids shell parsing of JSON
AGENT_DATA_FILE="$(mktemp)"
python3 - "$AGENTS_JSON" "$POOL_FILE" "$AGENT_DATA_FILE" << 'PYEOF'
import json, sys

agents_path = sys.argv[1]
pool_path = sys.argv[2]
out_path = sys.argv[3]

with open(agents_path, "r") as f:
    agents_data = json.load(f)

selected = agents_data.get("selected", agents_data.get("agents", []))

# Build lookup for system_prompt from pool
pool_prompts = {}
try:
    with open(pool_path, "r") as f:
        pool = json.load(f)
    for role in pool.get("roles", pool.get("agents", [])):
        pool_prompts[role["role_id"]] = role.get("system_prompt", "")
except Exception:
    pass

# Output: one JSON object per line
result = []
for agent in selected:
    rid = agent.get("role_id", "unknown")
    result.append({
        "role_id": rid,
        "name": agent.get("name", rid),
        "category": agent.get("category", "unknown"),
        "system_prompt": agent.get("system_prompt", pool_prompts.get(rid, "You are a financial research analyst."))
    })

with open(out_path, "w") as f:
    json.dump(result, f)
PYEOF

AGENT_COUNT="$(python3 -c "import json; print(len(json.load(open('${AGENT_DATA_FILE}'))))")"
log "Loaded ${AGENT_COUNT} agents for parallel research"

# ---------------------------------------------------------------------------
# Run each agent in parallel
# ---------------------------------------------------------------------------

PIDS=()
ROLE_IDS=()

run_single_agent() {
    local idx="$1"
    local agent_json_file="$2"

    # Extract this agent's fields via python (safe, no shell expansion)
    local agent_tmp
    agent_tmp="$(mktemp)"
    python3 - "$agent_json_file" "$idx" "$agent_tmp" << 'PYEOF'
import json, sys
data = json.load(open(sys.argv[1]))
agent = data[int(sys.argv[2])]
out = sys.argv[3]
# Write each field to a separate file for safe shell consumption
with open(out + ".role_id", "w") as f: f.write(agent["role_id"])
with open(out + ".name", "w") as f: f.write(agent["name"])
with open(out + ".category", "w") as f: f.write(agent["category"])
with open(out + ".system_prompt", "w") as f: f.write(agent["system_prompt"])
PYEOF

    local role_id name category
    role_id="$(cat "${agent_tmp}.role_id")"
    name="$(cat "${agent_tmp}.name")"
    category="$(cat "${agent_tmp}.category")"

    local output_file="${PHASE1_DIR}/${role_id}.md"
    local prompt_file
    prompt_file="$(mktemp)"

    # --- Build prompt file safely ---

    # 1. System prompt (from agent data, written by python)
    printf 'You are playing the role of: %s (%s)\n\n' "$name" "$category" >> "$prompt_file"
    printf 'Your analytical perspective and instructions:\n' >> "$prompt_file"
    cat "${agent_tmp}.system_prompt" >> "$prompt_file"
    printf '\n\n' >> "$prompt_file"

    # 2. Topic/mode/iteration context
    printf '%s\n\n' '---' >> "$prompt_file"
    printf 'RESEARCH TASK\n' >> "$prompt_file"
    printf 'Topic: %s\n' "$TOPIC" >> "$prompt_file"
    printf 'Mode: %s\n' "$MODE" >> "$prompt_file"
    printf 'Iteration: %s\n\n' "$ITERATION_ID" >> "$prompt_file"

    # 3. Append relevant KB context if it exists
    local kb_concepts_dir="${KB_DIR}/concepts"
    local kb_rels_dir="${KB_DIR}/relationships"

    local topic_slug
    topic_slug="$(printf '%s' "$TOPIC" | tr ' ' '_' | tr '[:upper:]' '[:lower:]')"

    local has_kb_context=false

    if [[ -d "$kb_concepts_dir" ]]; then
        for concept_file in "${kb_concepts_dir}"/*.json; do
            [[ -f "$concept_file" ]] || continue
            if grep -qi "$topic_slug" "$concept_file" 2>/dev/null; then
                if [[ "$has_kb_context" == "false" ]]; then
                    printf 'EXISTING KNOWLEDGE BASE CONTEXT:\n\n' >> "$prompt_file"
                    has_kb_context=true
                fi
                printf '%s\n' '--- Concept from KB ---' >> "$prompt_file"
                cat "$concept_file" >> "$prompt_file"
                printf '\n\n' >> "$prompt_file"
            fi
        done
    fi

    if [[ -d "$kb_rels_dir" ]]; then
        for rel_file in "${kb_rels_dir}"/*.json; do
            [[ -f "$rel_file" ]] || continue
            if grep -qi "$topic_slug" "$rel_file" 2>/dev/null; then
                if [[ "$has_kb_context" == "false" ]]; then
                    printf 'EXISTING KNOWLEDGE BASE CONTEXT:\n\n' >> "$prompt_file"
                    has_kb_context=true
                fi
                printf '%s\n' '--- Relationship from KB ---' >> "$prompt_file"
                cat "$rel_file" >> "$prompt_file"
                printf '\n\n' >> "$prompt_file"
            fi
        done
    fi

    # 4. Required output structure
    cat >> "$prompt_file" << 'TEMPLATE'
---

Please produce your analysis in EXACTLY this structure:

# [Topic] — [Agent Name] Analysis

## Key Claims
(Numbered list. Each claim must be a specific, testable assertion.)

## Evidence & Reasoning
(For each claim above, the supporting evidence or logic.)

## Confidence Assessment
(1-10 for each major claim, with justification.)

## Connections to Other Topics
(How does this connect to concepts in other topic categories?)

## Open Questions
(What can't you answer? What would you need to know?)
TEMPLATE

    # --- Run Claude ---
    log "Starting agent: ${role_id} (${name})"

    if cat "$prompt_file" | claude --print --no-session-persistence --dangerously-skip-permissions --effort max > "$output_file" 2>/dev/null; then
        log "Agent ${role_id} completed successfully"
    else
        local exit_code=$?
        log "Agent ${role_id} FAILED (exit code: ${exit_code})"
        # Write stub noting failure
        cat > "$output_file" << STUBEOF
# ${TOPIC} — ${name} Analysis

<!-- AGENT_FAILURE: Agent ${role_id} failed with exit code ${exit_code} -->

## Key Claims
(Agent failed to produce output.)

## Evidence & Reasoning
(No output available.)

## Confidence Assessment
(N/A)

## Connections to Other Topics
(N/A)

## Open Questions
(Agent needs to be re-run.)
STUBEOF
    fi

    # Cleanup temp files
    rm -f "$prompt_file" "$agent_tmp" "${agent_tmp}.role_id" "${agent_tmp}.name" \
          "${agent_tmp}.category" "${agent_tmp}.system_prompt"
}

# Launch all agents in parallel
for i in $(seq 0 $((AGENT_COUNT - 1))); do
    run_single_agent "$i" "$AGENT_DATA_FILE" &
    PIDS+=($!)

    # Extract role_id for tracking
    rid="$(python3 -c "import json; print(json.load(open('${AGENT_DATA_FILE}'))[$i]['role_id'])")"
    ROLE_IDS+=("$rid")
done

log "Launched ${#PIDS[@]} agents in parallel, waiting for completion..."

# Wait for all and track results
SUCCESS_COUNT=0
FAIL_COUNT=0

for pidx in "${!PIDS[@]}"; do
    pid="${PIDS[$pidx]}"
    rid="${ROLE_IDS[$pidx]}"
    if wait "$pid" 2>/dev/null; then
        # Check if output is a stub
        outf="${PHASE1_DIR}/${rid}.md"
        if [[ -f "$outf" ]] && ! grep -q "AGENT_FAILURE" "$outf" 2>/dev/null; then
            SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
        else
            FAIL_COUNT=$((FAIL_COUNT + 1))
        fi
    else
        FAIL_COUNT=$((FAIL_COUNT + 1))
        log "Agent process for ${rid} exited with error"
    fi
done

# Cleanup
rm -f "$AGENT_DATA_FILE"

log "Phase 1 results: ${SUCCESS_COUNT} succeeded, ${FAIL_COUNT} failed out of ${AGENT_COUNT}"
