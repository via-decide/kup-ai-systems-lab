You are working in repository via-decide/kup-ai-systems-lab on branch main.

MISSION
Implement the 'Physical Stream Ingestor' in src/bridge/nhai-sync.js. Create a secure WebSocket listener that maps raw telemetry from the NH-41 physical sensors (Kistler WIM + Thermal Cameras) into the 'Scenario 2' refinery.

CONSTRAINTS
- Use the 'Sovereign' Auth-Token system to prevent unauthorized data injection. - Log "PHYSICAL SYNC ACTIVE: [SITE_ID]" in the terminal. - Ensure the 'Edge Architect' agent validates that real-world noise matches the $D_{KL}$ simulated baseline.

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