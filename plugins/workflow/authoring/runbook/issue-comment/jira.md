## jira — append a comment

```bash
workflow issue comment \
  --issue <KEY> \
  --body-file <path> \
  [--type <task|bug|...>] \
  [--state <verb>] \
```

Required: `--issue`, `--body-file`. `--state` is a free-form verb
keyed in `providers.issues.state_transitions.<verb>`; the script POSTs
the configured transition after the comment is added. Discover and
confirm verbs through the setup skill's State Transition Profiling
step before relying on `--state` writes; an unknown verb raises
`ProviderOperationError`.

See `../issue-write/jira.md` for the shared body-bearing write
procedure.
