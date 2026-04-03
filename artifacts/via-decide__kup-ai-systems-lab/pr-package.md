Branch: simba/implement-the-regional-rollout-engine-in-srcexpa
Title: Implement the 'Regional Rollout Engine' in src/expansion/national-dep...

## Summary
- Repo orchestration task for via-decide/kup-ai-systems-lab
- Goal: Implement the 'Regional Rollout Engine' in src/expansion/national-deploy.js. Create a configuration-driven deployment script that clones the 'Kutch Reference Architecture' for new geographical zones. [span_5](start_span)[span_6](start_span)constraints: The script must adjust the 'Scenario 2' chaos parameters automatically based on local climate data (e.g., adjusting the temperature drift threshold for Rajasthan's heat).[span_5](end_span)[span_6](end_span)

## Testing Checklist
- [ ] Run unit/integration tests
- [ ] Validate command flow
- [ ] Validate generated artifact files

## Risks
- Prompt quality depends on repository metadata completeness.
- GitHub API limits/token scope can block deep inspection.

## Rollback
- Revert branch and remove generated artifact files if workflow output is invalid.