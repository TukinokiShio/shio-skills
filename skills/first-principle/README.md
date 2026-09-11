# First-Principles Problem Solving

Use this skill when a task is ambiguous, solution-led, likely to expand, or sensitive to evidence and trade-offs.

## What it does

It guides an agent from the observable outcome to the smallest complete mechanism within the
declared scope. Completeness means covering the required outcome, relevant states and transitions,
invariants, failure or recovery behavior, observability, and acceptance evidence before optimizing
for fewer concepts or steps:

```text
Goal → Scope → Facts → States → Transitions → Invariants
     → Failure/Recovery → Observability → Minimal Complete Mechanism
     → Experiment → Evidence → Revised Model
```

The skill is useful for product decisions, research, writing, operations, learning, architecture, and engineering work. It defines a completeness boundary, explicit non-goals, and asks for a small test that could disprove the model or expose an incomplete path.

## Use it when

- several plausible solutions compete;
- requirements, ownership, ordering, or failure behavior are unclear;
- a proposed solution is accumulating unsupported complexity;
- a collaborator's implementation looks reasonable but lacks evidence.

For routine lookups and simple one-step changes, the skill intentionally stays out of the way.

## Compatibility

No extra dependency is required. It works with the files, tests, tools, and evidence available in the current task.

Read [`SKILL.md`](SKILL.md) for the complete workflow.

