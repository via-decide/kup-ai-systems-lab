Branch: simba/implement-the-hardware-in-the-loop-hitl-connecto
Title: Implement the 'Hardware-In-The-Loop' (HITL) connector in src/bridge/j...

## Summary
- Repo orchestration task for via-decide/kup-ai-systems-lab
- Goal: Implement the 'Hardware-In-The-Loop' (HITL) connector in src/bridge/jetson-sim-link.js. [span_14](start_span)Create a pipeline where the Digital Twin sends vehicle passages directly to a physical Jetson Orin NX for inference, rather than simulating the inference locally[span_14](end_span). [span_15](start_span)[span_16](start_span)constraints: Log the real-world latency and power consumption of the Jetson during 1M passage bursts[span_15](end_span)[span_16](end_span). [span_17](start_span)Ensure the Sovereign terminal theme displays a live comparison between "Simulated Latency" vs "Actual Edge Latency"[span_17](end_span).

## Testing Checklist
- [ ] Run unit/integration tests
- [ ] Validate command flow
- [ ] Validate generated artifact files

## Risks
- Prompt quality depends on repository metadata completeness.
- GitHub API limits/token scope can block deep inspection.

## Rollback
- Revert branch and remove generated artifact files if workflow output is invalid.