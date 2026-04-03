Branch: simba/create-the-national-rollout-blueprint-generator-
Title: Create the 'National Rollout Blueprint' generator in src/expansion/ro...

## Summary
- Repo orchestration task for via-decide/kup-ai-systems-lab
- Goal: Create the 'National Rollout Blueprint' generator in src/expansion/rollout-template.js. This module must pull data-centric AI reference architectures and edge inference cost-benchmarks from the lab's history and compile them into a ready-to-deploy RFP (Request for Proposal) template. [span_9](start_span)constraints: Ensure the blueprint emphasizes why the "Kutch Extreme Climate" proof-of-concept makes the system robust for any tropical or subtropical region[span_9](end_span).

## Testing Checklist
- [ ] Run unit/integration tests
- [ ] Validate command flow
- [ ] Validate generated artifact files

## Risks
- Prompt quality depends on repository metadata completeness.
- GitHub API limits/token scope can block deep inspection.

## Rollback
- Revert branch and remove generated artifact files if workflow output is invalid.