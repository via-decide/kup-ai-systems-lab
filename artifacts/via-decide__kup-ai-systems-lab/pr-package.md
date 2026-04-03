Branch: simba/implement-the-physical-stream-ingestor-in-srcbri
Title: Implement the 'Physical Stream Ingestor' in src/bridge/nhai-sync.js. ...

## Summary
- Repo orchestration task for via-decide/kup-ai-systems-lab
- Goal: Implement the 'Physical Stream Ingestor' in src/bridge/nhai-sync.js. Create a secure WebSocket listener that maps raw telemetry from the NH-41 physical sensors (Kistler WIM + Thermal Cameras) into the 'Scenario 2' refinery.

## Testing Checklist
- [ ] Run unit/integration tests
- [ ] Validate command flow
- [ ] Validate generated artifact files

## Risks
- Prompt quality depends on repository metadata completeness.
- GitHub API limits/token scope can block deep inspection.

## Rollback
- Revert branch and remove generated artifact files if workflow output is invalid.