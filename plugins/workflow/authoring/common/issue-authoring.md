# Workflow Issue Authoring

Common semantic rules for issue-backed items.

Read this with the semantic authoring file for the item type, plus:

- `./issue-body.md`

## Scope

Use these rules for issue-backed items:

- `task`
- `bug`
- `spike`
- `epic`
- `review`
- workflow side of `usecase`
- workflow side of `research`

## Identity

Use the issue identity supplied by the configured issue backend.

Do not introduce workflow-local issue IDs. Do not use local projection paths or local numeric IDs as canonical issue identity.

## Type and status

Every issue-backed item has a workflow type and lifecycle status.

`type` is the issue-backed item discriminator. Type-specific authoring files define the remaining semantic metadata fields, requiredness, and lifecycle states. Backend-specific authoring files define how those values are stored and displayed.

## Motivation and rationale

Issue-backed items should record why the work exists when the reason is not
obvious from the title or acceptance criteria.

Use the issue body for durable rationale that defines the current work:

- Why the work is needed.
- What problem, risk, or decision triggered it.
- Why the selected scope or boundary matters.
- Why a removal, reversal, or responsibility split should not be undone later.

Use comments for rationale that belongs to the work timeline:

- Why implementation direction changed.
- Why a task is being closed, discarded, or split.
- Why the final result differs from the original plan.

Do not create metadata fields only to hold rationale. Keep rationale in the body
or comments using the selected item type and provider conventions.

## Relationships

Issue relationships are not issue metadata fields. Type-specific authoring files define required and optional relationships. Provider relationship files define native storage and body-boundary rules.

Canonical relationship intents used by provider authoring files and the workflow scripts:

- `parent` — epic or parent work item that coordinates this item.
- `blocked_by` — the source item is blocked by the target item. Aliases `depends_on`, `dependency`, `blockedBy`, and `blockedby` are normalized to `blocked_by`.
- `blocking` — the source item blocks the target item. Read-back counterpart of `blocked_by`; the alias `blocks` normalizes to `blocking`.
- `related` — useful non-blocking relationship between items.

## Comments and history

Use comments, work notes, discussions, or history for:

- Back-and-forth discussion.
- Raw investigation notes.
- Progress notes.
- Review feedback.
- Audit facts.

Keep the issue body structured and current. Do not turn it into a transcript.

## Write workflow

Resolve and read the required authoring files before drafting issue-backed item changes. Provider/cache write commands perform the requested mutation and verification; they do not enforce hidden authoring read state.

## Completion baseline (all issue-backed types)

Completion conditions that apply to every issue-backed item. Type-specific authoring files add further conditions that apply to one type only.

Treat an issue-backed item as complete only when:

- Acceptance criteria are satisfied, when the type defines them.
- Affected knowledge pages are updated when the work changes documented behavior, architecture, domain, NFRs, CI, specs, use cases, or research conclusions.
- Follow-up feedback is captured as `review` items rather than hidden in comments.

## Common mistakes (all issue-backed types)

Mistakes that apply to every issue-backed item, regardless of type. Type-specific authoring files list additional mistakes that apply to one type only.

- Using local projection paths or local integer ids as canonical issue identity. Canonical identity comes from the configured issue backend.
