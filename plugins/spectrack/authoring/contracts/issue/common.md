# Issue Common Rules

Common semantic rules for issue-backed items.

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

Record every relationship the configured issue backend natively supports, through the backend's native relationship mechanism. Run `spectrack issue link --help` to see the relationship kinds the configured backend accepts; type-specific authoring files define which relationships an item needs.

## Comments and history

Use comments, work notes, discussions, or history for:

- Back-and-forth discussion.
- Raw investigation notes.
- Progress notes.
- Review feedback.
- Audit facts.

Keep the issue body structured and current. Do not turn it into a transcript.

## Write workflow

Resolve and read the required authoring files before drafting issue-backed changes. Write commands perform the mutation and verification only; they do not enforce that the authoring files were read.

## Completion baseline (all issue-backed types)

Completion conditions that apply to every issue-backed item. Type-specific authoring files add further conditions that apply to one type only.

Treat an issue-backed item as complete only when:

- Acceptance criteria are satisfied, when the type defines them.
- Affected knowledge pages are updated when the work changes documented behavior, architecture, domain, NFRs, CI, specs, use cases, or research conclusions.
- Follow-up feedback is captured as `review` items rather than hidden in comments.

## Common mistakes (all issue-backed types)

Mistakes that apply to every issue-backed item, regardless of type. Type-specific authoring files list additional mistakes that apply to one type only.

- Using local projection paths or local integer ids as canonical issue identity. Canonical identity comes from the configured issue backend.
