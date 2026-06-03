## github — body-less verbs

For body-less changes use one of:

```bash
spec-track issue state <ref> close|reopen
spec-track issue assign <ref> me
spec-track issue unassign <ref>
spec-track issue set-type <ref> <new-type>
```

`set-type` preserves non-type labels and swaps only the workflow-type
label. Use `spec-track issue update` when the change must also rewrite
the body or title. Each verb accepts `--overwrite` to skip the
freshness check and replace the provider copy (see the conflict flow in
`../issue-write/github.md`).
