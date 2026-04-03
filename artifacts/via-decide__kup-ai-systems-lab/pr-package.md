Branch: simba/build-the-visual-refinery-in-srcvisionthermal-ve
Title: Build the 'Visual-Refinery' in src/vision/thermal-verify.js. Use the ...

## Summary
- Repo orchestration task for via-decide/kup-ai-systems-lab
- Goal: Build the 'Visual-Refinery' in src/vision/thermal-verify.js. Use the Jetson's ISP to detect the 'IR-Blur' around a moving tire.

## Testing Checklist
- [ ] Run unit/integration tests
- [ ] Validate command flow
- [ ] Validate generated artifact files

## Risks
- Prompt quality depends on repository metadata completeness.
- GitHub API limits/token scope can block deep inspection.

## Rollback
- Revert branch and remove generated artifact files if workflow output is invalid.