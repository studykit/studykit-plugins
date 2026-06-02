## jira — attach files to an issue

Attachment upload/download is **Jira only** — the GitHub issue backend has
no equivalent and the verb refuses any non-Jira provider.

### Upload

```bash
workflow issue attach add \
  --issue <KEY> \
  [--type <task|bug|...>] \
  <file> [<file> ...]
```

Required: `--issue` and at least one local file path. Each path must point
at an existing file; one invocation uploads them all in a single multipart
request. `--type` defaults to `task` and only labels the operation.

Attachments are additive: there is no freshness gate and no `--overwrite`.
Re-running with the same filename adds another attachment rather than
replacing it. After upload the issue cache is refreshed.

### Download

```bash
workflow issue attach get \
  --issue <KEY> \
  ( --id <ID> [--id <ID> ...] | --name <FILENAME> [--name ...] | --all ) \
  [--out <dir>]
```

Downloads attachment bytes to local disk so the file can be opened/read.
Pick attachments by `--id` (stable id shown in `attachment.md`), `--name`
(filename), or `--all`. Without `--out`, files land in the issue cache
dir's `attachments/` subdir; the printed JSON reports each `path`.

### Seeing what is attached

A fetch projects the issue's attachment list to a sibling `attachment.md`
(one line per attachment: `- <id>: <filename> (<size> bytes)`), written
only when the issue has attachments and surfaced in the fetch output
alongside `relation.md`. Use the listed id with `attach get --id`.

See `../issue-fetch/jira.md` for the fetch flow and cache layout.
