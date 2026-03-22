#!/usr/bin/env bash
set -euo pipefail

###############################################################################
# phase3_panel_synthesis.sh — Feed all agent + debate outputs to a synthesis agent
#
# Required env vars:
#   ITER_DIR       — Iteration output directory
#   TOPIC          — Topic slug
#   TOPIC_CATEGORY — Topic category
#   ITERATION_ID   — Iteration identifier
#   LOG_FILE       — Path to log file
#   TIMEOUT        — Synthesis timeout in seconds (default 360)
###############################################################################

TIMEOUT="${TIMEOUT:-360}"
PHASE1_DIR="${ITER_DIR}/phase1"
PHASE2_DIR="${ITER_DIR}/phase2"
PHASE3_DIR="${ITER_DIR}/phase3"
mkdir -p "$PHASE3_DIR"

log() {
    local ts
    ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
    printf '[%s] [%s] [phase3] %s\n' "$ts" "$ITERATION_ID" "$1" >> "$LOG_FILE"
}

OUTPUT_FILE="${PHASE3_DIR}/panel_synthesis.md"

# ---------------------------------------------------------------------------
# Build synthesis prompt by catting all files into a temp file
# ---------------------------------------------------------------------------

PROMPT_FILE="$(mktemp)"

# Header
cat >> "$PROMPT_FILE" << 'HEADER'
You are the chief synthesis analyst for a multi-agent finance research system. You have received analyses from 8 specialist agents and 4 pairwise critique reports. Your job is to produce a single, authoritative synthesis that:

1. Identifies claims with broad convergence (high confidence)
2. Flags partial convergence (moderate confidence)
3. Notes isolated claims that need future corroboration (low confidence)
4. Tracks claims killed during debate (refuted)
5. Highlights unresolved disagreements for future research
6. Credits each agent's unique contributions (for scoring)

Be rigorous. Confidence levels must reflect actual convergence across agents, not just how well-argued a single analysis is.

---

HEADER

printf 'TOPIC: %s\n' "$TOPIC" >> "$PROMPT_FILE"
printf 'CATEGORY: %s\n' "$TOPIC_CATEGORY" >> "$PROMPT_FILE"
printf 'ITERATION: %s\n\n' "$ITERATION_ID" >> "$PROMPT_FILE"

# ---------------------------------------------------------------------------
# Cat all Phase 1 agent outputs
# ---------------------------------------------------------------------------

printf '================================================================\n' >> "$PROMPT_FILE"
printf 'SECTION 1: INDIVIDUAL AGENT ANALYSES\n' >> "$PROMPT_FILE"
printf '================================================================\n\n' >> "$PROMPT_FILE"

agent_count=0
for agent_file in "${PHASE1_DIR}"/*.md; do
    [[ -f "$agent_file" ]] || continue
    agent_count=$((agent_count + 1))
    local_name="$(basename "$agent_file" .md)"
    printf '%s\n\n' "--- Agent: ${local_name} ---" >> "$PROMPT_FILE"
    cat "$agent_file" >> "$PROMPT_FILE"
    printf '\n\n' >> "$PROMPT_FILE"
done

log "Included ${agent_count} agent analyses in synthesis prompt"

# ---------------------------------------------------------------------------
# Cat all Phase 2 debate outputs
# ---------------------------------------------------------------------------

printf '================================================================\n' >> "$PROMPT_FILE"
printf 'SECTION 2: PAIRWISE CRITIQUE REPORTS\n' >> "$PROMPT_FILE"
printf '================================================================\n\n' >> "$PROMPT_FILE"

debate_count=0
for debate_file in "${PHASE2_DIR}"/*.md; do
    [[ -f "$debate_file" ]] || continue
    debate_count=$((debate_count + 1))
    local_name="$(basename "$debate_file" .md)"
    printf '%s\n\n' "--- Debate: ${local_name} ---" >> "$PROMPT_FILE"
    cat "$debate_file" >> "$PROMPT_FILE"
    printf '\n\n' >> "$PROMPT_FILE"
done

log "Included ${debate_count} debate reports in synthesis prompt"

# ---------------------------------------------------------------------------
# Append synthesis instruction template
# ---------------------------------------------------------------------------

cat >> "$PROMPT_FILE" << 'SYNTHESIS_INSTRUCTIONS'
================================================================
SYNTHESIS INSTRUCTIONS
================================================================

Produce your synthesis in EXACTLY this structure. Be thorough and specific.

## HIGH_CONFIDENCE
(Claims with strong convergence across agents that survived debate. For each: the claim, confidence 1-10, originating agents, surviving evidence.)

## MODERATE_CONFIDENCE
(Partial convergence or mixed debate results. Same format.)

## LOW_CONFIDENCE
(Isolated claims — one agent only, not yet refuted but not corroborated.)

## REFUTED
(Claims killed during debate, with reasoning.)

## KEY_DISAGREEMENTS
(Unresolved debates. Flag for future research.)

## NOVEL_CONTRIBUTIONS
(For each agent: list their unique contributions that survived to this stage. This is used for scoring.)
SYNTHESIS_INSTRUCTIONS

# ---------------------------------------------------------------------------
# Run Claude synthesis
# ---------------------------------------------------------------------------

log "Running synthesis (timeout: ${TIMEOUT}s, prompt file: $(wc -c < "$PROMPT_FILE") bytes)"

if cat "$PROMPT_FILE" | timeout "$TIMEOUT" claude --print --no-session-persistence --dangerously-skip-permissions --effort max > "$OUTPUT_FILE" 2>/dev/null; then
    local_size="$(wc -c < "$OUTPUT_FILE")"
    log "Panel synthesis completed successfully (${local_size} bytes)"
else
    local exit_code=$?
    log "Panel synthesis FAILED (exit code: ${exit_code})"

    cat > "$OUTPUT_FILE" << 'STUBEOF'
## HIGH_CONFIDENCE
(Synthesis failed — no output produced.)

## MODERATE_CONFIDENCE
(N/A)

## LOW_CONFIDENCE
(N/A)

## REFUTED
(N/A)

## KEY_DISAGREEMENTS
(N/A)

## NOVEL_CONTRIBUTIONS
(N/A)
STUBEOF
fi

# Cleanup
rm -f "$PROMPT_FILE"

log "Phase 3 output written to: ${OUTPUT_FILE}"
