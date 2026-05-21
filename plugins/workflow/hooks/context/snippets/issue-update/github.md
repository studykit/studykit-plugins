Body + state update (closing with a non-completion reason):

```bash
workflow issue update \
  --issue <implementation-ref> \
  --body-file <updated-body-path> \
  --state closed \
  --state-reason not_planned
```
