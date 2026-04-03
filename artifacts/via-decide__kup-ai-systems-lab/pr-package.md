Branch: simba/build-the-thermal-sync-utility-in-srcbridgejetso
Title: Build the 'Thermal Sync' utility in src/bridge/jetson-thermal-check.p...

## Summary
- Repo orchestration task for via-decide/kup-ai-systems-lab
- Goal: Build the 'Thermal Sync' utility in src/bridge/jetson-thermal-check.py. Run the Kalman-filtered inference on the Jetson Orin NX and measure the $T_{junction}$ (junction temperature) and $J_{load}$ (GPU load).

## Testing Checklist
- [ ] Run unit/integration tests
- [ ] Validate command flow
- [ ] Validate generated artifact files

## Risks
- Prompt quality depends on repository metadata completeness.
- GitHub API limits/token scope can block deep inspection.

## Rollback
- Revert branch and remove generated artifact files if workflow output is invalid.