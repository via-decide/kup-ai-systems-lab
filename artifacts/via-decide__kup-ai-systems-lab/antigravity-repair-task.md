Repair mode for repository via-decide/kup-ai-systems-lab.

TARGET
Validate and repair only the files touched by the previous implementation.

TASK
Build the 'Port Logistics Adapter' in src/templates/port-adaptation.json. [span_26](start_span)[span_27](start_span)Use the Jetson Orin architecture defined for the Deendayal Port partner to re-train the Vora model for heavy-duty fleet tire monitoring[span_26](end_span)[span_27](end_span). [span_28](start_span)constraints: The adapter must use the "Data-Centric AI" principle: correcting 10% of mislabeled training data from port environments is more valuable than doubling model complexity[span_28](end_span).

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