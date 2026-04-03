Branch: simba/implement-duty-cycle-management-in-srcpowerjetso
Title: Implement 'Duty-Cycle Management' in src/power/jetson-pulse.py. Creat...

## Summary
- Repo orchestration task for via-decide/kup-ai-systems-lab
- Goal: Implement 'Duty-Cycle Management' in src/power/jetson-pulse.py. Create a trigger that only ramps the GPU to 'Max-P' (Performance) mode when the thermal sensor detects a vehicle approach, then returns to 'Quiet' mode.

## Testing Checklist
- [ ] Run unit/integration tests
- [ ] Validate command flow
- [ ] Validate generated artifact files

## Risks
- Prompt quality depends on repository metadata completeness.
- GitHub API limits/token scope can block deep inspection.

## Rollback
- Revert branch and remove generated artifact files if workflow output is invalid.