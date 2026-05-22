## jira — body-less verbs

```bash
workflow issue state <KEY> <verb> [--comment <text>]
workflow issue assign <KEY> me
workflow issue unassign <KEY>
workflow issue set-type <KEY> <new-type>
```

`<verb>` for `state` is dynamic — any key in
`providers.issues.state_transitions`; unknown verbs print the
configured + reserved verb lists on stderr. `assign` / `unassign` /
`set-type` are reserved static verbs (setup rejects overrides).
`set-type` PUTs `fields.issuetype` using the `artifact_issue_types`
mapping. Use `workflow issue update` when the change must also rewrite
the body or title.
