Branch: simba/implement-the-sanjiwani-health-monitor-in-srcmon
Title: Implement the 'Sanjiwani Health Monitor' in src/monitoring/system-hea...

## Summary
- Repo orchestration task for via-decide/kup-ai-systems-lab
- Goal: Implement the 'Sanjiwani Health Monitor' in src/monitoring/system-health.js. [span_13](start_span)[span_14](start_span)This module must ping the Mac Mini's local LLM (Vora), the SQLite database, the Telegram Bot, and the Jetson HITL bridge every 60 seconds[span_13](end_span)[span_14](end_span).

## Testing Checklist
- [ ] Run unit/integration tests
- [ ] Validate command flow
- [ ] Validate generated artifact files

## Risks
- Prompt quality depends on repository metadata completeness.
- GitHub API limits/token scope can block deep inspection.

## Rollback
- Revert branch and remove generated artifact files if workflow output is invalid.