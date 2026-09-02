# Issue Common Rules

## Body conventions

Section lists in type files are minimum shape, not a closed schema. Add
purpose-specific sections when they make the issue clearer; keep each section
focused on current durable content.

## Comments and history

Keep the issue body structured and current — a snapshot of the work, not a transcript. Process and timeline content belongs in comments, work notes, or history, not the body.

Current handoff state belongs in the provider-backed `Resume` comment when the
issue backend supports updatable comments. The comment starts with the provider
heading for Resume (`## Resume` on GitHub, `h2. Resume` on Jira). Do not add a
body `Resume` section for routine handoff state.

## Common mistakes (all issue-backed types)

Mistakes that apply to every issue-backed item, regardless of type. Type-specific authoring files list additional mistakes that apply to one type only.

- Using local projection paths or local integer ids as canonical issue identity. Canonical identity comes from the configured issue backend.
