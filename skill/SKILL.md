---
name: always_on_finance_research
description: "Continuous Claude Code-driven finance research loop with parallel multi-agent analysis, debate, validation, and CIO synthesis. OpenClaw watchdog supervision. Use when: (1) Starting or restarting the always-on multi-agent research engine, (2) Checking health/status of the running research loop, (3) Investigating why research output stopped or degraded, (4) Understanding the research loop architecture and agent roster, (5) Resuming research after a system restart or crash. This skill defines the operational contract between Claude Code (the worker) and OpenClaw (the monitor/restart layer)."
---

# Always-On Finance Research

Operational instructions for the continuous multi-agent finance research loop. Current production runtime uses the v2 parallel+debate+validation script backend, with OpenClaw monitoring health and restarting on failure.

## Role Separation

| Layer | Role | Does NOT |
|-------|------|----------|
| **Research loop script (`finance_research/research_loop.sh`)** | Worker — runs parallel agents, debate, validation, synthesis per iteration | Monitor itself, restart itself |
| **OpenClaw watchdog (`research_watchdog_service.sh`)** | Supervisor — checks health every 5 min, kills zombies, restarts on failure | Generate research note content |

The watchdog never modifies research output. It only observes process/heartbeat/output signals and restarts the loop when unhealthy.

## Multi-Agent Research Loop (v2 — TRUE Concurrent Execution)

Stage-2 runs **>=8 agents concurrently** via parallel `claude --print` calls — these are real simultaneous Claude invocations, NOT sequential fake roles or simulated personas. Each agent is an independent process writing its own thesis file.

Each iteration follows this pipeline:

1. **Topic Selection** — One broad topic chosen for all agents (20-topic pool)
2. **Memory Grounding (per-agent)** — Before writing, each agent MUST first read current memory files (master_memory, key_frameworks, investment_playbook, experience_log) and the latest prior synthesis to ground on accumulated knowledge
3. **Concurrent Agent Execution** — All 8+ agents launch simultaneously as parallel Claude calls, each writing an independent thesis file to `agent_outputs/iteration_N/<agent>.md`. No agent waits for another; all run in true parallel
4. **Debate Phase (mandatory post-agent)** — CIO-moderated debate identifies contradictions, challenges assumptions, finds blind spots, scores evidence quality. Output: `debates/iteration_N.md`
5. **Validation Phase (mandatory post-agent)** — Independent analyst checks internal consistency, logical validity, unsupported claims, confidence calibration. Output: `validation/iteration_N.md`
6. **Final Synthesis (mandatory post-agent)** — CIO produces actionable output with PM takeaways, risk matrix, positioning recommendations, monitoring triggers. Output: `final_outputs/iteration_N.md`
7. **Experience Logging** — Structured entry appended to `memory/experience_log.md` + per-iteration record in `experience_logs/iteration_N.md`
8. **Retrieval-KB Routing (reuse-first)** — Before creating any new retrieval-ready destination, inspect `md/` and `md/topics/` and reuse existing topic files where appropriate. Only create missing files/folders when no suitable destination exists (avoid parallel duplicate structures, e.g. prefer existing `bonds.md` for fixed-income content unless a structural split is explicitly needed)
9. **Retrieval Distillation Quality Gate** — Before appending to retrieval-ready docs (`FINANCE_KB.md`, topic docs, `FINANCE_QA_INDEX.md`), require quality signals from the completed iteration. Gate checks for clear finding, evidence/reasoning, market implication, confidence, and reusable Q&A value. If quality is low/noisy/repetitive, keep raw outputs + memory logs but skip retrieval-ready append for that iteration.
10. **Deduplication Gate (retrieval layer)** — Before writing a KB block, topic block, or QA entry, compare against recent entries in destination files. If identical or near-identical wording, skip append. If there is meaningful refinement but high overlap, append a compact "Updated Understanding" marker instead of duplicating full content.
11. **Lightweight Metadata Tags** — Every retrieval-ready KB/topic entry should include compact tags for: primary topic, related topics, time horizon (near-term / medium-term / structural / mixed), and market regime context (e.g., inflation, recession, soft landing, policy easing, risk-off, risk-on, stagflation, mixed).
12. **Revision-Aware Save Behavior** — If a new iteration materially changes prior view, do not append a conflicting standalone duplicate. Mark entry as **Revised View** or **Updated Understanding**, state what changed briefly, keep prior view only for audit/history context, and make the newest actionable view explicit for retrieval.
13. **Rolling Summary View** — Maintain `/data/.openclaw/workspace/md/CURRENT_MARKET_VIEW.md` as a concise latest answer-ready snapshot (not archive) with sections: Current Regime, Highest-Confidence Views, Key Risks, Cross-Asset Implications, Open Questions, Last Updated.

**Sequential fallback is NOT the default.** Agents always launch concurrently. Sequential execution is used ONLY on explicit runtime failure (e.g., resource exhaustion, API rate limits). If fallback triggers, it is logged as an anomaly in the experience log.

### Agent Roster (8 specialists)

1. `macro_strategist` — GDP cycles, central bank policy, fiscal dynamics, inflation regimes
2. `equity_analyst` — sector rotation, earnings cycles, valuation frameworks, equity risk premium
3. `fixed_income` — yield curves, credit analysis, duration management, sovereign debt
4. `commodities` — energy markets, precious metals, industrial commodities, supply/demand
5. `fx_strategist` — currency valuation, carry dynamics, EM currency risk, capital flows
6. `crypto_analyst` — crypto cycles, DeFi, on-chain analytics, regulatory developments
7. `alternatives` — PE, hedge funds, real estate, infrastructure, alternative risk premia
8. `quant_strategies` — factor investing, volatility modeling, stat arb, risk parity, tail risk

Each agent receives a distinct role prompt ensuring independent, specialized analysis. All agents execute as true concurrent Claude calls — no sequential simulation. All outputs include required sections: Executive Summary, Core Thesis, Key Assumptions, Risk Factors, Evidence, Cross-Asset Implications, Confidence Level, What Could Change Your Mind.

## Storage Paths

### Research Output
```
/data/.openclaw/workspace/finance_research/
├── agent_outputs/           # Per-iteration agent analyses
│   └── iteration_N/         # 8 agent .md files per iteration
│       ├── macro_strategist.md
│       ├── equity_analyst.md
│       └── ... (8 total)
├── debates/                 # Debate transcripts
│   └── iteration_N.md
├── validation/              # Validation reports
│   └── iteration_N.md
├── final_outputs/           # CIO synthesis documents
│   └── iteration_N.md
├── experience_logs/         # Per-iteration experience records
│   └── iteration_N.md
├── memory/                  # Long-term memory files
├── notes/                   # Legacy per-agent notes (pre-v2)
├── research_loop.sh         # Main loop script (v2)
└── .loop_pid                # Current loop PID
```

### Logs
```
/data/.openclaw/workspace/logs/research_loop.log        # Detailed execution log
/data/.openclaw/workspace/logs/research_heartbeat.json   # Heartbeat (written per phase)
```

### Memory Files

Located in `/data/.openclaw/workspace/finance_research/memory/`:

| File | Purpose |
|------|---------|
| `master_memory.md` | Cumulative research synthesis and key findings |
| `key_frameworks.md` | Analytical frameworks and mental models |
| `investment_playbook.md` | Actionable investment theses and positioning |
| `experience_log.md` | Structured log of each iteration's outcomes |

The loop updates these files as research accumulates. They persist across restarts and are read by agents for grounding context at each iteration.

## Watchdog Health Checks

The watchdog runs every **5 minutes** and evaluates three signals:

| Check | Threshold | Failure |
|-------|-----------|---------|
| Process alive | PID from `.loop_pid` responds to `kill -0` | `process_dead` |
| Heartbeat fresh | < 600s (10 min) since last heartbeat epoch | `stale_heartbeat` |
| Output activity | < 1800s (30 min) since newest output file | `no_new_output` |

**All three must pass** for HEALTHY status. Thresholds are sized for v2 iterations (~5-12 min each with parallel agents + debate + validation + synthesis).

Zombie detection: process alive but heartbeat/output stale → kill + restart.
Telegram/runtime mismatch detection: if Telegram is paired but detached/duplicate runtime is detected, watchdog forces Telegram runtime restart from the canonical supervisor path.

### Heartbeat Phases

The v2 loop writes heartbeats at each phase within an iteration:
`agents_spawning` → `agents_complete` → `debate_phase` → `validation_phase` → `synthesis_phase` → `iteration_complete`

This keeps the heartbeat fresh even during long iterations.

### Alert Policy

- **Healthy**: silent — audit log only (`logs/research_watchdog.log`)
- **Unhealthy + restart succeeds**: logged, no user alert
- **Restart fails**: CRITICAL alert flag written
- **4+ restarts in 1 hour**: CRITICAL crash-loop alert flag

## Trigger / Run Commands

Start the full stack (loop + watchdog):
```bash
bash /data/.openclaw/workspace/scripts/start_research_stack.sh
```

Stop everything:
```bash
bash /data/.openclaw/workspace/scripts/stop_research_stack.sh
```

Manual health check:
```bash
bash /data/.openclaw/workspace/scripts/research_watchdog_check.sh
```

View current heartbeat:
```bash
cat /data/.openclaw/workspace/logs/research_heartbeat.json
```

Check for alerts:
```bash
cat /data/.openclaw/workspace/logs/research_watchdog_alert.flag 2>/dev/null
```

View watchdog audit log:
```bash
tail -30 /data/.openclaw/workspace/logs/research_watchdog.log
```

## Monitoring Cadence

| Interval | What |
|----------|------|
| ~5-12 min | Full iteration (>=8 concurrent agents + mandatory debate + validation + synthesis) |
| 60-180s | Sleep between iterations |
| 300s (5 min) | Watchdog health check |
| Per phase | Heartbeat updates within each iteration |
| Continuous | Watchdog service daemon (flock singleton) |

## Integration with Existing Scripts

This skill documents and references the existing operational backend. **Do not duplicate or replace these scripts**:

- `finance_research/research_loop.sh` — the research engine (v2: parallel+debate+validation)
- `scripts/start_research_stack.sh` — idempotent stack launcher
- `scripts/stop_research_stack.sh` — clean shutdown
- `scripts/research_watchdog_service.sh` — watchdog daemon
- `scripts/research_watchdog_check.sh` — single health check
- `md/RESEARCH_WATCHDOG.md` — full watchdog architecture doc

## Operational Note — Telegram Responsiveness During Heavy Iterations

If Telegram becomes non-responsive while research appears active:
1. Verify singleton Telegram supervisor and singleton plugin runtime first.
2. Verify pipeline stage progress (not just process existence).
3. Prefer controlled restart of Telegram supervisor runtime if channel ownership drift is detected.
4. Keep research Claude calls isolated from channel session persistence and use stdin/temp-file prompts for long stages.
