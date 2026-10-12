# Workflow Provider Profile

This document is intentionally scoped to workflow provider setup.

```yaml
providers:
  issues:
    kind: jira
    site: https://example.atlassian.net
    project: PROJ
    issue_type: Task
    relationship_mappings:
      blocked_by:
        surface: issue_link
        link_type: Blocks
        direction: inward
  knowledge:
    kind: github
    path: wiki/spectrack
commit_refs:
  style: issue-prefix
```
