# Health Criteria

## Three-Signal Check (all must pass)

| Signal | Source | Threshold | Failure Code |
|--------|--------|-----------|--------------|
| Process alive | `finance_research/.loop_pid` → `kill -0` | PID responds | `process_dead` / `no_pidfile` |
| Heartbeat fresh | `logs/research_heartbeat.json` → epoch field | < 360s (6 min) | `stale_heartbeat` / `no_heartbeat_file` |
| Output activity | Newest file in `finance_research/notes/` | < 900s (15 min) | `no_new_output` / `no_output_files` |

## Zombie Detection

| Condition | Classification |
|-----------|---------------|
| Process alive + heartbeat stale | `zombie_hung` |
| Process alive + output stale | `zombie_no_output` |

Zombies are killed (SIGTERM → 2s → SIGKILL) then restarted.

## Exit Codes

| Code | Meaning |
|------|---------|
| `0` | HEALTHY — all signals pass |
| `1` | UNHEALTHY — restarted successfully |
| `2` | CRITICAL — restart failed or crash loop (4+ in 1hr) |

## Thresholds Summary

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Check interval | 300s | ~2× max iteration time |
| Heartbeat stale | 360s | ~3× max iteration time |
| Output stale | 900s | Notes must flow regularly |
| Crash window | 3600s | Restart frequency measurement |
| Max crashes/window | 4 | Escalation trigger |
| Post-restart verify | 60s | Heartbeat must advance |
