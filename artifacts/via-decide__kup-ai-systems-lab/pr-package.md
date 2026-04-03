Branch: simba/implement-the-jetson-optimizer-in-srcbridgetrt-e
Title: Implement the 'Jetson Optimizer' in src/bridge/trt-exporter.py. Creat...

## Summary
- Repo orchestration task for via-decide/kup-ai-systems-lab
- Goal: Implement the 'Jetson Optimizer' in src/bridge/trt-exporter.py. Create a pipeline that takes the best-performing founder model and converts it into a TensorRT engine for the Jetson Orin NX.

## Testing Checklist
- [ ] Run unit/integration tests
- [ ] Validate command flow
- [ ] Validate generated artifact files

## Risks
- Prompt quality depends on repository metadata completeness.
- GitHub API limits/token scope can block deep inspection.

## Rollback
- Revert branch and remove generated artifact files if workflow output is invalid.