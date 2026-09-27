---
name: oq-governance
description: >-
  Identify material decisions that require the user's judgment, prepare a
  reviewable decision record, and track the answer without treating silence as
  approval. By default, maintain synchronized Markdown and JSON OQ lists.
compatibility: Standalone; no external tools or packages are required.
license: MIT
metadata:
  version: "1.3.0"
  last_updated: "2026-09-27"
---

# OQ Governance

An open question (OQ) is a material decision that belongs to the user and cannot be settled by available evidence, existing policy, or a safe reversible step. This skill helps an agent recognize those decisions, present clear choices, preserve the user's answer, and keep the decision record current.

Use this skill for consequential choices about scope, acceptance criteria, compatibility, user preferences, data or security boundaries, release behavior, and resource authorization. Do not use it as a general-purpose way to ask about every uncertainty.

## 1. Decide whether the issue is an OQ

Before asking the user:

1. **Check evidence.** Read the task, relevant project guidance, existing decisions, and applicable contracts. Use read-only inspection or a reversible experiment when that can settle the issue.
2. **Check prior authorization.** Apply preferences and boundaries the user has already stated for this task or that clearly apply from stable guidance.
3. **Separate knowledge from decisions.** Record a verifiable fact as `FACT`, a reasoned but provisional conclusion as `INFERENCE`, and a research or experiment gap as `UNKNOWN`. Only use `OQ` when the user must choose among materially different paths.
4. **Check impact.** Escalate only when the unresolved choice affects a meaningful boundary such as scope, quality, compatibility, safety, release, user preference, or authorization.
5. **Check reversibility.** If a draft, comparison, or reversible implementation can be completed first, do that work before asking.

These are normally not OQs:

- An unread document or an unfinished search.
- A technical detail that project evidence or an existing contract settles.
- A routine repair path or low-risk reversible implementation choice.
- Work already covered by the user's explicit authorization.
- A question created only because work is taking time or an agent wants to stop.

If no OQ applies, state `OQ_NOT_APPLICABLE` with a concise reason and supporting evidence. Do not manufacture a decision to fill a template.

## 2. Create synchronized Markdown and JSON records

When an OQ registry is needed, maintain both a human-readable Markdown list and a machine-readable JSON list. If the work item has no existing registry, use `open-questions.md` and `open-questions.json` in its established planning or documentation directory. Use the same stable OQ ID in both files.

Treat the files as two representations of one logical registry, not as independently maintained copies:

- When no fixed machine schema applies, Markdown is the default authoritative record and JSON is generated from the same OQ data.
- When an existing workflow requires a fixed JSON, YAML, or other machine schema, preserve that schema as the authoritative record and generate the Markdown reading view from it.
- When a registry already exists, preserve its location, fields, and established authority. Add or update its companion representation alongside it instead of creating a second registry elsewhere.
- If a project contract forbids a companion file, follow that contract and record which view could not be produced and why.

After creating, answering, rejecting, expiring, or returning an OQ to work, update the authoritative record and regenerate the companion view. Before asking the user and after each state change, compare both lists for OQ IDs, item counts, status, question, options, decision, user source and message digest, affected work items, and evidence. Never edit a generated view independently.

Before asking, save a draft with at least:

- One stable `oq_id` for each independent decision.
- The decision question and why the user must decide now.
- Background, risks, and the boundary of the decision.
- Verified facts, inferences, unknowns, and evidence paths.
- A recommendation and its verifiable reason.
- Two or three mutually exclusive, executable options.
- Each option's status, needed permissions, verification method, direct consequences, release consequences, and affected work items or files.
- The handling of no response, validity period, expiry conditions, rollback conditions, and actions the OQ does not authorize.
- A pending status and placeholders for the user's source and approval-message digest. Do not invent an answer or digest.

If evidence is insufficient to form meaningful options, mark the issue `RESEARCH_REQUIRED`, research it first, and do not present a false OQ.

## 3. Present one decision at a time

Ask one independent material question at a time. Separate choices with different consequences, such as scope, migration, and release authorization. The user should be able to answer with an option number or clearly identify an option in their own words.

Use this Markdown format:

```markdown
## OQ-<stable-id>: <one decision the user can make>

- **Status:** Pending user decision
- **Background and risk:** <why the choice exists and what a wrong choice could harm>
- **Decision object:** <the single matter being decided>
- **Why decide now:** <current blocker or impact>
- **Verified facts:** <up to three facts with evidence paths>
- **Constraints:** <existing authorization and invariants>
- **Unresolved difference:** <what the rules cannot settle>
- **Recommendation:** <option number and verifiable reason>

### Options

1. **<Option A>** — Status: <available/conditional/rejected>; permissions: <...>; verification: <...>; consequences: <...>; release consequences: <...>
2. **<Option B>** — Status: <available/conditional/rejected>; permissions: <...>; verification: <...>; consequences: <...>; release consequences: <...>

### Execution boundaries

- **Affected work items, files, versions, or gates:** <...>
- **If unanswered:** <hold the affected action or use only an already-authorized safe default>
- **Validity:** <scope and expiry condition>
- **Rollback:** <evidence and steps that would reverse the decision>
- **Not authorized:** <actions this OQ does not authorize>
- **Evidence:** <path, version, hash, or experiment ID>
```

Add a third option only when it is a meaningful, mutually exclusive path. Do not use “What do you think?”, “Should I continue?”, or “Do you approve everything above?” as the only question. Do not hide an unlisted choice in the wording.

## 4. Handle silence and answers carefully

- For material scope, compatibility, release, or irreversible decisions, keep the item `pending` and hold affected actions until the user answers.
- Use a default only when explicit, stable authorization already covers it and the path is reversible, within scope, and preserves safety and acceptance requirements. Record where that authorization came from.
- Do not treat an agent-authored decision, a summary, silence, elapsed time, or the recommended option as user approval.
- Map a natural-language answer to one option. If multiple interpretations remain, ask one narrow clarification and update the same OQ ID.
- On acceptance or rejection, preserve the user's original wording, message digest, timestamp, selected decision, impact, and state change. If the original answer or digest cannot be verified, keep the item `UNVERIFIED` or `PENDING`.
- A clear rejection is a resolved decision outcome, not an unanswered question.

## 5. Registry structure and format parity

In the generic registry below, registry status is `pending` if any item is pending, `resolved` when all items have been handled, and `not_applicable` only when the count is zero. Top-level source and digest identify the registry's initiating request; item-level values identify each item's user answer.

### Markdown record

```markdown
# Open Questions — <run or work-item ID>

- **Schema:** `oq-decision/v1`
- **Registry status:** `pending` / `resolved` / `not_applicable`
- **Source:** `user_message` / `existing_policy` / `not_applicable`
- **Approval message digest:** `null` or <digest>
- **Selection policy:** `independent_material_decisions`
- **Count:** <number of OQs>
- **Decision IDs:** <all OQ IDs>
- **Run ID / work-item ID:** <IDs or null>

## OQ-EXAMPLE — <one decision question>

- **Status:** `pending` / `resolved`
- **Context and background risks:** <...>
- **Decision object:** <...>
- **Facts / constraints / unknowns:** <...>
- **Recommendation:** <option and reason>
- **Consequences:** <...>
- **Affected work items / files:** <...>
- **Validity:** <scope and expiry>
- **Rollback conditions:** <...>
- **Not authorized:** <...>
- **Default handling:** <...>
- **Decision:** `null` or <decision>
- **Source / user original response / approval digest / decision time:** <...>
- **Evidence:** <path#anchor, version, hash, or experiment ID>

### Options

#### 1. <option text>

- **Status / permissions / verification:** <...>
- **Consequences / release consequences:** <...>

#### 2. <option text>

- **Status / permissions / verification:** <...>
- **Consequences / release consequences:** <...>
```

### JSON record

Generate the machine-readable view from the same registry data:

```json
{
  "schema": "oq-decision/v1",
  "status": "pending",
  "source": "user_message",
  "approval_message_digest": null,
  "registry": {
    "selection_policy": "independent_material_decisions",
    "count": 1,
    "decision_ids": ["OQ-EXAMPLE"]
  },
  "items": [
    {
      "id": "OQ-EXAMPLE",
      "question": "...",
      "context": "...",
      "background_risks": ["..."],
      "decision_object": "...",
      "facts": ["..."],
      "constraints": ["..."],
      "unknowns": ["..."],
      "recommendation": "...",
      "options": [
        {
          "id": "1",
          "text": "...",
          "status": "recommended",
          "permissions": ["..."],
          "verification": ["..."],
          "consequences": ["..."],
          "release_consequences": ["..."]
        },
        {
          "id": "2",
          "text": "...",
          "status": "conditional",
          "permissions": ["..."],
          "verification": ["..."],
          "consequences": ["..."],
          "release_consequences": ["..."]
        }
      ],
      "consequences": ["..."],
      "affected_work_items": ["..."],
      "affected_files": ["..."],
      "validity": {
        "scope": "run/work-item/version",
        "expires_when": "..."
      },
      "rollback_conditions": ["..."],
      "not_authorized": ["..."],
      "default_handling": "hold_pending_user_decision",
      "status": "pending",
      "decision": null,
      "source": "user_message",
      "user_original_response": null,
      "approval_message_digest": null,
      "decision_time": null,
      "evidence": ["path#anchor"],
      "run_id": null,
      "work_item_id": null
    }
  ]
}
```

For `not_applicable`, state the reason and evidence and set `count` to `0`; do not use an empty list to hide a skipped analysis. Preserve strict schemas required by an existing workflow, even when their field names differ from this generic example.

## 6. OQs in ongoing work

- An OQ should not interrupt a repair or delivery cycle unless new evidence creates a genuine user-owned decision about scope, acceptance, compatibility, or an irreversible action.
- Pause only the work item that depends on an unanswered OQ. Independent work may continue when its dependencies are recorded.
- After an interruption or context reset, resume from the saved registry and original user response. Do not recreate a decision from a summary; missing source or digest means the answer remains unverified.
- Bind each OQ's creation, answer, rejection, expiry, and return to work to its run and work-item IDs when the workflow provides them.

## 7. Final OQ check

- [ ] The issue needs a user decision; it is not merely a fact gap or implementation task.
- [ ] Evidence, existing rules, and prior decisions were checked first.
- [ ] There is one independent question with two or three meaningful options.
- [ ] Options have consequences, authorization needs, and verification steps.
- [ ] Unanswered handling and affected work are explicit.
- [ ] Markdown and JSON records agree, or a contract-based exception is documented.
- [ ] No answer, approval, digest, or authorization was inferred or fabricated.
- [ ] If no OQ applies, `OQ_NOT_APPLICABLE` includes a reason and evidence.

## 8. Limits

This skill governs how OQs are identified, presented, recorded, and resolved. It does not replace a project's workflow, acceptance, security, or release contract. When a project has a stricter verifiable OQ schema, preserve it while retaining the core rules: evidence first, one material decision at a time, user-source binding, silence is not approval, and pending work is not complete.
