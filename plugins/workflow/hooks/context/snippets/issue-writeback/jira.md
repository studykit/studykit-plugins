Body + state update (closing with a non-completion reason — `<verb>` is
the Jira transition the project uses, e.g. `Won't Do` or `Cancelled`):

```bash
"$WORKFLOW" issue_writeback.py update \
  --issue <implementation-key> \
  --body-file <updated-body-path> \
  --state <verb>
```
