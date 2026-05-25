# Workflow Issue Body Conventions

Body-level rules for issue-backed items stored in an issue backend.

Issue-backed item types include `task`, `bug`, `spike`, `epic`, `review`, and the workflow issue side of `usecase` and `research`.

## Scope

These rules apply to the visible issue body.

Type-specific authoring files define the required body shape for each item type. This file defines body structure, readability, reusable sections, and references for issue-backed items.

This file uses canonical section names only and does not embed literal markup. The literal markup form for headings, lists, inline emphasis, links, code, tables, and checklists is defined by the matching rendering convention.

## Section structure

An issue body is organized as a sequence of named sections.

Rules:

- Each section has a canonical Title Case name (`Description`, `Acceptance Criteria`, `Unit Test Strategy`, etc.).
- Each section starts with a level-2 heading rendered in the rendering convention's heading form. Subsections may appear inside a section using deeper heading levels.
- Do not put a top-level title heading inside the body when the issue title is stored separately.
- Avoid stray content above the first section unless the selected type template requires a short summary block.

## Tailoring the body

Beyond the required sections defined by the item's type-specific
authoring file, each issue author may add purpose-specific sections
when the issue has natural structure that the type-defined sections
do not capture. Pick short, descriptive Title Case section names;
keep each section narrow (one named thing per section); and keep
the overall body short — a custom section earns its place only when
its content would otherwise have to be folded awkwardly into an
existing section. If the content fits naturally into an existing
section, fold it back in instead of adding a new heading.

## Reference form

Use stable, readable references in body text.

| Target | Preferred body form |
| --- | --- |
| Issue-backed item | Issue reference from the selected issue backend |
| Knowledge page | Page, document, or file reference from the selected knowledge backend |
| External source | Native link form from the rendering convention |

Rules:

- Prefer the shortest reference that is unambiguous in the configured project.
- Use full URLs when a short reference would be ambiguous outside its source system.
- Do not require local file paths for targets whose canonical identity is not a local file.
- Do not introduce workflow-local numeric IDs when canonical identity already exists.

## Relationship body sections

Issue relationship body sections are defined by the type-specific authoring file or the matching rendering convention. Do not invent new relationship sections unless the selected authoring files require them.

## Optional reusable sections

The named sections defined below (`Related`, `Resume`, `Why
Discarded`, `Out of Scope`, `Alternatives Considered`, `Risks`)
are optional reusable building blocks for any issue type. Include
each only when its per-section guidance applies; otherwise omit
it. A type-specific authoring file may pin one of them as required
for a particular type — in that case the type contract overrides
this file's optional framing.

### `Related` section

Use for references that help interpret the issue but are not stored as native backend relationships. Express each reference using the native reference form from the configured issue or knowledge backend.

### `Resume` section

Purpose: current-state snapshot for a future session.

Use when an issue-backed item is mid-flight and the current state is not obvious from the existing body.

Suggested slots:

- **Approach.** Current strategy.
- **Waiting for.** External input or sequencing note.
- **Open questions.** Items left open for downstream resolution — questions awaiting input (decisions or info needed), deferred work tracked elsewhere, follow-up candidates surfaced during this work, or lateral concerns observed but not addressed within this issue's scope.
- **Next.** Next concrete step.

Rewrite the `Resume` section in place. Do not preserve history there.

### `Why Discarded` section

Use when an issue is intentionally abandoned and backend status alone does not explain why.

The section should hold one dated bullet per reason, citing the cause when relevant.

### `Out of Scope` section

Purpose: name what the issue explicitly does not cover.

Use when the issue title or `Description` could be read as covering broader work, or when a related concern was deliberately deferred to a follow-up.

Do not use when the body is small enough that scope is obvious from `Description` and `Affected Paths`, or when the only deferred item is a generic disclaimer with no concrete follow-up.

List one deferred item per bullet with a short reason or link to the follow-up.

### `Alternatives Considered` section

Purpose: record design or implementation options that were evaluated but not chosen, with the rejection reason.

Use when the chosen approach is non-obvious and a reviewer is likely to suggest one of the rejected options.

Do not use when no real alternatives were considered, or when the reasoning belongs in a curated knowledge page (create or update that page instead).

List one alternative per bullet with the rejection reason. Do not re-litigate the accepted decision here.

### `Risks` section

Purpose: name technical risks, regression hazards, or operational concerns specific to this issue.

Use when the change touches load-bearing code, migrations, contracts, or behavior with non-trivial blast radius, and the risk is not already covered by `Acceptance Criteria` or the test strategy.

Do not use when the change is small and routine, or when the risk is already represented by an `Open Questions` entry or test scenario.

List one risk per bullet with the mitigation or detection plan when known.

## Relationship lists

Relationship lists should keep one referenced item per bullet.

## Comments versus body

Use the issue body for the current structured issue content.

Use comments, work notes, discussions, or history for conversation, progress notes, review conversations, raw investigation notes, and audit facts.

Do not copy long comment threads into the body. Summarize the resulting decision or current state in the relevant body section instead.

## Filesystem projections

If workflow tooling creates local files as projections of external issues, do not treat projection paths as canonical identity.

- Do not use projection paths in commits, branches, or comments unless the local path itself is the topic.
- Do not edit projection metadata as authoring state. Use backend fields through the selected backend workflow, and keep canonical references in visible body text.

## Cross-references

- `./issue-authoring.md` — issue-backed item rules.
