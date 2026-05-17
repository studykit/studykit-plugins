# Workflow PRD Authoring

A PRD (Product Requirements Document) in this workflow is the **aggregate of several knowledge pages and issue-backed items** that together describe a project's framing, user-visible behavior, and decided requirements.

This file is an index, not a separate artifact type. The authoring resolver does not serve `prd` as a type. Each component below has its own authoring file and storage role.

## Components

| Component | Authoring | Storage role | Cardinality | Purpose |
| --- | --- | --- | --- | --- |
| `context` | `./context-authoring.md` | Knowledge | 1 per project | Original idea, problem framing, scope, coarse success. |
| `usecase` | `./usecase-authoring.md` | Issue + knowledge | N per project | How an actor achieves a goal in a specific situation. |
| `nfr` | `./nfr-authoring.md` | Knowledge | N per project | Non-functional targets. |
| `spec` | `./spec-authoring.md` | Knowledge | N per project | Implementation contracts. |
| `domain` | `./domain-authoring.md` | Knowledge | N per project | Shared vocabulary and concepts. |

`architecture`, `ci`, and implementation-level items (`task`, `spike`, `bug`, `review`, `epic`) are not part of the PRD. They describe internal system shape or execution, which the PRD intentionally leaves to downstream pages and items.

## Sequencing

A typical sequence:

1. Capture `context` first — original idea and problem framing.
2. Add `usecase` items as actor goals become clear. Workflow issue first; curated page once the flow is stable.
3. Add `domain` pages when shared vocabulary appears across use cases.
4. Add `nfr` pages when non-functional targets are decided.
5. Add `spec` pages when implementation contracts are decided.

Each component evolves independently. The PRD has no single draft-to-publish lifecycle — every page and issue follows its own publishing rule.

## When to consult this index

- When deciding where a piece of framing or requirement content belongs.
- When importing an existing project and you need to know which artifacts to create.
- When reviewing whether the PRD is complete enough to begin implementation tasks.

For authoring rules of any individual component, read its authoring file directly.

## Do not

- Do not create a single combined PRD page or issue. Each component is its own page or item.
- Do not duplicate content across components. Use cross-references (`## Related Work`, `## Sources`) instead.
- Do not treat this index as authoring rules — it only points to them.
