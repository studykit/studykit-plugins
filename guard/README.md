# Guard

Guard runs reviews that you define inside Claude Code and Codex:

- **Turn reviews** check a finished assistant response.
- **Plan reviews** check a plan file before implementation starts.
- **Answer documents** write a document, have your reviewer check it, and deliver the corrected file.
- **File reviews** collect changed files by pattern. Run a checkpoint yourself, or opt selected
  patterns into a confirmation question when the assistant finishes a turn.

Guard ships no reviewer agents or default review criteria. You choose an installed agent or
skill by its exact host name. An absent reviewer means that review does not run; an unavailable
reviewer is reported instead of being replaced.

Guard also refuses file searches rooted at `/`, adds a Claude Code status-line segment, and
provides an optional [Herdr](https://herdr.dev) popup for pending files and Git diffs.

## Install

**Claude Code**: add the marketplace and install the plugin:

```text
/plugin marketplace add studykit/studykit-plugins
/plugin install guard@studykit-plugins
```

**Codex**: open the plugin directory, choose the **Studykit Plugins** marketplace, and install
**guard**. If the marketplace was added while Codex was running, restart Codex first.

Every feature needs `uv` and Python 3.11 or newer on `PATH`. Review and trust Guard's hooks in
your host so change tracking and Stop questions can run. Stop questions also need an available
MCP connection and a host that permits interactive form requests.

## Configure project reviews

Run `/guard:settings` in Claude Code or `$guard:settings` in Codex. The skill helps you:

- Find an installed reviewer or create a project-local agent or skill using your review criteria.
- Choose the exact files and folders it should review, plus any exclusions.
- Select manual review or a Stop confirmation for each file pattern.
- View and change turn, plan, and answer reviewers without replacing unrelated settings.

Reviewer definitions belong to your project or user configuration; Guard does not install
bundled critics. Creating a new agent may require a new host session before it is available.
The settings skill distinguishes a saved rule from a reviewer that can actually be invoked.

Each project's settings live in `.claude/guard.local.json` for Claude Code and in
`.codex/guard.local.json` for Codex. A reviewer has a `kind` (`"agent"` or `"skill"`) and the
exact `name` that host uses. This example assumes you have created the named reviewers:

```json
{
  "turn_review":   {"kind": "agent", "name": "reviewer"},
  "plan_review":   {"kind": "agent", "name": "reviewer"},
  "answer_review": {"kind": "skill", "name": "review-answer"},
  "audit-plan": "on",
  "file_review_rules": [
    {
      "glob": "src/**",
      "action": {"kind": "agent", "name": "reviewer"},
      "on_stop": "ask"
    },
    {
      "glob": "docs/**/*.md",
      "action": {"kind": "skill", "name": "review-docs"},
      "on_stop": "manual"
    }
  ],
  "files_exclude": ["generated/**", "vendor/**"]
}
```

Names above are examples, not defaults. The two hosts may need different registered names.
An absent reviewer or `{}` disables that review. Invalid non-empty reviewer settings report
an error. With empty or absent `file_review_rules`, no files are queued.

## File reviews and Stop confirmation

`file_review_rules` maps project-relative globs to reviewers. Edits matching a rule enter the
session's pending queue. Each rule has an optional `on_stop` value:

| Value | Behavior |
| --- | --- |
| `"manual"` or omitted | Files wait until you invoke `audit-files`. |
| `"ask"` | When the assistant finishes a turn, Guard asks whether to review eligible pending changes. |

The same specificity rules select both the reviewer and `on_stop`; a more specific manual
rule can keep a file out of a broader Stop question. The feature applies to any configured
file type or folder, including files without an extension. It has no UI-specific criteria.
The question runs while the host is processing Stop, after the assistant's reply; it does
not wait for the CLI process to exit.

The question identifies the pending scope and offers **Run the configured reviewers** or
**Keep pending for later**, with no preselected answer. Select the review option and accept
to authorize the named reviewers to
check a frozen checkpoint of those changes, including reading its review scope and marking
the matching revisions reviewed afterwards. It does not approve a new design or authorize
implementation of the findings. The assistant invokes each exact configured agent or skill
and reports the results. If one is unavailable or fails, the affected files remain unreviewed;
Guard never supplies a fallback reviewer.
If file contents, selected reviewers or matching rules change after confirmation, the approved
token cannot authorize the changed scope. Request fresh consent before starting that review.

Declining, selecting no, or cancelling starts no review and leaves the files pending. Guard
does not ask again for the same file contents, selected rule and reviewer in that session.
A changed file, matching rule or reviewer can produce a new question. Review continuations
do not recursively prompt for the same changes. You can always request another checkpoint
explicitly.
An unavailable or failed form leaves the files unreviewed as well; the same offered revision
is not repeatedly prompted, and `audit-files` remains available for a retry.

Confirmation expires after five minutes. Expiration, unsupported forms, and failures explain
that no review started and point to `audit-files` for a manual retry. Approved Stop reviews
use Guard's connected tools with a single approval ID for checkpoint handling. Interrupted
connections can resume that approved scope, and repeating completion safely returns the
original result without clearing later edits. In Claude Code 2.1.274 or later,
Guard reuses that consent for its two internal checkpoint tools in the same project and
session, so those steps do not ask again. This does not grant permission to edit source files
or use other tools. Older hosts without MCP provenance keep their normal permission prompts;
Codex also retains its normal tool-permission flow.
The result separates reviewed files, findings, fixes, and files still pending. **Zero pending
files means the review queue is clear; it does not mean every finding was fixed.**

Run `/guard:audit-files` in Claude Code or `$guard:audit-files` in Codex to review the pending
queue at any time. Manual and confirmed reviews use the same reviewer grouping and checkpoint
completion rules. Only matching revisions are cleared; a file edited during review remains
pending. If ownership cannot be established for any selected path, report the partial review
and leave the checkpoint pending. Checkpoint completion records the caller's completed
workflow, not an independent proof that a reviewer ran or a guarantee that every finding was
resolved.

**Matching**

- `*` matches within one directory. `**` crosses directories, including zero levels.
- Rules apply to every file type, including files without an extension.
- When several rules match, the most specific one wins: an exact filename beats a filename
  pattern, then more literal directory depth and detail win. An exact tie uses the first rule.

**Exclusions**

- `files_exclude` entries apply in list order; the last match wins.
- `!pattern` restores files excluded earlier. A restored file still needs a matching rule.
- To match a filename starting with a literal `!`, write `\\!name.py` in JSON.
- `doc_dir` limits which directories count as ordinary Markdown documentation.

These are Guard's own project-relative globs, not full `.gitignore` syntax. An exception can
restore a single file inside an excluded directory.

## Turn reviews

Run `/guard:audit-turn` in Claude Code or `$guard:audit-turn` in Codex to review the last
completed response, or append a turn id to select an earlier response. Only your `turn_review`
reviewer runs. It receives recorded request, response, tool activity, and source location.

Each invocation requests a fresh review. Missing evidence, invalid configuration, and an
unavailable reviewer are errors, never a clean verdict. Reviewing a response does not authorize
project changes. `audit-turn` cannot be its own reviewer.

## Plan reviews

Run `/guard:audit-plan <path>` in Claude Code or `$guard:audit-plan <path>` in Codex to request
a fresh review by `plan_review`. Reviewing a plan does not start implementation; changes of
approach come back to you first. `audit-plan` cannot be its own reviewer.

Claude Code also requests this review when you approve a plan, before implementation begins.
The `audit-plan` setting (`"on"` by default, or `"off"`) controls that gate. The shell commands
`guard-plan on`, `guard-plan off`, and `guard-plan status` control it for the current session.
Codex supports the explicit plan-review command only.

## Answer documents

Run `/guard:answer <question>` in Claude Code or `$guard:answer <question>` in Codex. Guard
writes an English answer document, sends it to `answer_review`, and applies corrections within
the requested scope. Without a configured reviewer, it stops before drafting. `answer` cannot
be its own reviewer.

Documents are saved under `.claude/answers/` or `.codex/answers/`. For Korean readers, the
user-level `korean-translator` agent, if installed, translates the reviewed document. Otherwise
the reviewed English file is delivered with a note that translation was skipped.

## Status line (Claude Code)

`/guard:statusline` adds Guard's segment to your Claude Code status line. If you already have a
status line, it is kept and runs after Guard's segment. Without one, Guard installs its own
line: project path, git branch, remaining context, model and time. It uses Nerd Font icons and
24-bit colour, so it needs a Nerd Font and a truecolor terminal. The row looks like this, with
a shield icon in front of Guard's segment:

```text
 2 pending · ⚑    myrepo › src    main*    62%    Opus · xhigh ✻    3:41 PM
```

The number counts pending files. The flag shows the plan gate:
filled (`⚑`) when it is on, outlined (`⚐`) when it is paused for the session.

## Herdr

Inside Herdr, Guard offers a popup for the pending-file queue and an action that starts a
checkpoint. The popup needs two installs:

1. **The Guard Herdr plugin**, which provides the popup and the actions:

   ```sh
   herdr plugin install studykit/studykit-plugins/guard
   ```

2. **Herdr's agent integration for each host you use**. It reports each pane's agent session to
   Herdr, which is how the popup finds the right session's queue:

   ```sh
   herdr integration install claude   # Claude Code
   herdr integration install codex    # Codex
   ```

   Check with `herdr integration status`. The integration takes effect when a session starts.
   A session that was already running when you installed it is not recognized until it restarts,
   or until you run `/clear` in Claude Code.

Without the integration, the popup shows *"The focused pane has no Guard-compatible agent
session."* even though Guard itself is working. Guard keeps working normally without Herdr.

### Actions and popup

The plugin adds two actions:

- **Guard: show pending files** opens the popup for the focused Claude Code or Codex pane.
- **Guard: audit pending files** asks the agent in that pane to run the file checkpoint.

| Key | In the popup |
| --- | --- |
| `↑` `↓` / `j` `k` | Move the cursor |
| `Space` | Select or deselect a file |
| `Enter` | Open the current file in your editor |
| `d` / `Ctrl+D` | Show a read-only, side-by-side diff of Git `HEAD` against the working tree |
| `a` | Audit the selected files, or the whole queue when nothing is selected |
| `c` | Clear the selected files from the queue, after confirmation |
| `r` | Refresh |
| `q` | Close the popup, or return from a diff with your selections kept |

In the diff, `Tab` switches sides.

- The diff includes staged and unstaged changes. A new file is compared against an empty
  `HEAD` side.
- The diff needs a Git repository and `vimdiff` or Vim with diff support. Binary files and files
  over 8 MiB per side are not shown.
- Clearing files cancels an audit that is already running. Files edited afterwards start a
  fresh queue.

### Pending count in the sidebar

To show the count in Herdr's expanded Agent sidebar, add `$guard_pending` to an Agent row in
`~/.config/herdr/config.toml`:

```toml
[ui.sidebar.agents]
rows = [
  ["state_icon", "agent", "state_text"],
  ["$guard_pending"],
  ["workspace", "tab"],
]
```

The token disappears when the queue is empty.

### Editor and diff tool

By default, `Enter` opens `$VISUAL` or `$EDITOR`, falling back to `nvim`, `vim`, then `vi`. `d`
opens `vimdiff`. To choose other tools, create `~/.config/guard/herdr.toml`. Guard also reads
`$XDG_CONFIG_HOME/guard/herdr.toml`, or the path in `GUARD_HERDR_CONFIG`. The format is the same
as the `[editor]` and `[diff]` settings of [Lens](../lens/README.md#settings):

```toml
[editor]
# Replaces $VISUAL / $EDITOR for Enter. {file} is replaced and {line} becomes 1;
# without {file}, the path is appended.
command = "nvim {file}"

[diff]
# Replaces vimdiff for d and Ctrl+D. {before} is the HEAD copy and {after} the
# working copy, both temporary files; {name} is the path.
# Without {before}/{after}, the two paths are appended.
command = "difft {before} {after}"
pause = true       # wait for Enter afterwards, for tools that print and exit
```

The file is read when the popup opens and again on `r`. Mistakes are reported in the popup, and
the valid settings still apply. A configured tool must be on Herdr's `PATH`.
