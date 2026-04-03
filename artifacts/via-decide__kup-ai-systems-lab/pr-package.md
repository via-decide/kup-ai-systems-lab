Branch: simba/create-the-hardware-provisioning-script-in-scrip
Title: Create the 'Hardware Provisioning' script in scripts/setup-jetson.sh....

## Summary
- Repo orchestration task for via-decide/kup-ai-systems-lab
- Goal: Create the 'Hardware Provisioning' script in scripts/setup-jetson.sh. This script should automate the installation of the Zayvora-Edge environment on the Jetson Orin NX, including the local inference engine and the 'Hardware-In-The-Loop' bridge.

## Testing Checklist
- [ ] Run unit/integration tests
- [ ] Validate command flow
- [ ] Validate generated artifact files

## Risks
- Prompt quality depends on repository metadata completeness.
- GitHub API limits/token scope can block deep inspection.

## Rollback
- Revert branch and remove generated artifact files if workflow output is invalid.