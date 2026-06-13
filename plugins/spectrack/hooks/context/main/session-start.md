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

<implementing-issues>

A workflow `task` / `bug` / `spike` issue body is a spec — what / why /
done — not a plan. Before changing any code to implement one, settle the
approach against the current code in plan mode (where the runtime provides
it) and get the user's explicit approval of it. Then, with the
`AskUserQuestion` tool (offer selectable options so the user need not type
a reply), ask whether to validate the approved approach with a plan audit
— the `resolution-auditor` agent in plan-audit mode, pointed at the
settled approach. Dispatch that agent only if they agree; when it runs,
implement only after it resolves. If the user declines the audit,
implement the approved approach directly.

</implementing-issues>

Don't quote, paraphrase, or summarize issue bodies, comments, or knowledge
documents beyond what the user asked for. The cached `issue.md`, `state.md`,
and `comment-*.md` files are projection-owned and read-only — refresh them
via the matching fetch script; never edit them in place.
