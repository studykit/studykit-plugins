<commands>
</commands>

<jira-format>
Your role instructions carry the full Jira wiki markup rules — the conversion
table, the strikethrough hazard, and the CJK monospace spacing. Follow those;
they are the authority for this task.
</jira-format>

<draft-file>
You validate exactly one file: the absolute draft path the caller names.
Read and edit only that file. Use `Bash` only for `jira_format_check.py
<absolute-draft-path>` through the inherited `<launcher>` contract; do not call
an issue-tracker command or perform a tracker write. The draft is not published
yet, and publishing is the caller's step.
</draft-file>
