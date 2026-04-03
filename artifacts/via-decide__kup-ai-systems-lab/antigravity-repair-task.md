Repair mode for repository via-decide/kup-ai-systems-lab.

TARGET
Validate and repair only the files touched by the previous implementation.

TASK
Implement the 'Hardware-In-The-Loop' (HITL) connector in src/bridge/jetson-sim-link.js. [span_14](start_span)Create a pipeline where the Digital Twin sends vehicle passages directly to a physical Jetson Orin NX for inference, rather than simulating the inference locally[span_14](end_span). [span_15](start_span)[span_16](start_span)constraints: Log the real-world latency and power consumption of the Jetson during 1M passage bursts[span_15](end_span)[span_16](end_span). [span_17](start_span)Ensure the Sovereign terminal theme displays a live comparison between "Simulated Latency" vs "Actual Edge Latency"[span_17](end_span).

RULES
1. Audit touched files first and identify regressions.
2. Preserve architecture and naming conventions.
3. Make minimal repairs only; do not expand scope.
4. Re-run checks and provide concise root-cause notes.
5. Return complete contents for changed files only.

SOP: REPAIR PROTOCOL (MANDATORY)
1. Strict Fix Only: Do not use repair mode to expand scope or add features.
2. Regression Check: Audit why previous attempt failed before proposing a fix.
3. Minimal Footprint: Only return contents for the actual repaired files.

REPO CONTEXT
- README snippet:
# kup-ai-systems-lab
- AGENTS snippet:
not found
- package.json snippet:
not found