#!/usr/bin/env bash
set -euo pipefail

###############################################################################
# phase2_pairwise_debate.sh — Create 4 pairwise critiques from 8 agents
#
# Required env vars:
#   ITER_DIR       — Iteration output directory
#   AGENTS_JSON    — Path to selected agents JSON file
#   TOPIC          — Topic slug
#   LOG_FILE       — Path to log file
#   (no forced timeout — uses Claude's own defaults)
###############################################################################

# No artificial timeout — let Claude run to completion
PHASE1_DIR="${ITER_DIR}/phase1"
PHASE2_DIR="${ITER_DIR}/phase2"
mkdir -p "$PHASE2_DIR"

log() {
    local ts
    ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
    printf '[%s] [phase2] %s\n' "$ts" "$1" >> "$LOG_FILE"
}

# ---------------------------------------------------------------------------
# Build pairs: sort agents by category so pairs cross categories
# ---------------------------------------------------------------------------

PAIRS_FILE="$(mktemp)"

python3 - "$AGENTS_JSON" "$PHASE1_DIR" "$PAIRS_FILE" << 'PYEOF'
import json, sys, os

agents_path = sys.argv[1]
phase1_dir = sys.argv[2]
pairs_path = sys.argv[3]

with open(agents_path, "r") as f:
    agents_data = json.load(f)

selected = agents_data.get("selected", agents_data.get("agents", []))

# Filter to agents that have successful phase1 output
valid_agents = []
for agent in selected:
    rid = agent.get("role_id", "unknown")
    output_path = os.path.join(phase1_dir, f"{rid}.md")
    if os.path.isfile(output_path):
        with open(output_path, "r") as f:
            content = f.read()
        if "AGENT_FAILURE" not in content:
            valid_agents.append(agent)

# Sort by category to maximize cross-category pairing
# Order: generalist, specialist, challenger — pairs will cross categories
category_order = {"generalist": 0, "specialist": 1, "challenger": 2}
valid_agents.sort(key=lambda a: (category_order.get(a.get("category", ""), 9), a.get("role_id", "")))

# Create pairs: (0,1), (2,3), (4,5), (6,7)
pairs = []
for i in range(0, len(valid_agents) - 1, 2):
    pairs.append({
        "pair_index": i // 2,
        "agent_a": valid_agents[i],
        "agent_b": valid_agents[i + 1]
    })

with open(pairs_path, "w") as f:
    json.dump(pairs, f)
PYEOF

PAIR_COUNT="$(python3 -c "import json; print(len(json.load(open('${PAIRS_FILE}'))))")"
log "Created ${PAIR_COUNT} pairs for debate"

# ---------------------------------------------------------------------------
# Run each pair's debate in parallel
# ---------------------------------------------------------------------------

run_pair_debate() {
    local pair_idx="$1"
    local pairs_file="$2"

    # Extract pair details via python
    local pair_tmp
    pair_tmp="$(mktemp)"
    python3 - "$pairs_file" "$pair_idx" "$pair_tmp" << 'PYEOF'
import json, sys
pairs = json.load(open(sys.argv[1]))
pair = pairs[int(sys.argv[2])]
out = sys.argv[3]
with open(out + ".agent_a_id", "w") as f: f.write(pair["agent_a"]["role_id"])
with open(out + ".agent_a_name", "w") as f: f.write(pair["agent_a"].get("name", pair["agent_a"]["role_id"]))
with open(out + ".agent_b_id", "w") as f: f.write(pair["agent_b"]["role_id"])
with open(out + ".agent_b_name", "w") as f: f.write(pair["agent_b"].get("name", pair["agent_b"]["role_id"]))
PYEOF

    local agent_a_id agent_a_name agent_b_id agent_b_name
    agent_a_id="$(cat "${pair_tmp}.agent_a_id")"
    agent_a_name="$(cat "${pair_tmp}.agent_a_name")"
    agent_b_id="$(cat "${pair_tmp}.agent_b_id")"
    agent_b_name="$(cat "${pair_tmp}.agent_b_name")"

    local output_file="${PHASE2_DIR}/pair_${pair_idx}_${agent_a_id}_vs_${agent_b_id}.md"
    local agent_a_output="${PHASE1_DIR}/${agent_a_id}.md"
    local agent_b_output="${PHASE1_DIR}/${agent_b_id}.md"

    log "Pair ${pair_idx}: ${agent_a_name} vs ${agent_b_name}"

    # Build critique prompt via temp file
    local prompt_file
    prompt_file="$(mktemp)"

    cat >> "$prompt_file" << 'HEADER'
You are a rigorous analytical critic. Your job is to compare two financial research analyses on the same topic, identify where they agree, where they disagree, what novel insights each brings, and which claims don't survive scrutiny.

Be specific. Reference exact claims from each analysis. Don't be diplomatic — if one analysis is weaker, say so and explain why.

---

HEADER

    printf 'TOPIC: %s\n\n' "$TOPIC" >> "$prompt_file"

    printf '=== AGENT A: %s ===\n\n' "$agent_a_name" >> "$prompt_file"
    if [[ -f "$agent_a_output" ]]; then
        cat "$agent_a_output" >> "$prompt_file"
    else
        printf '(No output available for Agent A)\n' >> "$prompt_file"
    fi
    printf '\n\n' >> "$prompt_file"

    printf '=== AGENT B: %s ===\n\n' "$agent_b_name" >> "$prompt_file"
    if [[ -f "$agent_b_output" ]]; then
        cat "$agent_b_output" >> "$prompt_file"
    else
        printf '(No output available for Agent B)\n' >> "$prompt_file"
    fi
    printf '\n\n' >> "$prompt_file"

    cat >> "$prompt_file" << 'INSTRUCTIONS'
---

Produce your critique in EXACTLY this structure:

## AGREEMENTS
(Claims both agents support, with combined evidence)

## DISAGREEMENTS
(Claim, Agent A position, Agent B position, which is stronger and why)

## NOVEL_INSIGHTS
(Things only one agent raised that seem valuable)

## REFUTED_CLAIMS
(Claims that don't survive scrutiny, with reasoning)
INSTRUCTIONS

    # Run Claude
    if cat "$prompt_file" | claude --print --no-session-persistence --dangerously-skip-permissions --effort max > "$output_file" 2>/dev/null; then
        log "Pair ${pair_idx} debate completed successfully"
    else
        local exit_code=$?
        log "Pair ${pair_idx} debate FAILED (exit code: ${exit_code})"
        cat > "$output_file" << STUBEOF
## AGREEMENTS
(Debate failed — no output produced. Exit code: ${exit_code})

## DISAGREEMENTS
(N/A)

## NOVEL_INSIGHTS
(N/A)

## REFUTED_CLAIMS
(N/A)
STUBEOF
    fi

    # Cleanup
    rm -f "$prompt_file" "$pair_tmp" "${pair_tmp}.agent_a_id" "${pair_tmp}.agent_a_name" \
          "${pair_tmp}.agent_b_id" "${pair_tmp}.agent_b_name"
}

# Launch all pairs in parallel
PIDS=()
for i in $(seq 0 $((PAIR_COUNT - 1))); do
    run_pair_debate "$i" "$PAIRS_FILE" &
    PIDS+=($!)
done

log "Launched ${#PIDS[@]} pair debates in parallel, waiting for completion..."

# Wait for all
SUCCESS_COUNT=0
FAIL_COUNT=0

for pid in "${PIDS[@]}"; do
    if wait "$pid" 2>/dev/null; then
        SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
    else
        FAIL_COUNT=$((FAIL_COUNT + 1))
    fi
done

# Cleanup
rm -f "$PAIRS_FILE"

log "Phase 2 results: ${SUCCESS_COUNT} debates succeeded, ${FAIL_COUNT} failed out of ${PAIR_COUNT}"
