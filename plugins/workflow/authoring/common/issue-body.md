# Workflow Issue Body Conventions

Body-level rules for issue-backed items stored in an issue backend.

Issue-backed item types include `task`, `bug`, `spike`, `epic`, `review`, and the workflow issue side of `usecase` and `research`.

## Scope

These rules apply to the visible issue body.

Type-specific authoring files define the required body shape for each item type. This file defines body structure, readability, reusable sections, and references for issue-backed items.

The literal markup form for headings, lists, inline emphasis, links, code, tables, and checklists is defined by the matching provider convention file (`../providers/<provider>-issue-convention.md`). This file uses canonical section names only and does not embed provider markup.

## Section structure

An issue body is organized as a sequence of named sections.

Rules:

- Each section has a canonical Title Case name (`Description`, `Acceptance Criteria`, `Unit Test Strategy`, etc.).
- Each section starts with a level-2 heading rendered in the provider's heading form. Subsections may appear inside a section using deeper heading levels.
- Do not put a top-level title heading inside the body when the issue title is stored separately.
- Avoid stray content above the first section unless the selected type template requires a short summary block.
- Unknown sections are tolerated when they are useful, well-named, and well-formed.

Common reusable section names for issue-backed items:

- `Description`
- `Acceptance Criteria`
- `Unit Test Strategy`
- `Open Questions`
- `Related`
- `Resume`
- `Why Discarded`

## Reference form

Use stable, readable references in body text.

| Target | Preferred body form |
| --- | --- |
| Issue-backed item | Issue reference from the selected issue backend |
| Knowledge page | Page, document, or file reference from the selected knowledge backend |
| External source | Provider-native link form |

Rules:

- Prefer the shortest reference that is unambiguous in the configured project.
- Use full URLs when a short reference would be ambiguous outside its source system.
- Do not require local file paths for targets whose canonical identity is not a local file.
- Do not introduce workflow-local numeric IDs when canonical identity already exists.

## Relationship body sections

Issue relationship body sections are type-specific or provider-specific. Do not invent new relationship sections unless the selected authoring files require them.

Provider relationship files define which relationships are provider-native and which may appear as visible body context.

## `Related` section

Use for human-readable references that help interpret the issue but are not stored as provider-native relationships.

Provider convention files define when a `Related` section is appropriate and when a provider-native relationship should be used instead.

## `Resume` section

Purpose: current-state snapshot for a future session.

Use when an issue-backed item is mid-flight and the current state is not obvious from the existing body.

Suggested slots:

- **Approach.** Current strategy.
- **Waiting for.** External input or sequencing note.
- **Open questions.** Questions awaiting input.
- **Next.** Next concrete step.

Rewrite the `Resume` section in place. Do not preserve history there.

## `Why Discarded` section

Use when an issue is intentionally abandoned and provider status alone does not explain why.

The section should hold one dated bullet per reason, citing the cause when relevant. Provider files define the exact list and link form.

## Relationship lists

Relationship lists should keep one referenced item per bullet.

## Comments versus body

Use the issue body for the current structured issue content.

Use comments, work notes, discussions, or history for conversation, progress notes, review conversations, raw investigation notes, and audit facts.

Do not copy long comment threads into the body. Summarize the resulting decision or current state in the relevant body section instead.

## Filesystem projections

If workflow tooling creates local files as projections of external issues, do not treat projection paths as canonical identity.

- Do not use projection paths in commits, branches, or comments unless the local path itself is the topic.
- Do not edit projection metadata as authoring state. Use provider fields through the selected provider workflow, and keep canonical references in visible body text.

## Cross-references

- `./issue-authoring.md` — issue-backed item rules.
