# Context Authoring

A context page is a **knowledge-backed framing reference** — the original idea, problem framing, scope, and optional UI/navigation framing that every other work item and knowledge page assumes. It is not for detailed use case flows, the domain glossary, implementation design, or task plans.

## Body shape

An `Original Idea` section is required — the verbatim original user input or imported project brief. Preserve it faithfully: quote or clearly mark the initial idea, and append or separately summarize later clarifications rather than rewriting the original so heavily that the starting point disappears. When importing an existing project, use its brief or a source link instead of inventing one.

A `Problem Framing` section is strongly recommended, kept at framing level: who has the problem, what current situation is failing, why it matters, and what coarse success looks like. Detailed flows belong in use cases; implementation shape in architecture or specs.

Add other sections only when the project needs them — for example explicit scope boundaries, a coarse success definition, or, for UI-heavy projects, a screens/navigation grouping (each screen: name/slug, purpose, related use cases, and a link to design artifacts — do not embed large mockups inline).

## Content boundaries

Place content on the right page rather than here:

- `domain` — shared vocabulary and concepts.
- `usecase` — detailed user-visible flows and their actors.
- `architecture` — system shape.
- `spec` — implementation contracts.
- `nfr` — non-functional targets.
