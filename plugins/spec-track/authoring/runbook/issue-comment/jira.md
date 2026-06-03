## jira — append a comment

```bash
spec-track issue comment \
  --issue <KEY> \
  --body-file <path> \
  [--type <task|bug|...>] \
  [--state <verb>] \
  [--overwrite] \
```

Required: `--issue`, `--body-file`. `--state` is a verb whose
configured transition the script POSTs after the comment is added. Run
`spec-track issue state --help` to list the configured verbs before
relying on `--state`; an unknown verb raises `ProviderOperationError`.
`--overwrite` skips the freshness check and replaces the provider copy
(see the conflict flow in `../issue-write/jira.md`).

See `../issue-write/jira.md` for the shared body-bearing write
procedure.
