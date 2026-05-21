Body + state update (closing with a non-completion reason):

```bash
"$WORKFLOW" issue.py update \
  --issue <implementation-ref> \
  --body-file <updated-body-path> \
  --state closed \
  --state-reason not_planned
```
