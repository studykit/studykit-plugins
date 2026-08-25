# `UserPromptExpansion` hook — what the official docs do and do not specify

Source: https://code.claude.com/docs/en/hooks (fetched 2026-08-21)

## Specified

**Trigger.** From the lifecycle table:

> When a user-typed command expands into a prompt, before it reaches Claude. Can block
> the expansion

**Matcher.** From the matcher-patterns table:

| Event | What the matcher filters | Example matcher values |
| --- | --- | --- |
| `UserPromptExpansion` | command name | your skill or command names |

So the matcher filters on the **command name** — the skill or command name after the `/`.

The matcher is compared against the **bare command name, not the full typed prompt**. For
`/my-review src/app.ts --strict`, the matcher is evaluated against `my-review`; arguments
are not part of the matcher string. This is why guard's `$`-anchored matchers
(`^(guard:)?audit-claims$`) keep firing when the user passes file paths.

How a matcher value is interpreted (general hook rule):

| Matcher value | Evaluated as |
| --- | --- |
| `"*"`, `""`, or omitted | match all |
| Only letters, digits, `_`, `-`, spaces, `,`, `\|` | exact string, or `\|`/`,`-separated list of exact strings |
| Contains any other character | JavaScript regular expression, **unanchored** |

**Input.** The event receives the common input fields (`session_id`, `prompt_id`,
`transcript_path`, `cwd`, `permission_mode`, `hook_event_name`).

**Blocking.** The event can block the expansion (exit code 2).

## NOT specified

The page does **not** document a field carrying the user's **argument text** — whatever
the user typed after the command name. The common input fields do not include it, and the
event-specific input schema for `UserPromptExpansion` is not given on the page.

The page also does not give the `hookSpecificOutput` schema for this event specifically.
guard emits `{"hookSpecificOutput": {"hookEventName": "UserPromptExpansion",
"additionalContext": "..."}}`, which works in practice.

## Why guard cares

guard's three on-demand audit commands (`/guard:audit-claims`, `/guard:audit-deferrals`,
`/guard:correct-korean`) accept optional file-path arguments. Because the hook payload is
not documented to carry the argument text, guard reads it in the **skill body** via
`$ARGUMENTS` (a documented skill-content substitution) instead of in the hook. The hook
therefore emits its turn dispatch unconditionally, and each skill's file branch overrides
it. See `plugins/guard/dev/design.md`, "File mode lives in the skill, not the hook".

---

## Blocking the expansion — mechanism and turn effect

Source: https://code.claude.com/docs/en/hooks.md (raw markdown via `curl`)
Retrieved: 2026-08-25

### The event's own decision-control table

> #### UserPromptExpansion decision control
>
> `UserPromptExpansion` hooks can block the expansion or add context. All [JSON output fields](#json-output) are available.

| Field | Description |
| :--- | :--- |
| `decision` | `"block"` prevents the command from expanding. Omit to allow it to proceed |
| `reason` | Shown to the user when `decision` is `"block"` |
| `additionalContext` | String added to Claude's context alongside the expanded prompt. See [Add context for Claude](#add-context-for-claude) |

> A hook that blocks by exiting 2 routes the same way as `reason`: the block message shows the stderr text to the user.

```json
{
  "decision": "block",
  "reason": "This slash command is not available",
  "hookSpecificOutput": {
    "hookEventName": "UserPromptExpansion",
    "additionalContext": "Additional context for this expansion"
  }
}
```

So the mechanism is **top-level `decision: "block"` + `reason`**, not
`hookSpecificOutput.permissionDecision`. The decision-control summary table
confirms the family:

> | Events | Decision pattern | Key fields |
> | UserPromptSubmit, UserPromptExpansion, PostToolUse, PostToolUseFailure, PostToolBatch, Stop, SubagentStop, ConfigChange, PreCompact | Top-level `decision` | `decision: "block"`, `reason`. Stop and SubagentStop also accept `hookSpecificOutput.additionalContext` for non-error feedback that continues the conversation |

Note the parenthetical exemption: only `Stop`/`SubagentStop` are named as
continuing the conversation on block.

### Exit code 2

From the "Exit code 2 behavior per event" table:

> | Hook event | Can block? | What happens on exit 2 |
> | `UserPromptSubmit` | Yes | Blocks prompt processing and erases the prompt |
> | `UserPromptExpansion` | Yes | Blocks the expansion |

General exit-2 rules that apply:

> Exit 2 means a blocking error. On events that can block, exit 2 blocks whether or not you print JSON: even a JSON `permissionDecision` of `"allow"` can't override it. Claude Code still reads any valid JSON output on stdout.

> The blocking message is the reason from your JSON's blocking decision when it makes one, and your stderr text otherwise.

### Does the turn end without inference?

The page states this only in the **prompt-based hooks** section, describing
`ok: false` from a `type: "prompt"` hook — but the sentence explicitly
generalizes to `decision: "block"`:

> * `PostToolBatch`, `UserPromptSubmit`, and `UserPromptExpansion`: the turn ends and the reason appears as a warning line. These events end the turn on `decision: "block"` regardless of `continue`

That final clause is the only place the page ties `decision: "block"` on
`UserPromptExpansion` to "the turn ends", and the only place it says the
outcome is independent of `continue`.

**What the page does not say:** it never uses the words "no model call",
"no inference", or "Claude is not invoked". "The turn ends and the reason
appears as a warning line" is the strongest documented statement. It also
never says whether the `reason` is or is not placed in Claude's context on a
block — for `UserPromptExpansion` the table says only that `reason` is
"Shown to the user".

### `continue: false`

`continue` is a universal JSON output field, and the event's section says
"All JSON output fields are available."

> | Field | Default | Description |
> | `continue` | `true` | If `false`, Claude stops processing entirely after the hook runs. Takes precedence over any event-specific decision fields |
> | `stopReason` | none | Message shown to the user when `continue` is `false`. Not shown to Claude |

> To stop Claude entirely:
> ```json
> { "continue": false, "stopReason": "Build failed, fix errors before continuing" }
> ```

The page lists events that *ignore* `continue` (e.g. `TaskCreated`:
"`continue: false` is ignored"). `UserPromptExpansion` is not on that list;
instead it is named in the clause "These events end the turn on
`decision: "block"` **regardless of `continue`**" — i.e. `continue` is not
needed to end the turn there, which is not the same as saying it is ignored.

### Channels that reach the user without passing through the model

Documented fields whose text the page says goes to the user and explicitly
not to Claude:

> | `stopReason` | none | Message shown to the user when `continue` is `false`. **Not shown to Claude** |

> | `systemMessage` | none | Warning message shown to the user. In Agent SDK and `--output-format stream-json` output, it can arrive as an `SDKInformationalMessage` |

> | `terminalSequence` | none | A terminal escape sequence for Claude Code to emit on your behalf, such as a desktop notification, window title, or bell. Restricted to OSC `0`/`1`/`2`/`9`/`99`/`777` and BEL. … Use this instead of writing to `/dev/tty`, which is unavailable to hooks |

And for `UserPromptExpansion` specifically, `reason`:

> | `reason` | Shown to the user when `decision` is `"block"` |

Contrast with the stdout / `additionalContext` channel:

> Exit 0 means success, and is the intended exit code when you print JSON for structured control. For most events, stdout is written to the debug log but not shown in the transcript. The exceptions are `UserPromptSubmit`, `UserPromptExpansion`, and `SessionStart`, where Claude Code adds plain-text stdout as context that Claude can see and act on.

> Where the reminder appears depends on the event:
> * UserPromptSubmit and UserPromptExpansion: alongside the submitted prompt

Stderr on a non-blocking exit is neither channel:

> Stderr from a hook that exits 0 goes to the debug log only, never the transcript, and Claude never sees it.

**Derived** (from the `reason`/`stopReason`/`systemMessage` rows plus the
exit-2 routing sentence, none of which states this on its own): the page
describes at least four fields for `UserPromptExpansion` whose text it says
is shown to the user — `reason`, exit-2 stderr (which "routes the same way as
`reason`"), `stopReason`, and `systemMessage` — and only `stopReason` carries
an explicit "Not shown to Claude". For `reason`, exit-2 stderr and
`systemMessage` the page says where the text goes but never states whether
Claude also sees it.

### Not specified on this page

- Whether a blocked expansion results in **zero model inference**. The page
  says "the turn ends and the reason appears as a warning line"; it does not
  describe the model-call lifecycle.
- Whether the `reason` text on a `UserPromptExpansion` block is additionally
  placed in Claude's context.
- Whether `additionalContext` returned *together with* `decision: "block"`
  is still injected, or discarded because the expansion did not happen. The
  page's own example returns both fields in one object without saying.
- Whether `stopReason` / `continue: false` behaves any differently from
  `decision: "block"` on this event beyond the "regardless of `continue`"
  clause.
