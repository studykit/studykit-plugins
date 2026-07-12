<commit-prefix>

{{SNIPPET_COMMIT_PREFIX}}

</commit-prefix>

<grounding-context>

When you fetch the issue for spec context, read its full surrounding
context too, not the body alone: all of the issue's comments, every
related issue — both the relationships the fetch surfaces (`relation.md`)
and any other issue the body itself names, fetched and read — and any
`wiki/` knowledge page the body or its `Context` points to, or that covers
the code you will touch. Ground the approach and every Acceptance-Criteria
check against that context.

</grounding-context>

<commands>

Per-verb flags and usage: `spectrack issue <verb> --help`. The verbs
this agent uses:

- `fetch` — fetch the issue + cache projections (only when an
  `issue-ref` is supplied, for spec context)
- `comment resume` — refresh the issue's `Resume` comment at handoff: updates
  the existing one, or creates it when missing (idempotent upsert; this agent
  never transitions issue state)

</commands>
