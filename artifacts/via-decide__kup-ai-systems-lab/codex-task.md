You are working in repository via-decide/kup-ai-systems-lab on branch main.

MISSION
Implement the 'Inference Gatekeeper' in src/vision/logic-gate.c. Using NVIDIA DeepStream, create a trigger that only activates full model inference if the "Motion Delta" or "Thermal Gradient" exceeds a specific threshold.

CONSTRAINTS
Calculate the "Inference Energy Savings" ($E_{saved} = P_{full} \times (1 - \text{DutyCycle})$). Log the savings to the Sovereign terminal. This is critical for the "Cost-per-lane" metric in the NHAI brief.

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