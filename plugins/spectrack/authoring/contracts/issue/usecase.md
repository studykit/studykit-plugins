# Use Case Authoring — Issue Side

This file covers the issue-side workflow item for shaping a use case. The curated use case, when stable, lives on the knowledge side.

## Storage role (issue side)

Purpose: discovery, questions, status, feedback, and task linkage while the flow is being shaped.

## Workflow issue body

The issue body summarizes discovery state and links to the curated page when one exists.

Recommended sections:

- `Description` — why this use case is being explored and who needs it.
- `Actors` — list of actor canonical names that participate in this use case, one per bullet. Identity (general role, type, privileges) is defined on the actors registry — see `../knowledge/actors.md`.
- `Current Draft` — short current summary or link to the curated page draft.
- `Open Questions` — outstanding questions, one per bullet.

Common optional sections:

- `Related Work` — related tasks, specs, reviews, research, or pages.
- `Supersedes` — prior use case when replacing one.
- `Resume` — current-state snapshot while shaping.

Add purposeful sections when useful.

Use comments for conversation, interview notes, and feedback threads.

## Actor citation

Cite `Actors` entries by canonical names from the actors registry. Do not define actor identity in the issue body; the registry is the only place identity lives.

## Splitting a use case

Split a use case when the actor goal forks or the flow contains multiple independent goals.

When splitting, confirm with the user, create separate child use case issues, link parent/child issues, and use supersession only when replacing an older published use case.

## Do not (issue side)

- Do not store use case discussion only in a knowledge page — the workflow issue is the discovery surface.
- Do not pack multiple actor goals into one use case.
