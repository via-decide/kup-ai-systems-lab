Branch: simba/build-the-drift-debugger-in-srcdebugcontext-rot-
Title: Build the 'Drift Debugger' in src/debug/context-rot-detect.py. Develo...

## Summary
- Repo orchestration task for via-decide/kup-ai-systems-lab
- Goal: Build the 'Drift Debugger' in src/debug/context-rot-detect.py. Develop a script that calculates the "Semantic Entropy" of the LLM's output. If the entropy score spikes (indicating the model is guessing rather than reasoning), flag the specific sensor passage for manual re-labeling.

## Testing Checklist
- [ ] Run unit/integration tests
- [ ] Validate command flow
- [ ] Validate generated artifact files

## Risks
- Prompt quality depends on repository metadata completeness.
- GitHub API limits/token scope can block deep inspection.

## Rollback
- Revert branch and remove generated artifact files if workflow output is invalid.