<issue-provider>

Issue provider for this project: `{{SPECTRACK_ISSUE_PROVIDER}}`.

</issue-provider>

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

<commands>

Issue CLI. Run `spectrack issue --help` to list the verbs available for
this project's backend, then `spectrack issue <verb> --help` for a verb's
flags and usage.

</commands>

Don't quote, paraphrase, or summarize issue bodies, comments, or knowledge
documents beyond what the user asked for. The cached `issue.md`, `state.md`,
and `comment-*.md` files are projection-owned and read-only — refresh them
via the matching fetch script; never edit them in place.
