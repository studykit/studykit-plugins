# Knowledge Body Conventions

Body-level rules for knowledge pages (`spec`, `architecture`, `domain`, `context`, `nfr`, `ci`, and the curated side of `usecase` and `research`). Knowledge pages hold curated, current, durable content — not raw discussion, transient questions, or work logs, which belong in the issue backend.

Use canonical Title Case section names only; the matching provider convention file (`../providers/<provider>-<knowledge-form>-convention.md`) defines the literal markup for headings, lists, inline emphasis, links, code, tables, and checklists.

## Section structure

A knowledge page is a sequence of named sections.

- Each section has a canonical Title Case name (`Context`, `Specification`, `Change Log`, etc.) and starts with a level-2 heading. Subsections use deeper heading levels.
- Do not put a top-level title heading in the body when the page title is stored separately.
- Avoid stray content above the first section unless the type template requires a short summary block.

## Tailoring the body

Beyond the required sections, an author may add purpose-specific Title Case sections when the page has natural structure the type-defined sections do not capture. Keep each section narrow (one named thing) and the overall body short. A custom section earns its place only when its content would otherwise fold awkwardly into an existing one; if it fits naturally, fold it back in instead.

## Curated content only

Write knowledge pages as reference material: current decisions, stable requirements, specifications, domain concepts, architecture shape, final research findings, final use case descriptions.

Keep out: long discussion transcripts, untriaged feedback, session notes, raw scratch work, routine progress logs.

## Reference form

Use stable, readable references in body text.

| Target | Preferred body form |
| --- | --- |
| Issue-backed item | Issue reference from the selected issue backend |
| Knowledge page | Page, document, or file reference from the selected knowledge backend |
| External source | Provider-native link form |

- Prefer the shortest reference unambiguous in the configured project; use full URLs when a short reference would be ambiguous outside its source system.
- Do not require local file paths for targets whose canonical identity is not a local file.
- Do not introduce workflow-local numeric IDs when canonical identity already exists.
- Keep one referenced item per bullet in relationship lists.

## `Change Log` section

Every material change should append a concise semantic-cause entry. Version history records who changed what and when; `Change Log` records why the page changed and which work item caused it.

Each entry should:

- Be one bullet per material change, kept concise.
- Identify the date (`YYYY-MM-DD`), the causing work item, and the reason, in that order.
- Link to the causing issue, review, task, use case workflow issue, or research workflow issue in the provider's link form.
- Avoid duplicating discussion from the causing issue.
- Be appended, not rewritten, except for obvious formatting errors.

When a page is created or materially updated because of an issue-backed item, include a visible link back to that item in `Change Log`, `Related Work`, or another relevant section.

## Optional reusable sections

`Supersedes`, `Related Work`, and `Sources` are optional building blocks for any knowledge page type. Include each only when its per-section guidance applies. A type-specific authoring file may pin one as required for a type, overriding this file's optional framing.

- **`Supersedes`** — for specs or curated documents that replace older ones. Reference each prior page in the provider's link form.
- **`Related Work`** — for issue-backed items that informed or depend on this page. Use the configured issue backend's reference form.
- **`Sources`** — for reports or decisions relying on external evidence. Use the provider's link form for citations.

## Page comments

Use page comments for page-local review and clarification only. If feedback must be triaged, prioritized, assigned, or resolved through workflow, create a `review` item in the issue backend instead.

## Identity and projections

Use the canonical page, document, or file identity supplied by the selected knowledge backend; the visible body is the durable reading surface for humans and agents. Provider and cache metadata are operational state, not authoring content — keep it in provider workflows or cache sidecars, duplicating it in the body only when readers need it.

If workflow tooling creates local files as projections of external pages, do not treat projection paths as canonical identity:

- Do not use projection paths in commits, branches, or comments unless the local path itself is the topic.
- Do not edit projection metadata as authoring state.

## Common mistakes (all knowledge types)

Type-specific authoring files list additional mistakes that apply to one type only.

- Using local projection paths or local file identity as canonical page identity. Canonical identity comes from the configured knowledge backend.
- Using page comments as a substitute for `review` items when feedback needs workflow tracking (triage, ownership, priority, or durable resolution).
