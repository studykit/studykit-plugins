# wiki/ref/

Local copies of official documentation cited as evidence in this repository, saved
under guard's evidence contract: when a claim rests on official docs, the cited
content is saved here and the answer cites both the source URL and this local path.
Each file records the relevant excerpt of one source and names its origin URL and
retrieval date, so a citation stays inspectable after the upstream page changes.

This is guard's default refs directory; `refs_dir` in `.claude/guard.local.json`
overrides the location. Files are committed through the normal git workflow — guard
never commits.

**Adding a reference:** save the excerpt as `<topic>.md` with `Source:` and
`Retrieved:` lines at the top, then add a row below. A file missing from this index
reads as a file nobody saved — the index is how the next reader finds it without
opening ten files. guard's `refs-index` hook fails the write when a new file is not
listed here.

## Index

| File | Subject | Source |
| --- | --- | --- |
| `claude-code-hooks-session-env.md` | SessionStart env persistence (`$CLAUDE_ENV_FILE`) and hook output fields | code.claude.com/docs/en/hooks |
| `claude-code-output-styles.md` | Output-style frontmatter schema, plugin `output-styles/` discovery, subagent scope | code.claude.com/docs/en/output-styles |
| `claude-code-pretooluse-permission-decision.md` | PreToolUse `permissionDecision` values | code.claude.com/docs/en/hooks |
| `claude-code-prompt-hooks.md` | Prompt-type hooks | code.claude.com/docs/en/hooks |
| `claude-code-subagent-frontmatter.md` | Subagent frontmatter fields; `tools` omitted inherits all, no way to express none | code.claude.com/docs/en/sub-agents |
| `jira-wiki-markup-notation.md` | Jira wiki markup notation (headings, effects, lists, links, tables, code) | Jira `WikiRendererHelpAction.jspa` |
| `markdown-footnotes.md` | Markdown footnote syntax (extended) | markdownguide.org/extended-syntax |
| `obsidian-block-links.md` | Obsidian block identifiers and block links | obsidian.md/help/links |
| `openai-codex-hooks-2026-08-14.md` | Codex plugin hook env vars and payloads | learn.chatgpt.com/docs/hooks |
| `openai-codex-skills-2026-08-14.md` | Codex `SKILL.md` requirements | learn.chatgpt.com/docs/build-skills |
| `openai-codex-subagents-2026-08-14.md` | Codex custom agents (TOML under `.codex/agents/`) | learn.chatgpt.com/docs/agent-configuration/subagents |
| `python-strenum.md` | `enum.StrEnum` version added and string behavior | docs.python.org/3/library/enum |
