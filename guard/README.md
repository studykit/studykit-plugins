# Guard

Guard lets you run reviews that you define yourself inside Claude Code and Codex:

- **Turn reviews**: check a finished assistant response.
- **Plan reviews**: check a plan file before implementation starts.
- **Answer documents**: write a document for a question, have it reviewed, and correct it.
- **Edited-file checkpoints**: record the files the agent changes, then review them with an agent or
  skill chosen by glob when you are ready.

Guard ships no review criteria of its own. Every reviewer is an agent or skill you install and
name in the settings. With no reviewer set, Guard does not review. Reviews never run on their
own, with one exception: Claude Code's plan gate, which runs when you approve a plan.

Guard also refuses file searches that start at the filesystem root (`/`). It adds a status
line segment and an optional [Herdr](https://herdr.dev) popup for the pending-file queue.

## Install

**Claude Code**: add the marketplace and install the plugin:

```text
/plugin marketplace add studykit/studykit-plugins
/plugin install guard@studykit-plugins
```

**Codex**: open the plugin directory, choose the **Studykit Plugins** marketplace, and install
**guard**. If the marketplace was added while Codex was running, restart Codex first. To use
Guard's bundled document reviewers in Codex, run `$guard:setup` once per project. It creates
their agent files under `.codex/agents/`. Start a new Codex session afterwards.

Every feature needs `uv` and Python 3.11 or newer on `PATH`.

## Settings

Each project's settings live in `.claude/guard.local.json` for Claude Code and in
`.codex/guard.local.json` for Codex. A reviewer is always written as an object with a
`kind` (`"agent"` or `"skill"`) and the exact `name` the host uses to invoke it:

```json
{
  "turn_review":   {"kind": "agent", "name": "my-turn-reviewer"},
  "plan_review":   {"kind": "agent", "name": "my-plan-reviewer"},
  "answer_review": {"kind": "skill", "name": "my-answer-reviewer"},
  "audit-plan": "on",
  "file_review_rules": [
    {"glob": "**/*.md", "action": {"kind": "agent", "name": "guard:doc-auditor"}}
  ],
  "files_exclude": ["vendor/**"]
}
```

An absent reviewer or `{}` means that review does not happen. A reviewer object that is set
but invalid is reported as an error. In Claude Code, `/guard:settings` views and changes these
settings through conversation and can suggest file-review rules.

## Turn reviews

Run `/guard:audit-turn` in Claude Code or `$guard:audit-turn` in Codex to review the last
completed response. To review an earlier response, append its turn id.

Your `turn_review` reviewer receives a JSON file with these fields:

- `turn_id`
- `user`: the request
- `assistant`: the response
- `tools`: recorded tool activity
- `source_path`: where to find more context

The reviewer should read this evidence and return findings without changing the evidence or
any project file. Findings are reported in the conversation.

Each run starts a fresh review. The evidence comes from what Guard's hooks recorded during the
session, so the hooks must be active. Missing evidence or an unavailable reviewer is reported
as an error, never as a clean review. `audit-turn` cannot be registered as its own reviewer.

## Plan reviews

Run `/guard:audit-plan <path>` in Claude Code or `$guard:audit-plan <path>` in Codex to review a
plan file with your `plan_review` reviewer. Every run requests a fresh review, even when the plan
was already reviewed. The assistant applies the findings you agree with to the plan and records
that the review is complete. Changes of approach are brought back to you first. Reviewing a plan
never starts implementation. `audit-plan` cannot be registered as its own reviewer.

In Claude Code, Guard also requests the review each time you approve a plan, before
implementation begins. A plan that changed is reviewed again at its next approval.

- The `audit-plan` setting (`"on"` / `"off"`) sets the project default for this gate.
- The shell commands `guard-plan on`, `guard-plan off`, and `guard-plan status` switch it or
  report its state for the current session.

Codex supports only the explicit command.

## Answer documents

Run `/guard:answer <question>` in Claude Code or `$guard:answer <question>` in Codex. Guard runs
these steps:

1. Writes an English answer document.
2. Has your `answer_review` reviewer read it and return findings.
3. Applies the corrections that fall within the question's scope.

Documents are saved under `.claude/answers/` or `.codex/answers/`. For Korean readers, a
user-level `korean-translator` agent, if installed, translates the reviewed document. Without
it, you receive the reviewed English file and a note that the translation was skipped.

Without a configured reviewer, the workflow stops before anything is drafted. `answer` cannot
review itself.

## Edited-file checkpoints

`file_review_rules` maps project-relative globs to reviewers. When the agent edits a file that
matches a rule, Guard adds it to a pending queue. Nothing is reviewed until you run
`/guard:audit-files` in Claude Code or `$guard:audit-files` in Codex. The checkpoint groups the
queued files by reviewer. It clears only the revisions that were reviewed successfully, so a file
edited again during the review stays queued.

```json
{
  "file_review_rules": [
    {"glob": "**/*.py",         "action": {"kind": "agent", "name": "guard:comment-corrector"}},
    {"glob": "**/*.md",         "action": {"kind": "agent", "name": "guard:doc-auditor"}},
    {"glob": "**/AGENTS.md",    "action": {"kind": "agent", "name": "guard:agents-md-auditor"}},
    {"glob": "config/**/*.json", "action": {"kind": "skill", "name": "my-config-review"}}
  ],
  "files_exclude": ["generated/**", "!generated/handwritten.py", "vendor/**"]
}
```

These are examples, not defaults. With an empty or absent `file_review_rules`, no file is
queued. A matching rule is the only way to opt a file in.

**Matching**

- `*` matches within one directory. `**` crosses directories, including zero levels.
- Rules apply to every file type, including files without an extension.
- When several rules match, the most specific one wins:
  1. An exact filename beats a filename pattern.
  2. Next, more literal directory depth and detail win.
  3. On an exact tie, the first rule in the list wins.

**Exclusions**

- `files_exclude` entries are applied in list order, and the last matching entry wins.
- `!pattern` restores files that an earlier entry excluded. In the example above,
  `generated/handwritten.py` is restored after `generated/**`. A restored file still needs a
  matching rule to be queued.
- To exclude a filename that starts with a literal `!`, write `\\!name.py` in the JSON.
- `doc_dir` limits which directories count as ordinary Markdown documentation.

These patterns are Guard's own globs with negation, not full `.gitignore` syntax. For example, a
`!` entry can restore a single file inside an excluded directory.

### Bundled reviewers

| Agent | What it does | Hosts |
| --- | --- | --- |
| `guard:doc-auditor` | Audits a project's ordinary Markdown documentation | Claude Code, Codex (after `$guard:setup`) |
| `guard:agents-md-auditor` | Audits agent instruction files (`AGENTS.md`, `CLAUDE.md`) | Claude Code, Codex (after `$guard:setup`) |
| `guard:ext-docs-auditor` | Audits files saved as local copies of external references | Claude Code, Codex (after `$guard:setup`) |
| `guard:comment-corrector` | Audits source comments and **edits them in place**; never changes code | Claude Code |
| `guard:claims-auditor` | Audits a text for claims it does not support | Claude Code |
| `guard:deferrals-auditor` | Audits a text for open questions its author could have resolved | Claude Code |
| `guard:clarity-auditor` | Audits whether a specific reader can follow an answer | Claude Code |

In Codex, keep the `guard:` names in your rules. Guard maps them to the agents that
`$guard:setup` installed. For source-code review in Codex, choose your own agent or skill.

The clarity auditor judges against a profile of you as a reader. Run `/guard:reader-profile`
in Claude Code to create or correct it.

## Status line (Claude Code)

`/guard:statusline` adds Guard's segment to your Claude Code status line. If you already have a
status line, it is kept and runs alongside Guard's segment. The segment looks like this:

```text
guard 2 pending · ⚑
```

The number counts the files waiting for `/guard:audit-files`. The flag shows the plan gate:
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
