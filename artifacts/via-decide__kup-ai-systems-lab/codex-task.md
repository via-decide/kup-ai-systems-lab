You are working in repository via-decide/kup-ai-systems-lab on branch main.

MISSION
Implement the 'Autonomous Infrastructure Scheduler' in src/orchestrator/sovereign-scheduler.py.

CONSTRAINTS
- Design a priority queue capable of handling 100k infrastructure events per minute. - Implement dynamic task arbitration between: SENSOR_NETWORK TRAFFIC_ENGINE INFRASTRUCTURE_AI - Use adaptive load balancing formula: Load_factor = Events_per_sec / Node_capacity - If Load_factor > 0.9 trigger emergency compute burst. - Log "SCHEDULER_STATE: AUTONOMOUS_INFRASTRUCTURE_COORDINATION_ACTIVE".

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
- Primary language: Python
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