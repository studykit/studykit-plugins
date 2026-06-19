<commit-prefix>

{{SNIPPET_COMMIT_PREFIX}}

</commit-prefix>

<commands>

Per-verb flags and usage: `spectrack issue <verb> --help`. The verbs
this agent uses:

- `fetch` — fetch the issue + cache projections (only when an
  `issue-ref` is supplied, for spec context)
- `comment update` — refresh the issue's existing `Resume` comment at handoff
- `comment append` — create the issue's first `Resume` comment when missing
  (comment writeback; this agent never transitions issue state)

</commands>
