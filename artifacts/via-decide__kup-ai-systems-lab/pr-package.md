Branch: simba/build-the-port-logistics-adapter-in-srctemplates
Title: Build the 'Port Logistics Adapter' in src/templates/port-adaptation.j...

## Summary
- Repo orchestration task for via-decide/kup-ai-systems-lab
- Goal: Build the 'Port Logistics Adapter' in src/templates/port-adaptation.json. [span_26](start_span)[span_27](start_span)Use the Jetson Orin architecture defined for the Deendayal Port partner to re-train the Vora model for heavy-duty fleet tire monitoring[span_26](end_span)[span_27](end_span). [span_28](start_span)constraints: The adapter must use the "Data-Centric AI" principle: correcting 10% of mislabeled training data from port environments is more valuable than doubling model complexity[span_28](end_span).

## Testing Checklist
- [ ] Run unit/integration tests
- [ ] Validate command flow
- [ ] Validate generated artifact files

## Risks
- Prompt quality depends on repository metadata completeness.
- GitHub API limits/token scope can block deep inspection.

## Rollback
- Revert branch and remove generated artifact files if workflow output is invalid.