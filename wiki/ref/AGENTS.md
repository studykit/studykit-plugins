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
opening ten files. guard's `post-edit` hook fails the write when a new file is not
listed here.

## Index

| File | Subject | Source |
| --- | --- | --- |
| `claude-code-headless-child-flags.md` | Flags for a lightweight `claude -p` child: `--safe-mode` disables hooks while keeping auth, why `--bare` is rejected, and a probe table showing that omitting `--allowedTools` does NOT withhold tools | `claude --help` + probes (2.1.238) |
| `claude-code-hooks-in-subagents.md` | That `PreToolUse`/`PostToolUse` fire the same hooks for a subagent's tool calls as for the main conversation, the `agent_id`/`agent_type` fields that tell them apart, and that a plugin subagent reports the plugin-scoped name (so a matcher must be anchored) | code.claude.com/docs/en/hooks |
| `claude-code-hooks-session-env.md` | SessionStart env persistence (`$CLAUDE_ENV_FILE`), hook output fields, the matcher `source` values (`startup`/`resume`/`clear`/`compact`/`fork`), and which events show plain stdout to the model | code.claude.com/docs/en/hooks |
| `claude-code-session-id-env.md` | That `CLAUDE_CODE_SESSION_ID` is set automatically in Bash and hook command subprocesses — matching the hook payload's `session_id`, updated on `/clear` — and where `--continue` / `--resume` without an explicit id may diverge from it; plus a retrieval note that a summarizing `WebFetch` of this ~464 KB page twice reported the variable absent when it is present | code.claude.com/docs/en/env-vars |
| `claude-code-output-styles.md` | Output-style frontmatter schema, plugin `output-styles/` discovery, subagent scope | code.claude.com/docs/en/output-styles |
| `claude-code-userpromptexpansion-needs-a-command-file.md` | Probe: a `UserPromptExpansion` matcher never fires for a name with no skill/command file — the host answers `Unknown command` before any hook runs — so deleting a command file silently disarms its matcher with nothing reporting the orphan | probe of `claude` 2.1.241 |
| `markitdown-mcp.md` | That the server exposes exactly one tool, `convert_to_markdown(uri)`, accepting `http:`/`https:`/`file:`/`data:` — so it is a fetch path as well as a converter; that it ships on PyPI with a `uvx` runtime hint over stdio at alpha version `0.0.1a4`; and that the tool is an arbitrary-local-file read no `tools` allowlist narrows | github.com/microsoft/markitdown + github.com/mcp/microsoft/markitdown |
| `claude-code-plugin-mcp-servers.md` | That a plugin ships MCP servers through a root `.mcp.json` (started automatically, session-wide) while a plugin-shipped **agent** may not declare `mcpServers` at all — the field is silently ignored, not rejected — so scoping an MCP tool to one agent can only be done with that agent's `tools` allowlist, and even then the main session still sees the server | code.claude.com/docs/en/plugins-reference + /plugins |
| `claude-code-pretooluse-deny-reason-visibility.md` | Probe: a PreToolUse `deny` reason reaches the model verbatim as the tool's `<error>` result (the docs do not say so); the call is attempted before it is blocked; and a reason naming a replacement is read as tool output, not as an instruction the session must follow | probe of `claude` 2.1.240 |
| `claude-code-pretooluse-permission-decision.md` | PreToolUse `permissionDecision` values | code.claude.com/docs/en/hooks |
| `claude-code-prompt-hooks.md` | Prompt-type hooks | code.claude.com/docs/en/hooks |
| `claude-code-skill-arguments.md` | That BOTH the model and the user can pass arguments to a skill, the `$ARGUMENTS` / `$ARGUMENTS[N]` / `$N` / `$name` placeholders and the `arguments` frontmatter list behind named ones, and how a missing argument behaves differently for an indexed placeholder than for a named one | code.claude.com/docs/en/skills |
| `claude-code-skill-fork-context.md` | Skill frontmatter `context: fork` / `agent` / `background`: running a skill's body in an isolated subagent that does NOT inherit conversation history, why the agent supplies the system prompt and the skill body the task, the background default and what overrides it | code.claude.com/docs/en/skills |
| `claude-code-skill-invocation-paths.md` | Probe: a skill invoked by the MODEL (`Skill` tool) does not fire `UserPromptExpansion`, while a user-typed `/name` does; `` !`command` `` body injection runs on both — plus the documented abort, pre-approval and re-append rules that follow for anything built on injection, and a companion probe showing `context: fork` accepts a plugin-scoped `agent: <plugin>:<name>` | probe of `claude` 2.1.240 + code.claude.com/docs/en/skills, /hooks |
| `claude-code-skill-injection-and-fork-probe.md` | Probe: argument placeholders and `${CLAUDE_SESSION_ID}` are substituted **before** an injected `` !`command` `` runs (the script saw real values in its own `argv`), the injected call surfaces no `tool_use` event of its own, and a `context: fork` skill keeps the `Agent` tool — plugin-scoped agents included — with only the fork's final message reaching the parent | probe of `claude` 2.1.241 |
| `claude-code-skill-substitutions.md` | Which placeholder a plugin skill or flat command file may use to reach a bundled script | code.claude.com/docs/en/skills |
| `claude-code-statusline.md` | Status line as a user/project setting rather than a plugin capability, its input fields and invocation; also `commands/` vs `skills/` in a plugin and the `command_args` field on `UserPromptExpansion` and the fact that it fires only on a **user-typed** command expansion | code.claude.com/docs/en/statusline + /plugins-reference |
| `claude-code-stop-hook-decision-control.md` | Stop hook output: `decision: "block"` vs `hookSpecificOutput.additionalContext`, their shared loop protections, and how `additionalContext` reaches the model | code.claude.com/docs/en/hooks |
| `claude-code-subagent-resume.md` | Naming a subagent at dispatch, resuming one by name with `SendMessage` (full history retained, auto-resume in background), how long subagent transcripts persist, the interactive panel that lets the **user** open a background agent's transcript and message it directly, what decides foreground vs background, and fork vs plain subagent | code.claude.com/docs/en/sub-agents |
| `claude-code-subagent-frontmatter.md` | Subagent frontmatter fields; `tools` omitted inherits all, no way to express none | code.claude.com/docs/en/sub-agents |
| `claude-code-subagent-memory.md` | The `memory` frontmatter field: `user`/`project`/`local` scopes and their directories, MEMORY.md auto-injection limits, and the fact that it silently enables Write/Edit | code.claude.com/docs/en/sub-agents |
| `jira-wiki-markup-notation.md` | Jira wiki markup notation (headings, effects, lists, links, tables, code) | Jira `WikiRendererHelpAction.jspa` |
| `markdown-footnotes.md` | Markdown footnote syntax (extended) | markdownguide.org/extended-syntax |
| `obsidian-block-links.md` | Obsidian block identifiers and block links | obsidian.md/help/links |
| `openai-codex-hooks-2026-08-14.md` | Codex plugin hook env vars and payloads | learn.chatgpt.com/docs/hooks |
| `openai-codex-pretooluse-payload.md` | Codex `PreToolUse` payload fields — carries no `agent_id`/`agent_type` | learn.chatgpt.com/docs/hooks |
| `openai-codex-skills-2026-08-14.md` | Codex `SKILL.md` requirements | learn.chatgpt.com/docs/build-skills |
| `openai-codex-subagents-2026-08-14.md` | Codex custom agents (TOML under `.codex/agents/`) | learn.chatgpt.com/docs/agent-configuration/subagents |
| `python-strenum.md` | `enum.StrEnum` version added and string behavior | docs.python.org/3/library/enum |
