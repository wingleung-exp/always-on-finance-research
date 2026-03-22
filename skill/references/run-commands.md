# Run Commands Reference

## Start

```bash
# Full stack (loop + watchdog) — idempotent, safe to run multiple times
bash /data/.openclaw/workspace/scripts/start_research_stack.sh
```

## Stop

```bash
# Clean shutdown of loop + watchdog
bash /data/.openclaw/workspace/scripts/stop_research_stack.sh
```

## Health / Status

```bash
# Single health check (exit 0=HEALTHY, 1=UNHEALTHY, 2=CRITICAL)
bash /data/.openclaw/workspace/scripts/research_watchdog_check.sh

# Current heartbeat
cat /data/.openclaw/workspace/logs/research_heartbeat.json

# Alert flag (empty = no alerts)
cat /data/.openclaw/workspace/logs/research_watchdog_alert.flag 2>/dev/null

# Watchdog audit log (last 30 entries)
tail -30 /data/.openclaw/workspace/logs/research_watchdog.log

# Research loop log (last 50 lines)
tail -50 /data/.openclaw/workspace/logs/research_loop.log

# Loop PID
cat /data/.openclaw/workspace/finance_research/.loop_pid

# Watchdog PID
cat /data/.openclaw/workspace/logs/.watchdog_service.pid
```

## Research Output

```bash
# Latest notes across all agents
ls -lt /data/.openclaw/workspace/finance_research/notes/*/ | head -20

# Memory files
ls -la /data/.openclaw/workspace/finance_research/memory/

# Loop iteration count (from heartbeat)
jq .iteration /data/.openclaw/workspace/logs/research_heartbeat.json
```
