<launcher>

{{SNIPPET_LAUNCHER}}

</launcher>

<authoring-resolver>

Resolve authoring paths before any issue or knowledge pages:

{{SNIPPET_AUTHORING}}

</authoring-resolver>

<prd-path>

Resolve PRD-component page locations before reading or writing them:

{{SNIPPET_PRD_PATH}}

</prd-path>

<runbook>

Reference docs (read on demand) at
`{{SPEC_TRACK_RUNBOOK_DIR}}/<intent>/{{SPEC_TRACK_ISSUE_PROVIDER}}.md`:

- `issue-fetch` — fetch issues + cache projections
- `issue-write` — body-bearing writes (publish / comment / update) — procedure index
- `issue-new` — publish a new issue
- `issue-comment` — append a comment
- `issue-update` — update body, title, labels, or state
- `issue-link` — relationships
- `issue-state` — body-less verbs (state, assign, unassign, set-type)
{{SNIPPET_PROVIDER_RUNBOOK}}

</runbook>

Don't quote, paraphrase, or summarize issue bodies, comments, or knowledge
documents beyond what the user asked for. The cached `issue.md` and
`comment-*.md` files are projection-owned and read-only — refresh them
via the matching fetch script; never edit them in place.
