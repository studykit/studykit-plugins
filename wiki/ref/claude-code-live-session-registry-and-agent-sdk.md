# The live session registry (`claude agents --json`) vs. the Agent SDK's session API

Source: `claude --help` / `claude agents --help` / `claude stop --help` on Claude Code
2.1.258 (local binary), probes of the same binary, and
https://code.claude.com/docs/en/agent-sdk (overview),
https://code.claude.com/docs/en/agent-sdk/python,
https://code.claude.com/docs/en/agent-sdk/sessions
Retrieved: 2026-09-03

Why this is saved: the `peers` plugin addresses Claude sessions running in other folders
on the same machine. Two questions decide its design — how a folder is mapped to a live
session, and whether the Agent SDK is a better foundation than shelling out to the CLI.
Both were answered here rather than assumed.

## `ListAgents` names peers but does not report their working directory

The `ListAgents` tool lists live peers as `name [ref] · kind · status · started Nm ago`.
It carries no `cwd`. Measured output (2026-09-03):

```
Peer sessions (5):
  notes [aae59c]  ·  interactive  ·  idle  ·  started 20m ago
  probe-agent [d88675]  ·  bg  ·  busy  ·  started 2s ago
```

`claude agents --json` is the surface that carries the directory. From its own help:

> `--json`  Print active sessions (interactive and background) as a JSON array and exit
> (for scripting; does not require a TTY)

Measured shape of one element:

```json
{
  "pid": 23397,
  "cwd": "/Volumes/NVME/Users/nekopilot/GitHub/Notes",
  "kind": "interactive",
  "startedAt": 1788363148205,
  "sessionId": "5e6673d6-51b5-42ad-80e7-45c38264c8d4",
  "name": "notes",
  "status": "idle"
}
```

`kind` is `interactive` or `background`; the same session that `ListAgents` renders as
`bg` appears here as `background`. The current session is in this list too — it is
identified by `sessionId == $CLAUDE_CODE_SESSION_ID`, verified by matching the env var
against the array.

A registry entry may omit `status`: the SDK-driven session in the probe below had no
`status` key while every CLI-started session had one.

## Two facts about starting a peer

**`--bg` is the only unattended launch.** Starting `claude` interactively in a directory
it has not been used in before stops on the workspace-trust prompt:

> Quick safety check: Is this a project you created or one you trust? … Claude Code'll be
> able to read, edit, and execute files here.

The prompt blocks startup (`herdr agent start` reported `agent_not_ready: blocked during
startup`). `--bg` reaches `idle` in the same directory without showing it, consistent
with the `-p/--print` help text:

> The workspace trust dialog is skipped when Claude is run in non-interactive mode (via
> `-p`, or when stdout is not a TTY, e.g. piped or redirected output).

**`claude stop` is background-only.** Its whole help text:

> `Usage: claude stop <id>` — Stop a background session. Its conversation is kept; resume
> it later with `claude attach <id>`.

There is no CLI verb that stops an `interactive` peer, which is the terminal a person is
sitting in front of.

`claude logs <id>` returns the raw ANSI terminal capture of the session's TUI — cursor
addressing, spinner frames and all. It is not a transcript and cannot be parsed for a
result.

## The Agent SDK does not answer "which session is live"

The overview places the SDK next to the CLI rather than over it:

> | Building an agent without implementing the tool loop yourself | **Agent SDK** | A
> library that runs the agent loop in your own process, in Python or TypeScript. |

Its session functions read transcripts from disk, not the live registry. `list_sessions()`
returns `SDKSessionInfo`:

```python
@dataclass
class SDKSessionInfo:
    session_id: str
    summary: str
    last_modified: int
    file_size: int | None
    custom_title: str | None
    first_prompt: str | None
    git_branch: str | None
    cwd: str | None
    tag: str | None
    created_at: int | None
```

There is no `pid`, no `kind`, no `status` — nothing that separates a running session from
a finished one. The sessions page confirms what is being enumerated:

> Claude Code stores sessions under `~/.claude/projects/<encoded-cwd>/*.jsonl`.

and describes `resume` as re-reading such a file, with the constraint:

> **Same machine only**: the session file still needs to exist on the current machine.

Nothing in the full Python export list (`query`, `tool`, `create_sdk_mcp_server`,
`list_sessions`, `get_session_messages`, `get_session_info`, `rename_session`,
`tag_session`, `ClaudeSDKClient`) addresses another *running* session.

## Probe: an SDK-driven session does register, and dies with its process

Assumption worth having checked — a `ClaudeSDKClient` session **is** visible in the live
registry while connected. Probed on 2.1.258 with `claude-agent-sdk` via
`uv run --with claude-agent-sdk`, reading `claude agents --json` from inside the `async
with` block:

```
NEW_IN_REGISTRY: [{"pid": 37749, "cwd": "/private/tmp/sdk-probe", "kind": "interactive",
                   "startedAt": 1788365105676,
                   "sessionId": "dcd9578b-4da3-40a0-bd55-6faa172a1c98",
                   "name": "sdk-probe-96"}]
SDK_SESSION_ID: dcd9578b-4da3-40a0-bd55-6faa172a1c98 subtype: success
```

The name is auto-derived from the directory the same way a CLI session's is. After the
script exited, the entry was gone from `claude agents --json`.

That lifetime is the finding: an SDK peer lives exactly as long as the Python process
holding the connection, so a short-lived command cannot leave one running. `claude --bg`
produces a peer that outlives the command that started it and that `claude stop` can end
later.

One more constraint on building peers with the SDK, from the overview:

> Unless previously approved, Anthropic does not allow third party developers to offer
> claude.ai login or rate limits for their products, including agents built on the Claude
> Agent SDK. Use the API key authentication methods described in the Quickstart instead.

## Probe: permission mode comes from settings, not from the parent

A peer started from a session running in bypass mode came up in bypass mode too, which
looks like environment inheritance but is not: no permission-related variable is exported
(`env | grep -i -E "claude|permission"` lists `CLAUDE_CODE_SESSION_ID`,
`CLAUDE_CODE_MESSAGING_SOCKET`, `CLAUDE_CODE_ENTRYPOINT` and similar, none of them a
mode). The mode came from `~/.claude/settings.json`:

```json
"permissions": { "defaultMode": "bypassPermissions" }
```

So a launcher that passes no `--permission-mode` gets the target project's own settings —
and one that passes a mode silently overrides the user's configured default.
