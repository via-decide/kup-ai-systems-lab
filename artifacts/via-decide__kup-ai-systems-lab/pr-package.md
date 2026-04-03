Branch: simba/implement-the-regional-calibrator-in-srcexpansio
Title: Implement the 'Regional Calibrator' in src/expansion/heat-calibration...

## Summary
- Repo orchestration task for via-decide/kup-ai-systems-lab
- Goal: Implement the 'Regional Calibrator' in src/expansion/heat-calibration.js. Create a script that automatically adjusts the 'Scenario 2' chaos parameters (temperature-drift thresholds) based on local meteorological data for the new deployment zone.

## Testing Checklist
- [ ] Run unit/integration tests
- [ ] Validate command flow
- [ ] Validate generated artifact files

## Risks
- Prompt quality depends on repository metadata completeness.
- GitHub API limits/token scope can block deep inspection.

## Rollback
- Revert branch and remove generated artifact files if workflow output is invalid.