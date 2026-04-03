You are working in repository via-decide/kup-ai-systems-lab on branch main.

MISSION
Build the 'Drift Debugger' in src/debug/context-rot-detect.py. Develop a script that calculates the "Semantic Entropy" of the LLM's output. If the entropy score spikes (indicating the model is guessing rather than reasoning), flag the specific sensor passage for manual re-labeling.

CONSTRAINTS
Use the LaTeX formula for Entropy: $H(X) = -\sum_{i=1}^{n} P(x_i) \log P(x_i)$. Log the "Entropy Spike" in the Sovereign terminal to alert the founder.

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