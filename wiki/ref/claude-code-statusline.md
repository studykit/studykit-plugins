# Status line — plugin support, input fields, invocation

Source: https://code.claude.com/docs/en/statusline (fetched via
`https://code.claude.com/docs/en/statusline.md`, 2026-08-22) and
https://code.claude.com/docs/en/plugins-reference (same date).

## Configuration is a user/project setting, not a plugin capability

> Add a `statusLine` field to your user settings (`~/.claude/settings.json`, where `~` is
> your home directory) or [project settings](/docs/en/settings#where-settings-live). Set
> `type` to `"command"` and point `command` to a script path or an inline shell command.

```json
{
  "statusLine": {
    "type": "command",
    "command": "~/.claude/statusline.sh",
    "padding": 2
  }
}
```

From `plugins-reference`, the plugin layout table — the only two settings keys a plugin's
`settings.json` may carry:

> | **Settings** | `settings.json` | Default configuration applied when the plugin is
> enabled. Only the [`agent`](/docs/en/sub-agents) and
> [`subagentStatusLine`](/docs/en/statusline#subagent-status-lines) keys are supported |

And, on `subagentStatusLine` specifically:

> Plugins can ship a default `subagentStatusLine` in their
> [`settings.json`](/docs/en/plugins-reference#standard-plugin-layout), but unlike hooks,
> plugin values don't run under `allowManagedHooksOnly` even when the plugin is
> force-enabled in managed settings `enabledPlugins`.

A third source agrees. From `settings-reference`, the settings table — the "scope" column
names which *settings files* may carry the key (user / project / local / managed), not
plugins:

> | [`statusLine`](#statusline) | Run your own command to render a
> [status line](/docs/en/statusline) below the prompt | Interface and terminal | Any file |
> | [`subagentStatusLine`](#subagentstatusline) | Rewrite rows in the
> [subagent](/docs/en/sub-agents) task display with your own command | Interface and
> terminal | Any file |

And the `.claude-plugin/plugin.json` manifest field table lists no status-line key at all:
`$schema`, `displayName`, `version`, `description`, `author`, `homepage`, `repository`,
`license`, `keywords`, `metadata`, `defaultEnabled`.

## What a plugin CAN ship: `subagentStatusLine`

This is the narrow case, and it is a real one — it renders the rows in the agent panel, not
the main bar:

> The `subagentStatusLine` setting renders a custom row body for each
> [subagent](/docs/en/sub-agents) shown in the agent panel below the prompt. Use it to
> replace the default `name · description · token count` row with your own formatting.

> The command runs once per refresh tick and receives all visible subagent rows as a single
> JSON object on stdin. The input includes the [base hook
> fields](/docs/en/hooks#common-input-fields), a `columns` field with the usable row width,
> and a `tasks` array. Each task has `id`, `name`, `type`, `status`, `description`, `label`,
> `startTime`, `model`, `effort`, `contextWindowSize`, `tokenCount`, `tokenSamples`, and
> `cwd`.

> Write one JSON line to stdout per row you want to override, in the form
> `{"id": "<task id>", "content": "<row body>"}`. […] Omit a task's `id` to keep the default
> rendering for that row; emit an empty `content` string to hide it.

## Input fields (stdin JSON) relevant to a per-session plugin segment

> | `session_id` | Unique session identifier |
> | `workspace.project_dir` | Directory where Claude Code was launched, which may differ
> from `cwd` if the working directory changes during a session |
> | `cwd`, `workspace.current_dir` | Current working directory. Both fields contain the
> same value; `workspace.current_dir` is preferred for consistency with
> `workspace.project_dir`. |
> | `prompt_id` | UUID identifying the user prompt currently being processed. […] Absent
> until the first user input. Requires Claude Code v2.1.196 or later |
> | `transcript_path` | Path to conversation transcript file |

## Invocation frequency and failure behaviour

> Your script runs once when a session starts, including when you resume one. After that,
> it runs again when:
>
> * A new assistant message arrives
> * `/compact` finishes
> * The permission mode changes
> * Vim mode toggles
> * A [`refreshInterval`](#manually-configure-a-status-line) timer elapses, if you set one
>
> Claude Code debounces updates at 300ms, so rapid changes batch together and your script
> runs once after the changes stop. If a new update triggers while your script is still
> running, Claude Code cancels the in-flight script.

> Your status line script runs frequently during active sessions. Commands like
> `git status` or `git diff` can be slow, especially in large repositories.

> The status line runs locally and does not consume API tokens.

Output: stdout is displayed; each line printed becomes a row; ANSI colour codes are
honoured when the terminal supports them.

## Bearing on guard

- **guard cannot install its own MAIN status line.** Three sources agree: the plugin layout
  table limits plugin `settings.json` to `agent` and `subagentStatusLine`; the statusline
  page names only `subagentStatusLine` in the sentence about what plugins may ship; and the
  plugin manifest has no status-line field. So a persistent "audits on/off" indicator has to
  be a *segment* the user composes into whatever status line they already run — guard
  supplies the command, the user (or guard's setup skill, with consent) wires it.
- **A plugin CAN ship `subagentStatusLine`**, which is a genuine plugin-owned status line —
  but it only renders rows for subagents *currently visible in the agent panel*. It could
  label guard's audit agents while they run; it cannot show that auditing is switched on
  when nothing is running, which is the state a user needs to see.
- **A per-session segment is possible**, because the stdin JSON carries `session_id` and
  `workspace.project_dir`, which together locate `.claude/guard/state/<sid>.json`.
- **It must be fast and silent on failure.** It runs on every assistant message, debounced
  at 300ms, and an in-flight script is cancelled by the next update. Reading one small JSON
  file is within budget; anything that shells out is not. On any error it must print
  nothing rather than an error, since its output goes straight into the user's status bar.
- It costs no tokens, which is why a status line is the right home for state the user needs
  continuously — unlike a per-turn hook line, which is paid for in context every turn.

---

# Related: plugin `commands/` vs `skills/`, and command arguments

Source: https://code.claude.com/docs/en/plugins-reference and
https://code.claude.com/docs/en/hooks (fetched 2026-08-22).

## `commands/` is the flat-file form of a skill, not a separate mechanism

From the plugin layout table:

> | **Skills** | `skills/` | Skills with `<name>/SKILL.md` structure |
> | **Commands** | `commands/` | Skills as flat Markdown files. Use `skills/` for new plugins |

`plugin inspect` counts both in one group:

> The output lists all components the plugin contributes, grouped as Skills, Agents, Hooks,
> MCP servers, and LSP servers […] The Skills group includes both `skills/` and `commands/`
> entries.

So the choice between them is file layout — one flat `.md` versus a directory with
`SKILL.md` — and the same frontmatter and `/plugin:name` invocation apply either way. The
docs steer new plugins to `skills/`.

## `UserPromptExpansion` receives the command's arguments

From the hook-lifecycle table (retrieved 2026-08-23, same page):

> When a **user-typed** command expands into a prompt, before it reaches Claude. Can block
> the expansion

The emphasis is added; the word "user-typed" is the page's own. It is the whole answer to
"does this fire when the MODEL invokes a skill" — a model invocation goes through the
`Skill` tool rather than through prompt expansion, so nothing expands and this event never
fires. The docs do not say that in so many words, so treat the inference as an inference:
what is quoted is the trigger, and a Skill-tool invocation is not it.

> Matches on `command_name`. Leave the matcher empty to fire on every prompt-type command.

> In addition to the [common input fields](#common-input-fields), UserPromptExpansion hooks
> receive `expansion_type`, `command_name`, `command_args`, `command_source`, and the
> original `prompt` string.

```json
{
  "session_id": "abc123",
  "hook_event_name": "UserPromptExpansion",
  "expansion_type": "slash_command",
  "command_name": "example-skill",
  "command_args": "arg1 arg2",
  "command_source": "plugin",
  "prompt": "/example-skill arg1 arg2"
}
```

And stdout is context the model sees:

> The exceptions are `UserPromptSubmit`, `UserPromptExpansion`, and `SessionStart`, where
> Claude Code adds plain-text stdout as context that Claude can see and act on.

## Bearing on guard

`command_args` is what makes `/guard:toggle`, `/guard:toggle on` and `/guard:toggle off` one
command rather than three. The hook does the work — flips the session flag and prints the
resulting state — so the command file is an entry point rather than instructions for the
model to follow, and the outcome does not depend on the model reading and obeying a
procedure. This is the same shape guard already uses for `verify <agent>`, except that there
the agent name is hardcoded per matcher in `hooks.json` and here it comes from the payload.

