# Knowledge Body Conventions

Body-level rules for knowledge pages stored in a knowledge backend.

Knowledge page types include `spec`, `architecture`, `domain`, `context`, `nfr`, `ci`, and the curated output side of `usecase` and `research`.

## Purpose

Knowledge pages contain curated, current, durable content.

They should not contain raw discussion, transient questions, or detailed work logs. Those belong in the issue backend.

The literal markup form for headings, lists, inline emphasis, links, code, tables, and checklists is defined by the matching provider convention file (`../providers/<provider>-<knowledge-form>-convention.md`). This file uses canonical section names only and does not embed provider markup.

## Section structure

A knowledge page is organized as a sequence of named sections.

Rules:

- Each section has a canonical Title Case name (`Context`, `Specification`, `Change Log`, etc.).
- Each section starts with a level-2 heading rendered in the provider's heading form. Subsections may appear inside a section using deeper heading levels.
- Do not put a top-level title heading inside the body when the page title is stored separately.
- Avoid stray content above the first section unless the selected type template requires a short summary block.

## Tailoring the body

Beyond the required sections defined by the page's type-specific
authoring file, each page author may add purpose-specific sections
when the page has natural structure that the type-defined sections
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
| External source | Provider-native link form |

Rules:

- Prefer the shortest reference that is unambiguous in the configured project.
- Use full URLs when a short reference would be ambiguous outside its source system.
- Do not require local file paths for targets whose canonical identity is not a local file.
- Do not introduce workflow-local numeric IDs when canonical identity already exists.

## Curated content only

Write knowledge pages as reference material:

- Current decisions.
- Stable requirements.
- Specifications.
- Domain concepts.
- Architecture shape.
- Final research findings.
- Final use case descriptions.

Avoid:

- Long discussion transcripts.
- Untriaged feedback.
- Session notes.
- Raw scratch work.
- Routine progress logs.

## `Change Log` section

Every material knowledge-page change should add a concise semantic cause entry to the `Change Log` section.

Version history records who changed what and when. The `Change Log` section records why the page changed and which work item caused it.

Each entry should:

- Be one bullet per material change.
- Stay concise.
- Identify the date, the causing work item, and the reason.
- Use the date format `YYYY-MM-DD`.
- Link to the causing issue, review, task, use case workflow issue, or research workflow issue in the provider's link form.
- Avoid duplicating discussion from the causing issue.
- Be appended; do not rewrite history except for obvious formatting errors.

## Links back to work items

When a knowledge page is created or materially updated because of an issue-backed item, include a visible link back to that work item in `Change Log`, `Related Work`, or another relevant section.

## Optional reusable sections

The named sections defined below (`Supersedes`, `Related Work`,
`Sources`) are optional reusable building blocks for any knowledge
page type. Include each only when its per-section guidance applies;
otherwise omit it. A type-specific authoring file may pin one of
them as required for a particular type — in that case the type
contract overrides this file's optional framing.

### `Supersedes` section

For specs or curated documents that replace older documents. Each entry should reference the prior page in the provider's link form.

### `Related Work` section

For issue-backed items that informed or currently depend on this page. Use issue references in the configured issue backend's reference form.

### `Sources` section

For research reports or decisions that rely on external evidence. Use the provider's link form for external citations.

## Page comments

Use page comments for page-local review and clarification only.

If feedback must be triaged, prioritized, assigned, or resolved through workflow, create a `review` item in the issue backend instead of relying on a page comment.

## Identity and authoring surface

Use the canonical page, document, or file identity supplied by the selected knowledge backend. Do not treat local projection paths as canonical identity unless the page is truly file-backed.

Keep workflow meaning in the visible body sections defined by type-specific authoring files.

Provider and cache metadata are operational state, not authoring content. Use provider workflows or cache sidecars for that state. Duplicate provider state in the body only when readers need it.

The visible body remains the durable reading surface for humans and agents.

## Relationship lists and change-log entries

Relationship lists should keep one referenced item per bullet.

`Change Log` entries should record date, causing work item, and reason in that order. The provider convention defines the literal bullet, date, and link form.

## Filesystem projections

If workflow tooling creates local files as projections of external knowledge pages, do not treat projection paths as canonical identity.

- Do not use projection paths in commits, branches, or comments unless the local path itself is the topic.
- Do not edit projection metadata as authoring state. Use provider workflows or cache sidecars for provider state, and keep canonical references in visible body text.

## Common mistakes (all knowledge types)

Mistakes that apply to every knowledge page, regardless of type. Type-specific authoring files list additional mistakes that apply to one type only.

- Using local projection paths or local file identity as canonical page identity. Canonical identity comes from the configured knowledge backend.
- Using page comments as a substitute for review items when feedback needs workflow tracking. Create a `review` item when feedback requires triage, ownership, priority, or durable resolution tracking.
