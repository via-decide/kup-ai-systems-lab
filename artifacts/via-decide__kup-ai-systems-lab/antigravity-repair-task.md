Repair mode for repository via-decide/kup-ai-systems-lab.

TARGET
Validate and repair only the files touched by the previous implementation.

TASK
Implement the 'Regional Rollout Engine' in src/expansion/national-deploy.js. Create a configuration-driven deployment script that clones the 'Kutch Reference Architecture' for new geographical zones. [span_5](start_span)[span_6](start_span)constraints: The script must adjust the 'Scenario 2' chaos parameters automatically based on local climate data (e.g., adjusting the temperature drift threshold for Rajasthan's heat).[span_5](end_span)[span_6](end_span)

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