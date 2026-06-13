<commit-prefix>

{{SNIPPET_COMMIT_PREFIX}}

</commit-prefix>

<commands>

Per-verb flags and usage: `spectrack issue <verb> --help`. The verbs
this agent uses:

- `fetch` — fetch the issue + cache projections (only when an
  `issue-ref` is supplied, for spec context)
- `update` — refresh the issue body's `Resume` at handoff
  (body-only writeback; this agent never transitions issue state)

</commands>
