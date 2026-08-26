# Studykit Plugin Marketplace

This is the plugin marketplace directory - a collection of Claude Code and Codex plugins for various use cases.

## Version Management

Claude plugin versions live in each plugin's `plugins/<name>/.claude-plugin/plugin.json` (top-level `version` field, SemVer). Plugin entries in `.claude-plugin/marketplace.json` MUST NOT set `version` — if `version` is set in both places, `plugin.json` wins silently and a stale marketplace value would be masked.

Codex plugin manifests at `plugins/<name>/.codex-plugin/plugin.json` carry their own top-level `version` field. When a plugin supports both runtimes, bump the Claude and Codex `version` strings together and keep them identical.

When a new plugin is added or new features are added to an existing plugin, update the relevant marketplace files accordingly — `.claude-plugin/marketplace.json` for Claude and `.agents/plugins/marketplace.json` for Codex (registration only, not version).

## Claude and Codex Compatibility

Plugins should be designed and maintained to run in both Claude Code and Codex whenever possible. Avoid hardcoding agent-specific assumptions unless the feature is explicitly agent-specific. Keep shared behavior, scripts, documentation, and metadata portable across both environments, and clearly isolate any Claude-only or Codex-only implementation details.

Start with `guide/AGENTS.md` when adding or changing plugin manifests, hooks, skills, agents, commands, runtime scripts, or marketplace metadata. Use `guide/cross-runtime-guide.md` for cross-runtime architecture and marketplace/version policy, and `guide/adapter-guide.md` for adapter, hook, skill, and script runtime compatibility.

When developing or changing skills, hooks, plugins, or agents, always check the current official Claude Code and Codex documentation before relying on runtime behavior, manifest schemas, metadata fields, placeholders, environment variables, hook payloads, tool names, or marketplace behavior. Do not rely on memory or repository examples alone when an official behavior may have changed.

## Testing a Plugin in a Real Session

A plugin's runtime behavior — hooks firing, env exports reaching Bash, commands resolving —
cannot be verified by calling its scripts directly. Setting the variables a hook would have
set only tests the script; it does not test whether the host ever sets them.

**The installed copy is not your working tree.** Claude Code loads plugins from a versioned
cache (`~/.claude/plugins/cache/<marketplace>/<plugin>/<version>/`), so a session started
normally runs the last *installed* version and your edits are invisible to it. This is the
failure to plan for: the test passes or fails against code you did not write, and nothing
says so. Pass `--plugin-dir <absolute path to the plugin>` to load the working tree instead.

When a session runs inside [Herdr](https://herdr.dev), drive the test from a second pane
rather than the session you are working in — a hook under test that misbehaves takes down
the session it runs in, and testing in your own would take your work with it.

```sh
test "${HERDR_ENV:-}" = 1                      # refuse to drive Herdr from outside it
herdr pane split --current --direction down --cwd "$PWD" --no-focus
herdr agent start <name> --kind claude --pane <returned pane id> \
  -- --plugin-dir /abs/path/to/plugins/<plugin>
herdr agent prompt <name> '<what to run>' --wait --timeout 120000
herdr agent read <name> --source recent-unwrapped --lines 60
```

A plugin that ships a shell command can put it on `PATH` for the session with no install
step: `$CLAUDE_ENV_FILE` is a shell script the host *sources*, not a list of `export` lines,
so a `PATH` prepend written there from `SessionStart` reaches every later Bash command.
Prefer an executable over a shell function — a function is not inherited by subprocesses.

Test in a **throwaway project directory**, not in this repository. A plugin under test
writes state, and this repo already holds real state for the session you are working in:
`--cwd /tmp/<something>` keeps a bad write from landing on it, and a fresh directory is also
the only honest test of what a plugin does on first contact with a project that has never
seen it.

Two things to check before believing a result:

- **Confirm the new pane's environment is clean** before starting the agent. A pane
  inherits the environment of the shell that spawned it, so a variable your session already
  exports will appear set in the child and the test will pass without the hook doing
  anything. Print the variables first; they must be empty.
- **Ask for the raw output, verbatim.** The test session is an agent: it may summarize, and
  it may decline a command that looks like it exfiltrates an environment variable. Phrase
  probes as set/unset flags rather than value dumps, and re-read the pane rather than
  trusting a summary of what the pane showed.

## Language Requirements

**All documentation must be written in English.** When creating or editing markdown files, README files, CLAUDE.md files, or any other documentation, always use English.

## Shipped Definitions Must Be Repo-Portable

Everything this repository publishes gets installed into **someone else's repository**.
That applies to every plugin here, not one of them: `plugins/*/agents/*.md`,
`plugins/*/skills/*/SKILL.md`, and any instruction text a plugin injects at runtime
(hook context, dispatch playbooks, command bodies).

So a shipped definition must not name anything that exists only here — `dev/design.md`,
`wiki/ref/...`, `guide/...`, this repo's env vars, or the plugin's own command surface as
though the target project had it — and must not carry a measurement taken against this
repo. Teach the agent **how to find** the equivalent wherever it lands instead: "look for a
README or CONTRIBUTING section on testing, a `docs/` or `dev/` document, a Makefile target,
a CI workflow, a test directory".

The failure is silent, which is why this is a rule rather than a preference. A hardcoded
path does not raise an error in a stranger's checkout; the agent reads the absence as "this
project has no such thing" and its verdict changes without anyone noticing.

Rationale, measurements and this-repo specifics belong in the plugin's `dev/` notes or its
`AGENTS.md` — the files that stay behind. A frontmatter comment citing `wiki/ref/...` for a
design decision is fine: it addresses contributors, not the agent. When editing a shipped
definition, ask whether the sentence would still be true in a repository you have never
seen.

## Agent Instruction Files

Do **not** write detailed implementation content into any `AGENTS.md` file: no long procedures, step-by-step walkthroughs, code-level specifics, or internal mechanics. Keep that detail in the deeper docs it belongs to (deeper docs, `dev/` design notes, source) and link to it from `AGENTS.md` instead of inlining it.

- **Omit anything the code already shows.** If a fact is evident from reading the source — file/module layout, function names, control flow, which file handles what — leave it out; it only drifts out of date. Capture the *why* and the constraints the code cannot express, not a restatement of the code.
- **Detailed rationale belongs in code comments, not `AGENTS.md`** — and only when the code alone does not make it clear. If reading the code answers the question, no comment is needed either.
- **Keep a way to run the tests.** `AGENTS.md` may say how to test the component; when those instructions grow long, replace them with a pointer to the file that holds them (e.g. under `dev/`).

## Plugin README Scope

Each plugin's `plugins/<name>/README.md` is written for **end users who install the plugin from the marketplace**. It is not a contributor guide and is not context for the assistant at runtime.

Keep it scoped to user-visible surface:

- What the plugin does at a high level.
- Supported backends / providers / integrations.
- How to install and configure the plugin (config files, bootstrap skills).
- The slash commands, skills, or agents the plugin exposes and what each one does for the user.
- Pointers to deeper schema / reference docs (e.g. under `wiki/`).

Do **not** put in `README.md`:

- Directory or file-structure listings (script paths, hook layout, authoring tree, cache layout, internal module names).
- Hook-injected context, snippet substitution, runbook internals, or any other runtime-injected text.
- Test commands, validation, or anything else only contributors run.
- Implementation details of launchers, scripts, caches, or other plugin internals.

Contributor- and runtime-facing guidance lives in `AGENTS.md` files and under each plugin's `dev/`; runtime-injected context lives under `hooks/context/` (or the equivalent path for that plugin). When in doubt, ask whether a plugin user — not an author of the plugin — needs the information to install, configure, or invoke the plugin. If not, it does not belong in `README.md`.

