## issue-implementer subagent context

These provider-specific command shapes back the agent's review-publish
and implementation-task writeback flows. The active issue provider's
variant is substituted at SubagentStart so the agent body does not have
to restate command details.

### Publish a review (blocker handling)

{{ISSUE_DRAFTS_REVIEW_BLOCK}}

### Link the implementation task as blocked by the review

{{ISSUE_RELATIONSHIPS_BLOCKED_BY_BLOCK}}

### Refresh the implementation task's body (handoff Resume / closed snapshot)

{{ISSUE_WRITEBACK_BODY_BLOCK}}
