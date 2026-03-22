# Incident Playbook

## Triage Flow

```
Alert received
  ├─ Check heartbeat.json → is epoch recent?
  │   ├─ Yes → loop running, check output staleness
  │   └─ No  → check PID alive
  │       ├─ PID dead → restart via start_research_stack.sh
  │       └─ PID alive → zombie — kill PID, then restart
  └─ Check alert flag → crash loop?
      ├─ Yes → investigate root cause before restarting
      └─ No  → standard restart
```

## Common Scenarios

### 1. Loop process died

**Symptoms**: `process_dead`, no heartbeat updates.
**Action**: Run `bash scripts/start_research_stack.sh`. Idempotent — safe to run.
**Verify**: `cat logs/research_heartbeat.json` — epoch should advance within 120s.

### 2. Zombie (hung process)

**Symptoms**: PID alive but heartbeat age > 360s.
**Action**: Watchdog auto-handles. If manual: `kill <PID>`, wait 2s, `kill -9 <PID>` if needed, then restart.
**Verify**: New PID in `.loop_pid`, fresh heartbeat.

### 3. Output stale but heartbeat fresh

**Symptoms**: Heartbeat updating, but no new note files in 15 min.
**Action**: Check `logs/research_loop.log` for errors in agent execution. Loop may be running but agents are failing to write output.
**Verify**: Tail research_loop.log for recent errors.

### 4. Crash loop (4+ restarts/hour)

**Symptoms**: `logs/research_watchdog_alert.flag` exists with CRITICAL.
**Action**:
1. Stop the stack: `bash scripts/stop_research_stack.sh`
2. Check `logs/research_loop.log` and `logs/research_loop_stdout.log` for root cause
3. Common causes: disk full, permission error, broken agent definition, API rate limit
4. Fix root cause, then restart: `bash scripts/start_research_stack.sh`
5. Clear alert: `rm logs/research_watchdog_alert.flag`

### 5. Watchdog itself is down

**Symptoms**: No recent entries in `logs/research_watchdog.log`.
**Action**: `bash scripts/start_research_stack.sh` — restarts both loop and watchdog.
**Verify**: `cat logs/.watchdog_service.pid` and check `kill -0 <PID>`.

## Post-Incident

- Check `logs/research_watchdog.log` for pattern of failures
- If recurring: review agent definitions in `finance_research/agents/`
- Update `finance_research/memory/lessons_learned.md` with findings
