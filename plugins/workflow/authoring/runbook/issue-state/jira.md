## jira — body-less verbs

```bash
workflow issue state <KEY> <verb> [--comment <text>]
workflow issue assign <KEY> me
workflow issue unassign <KEY>
workflow issue set-type <KEY> <new-type>
```

`<verb>` for `state` is dynamic. Run `workflow issue state --help` to
list the currently-configured verbs; an unknown verb also prints the
configured + reserved verb lists on stderr. Discover verbs through the
CLI, not by reading config. `assign` / `unassign` /
`set-type` are reserved static verbs (setup rejects overrides).
`set-type` PUTs `fields.issuetype` using the `artifact_issue_types`
mapping. Use `workflow issue update` when the change must also rewrite
the body or title. Each verb accepts `--overwrite` to skip the
freshness check and replace the provider copy (see the conflict flow in
`../issue-write/jira.md`).
