## workflow policy

Before editing a workflow issue or knowledge document, ask `workflow-operator` for the required authoring paths, then read those files locally before drafting or editing content.
For comment-only workflow issue updates, ask `workflow-operator` for comment-scope authoring paths and read only those files before drafting the comment.
For workflow issues, draft or edit title/body/labels locally. After local draft/edit content is complete, tell `workflow-operator`; it will publish and verify provider updates.
For new workflow issues, stop at the pending draft until the user explicitly approves provider issue creation.
