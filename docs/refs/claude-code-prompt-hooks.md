# Claude Code — Prompt-type hooks

Source: https://code.claude.com/docs/en/hooks.md (fetched 2026-07-12)

## Prompt hook type
> **Prompt hooks** (`type: "prompt"`): send a prompt to a Claude model for
> single-turn evaluation. The model returns a yes/no decision as JSON.

## Prompt and agent hook fields
| Field | Required | Description |
| :--- | :--- | :--- |
| `prompt` | yes | Prompt text to send to the model. Use `$ARGUMENTS` as a placeholder for the hook input JSON. Escape with a backslash to include literal text: `\$1.00` renders as `$1.00` |
| `model` | no | Model to use for evaluation. Defaults to a fast model |

- Prompt hooks receive the same JSON input as command/HTTP hooks: common input
  fields (session_id, cwd, permission_mode, …) plus event-specific fields; for
  tool events that includes `tool_name` and `tool_input`.
- `$ARGUMENTS` is substituted with the entire hook input JSON object.

## Not documented on this page
The reference page does NOT specify the prompt-hook JSON *output* schema
(`{"ok": true/false, "reason": "..."}`), nor how a block/deny is surfaced to the
agent, nor whether the prompt template is echoed back on a block. (The
`ok`/`reason` shape is what SpecTrack's gate emits; the "hook error: [prompt]:
reason" rendering is observed empirically in transcripts, not documented here.)
