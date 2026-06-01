## github — body-less verbs

For body-less changes use one of:

```bash
workflow issue state <ref> close|reopen
workflow issue assign <ref> me
workflow issue unassign <ref>
workflow issue set-type <ref> <new-type>
```

`set-type` preserves non-type labels and swaps only the workflow-type
label. Use `workflow issue update` when the change must also rewrite
the body or title. Each verb accepts `--overwrite` to skip the
freshness check and replace the provider copy (see the conflict flow in
`../issue-write/github.md`).
