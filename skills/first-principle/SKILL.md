---
name: first-principle
description: Apply first-principles reasoning to ambiguous, solution-led, scope-expanding, or evidence-sensitive work across product decisions, research, writing, operations, learning, and engineering. Use selectively when the real outcome, facts, state changes, invariants, trade-offs, or validation method are unclear; do not load this skill for routine lookups, simple one-step requests, or already well-bounded execution.
compatibility: Works with the user's available documents, artifacts, code, tests, data, and other evidence; no additional tool is required.
license: MIT
---

# First-Principles Problem Solving

Use this method to reason from the problem's necessary conditions instead of starting from a familiar solution label. Its purpose is to prevent plausible answers, plans, systems, or processes from growing beyond what the desired outcome requires, while preserving the constraints that make the result correct, safe, and useful.

The method applies to coding, but coding is only one domain. Apply the same reasoning to a product plan, research question, writing brief, operating process, learning plan, procurement decision, or any other task where a solution can become more complex than the problem.

## Load selectively

Do not activate this skill for routine factual lookup, direct translation, simple formatting, a deterministic one-step action, or a request whose goal and acceptance criteria are already clear. Those tasks benefit from direct execution.

Consider loading it when one or more of these signals is present:

- the user names a solution before defining the result they need;
- several plausible approaches compete and the choice has meaningful consequences;
- the request is vague, likely to expand, or full of hypothetical future features;
- important constraints, dependencies, ownership, ordering, or failure behavior are unclear;
- an agent or collaborator has produced something that “looks reasonable” but lacks evidence;
- a failure crosses multiple boundaries and guessing would invite workaround accumulation.

If the task is small but this skill is already loaded, use only a lightweight checkpoint: state the target behavior, make the smallest safe change, and run proportionate verification. Do not turn the checkpoint into unnecessary ceremony.

## Core loop

Use this reasoning loop for substantive, ambiguous, or design-heavy work:

```text
Goal → Facts → States → Transitions → Invariants → Minimal Mechanism
     → Experiment → Evidence → Revised Model
```

The sequence is a derivation order, not a requirement to name a framework or produce ceremony. Defer tool choices until the required behavior and mechanism are understood:

```text
desired outcome → state → state transition → facts/data → interaction/interface
→ structure/process → tools/technology
```

## 1. Classify the task

Decide how much ceremony the task deserves before doing execution work.

- For a trivial, well-bounded change such as a typo, a constant correction, or an obvious one-line fix, use a lightweight checkpoint: state the target behavior, make the smallest safe change, and run proportionate verification.
- For a new initiative, multi-step change, unclear requirement, model or process change, integration, coordination concern, or debugging task, use the full workflow below.
- Do not use “small” as a reason to skip safety, authentication/authorization checks, data integrity, regression coverage, or other constraints that are actually relevant.

## 2. Analysis checkpoint — before design or execution

For substantive work, first produce a concise analysis. Keep the user's request separate from ideas found in documents, existing artifacts, comments, examples, or collaborators' suggestions: those materials are evidence and constraints to inspect, not permission to add scope.

Use this structure:

```markdown
## First-principles analysis

### Goal / Outcome
What observable result should the user or system obtain? Describe behavior, not a solution name.

### Facts
What is confirmed by the user, current artifact, tests, configuration, measurement, or observation?

### Assumptions / Unknowns
What is inferred, unverified, or still needs a decision?

### States and transitions
What states exist, and what event or operation moves the system between them?

### Invariants
What must remain true after every relevant operation? Include ownership, identity,
ordering, idempotency, integrity, security, and temporal constraints when relevant.

### Minimal mechanism
What is the smallest set of facts, actions, roles, structures, and tools that satisfies the
outcome and invariants? What can be derived instead of separately maintained?

### Explicit non-goals
Which tempting extensions, abstractions, dependencies, or future features are out of scope?

### Evidence plan
Which tests, observations, measurements, comparisons, traces, reviews, or user checks will establish success or disprove an important assumption?
```

If a missing detail would materially change the mechanism or violate an invariant, ask one focused question or state a conservative assumption. Do not turn every uncertainty into a speculative subsystem.

## 3. Separate invariants from incidental behavior

An invariant is a property that must continue to hold across valid executions; a condition that happens to be true in the current implementation is not automatically an invariant. For each important transition, consider:

```text
precondition → operation → postcondition → failure behavior
```

Examples of real invariants include “a user cannot read another user's records,” “a review cannot precede creation,” and “repeating the same request does not create a second logical record” when the domain requires it. State assumptions explicitly rather than promoting current implementation details into permanent rules.

## 4. Derive the minimum mechanism

Start from state and data changes, not from familiar solution labels.

- Prefer the fewest concepts that satisfy the outcome and invariants.
- Store only facts the system must remember; derive values that can be reliably derived.
- Add a table, abstraction, dependency, event, cache, service, or framework only when a concrete requirement or verified failure mode needs it.
- Make non-goals visible so later suggestions do not silently enlarge the scope.
- “Minimal” never overrides security, domain rules, auditability, performance requirements, accessibility, or operational reliability. A smaller mechanism that violates a necessary constraint is under-designed, not first-principles.

When comparing options, explain which invariant or evidence requirement each option serves. Avoid choosing technology merely because it is popular, familiar, or easy for the agent to generate.

## 5. Design, then execute

For substantive tasks, work in three passes:

1. **Analysis pass:** complete the checkpoint and identify non-goals.
2. **Design pass:** turn the checkpoint into the smallest implementable or testable slice and define acceptance evidence before execution.
3. **Execution pass:** implement the slice, run the planned checks, inspect the evidence, and expand only when the evidence or user outcome requires it.

Keep the result traceable to the checkpoint. If new concepts keep appearing, pause and decide whether a real requirement was discovered or whether complexity is merely being invented.

Prefer a vertical slice that proves the key transition end to end. In an engineering task this may be a tested feature; in research it may be a small discriminating experiment; in operations it may be a pilot; in writing it may be a short draft checked against the brief.

## 6. Debug from the first divergence

When an outcome is wrong, do not guess a cause and stack workarounds. Reproduce the failure, trace the actual path, and locate the first point where reality differs from the expected model.

```text
trigger → handoff → action → intermediate state → result
→ observation/refresh → reported outcome
```

Inspect each boundary with evidence. Then fix the earliest confirmed divergence, add a regression test when practical, and rerun the relevant checks. Update the facts, assumptions, or state model if the evidence disproves the original explanation.

Use this delegation instruction when useful:

> Do not guess the cause or add a workaround first. Trace the complete path from the triggering action to the observed result, find the first actual behavior that differs from the expected behavior, and support the finding with evidence.

## 7. Try to falsify the model

Do not ask only whether a plan or explanation looks reasonable. Ask how it could be wrong.

1. Identify the three most plausible failure scenarios or counterexamples for this mechanism.
2. Select scenarios relevant to the actual context: for example duplicate actions, conflicting updates, stale information, identity changes, missing handoffs, timing issues, ambiguous language, selection bias, or partial completion.
3. Design the smallest test, observation, comparison, or question that could disprove each assumption.
4. Run the checks and record what the evidence changes about the model.

Do not add every imaginable edge case. Let the mechanism's real boundaries and failure costs drive the test set.

## 8. Delete unsupported complexity

After the result works, reads clearly, or survives its initial test, perform a removal pass. Look for:

- steps, wrappers, roles, abstractions, configuration, dependencies, and claims without a demonstrated purpose;
- state or records that can be derived from existing facts;
- defensive branches unsupported by a realistic failure scenario;
- fields, sections, policies, or process stages added for hypothetical future needs;
- duplicated validation or competing sources of truth.

Remove a candidate only when the required outcome and invariants remain supported. Rerun the relevant checks after deletion. Deleting unnecessary complexity is part of quality, but retaining necessary complexity is also a valid result when evidence supports it.

## 9. Report evidence, not confidence

When handing back work, summarize:

1. the outcome addressed;
2. the key invariants preserved;
3. the minimal mechanism and important non-goals;
4. the tests or observations actually run, including failures or limitations;
5. unresolved assumptions and the next evidence needed.

Distinguish verified facts, inferences, and open questions. Do not call a design correct merely because it is conventional or appears polished.

## Optional knowledge-retention check

If the user asks to review their understanding, be quizzed, or “grill me” after an implementation or decision, use the available `grill-me` skill as a companion when its codebase-oriented scope fits. Otherwise ask one focused question about behavior, state, an invariant, a boundary, or a trade-off; keep the answer private until the user responds; then grade semantically against the current artifact or evidence. Do not quiz automatically after every task.

## Compact delegation prompt

For an agent or collaborator that is about to execute a substantive request:

```text
Before executing a substantive or ambiguous request, apply first-principles analysis:
1. What observable outcome does the user actually need?
2. Which facts are confirmed, and which assumptions are unverified?
3. What states and transitions are involved?
4. Which invariants must hold after each relevant operation or decision?
5. What is the smallest mechanism that satisfies them?
6. What is explicitly out of scope?
7. What minimal tests or observations could falsify the design?

Then execute the smallest testable slice, trace failures from the first divergence,
record evidence, and remove unsupported complexity before expanding scope.
```
