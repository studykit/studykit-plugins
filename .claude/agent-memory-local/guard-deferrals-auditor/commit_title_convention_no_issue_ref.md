---
name: commit-title-convention-no-issue-ref
description: This project's commit titles carry no issue-ref prefix any more, so "I have not picked an issue ref yet" is a stale reason for not committing — check git log before accepting it.
metadata:
  type: project
---

Older commits here prefixed the title with a GitHub issue number (`#NNN guard: ...`). Recent
ones do not: the shape is `guard: v<version> — <headline>` for a release and
`guard: <headline>` for a fix without one, checked across the last 25 commits with no `#NNN`
anywhere. So when a turn says it cannot commit because the issue ref is undecided, the
premise is checkable and currently false — read `git log --oneline` before letting that
sentence stand.

This entry deliberately records the **checkable fact** and not a verdict. An earlier version
of it also stored the conclusion "treat the undecided-ref deferral as legitimate", which the
definition forbids: a remembered `legitimate` suppresses findings silently and reproduces
itself. Whether any particular turn's deferral is legitimate is re-derived each time.

Related: [[async_agent_status_not_deferral]]
