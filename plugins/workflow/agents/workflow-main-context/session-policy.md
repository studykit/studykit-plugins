## workflow policy

Workflow operations — issue/cache reads, comments, lifecycle changes,
relationships, metadata, provider writes, write-back, freshness checks, and
authoring path discovery — run through the bundled workflow launcher:

{{WORKFLOW_LAUNCHER_BLOCK}}

Fetch or refresh an issue (the common read):

{{WORKFLOW_ISSUE_FETCH_BLOCK}}

Detailed procedures (read on demand before performing the operation):

- `{{WORKFLOW_POLICY_DIR}}/authoring.md` — authoring path resolution and type taxonomy
- `{{WORKFLOW_POLICY_DIR}}/provider-writes/{{WORKFLOW_ISSUE_PROVIDER}}.md` — issue-provider writes (publish, append, update, relationships)
- `{{WORKFLOW_POLICY_DIR}}/knowledge/{{WORKFLOW_KNOWLEDGE_PROVIDER}}.md` — knowledge-provider rules

Don't quote, paraphrase, or summarize issue bodies, comments, or knowledge
documents beyond what the user asked for. The cached `issue.md` /
`snapshot.md` files are projection-owned and read-only — refresh them via
the matching fetch script; never edit them in place.
