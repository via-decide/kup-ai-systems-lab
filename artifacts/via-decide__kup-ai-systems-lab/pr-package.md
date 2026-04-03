Branch: simba/build-the-million-passage-dashboard-in-srcmonito
Title: Build the 'Million-Passage Dashboard' in src/monitor/throughput.js. T...

## Summary
- Repo orchestration task for via-decide/kup-ai-systems-lab
- Goal: Build the 'Million-Passage Dashboard' in src/monitor/throughput.js. Track: 1) Passages per second, 2) Token savings (vs. legacy), and 3) M4 Thermal Headroom ($T_{max} - T_{current}$).

## Testing Checklist
- [ ] Run unit/integration tests
- [ ] Validate command flow
- [ ] Validate generated artifact files

## Risks
- Prompt quality depends on repository metadata completeness.
- GitHub API limits/token scope can block deep inspection.

## Rollback
- Revert branch and remove generated artifact files if workflow output is invalid.