# Always-On Finance Research

An autonomous multi-agent finance research system powered by Claude. Runs 8 specialist AI agents in parallel, pits them against each other in structured debates, synthesizes findings through a panel process, and accumulates a persistent knowledge base that grows smarter over time.

## What It Does

Each iteration of the research loop:

1. **Selects a topic** from a 25-topic curriculum spanning macro, credit, equities, commodities, FX, and structural themes using a UCB1-based curriculum scheduler
2. **Selects 8 agents** from a pool of 20 specialists using UCB1 bandit scoring (balancing exploration of untried agents vs. exploitation of top performers)
3. **Phase 1 -- Parallel Research**: 8 agents run simultaneously as independent Claude calls, each producing a structured thesis
4. **Phase 2 -- Pairwise Debate**: 4 cross-category agent pairs critique each other's work, identifying agreements, contradictions, novel insights, and refuted claims
5. **Phase 3 -- Panel Synthesis**: A synthesis agent reads all 8 analyses + 4 debate reports and produces confidence-ranked findings
6. **Phase 4 -- Knowledge Extraction**: Structured JSON extraction of concepts, relationships, frameworks, anti-knowledge, and provenance
7. **Phase 5 -- KB Write**: Merge-or-create logic writes surviving knowledge to a persistent knowledge base with weighted confidence updates
8. **Phase 6 -- Score Update**: Agent performance scores and topic registry metadata are updated based on claim survival rates

## Architecture

```
research_loop.sh          # Outer loop: topic → agents → pipeline → score → sleep → repeat
├── topic_registry/
│   ├── select_topic.py   # Curriculum-aware topic selection (UCB1-style scoring)
│   └── topic_registry.json  # 25 topics across 5 categories with depth/confidence tracking
├── agent_selection/
│   └── select_agents.py  # UCB1 bandit agent selection with role constraints
├── agents/
│   └── agent_pool.json   # 20 agents: macro, credit, rates, equity, FX, commodities, quant, risk, generalist, challenger
├── pipeline/
│   ├── run_iteration.sh           # Orchestrates phases 1-6 for one iteration
│   ├── phase1_parallel_research.sh  # 8 parallel Claude calls
│   ├── phase2_pairwise_debate.sh    # 4 parallel debate calls
│   ├── phase3_panel_synthesis.sh    # Single synthesis call
│   ├── phase4_knowledge_extraction.py  # JSON extraction via Claude
│   ├── phase5_kb_write.py          # Merge/create KB entries
│   └── phase6_score_update.py      # Update agent scores + topic registry
├── scoring/
│   ├── update_scores.py  # Incremental mean update of agent contribution scores
│   └── agent_scores.json # Per-agent, per-category performance tracking
├── knowledge_base/
│   ├── concepts/         # One JSON file per concept (confidence, evidence, agents)
│   ├── relationships/    # Concept-pair relationship files
│   ├── frameworks/       # Analytical framework definitions
│   ├── evidence/         # Anti-knowledge + low-confidence pending entries
│   └── index.json        # KB index with metadata
├── config/
│   └── pipeline_config.yaml  # All tunable parameters
└── skill/
    └── SKILL.md          # Operational skill definition for OpenClaw integration
```

## How It Works

### Topic Selection (Curriculum Scheduler)

Topics are scored by: low confidence (30%), staleness (25%), knowledge gaps (25%), unexplored connections (15%), and low depth (5%). The highest-scoring topic is selected. Topics with depth >= 3 switch to "deep dive" mode focusing on subtopics and gap closure.

### Agent Selection (UCB1 Bandit)

Each agent has a performance score per topic category. UCB1 balances exploitation (high-performing agents) with exploration (untried agents). Constraints enforce at least 2 generalists and 1 challenger per iteration.

### Knowledge Base

The KB uses merge-or-create semantics. When a concept is seen again, its confidence is updated via weighted average, evidence is merged (deduplicated), and iteration history is tracked. Claims below confidence threshold 4 go to a low-confidence pending file. Refuted claims go to anti-knowledge.

### Quality Gates

- Phase 1 requires at least 5/8 agents to succeed before downstream phases run
- KB writes require minimum confidence of 4
- Anti-knowledge tracks what was explicitly refuted (preventing re-discovery of dead-end ideas)

## Requirements

- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) (`claude` command available in PATH)
- Python 3.10+
- Bash 4+

## Running

```bash
# Start the research loop (runs continuously)
bash research_loop.sh

# Or run a single iteration manually
TOPIC="monetary_policy" \
TOPIC_CATEGORY="macro_frameworks" \
MODE="overview" \
AGENTS_JSON="path/to/agents.json" \
ITERATION_ID="iter_0001" \
BASE_DIR="$(pwd)" \
LOG_FILE="logs/research.log" \
HEARTBEAT_FILE="logs/heartbeat.json" \
bash pipeline/run_iteration.sh
```

### Configuration

All tunable parameters are in `config/pipeline_config.yaml`:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `phase1_agents` | 8 | Parallel agents per iteration |
| `phase2_pairs` | 4 | Parallel debate pairs |
| `agent_research` timeout | 300s | Per-agent timeout |
| `pairwise_debate` timeout | 300s | Per-debate timeout |
| `panel_synthesis` timeout | 360s | Synthesis timeout |
| `ucb_exploration_constant` | 1.414 | UCB1 C parameter |
| `min_agents_for_downstream` | 5 | Quality gate threshold |
| `min_confidence_for_kb_write` | 4 | KB write confidence floor |

## Topic Coverage

5 categories, 25 topics:

- **Macro Frameworks**: monetary policy, fiscal policy, inflation regimes, growth models, labor markets
- **Credit & Rates**: yield curves, credit cycles, central bank balance sheets, sovereign debt, corporate credit
- **Asset Class Dynamics**: equity cycles, commodity supercycles, FX regimes, real estate, volatility regimes
- **Structural Themes**: deglobalization, energy transition, demographics, AI disruption, fiscal dominance
- **Cross-Asset**: stock-bond correlation, credit-equity linkage, commodity-inflation transmission, FX-rates divergence, risk appetite regimes

## Agent Pool

20 agents across 7 specialist categories + generalists + challengers:

| Category | Agents | Role |
|----------|--------|------|
| Macro Strategist | 2 | GDP, policy, inflation, fiscal |
| Credit Analyst | 2 | Spreads, defaults, HY/IG, private credit |
| Rates Strategist | 2 | Yield curves, duration, term premium |
| Equity Analyst | 2 | Sectors, earnings, valuation, ERP |
| FX Strategist | 2 | Currency regimes, carry, EM risk |
| Commodities | 2 | Energy, metals, agriculture |
| Quant Researcher | 2 | Factors, vol modeling, stat arb |
| Risk Analyst | 2 | Tail risk, correlation, systemic risk |
| Generalist | 2 | Cross-cutting synthesis |
| Challenger | 2 | Contrarian, assumption stress-testing |

## Watchdog Integration (Optional)

The system is designed to run under a watchdog supervisor that monitors three health signals:

| Signal | Threshold | Check |
|--------|-----------|-------|
| Process alive | PID responds to kill -0 | Every 5 min |
| Heartbeat fresh | < 10 min since last heartbeat | Every 5 min |
| Output activity | < 30 min since newest output | Every 5 min |

See `skill/SKILL.md` for full operational documentation including the incident playbook.

## License

MIT
