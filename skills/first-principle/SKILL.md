---
name: first-principle
description: Apply first-principles reasoning to ambiguous, solution-led, scope-expanding, evidence-sensitive, or convention-bound work: product, research, writing, operations, learning, engineering. Strip the request to its least-dependent facts, separate hard constraints from soft ones (conventions, habits, "everyone does it this way"), interrogate why each is treated as necessary, and derive the theoretical bound plus where the current approach's gap comes from. Then pick the endpoint the task requires: an explanation or falsifiable model for analysis, diagnosis, and evaluation; the smallest complete mechanism (outcome, states, invariants, failure or recovery, observability, acceptance evidence) only when something must be built or changed. Use selectively when outcome, facts, constraints, trade-offs, or validation method are unclear; not for routine lookups or well-bounded execution.
version: 1.4.0
compatibility: Works with the user's available documents, artifacts, code, tests, data, and other evidence; no additional tool is required.
---

# First-Principles Problem Solving

Reason from the problem's necessary conditions instead of a familiar solution label or an inherited convention. The mode this displaces is analogy: copying how similar problems are usually solved, which silently imports their assumptions and leaves you optimising the existing approach rather than the problem. First principles are not maximal decomposition: within a declared scope they are the least-dependent facts and constraints that serve as reasoning starting points, alongside the stated outcome and explicit assumptions. Decomposition, separating essentials from incidentals, and locating what something actually is are one part of the method; it is complete only once the answer is rebuilt from those starting points and tested against evidence — an explanation for an understanding task, a mechanism for a change task. Recombine the parts with their interactions; decomposition alone produces no answer.

**The failure this method exists to prevent is manufactured complexity**: frameworks, dependencies, tables, abstractions, and features chosen before the outcome is known — each locally defensible, collectively unnecessary. Agents produce it easily, because a plausible-sounding addition costs nothing to propose, and it is hard to see because every piece looks reasonable. So the standing question is not "might this be useful later" but "what in the stated outcome requires this now", and the burden of proof sits on the addition, not on the omission. A solution can be too small to work; it can also be too large to be worth having, and the second failure is the more common one here.

Its purpose depends on what the task must produce, and the task decides which endpoint counts as done.

- **Understanding work** — analysis, diagnosis, evaluation, explanation, judging what something is — is complete when there is an explanation stated against the hard constraints, the strongest rival it beats, and the observation that would overturn it. No mechanism is owed; appending one is scope the user did not ask for.
- **Change work** — building or altering a system, process, plan, or decision — is complete when the smallest complete mechanism within scope is derived: enough to reach the outcome, preserve the constraints, handle relevant failure, and produce evidence of success, without hypothetical complexity.

“Least-dependent” is scope-relative; it does not require descending to physical atoms or breaking every system into individual parts. Choose the level of abstraction that preserves behavior relevant to the outcome, since emergent properties can make finer decomposition less explanatory.

Constraints come in two kinds, and telling them apart is where this method earns its keep. **Hard constraints** — physics, law, budget ceilings, safety, physiological limits, stated acceptance criteria — cannot be argued away; respect them. **Soft constraints** — industry practice, tradition, "everyone does it this way", inherited tooling and org structure — bind only because nobody has questioned them. Naming a soft constraint is what makes it revisable; leaving it in the constraints column makes it look like a fact. The highest-yield case for this method is the convention-shaped problem: a step that is "just how it is done" and has never been asked why.

Two safeguards keep that challenge honest. First, when a constraint is owned by someone outside the room — a law, a regulator, an auditor, a contract, a safety certification — treat it as hard even where it looks conventional, and renegotiate only its implementation, never its coverage, and only with that owner's agreement; narrowing the coverage of a compliance or safety control is not "questioning a convention", it is removing the control. Second, where you cannot tell which kind a constraint is, split the question rather than guessing: **hard about whether it exists, soft about how it is done** — and say who has to agree before the "how" changes.

Coding is only one domain: use the same reasoning for a product plan, a research question, a writing brief, an operating process, a learning plan, or a procurement decision, wherever a solution can grow more complex than the problem. Which dimensions to decompose along depends on the domain — physical limits, money and incentives, or time, energy and relationships — so pick the dimension that makes the parts verifiable rather than the one that is habitual.

## Load selectively

Do not activate this skill for routine factual lookup, direct translation, simple formatting, a deterministic one-step action, or a request whose goal and acceptance criteria are already clear. Those tasks benefit from direct execution.

Consider loading it when one or more of these signals is present:

- the user names a solution before defining the result they need;
- a practice, tool, team structure, or process is taken as given because "that is how it is done", and nobody has asked whether it must exist;
- the user asks what something really is, why something happens, or whether a claim, number, or option is sound, and the answer is not settled by looking it up;
- several plausible approaches compete and the choice has meaningful consequences;
- the request is vague, likely to expand, or full of hypothetical future features;
- important constraints, dependencies, ownership, ordering, or failure behavior are unclear;
- an agent or collaborator has produced something that “looks reasonable” but lacks evidence;
- a failure crosses multiple boundaries and guessing would invite workaround accumulation.

Understanding tasks use the same load criteria; do not withhold the method from an analysis just because nothing will be built.

If the task is small but this skill is already loaded, use only a lightweight checkpoint: state the target behavior and completion boundary, make the smallest change that is complete within that boundary, and run proportionate verification. Do not turn the checkpoint into unnecessary ceremony.

For route-governed workflows, mark applicability explicitly: `NOT_APPLICABLE` (routine or already bounded — say why and continue), `REQUIRED` (ambiguity, competing approaches, meaningful failure cost, or evidence-sensitive judgment), or `UNAVAILABLE` (the method or its evidence cannot be used — say so, and do not manufacture a completed analysis).

## Where this method leads, and where it only assists

Sharpest where the outcome is single and observable, the effort breaks into countable parts, the hard constraints are physical or contractual rather than interpretive, and a small experiment could settle the question — engineering and commercial problems of that shape are where it leads.

It is an **assistant, not the leading method**, when the real work is elsewhere:

- **symbolic value** — what something means to a group: status, identity, belonging;
- **value conflict** — legitimate goods that argument cannot trade off against each other;
- **aesthetic resonance** — rightness that is felt rather than derived;
- **tacit knowledge** — skill that lives in hands and habit, and cannot be written down;
- **time pressure** — a decision needed before any decomposition could be tested.

In those settings keep only the parts that survive — naming hard constraints, separating facts from assumptions, refusing structure nobody asked for — and do not let a derivation drive the conclusion. Say which situation you are in; a tidy decomposition of a value conflict is still a value conflict.

## Core loop

Use this reasoning loop for substantive, ambiguous, or design-heavy work:

```text
shared front end:
Goal / Scope → Facts → Assumptions → Constraints (hard, then soft)
→ Interrogate: why must each exist? what breaks without it? from zero, what would this look like?
→ Bound and gap: theoretical floor or ceiling, and what creates the distance from it

then branch on what the task must produce:

understanding: → Explanation / Model → Competing explanation → Falsification → Revised Model
change:        → States → Transitions → Completeness boundary → Failure/Recovery
               → Observability → Minimal Complete Mechanism → Experiment → Evidence
```

The front end is the same in both branches: separating the request from the solution label it arrived with, the confirmed facts from the inherited assumptions, and the real constraints from the ones that are merely conventional is what makes either endpoint reachable — and for a convention-shaped problem it is where the work happens. The mechanism branch is not the default; it is one of two exits, and choosing the wrong exit is itself a first-principles failure.

The sequence is a derivation order, not a requirement to name a framework or produce ceremony. Nothing gets added — a table, a dependency, a layer, a tool — until the behavior it serves is already known.

## 1. Classify the task

Decide two things before doing execution work: what the task must produce, and how much ceremony it deserves.

**Task type — understanding or change.** Understanding tasks (analysis, diagnosis, evaluation, explanation, judging the nature of something) end at a supported model plus the evidence that would falsify it. Change tasks (build, redesign, process, plan, artifact) end at a smallest complete mechanism plus acceptance evidence. A mostly-understanding task may yield a small design as a by-product; do not let that by-product become the goal. When the type is genuinely mixed, run the understanding branch first — a mechanism derived before the situation is understood is usually the solution the requester arrived with.

**Ceremony.**

- For a trivial, well-bounded change such as a typo or a one-line fix, use the lightweight checkpoint above instead of the full workflow.
- For a new initiative, multi-step change, unclear requirement, model or process change, integration, coordination concern, or debugging task, use the full workflow below.
- Do not use “small” as a reason to skip safety, authentication/authorization checks, data integrity, regression coverage, or other constraints that are actually relevant.

## 2. Analysis checkpoint — before design or execution

For substantive work, first produce a concise analysis. Keep the user's request separate from ideas found in documents, existing artifacts, comments, examples, or collaborators' suggestions: those materials are evidence and constraints to inspect, not permission to add scope.

Use this structure:

```markdown
## First-principles analysis

### Task type
Understanding, change, or mixed? What must exist at the end for this to be done?

### Goal / Outcome
What observable result should the user or system obtain? Describe behavior, not a solution name.

### Facts
What is confirmed by the user, the current artifact, tests, configuration, measurement, or
observation? Keep facts, constraints, goals, and assumptions in separate fields: something the user
asserts, or that the current implementation happens to do, is not a fact until evidence supports it.

### Assumptions / Unknowns
What is inferred, unverified, or still needs a decision?

### Constraints — hard, then soft
Hard: which limits hold regardless of implementation (physics, law, budget ceiling, safety, stated
acceptance criteria)? Write each as a fact about the world, not as a preference. Anything owned by an
authority outside the room (regulator, auditor, contract, certification) belongs here, and its
coverage is not yours to narrow.
Soft: which practices, conventions, or inherited choices are being treated as limits? For each, note
who would actually be harmed if it were dropped, what evidence would show it is load-bearing, and who
must agree before it changes. Where you cannot tell, mark it "hard about whether, soft about how".
An unexamined soft constraint is the commonest reason a first-principles analysis still lands on the
conventional answer. For understanding tasks, the hard constraints are the conditions any acceptable
explanation must satisfy.

### Interrogation
For each constraint and each inherited part of the current approach: why does it exist, what breaks
if it is removed, and if this were designed from zero with no legacy, what would it look like? Chain
the "why" until the answer stops being "because that is what we do".
Then state the bound and the gap: the theoretical floor or ceiling here — least cost, least
irreversibility, fewest moving parts, strongest achievable evidence — and what specifically creates the
distance between it and the current approach.

### States and transitions (change tasks; optional for understanding tasks)
What states exist, and what event or operation moves the system between them?

### Completeness boundary (change tasks)
Within the declared scope, what must be covered for this to count as complete — the normal path,
relevant failure or recovery, ownership and closure of each in-scope state, observability, and
acceptance evidence? Which cases are intentionally excluded?

### Minimal complete mechanism (change tasks only)
After the completeness boundary, what is the smallest set of facts, actions, roles, structures, and
tools that satisfies it? What can be derived rather than separately maintained?

### Rival explanation and falsifier (understanding tasks only)
What is the strongest competing account of the same facts, why do the facts favour yours, and which
observation would overturn it?

### Explicit non-goals
Which tempting extensions, abstractions, dependencies, or future features are out of scope?

### Evidence plan
Which tests, observations, measurements, comparisons, traces, reviews, or user checks will establish success or disprove an important assumption?
```

**Closing the checkpoint.** A change task carries forward into the completeness boundary and the minimum mechanism. An understanding task closes here, and that is a legitimate finished result: the explanation stated against the hard constraints and the conditions any acceptable account must satisfy, the rival it beats, the falsifier, and whatever remains unresolved. Do not append a mechanism to an analysis that never asked for one; if the user wants a design next, that is a new task with its own checkpoint.

If a missing detail would materially change the mechanism or violate an invariant, ask one focused question or state a conservative assumption. Do not turn every uncertainty into a speculative subsystem.

## 3. Separate invariants and constraints from incidental behavior

An invariant is a property that must continue to hold across valid executions; a condition that happens to be true in the current implementation is not automatically an invariant. For each important transition, consider:

```text
precondition → operation → postcondition → failure behavior
```

Examples of real invariants include “a user cannot read another user's records,” “a review cannot precede creation,” and “repeating the same request does not create a second logical record” when the domain requires it. State assumptions explicitly rather than promoting current implementation details into permanent rules.

The commonest false invariant is a convention wearing the clothes of a requirement: a weekly approval meeting, a staging environment, a fixed sprint length, a mandatory document — each may be load-bearing or may be pure inertia, and the distinction only appears when you ask who is harmed by removing it. Treat "the current approach does it this way" as the weakest possible evidence that it must.

For an understanding task the same test applies to whatever the explanation treats as necessary: a pattern that merely happens to hold in the sample at hand is not a condition the explanation is owed, and treating it as one is how an analysis overfits to a single case. Ask what has to be true for any acceptable account, not just for the account you currently hold.

## 4. Establish completeness before minimizing

“Complete” is relative to the declared scope, not a demand to handle every imaginable edge case.

**For a change task**, before optimizing for fewer concepts or steps, check that the proposed mechanism
closes the necessary loop:

1. The normal path can reach the observable outcome.
2. Each relevant transition has a precondition, operation, postcondition, and failure behavior.
3. Required invariants and responsibility boundaries are checked where they can be violated.
4. Failure, recovery, rollback, or compensation is defined when silent corruption, partial completion, or irreversibility would be costly.
5. The owner, terminal state, or explicit handoff for each in-scope state is clear.
6. Success and important failure are observable and distinguishable by the evidence plan.

Choose failure modes by impact, likelihood, reversibility, and the user's stated constraints. Do not add edge cases merely because they are conceivable; if a check is not needed at this scope, mark it as a non-goal rather than silently omitting it.

**For an understanding task**, the parallel check to run before trimming or simplifying the
explanation:

1. Every fact inside the declared scope is accounted for, including the ones that cut against the
   explanation you hold.
2. The conditions it treats as essential are the ones this case actually requires, not patterns
   that merely co-occur in the sample at hand.
3. The rival explanation that fits the same facts is stated, and the evidence that separates them
   exists rather than being assumed.
4. The falsifier is specified, and whatever the evidence cannot reach is marked unresolved instead
   of being filled in by the explanation.

A simpler explanation that leaves an in-scope fact unexplained is under-analyzed, not
first-principles. Do not simplify before these four hold; equally, do not carry complexity that no
in-scope fact requires.

## 5. Derive the minimum mechanism (change tasks)

**Skip this section when the task type is understanding.** An analysis that jumps here has answered a question the user did not ask; finish the falsification loop in §8 instead.

Only after the completeness boundary is satisfied, minimize the mechanism. Start from state and data changes at the right abstraction level, not from familiar solution labels, and not from a demand to make the implementation physically as small as possible.

- Prefer the fewest concepts that satisfy the outcome, invariants, failure behavior, and evidence.
- Recombine rather than enumerate: the answer is usually in how the surviving parts interact, not in the list of parts. An uncombined decomposition is an inventory, not a mechanism.
- Compare against the bound: the least this could cost in steps, moving parts, or irreversibility, and which part of the current approach creates the distance. Where the gap is an unexamined soft constraint, challenge it there.
- Store only what the system must remember; derive what can be derived.
- Add a table, abstraction, dependency, service, or framework only when a concrete requirement or verified failure mode needs it.
- Make non-goals visible so later suggestions do not silently enlarge the scope.
- “Minimal” never overrides security, domain rules, auditability, performance, accessibility, reliability, failure handling, or acceptance evidence. A smaller mechanism that leaves an in-scope gap is under-designed, not first-principles.

When comparing options, say which invariant or evidence requirement each serves. Avoid a technology because it is popular, familiar, or easy to generate.

## 6. Design, then execute

For substantive change tasks, work in three passes:

1. **Analysis pass:** complete the checkpoint and identify non-goals.
2. **Design pass:** turn the checkpoint into the smallest complete implementable or testable slice
   and define acceptance evidence for the normal path and relevant non-happy paths before execution.
3. **Execution pass:** implement the slice, run the planned checks, inspect the evidence, and expand only when the evidence or user outcome requires it.

Understanding tasks stop after pass 1. Their analysis pass is the work product, not a preamble to it.

**Diagnosis is a mixed case, and the stopping rule does not apply to it.** Locating the first
divergence (§7) is understanding work; repairing it is change work. Once the root cause is confirmed
against evidence, re-classify the task and continue into passes 2 and 3 rather than reporting the
cause and stopping — unless the user asked only for the cause.

Keep the result traceable to the checkpoint. If new concepts keep appearing, pause and decide whether a real requirement was discovered or whether complexity is merely being invented.

Prefer a vertical slice that proves the key transition end to end: a tested feature, a discriminating experiment, a pilot, a short draft checked against the brief.

## 7. Debug from the first divergence

When an outcome is wrong, do not guess a cause and stack workarounds. Reproduce the failure, trace the actual path, and locate the first point where reality differs from the expected model.

```text
trigger → handoff → action → intermediate state → result
→ observation/refresh → reported outcome
```

Inspect each boundary with evidence. Do not touch code before the divergence is located. Then fix the earliest confirmed divergence, add a regression test when practical, and rerun the relevant checks; update the facts, assumptions, or state model if the evidence disproves the original explanation. When the user asked for the failure to be repaired, these repair steps are change work: once the root cause is confirmed, §6 passes 2 and 3 apply, and the fix is held to the change-task checklist in §4.

## 8. Try to falsify the model and the completeness boundary

Do not ask only whether a plan or explanation looks reasonable or minimal. Ask how the model could be wrong and which in-scope path the mechanism might fail to close; for an understanding task this section finishes the work rather than checking it, so give the rival explanation and its decisive test real space.

1. Identify the three most plausible failure scenarios or counterexamples for this model or mechanism.
2. Pick the ones that fit the context: duplicate actions, conflicting updates, stale information, identity changes, missing handoffs, timing, ambiguous language, selection bias, partial completion.
3. Design the smallest test, observation, comparison, or question that could disprove each assumption.
4. Run the checks and record what the evidence changes about the model.

Do not add every imaginable edge case. Let the real boundaries and failure costs drive the test set.

## 9. Delete unsupported complexity

After the result works, reads clearly, or survives its initial test, perform a removal pass. First
confirm that the completeness boundary is still covered; then look for:

- steps, wrappers, roles, abstractions, configuration, dependencies, and claims without a demonstrated purpose;
- state or records that can be derived from existing facts;
- defensive branches unsupported by a realistic failure scenario;
- fields, sections, policies, or process stages added for hypothetical future needs;
- constraints carried over from the previous approach that survived interrogation only through inertia;
- duplicated validation or competing sources of truth.

Remove a candidate only when the outcome, invariants, failure/recovery paths, and evidence remain supported, then rerun the checks. Deleting unnecessary complexity is part of quality; keeping necessary complexity is an equally valid result when the completeness boundary supports it.

## 10. Report evidence, not confidence

When handing back work, summarize: the outcome addressed; the invariants preserved or the hard constraints established; for a change task the minimal complete mechanism, its completeness boundary and non-goals, for an understanding task the explanation, the rival it beats and what would falsify it; the checks actually run, including failures; and the assumptions still open with the next evidence needed.

Distinguish verified facts, inferences, and open questions. Do not call a design correct merely because it is conventional or appears polished.

## Quality check before sending

Run this before reporting; it takes a minute and catches the usual failure modes of this method.

1. Is the outcome stated as observable behavior, or did a solution name slip back in?
2. Which soft constraints did I name — and is any of them still sitting unexamined in the constraints
   column?
3. Did I give both the bound and the gap, or only a mechanism?
4. Did any constraint owned by someone outside the room — regulator, auditor, contract — get
   renegotiated by me, or have its coverage quietly narrowed?
5. Which single assumption, if false, would overturn the conclusion — and is it labelled as an
   assumption rather than presented as a fact?
6. Is the falsifier (understanding) or the acceptance evidence (change) something that could actually
   be collected — by whom, at what cost?
7. What did I remove? A pass that only adds is unfinished.

## Evaluating the method

Treat claims about a method's effect as hypotheses. When evaluating a revision, compare versions on representative tasks with the same model settings and independent criteria. Report sample counts and limitations, distinguish screening signals from judgments, and avoid causal claims from a single run or a test case that already contains the expected conclusion.

## Optional knowledge-retention check

If the user asks to review their understanding or be quizzed after a decision, use the `grill-me` skill when its scope fits; otherwise ask one focused question about behavior, state, an invariant, a boundary, or a trade-off, keep the answer private until they respond, then grade it against the artifact. Do not quiz automatically.

## Compact delegation prompt

For an agent or collaborator that is about to execute a substantive request:

```text
Before executing a substantive or ambiguous request, apply first-principles analysis:
1. Understanding task or change task — and what must exist at the end for this to be done?
2. What observable outcome does the user need, stated as behavior rather than a solution name?
3. Which facts are confirmed, and which are only inherited assumptions?
4. Which constraints are hard, which are soft conventions nobody has questioned — and for each soft
   one, why it exists and what actually breaks if it goes? Anything owned by an outside authority is
   hard, and its coverage is not yours to narrow.
5. From zero, what would this look like? Where is the theoretical bound, and what creates the gap?
6. Nothing gets added — tool, table, dependency, layer — until the behavior it serves is known.
7. Understanding: the strongest rival explanation, and what would overturn yours. Change: the
   smallest complete mechanism that satisfies the outcome, and how you will know it works.

Then execute the smallest complete testable slice for a change task, trace failures from the first
divergence, and delete unsupported complexity before expanding. For an understanding task, stop at the
supported explanation and its falsifier instead of designing something nobody asked for.
```

## Changelog

Release history for this skill lives in `CHANGELOG.md` (moved out at 1.3.0 — it is not needed while
reasoning). Latest: **1.4.0**, which adds where this method leads, where it only assists, and the anti-complexity measure.
