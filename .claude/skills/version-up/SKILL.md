---
name: version-up
description: Bump the SemVer `version` in a single plugin's `plugin.json` manifests (Claude and Codex, when present). Edits manifests only — no commit, tag, or push.
argument-hint: "<plugin-name> <patch|minor|major|X.Y.Z>"
disable-model-invocation: true
context: fork
model: sonnet
allowed-tools: Read Edit
---

# Plugin Version Up

Bump the SemVer version of a single marketplace plugin's manifest files. This skill edits `plugin.json` only — it does not stage, commit, tag, or push.

## Inputs

- `$plugin` — plugin directory name under `plugins/` (e.g., `spec-track`, `a4`, `doc`).
- `$level` — one of `patch`, `minor`, `major`, or an explicit version string in `X.Y.Z` form.

If either argument is missing, stop and ask the user. If `$plugin` does not resolve to a directory under `plugins/`, stop and report the mismatch — do not guess the intended plugin.

## Procedure

1. Read `plugins/$plugin/.claude-plugin/plugin.json`. This is the canonical Claude manifest and must exist; if it does not, stop and report — the plugin name is wrong.
2. Capture the current top-level `version` field. Expected format: `MAJOR.MINOR.PATCH`.
3. Compute the new version from `$level`:
   - `patch` → increment `PATCH`.
   - `minor` → increment `MINOR`, reset `PATCH` to `0`.
   - `major` → increment `MAJOR`, reset `MINOR` and `PATCH` to `0`.
   - Explicit `X.Y.Z` → use as given. Validate against `^\d+\.\d+\.\d+$`; reject anything else.
4. Edit `plugins/$plugin/.claude-plugin/plugin.json` with the Edit tool. Match the exact old `"version": "<old>"` line so the replacement is unambiguous.
5. Check whether `plugins/$plugin/.codex-plugin/plugin.json` exists.
   - If it does, read it and Edit its top-level `version` to the same new value. The Claude and Codex versions of a dual-runtime plugin must stay identical (see project `AGENTS.md`, "Version Management").
   - If it does not, skip silently — the plugin is Claude-only.
6. Report the result on a single line: `<plugin>: <old> → <new>`, followed by the manifest paths that were touched.

## Constraints

- Single plugin per invocation. If `$plugin` looks like a list, glob, or `--all`, refuse and ask the user to invoke the skill once per plugin.
- Do not edit `.claude-plugin/marketplace.json` or `.agents/plugins/marketplace.json`. Per project `AGENTS.md`, marketplace plugin entries must not carry a `version` field; `plugin.json` is the single source of truth.
- Do not run `git add`, `git commit`, `git tag`, `git push`, or any other state-mutating shell command. Version commits, tags, and release notes are handled separately by the user.
- Do not modify any field of `plugin.json` other than `version`. Leave `description`, `keywords`, `author`, and every other field untouched.
