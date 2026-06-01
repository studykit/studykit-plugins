## jira — append a comment

```bash
workflow issue comment \
  --issue <KEY> \
  --body-file <path> \
  [--type <task|bug|...>] \
  [--state <verb>] \
```

Required: `--issue`, `--body-file`. `--state` is a verb whose
configured transition the script POSTs after the comment is added. Run
`workflow issue state --help` to list the configured verbs before
relying on `--state`; an unknown verb raises `ProviderOperationError`.

See `../issue-write/jira.md` for the shared body-bearing write
procedure.
