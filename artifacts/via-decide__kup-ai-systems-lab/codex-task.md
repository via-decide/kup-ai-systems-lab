You are working in repository via-decide/kup-ai-systems-lab on branch main.

MISSION
Implement the 'Hardware-In-The-Loop' (HITL) connector in src/bridge/jetson-sim-link.js. [span_14](start_span)Create a pipeline where the Digital Twin sends vehicle passages directly to a physical Jetson Orin NX for inference, rather than simulating the inference locally[span_14](end_span). [span_15](start_span)[span_16](start_span)constraints: Log the real-world latency and power consumption of the Jetson during 1M passage bursts[span_15](end_span)[span_16](end_span). [span_17](start_span)Ensure the Sovereign terminal theme displays a live comparison between "Simulated Latency" vs "Actual Edge Latency"[span_17](end_span).

CONSTRAINTS
Preserve existing code; prefer additive changes.

PROCESS (MANDATORY)
1. Read README.md and AGENTS.md before editing.
2. Audit architecture before coding. Summarize current behavior.
3. Preserve unrelated working code. Prefer additive modular changes.
4. Implement the smallest safe change set for the stated goal.
5. Run validation commands and fix discovered issues.
6. Self-review for regressions, missing env wiring, and docs drift.
7. Return complete final file contents for every modified or created file.

REPO AUDIT CONTEXT
- Description: 
- Primary language: unknown
- README snippet:
# kup-ai-systems-lab

- AGENTS snippet:
not found


SOP: PRE-MODIFICATION PROTOCOL (MANDATORY)
1. Adherence to Instructions: No deviations without explicit user approval.
2. Mandatory Clarification: Immediately ask if instructions are ambiguous or incomplete.
3. Proposal First: Always propose optimizations or fixes before implementing them.
4. Scope Discipline: Do not add unrequested features or modify unrelated code.
5. Vulnerability Check: Immediately flag and explain security risks.

OUTPUT REQUIREMENTS
- Include: implementation summary, checks run, risks, rollback notes.
- Generate branch + PR package.
- Keep prompts deterministic and preservation-first.