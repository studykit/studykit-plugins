## jira — attach files to an issue

```bash
workflow issue attach \
  --issue <KEY> \
  [--type <task|bug|...>] \
  <file> [<file> ...]
```

Required: `--issue` and at least one local file path. Each path must
point at an existing file on disk; one invocation uploads them all in a
single multipart request. `--type` is the workflow artifact type and
defaults to `task` — it only labels the operation and does not change the
upload.

Attachments are additive: there is no freshness gate and no `--overwrite`
verb. Re-running with the same filename adds another attachment rather
than replacing the existing one. After upload the issue cache is
refreshed so a later body-bearing write does not false-conflict.

The printed JSON reports each created attachment's `id`, `filename`, and
`size`. Attachment upload is **Jira only** — the GitHub issue backend has
no equivalent and the verb refuses any non-Jira provider.
