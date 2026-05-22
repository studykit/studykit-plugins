# Workflow Provider Profile

This document is intentionally scoped to workflow provider setup.

```yaml
providers:
  issues:
    kind: jira
    site: https://jira.example.test
    deployment: data_center
    project: PROJ
    issue_type: Task
    relationship_mappings:
      blocked_by:
        surface: issue_link
        link_type: Blocks
        direction: inward
  knowledge:
    kind: github
    path: wiki/workflow
commit_refs:
  style: issue-prefix
```
