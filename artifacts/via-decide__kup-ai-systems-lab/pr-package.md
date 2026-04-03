Branch: simba/implement-the-thermal-stress-profiler-in-srcbenc
Title: Implement the 'Thermal Stress Profiler' in src/benchmarks/power-therm...

## Summary
- Repo orchestration task for via-decide/kup-ai-systems-lab
- Goal: Implement the 'Thermal Stress Profiler' in src/benchmarks/power-thermal.py. Calculate the thermal dissipation requirement using the formula: $R_{th} = \frac{T_{junction} - T_{ambient}}{P_{total}}$.

## Testing Checklist
- [ ] Run unit/integration tests
- [ ] Validate command flow
- [ ] Validate generated artifact files

## Risks
- Prompt quality depends on repository metadata completeness.
- GitHub API limits/token scope can block deep inspection.

## Rollback
- Revert branch and remove generated artifact files if workflow output is invalid.