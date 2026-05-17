# Workflow Epic Authoring

A workflow epic is an **issue-backed coordination parent** for a larger goal delivered through multiple member issues.

An epic may represent a user-facing feature, platform capability, subsystem implementation effort, migration, stabilization campaign, or cross-cutting quality initiative. It is not an implementation unit; the work belongs to its member issues.

Epics are stored in the configured issue backend.

Companion contracts:

- `./issue-body.md`
- Issue rules: `./issue-authoring.md`

## Storage role

`epic` is stored in the issue backend.

Use canonical issue identity. Do not use local integer ids.

## When to create an epic

Create an epic when one or more of these holds:

- A larger goal will be split into multiple member issues.
- Several existing issues need a shared coordination home.
- Cross-cutting decisions affect more than one member issue.
- Integration-level acceptance criteria span several member issues.
- A feature, migration, or stabilization campaign needs progress visibility.

Do not create an epic when:

- One issue is enough.
- Issues are unrelated and have no shared narrative.
- A spec or architecture page is the real home for the decision.
- The work is only a single implementation task.

## Shared narrative

The epic is the home for narrative that spans its member issues:

- Decisions across member issues.
- Integration constraints.
- Shared blockers.
- Sequencing choices.
- Scope changes that affect several member issues.

Use comments for discussion. Keep the epic body as the current coordination summary.

Member issues should link to the epic when their own approach depends on epic-level narrative.

## Body shape

Required:

```markdown
## Description

<what the member issues together accomplish and why they are grouped>
```

Recommended:

```markdown
## Coordination Notes

<current decisions across member issues, constraints, or sequencing notes>
```

Optional sections:

- `## Acceptance Criteria` — integration outcome not naturally owned by a single member issue; do not restate per-member criteria.
- `## Resume` — current-state snapshot while open. See `./issue-body.md`.
- `## Why Discarded` — reason when discarded. See `./issue-body.md`.

Unknown Title Case H2 headings are tolerated.

## Relationship to knowledge pages

Epics coordinate work. They do not define the product, architecture, or implementation contract.

Use knowledge pages for durable content:

- User-facing behavior → use case curated page.
- Implementation contract → spec.
- Component shape → architecture.
- Vocabulary → domain.
- Non-functional target → nfr.

If an epic discussion creates durable knowledge, update the relevant knowledge page and add a `## Change Log` entry there.

## Completion criteria

Completion is author-judged; closing all member issues does not automatically close the epic.

Treat an epic as complete only when:

- The coordinated outcome has been reached or explicitly descoped.
- Member issues are closed, discarded, or moved elsewhere.
- Integration-level acceptance criteria are satisfied or explicitly waived.
- Durable decisions surfaced during coordination are recorded on the relevant knowledge page.
- Follow-up feedback is captured as review items rather than hidden in comments.

## Comments and discussion

Use comments for:

- Coordination discussion.
- Member-issue progress updates.
- Blocker resolution.
- Scope negotiation.

Keep the epic body as the current compact coordination surface.

## Common mistakes

- Using an epic as a spec or architecture document.
- Duplicating per-member-issue details in the epic body.
- Closing the epic while active member issues still depend on it.
- Nesting epics without explicit backend support and configuration.
- Using local projection paths or local integer ids as canonical identity.

## Do not

- Do not put implementation details or unit test strategy in the epic.
- Do not discard member issues automatically when discarding an epic.
- Do not store durable design decisions only in the epic; update the relevant knowledge page.
