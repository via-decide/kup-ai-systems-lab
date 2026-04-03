Branch: simba/implement-the-inference-gatekeeper-in-srcvisionl
Title: Implement the 'Inference Gatekeeper' in src/vision/logic-gate.c. Usin...

## Summary
- Repo orchestration task for via-decide/kup-ai-systems-lab
- Goal: Implement the 'Inference Gatekeeper' in src/vision/logic-gate.c. Using NVIDIA DeepStream, create a trigger that only activates full model inference if the "Motion Delta" or "Thermal Gradient" exceeds a specific threshold.

## Testing Checklist
- [ ] Run unit/integration tests
- [ ] Validate command flow
- [ ] Validate generated artifact files

## Risks
- Prompt quality depends on repository metadata completeness.
- GitHub API limits/token scope can block deep inspection.

## Rollback
- Revert branch and remove generated artifact files if workflow output is invalid.