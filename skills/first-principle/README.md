# First-Principles Problem Solving

**Version:** 1.4.0

Use this skill when the outcome, evidence, constraints, or validation method are unclear; when a solution is being treated as given; or when conventions may be mistaken for requirements. It applies across product decisions, research, writing, operations, learning, procurement, and engineering.

## What it does

It starts from the outcome and the least-dependent facts and constraints, questions inherited assumptions, and rebuilds an answer that fits the evidence. Its central check is whether each proposed step or structure is required by the outcome, which helps prevent manufactured complexity.

The completion criterion depends on the task:

- **Understanding work:** give a supported explanation, address the strongest rival explanation, and state what evidence would overturn the conclusion. A mechanism is not required.
- **Change work:** derive the smallest complete mechanism within scope, including the relevant states, invariants, failure or recovery behavior, observability, and acceptance evidence.

First principles are not maximal decomposition. Use the level of detail that preserves behavior relevant to the outcome. Treat physical, legal, contractual, safety, and stated acceptance limits as hard constraints; question conventions and inherited practices only when their ownership and purpose allow it.

## Use it when

- the user names a solution before defining the result they need;
- a convention or inherited process is treated as necessary without evidence;
- several plausible approaches compete and the choice has meaningful consequences;
- the request is likely to expand or important constraints and failure behavior are unclear;
- a claim or diagnosis needs more than a routine lookup.

For routine lookups, direct translation, simple formatting, or already bounded one-step work, use direct execution. For symbolic value, value conflicts, aesthetic judgment, tacit knowledge, and decisions under time pressure, first-principles reasoning should assist rather than dictate the conclusion.

## Compatibility

No extra dependency is required. It works with the files, tests, tools, and evidence available in the current task.

Read [`SKILL.md`](SKILL.md) for the complete workflow and [`CHANGELOG.md`](CHANGELOG.md) for public release notes.

