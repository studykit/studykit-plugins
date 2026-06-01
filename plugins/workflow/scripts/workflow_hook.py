#!/usr/bin/env python3
"""Shared workflow hook logic.

The executable entry points are runtime-specific:

- ``hook_claude.py`` adapts Claude Code hook payloads and environment values.
- ``hook_codex.py`` adapts Codex hook payloads and environment values.

This module contains only host-neutral workflow behavior such as workflow
policy text, issue-cache injection, provider cache projection checks, and
session-state coordination. Runtime-specific entry scripts parse their payloads, resolve
runtime values, and call the plain functions here with concrete arguments.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from typing import TextIO

_SCRIPTS_DIR = str(Path(__file__).resolve().parent)
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

from workflow_command import CommandRunner  # noqa: E402
from workflow_edit_target import EditTarget  # noqa: E402
from workflow_config import WorkflowConfig, WorkflowConfigError, load_workflow_config  # noqa: E402
from workflow_github import GitHubRepository, GitHubRepositoryError, normalize_issue_number  # noqa: E402
from workflow_github import resolve_github_repository  # noqa: E402
from issue.github.cache import (  # noqa: E402
    is_github_issue_cache_body_path,
    is_github_issue_cache_meta_path,
)
from issue.github.context import cache_github_issue_references  # noqa: E402
from issue.github.refs import extract_issue_numbers as extract_github_issue_numbers  # noqa: E402
from issue.cli_output import format_issue_cache_context  # noqa: E402
from issue.jira.cache import (  # noqa: E402
    is_jira_issue_cache_body_path,
    is_jira_issue_cache_meta_path,
)
from issue.jira.context import cache_jira_issue_references  # noqa: E402
from issue.jira.refs import jira_issue_keys_from_references  # noqa: E402
from issue.jira.refs import normalize_jira_issue_key  # noqa: E402
from workflow_main_context import build_commit_prefix_context  # noqa: E402
from workflow_main_context import build_session_policy_context, build_subagent_policy_context  # noqa: E402
from workflow_session_state import (  # noqa: E402
    commit_prefix_was_announced,
    read_session_issues,
    record_commit_prefix_announced,
    record_session_issues,
)
from util import emit_json  # noqa: E402

COMMIT_PROMPT_PATTERN = re.compile(
    r"(?i)(?<![A-Za-z])(?:commit|commits|committed|committing)(?![A-Za-z])|커밋"
)

# =============================================================================
# Common hook operations
# =============================================================================


def workflow_config_for_project(project_dir: Path | None) -> WorkflowConfig | None:
    """Resolve the active workflow config, silent on missing project or load errors."""

    if project_dir is None:
        return None
    try:
        return load_workflow_config(project_dir)
    except WorkflowConfigError:
        return None


def block_provider_cache_body_write(
    *,
    project_dir: Path | None,
    edit_targets: tuple[EditTarget, ...],
    stdout: TextIO | None = None,
) -> int:
    """Block unsafe provider cache issue body projection writes."""

    config = workflow_config_for_project(project_dir)
    if config is None:
        return 0

    for target in edit_targets:
        block_reason = provider_cache_body_write_reason(target, config)
        if block_reason:
            emit_json({"decision": "block", "reason": block_reason}, stdout=stdout)
            return 0
    return 0


def inject_prompt_issue_context(
    *,
    project_dir: Path | None,
    session_id: str,
    runtime: str,
    prompt_text: str,
    stdout: TextIO | None = None,
    runner: CommandRunner | None = None,
) -> int:
    """Cache issue refs from a prompt and inject concise context."""

    config = workflow_config_for_project(project_dir)
    if config is None or config.issues.kind not in {"github", "jira"}:
        return 0

    context_parts: list[str] = []
    commit_context = build_prompt_commit_context(config, prompt_text)
    if commit_context and commit_prefix_was_announced(config.root, session_id, runtime=runtime):
        commit_context = ""

    repo = None
    if config.issues.kind == "github":
        repo = github_repo_for_config(config, runner=runner)
        if repo is None:
            if commit_context:
                record_commit_prefix_announced(config.root, session_id, runtime=runtime)
                emit_user_prompt_context([commit_context], stdout=stdout)
            return 0

    if config.issues.kind == "github":
        prompt_numbers = extract_github_issue_numbers(prompt_text, repo=repo)
        issue_numbers = _ordered_issue_union(prompt_numbers, issue_id_format="github")
    else:
        prompt_numbers = jira_issue_keys_from_references([prompt_text])
        issue_numbers = _ordered_issue_union(prompt_numbers, issue_id_format="jira")
    if not issue_numbers:
        if commit_context:
            record_commit_prefix_announced(config.root, session_id, runtime=runtime)
            emit_user_prompt_context([commit_context], stdout=stdout)
        return 0

    already_announced = read_session_issues(config.root, session_id, "announced", runtime=runtime)
    if config.issues.kind == "github":
        assert repo is not None
        contexts = cache_github_issue_references(config, issue_numbers, repo=repo, runner=runner)
    else:
        contexts = cache_jira_issue_references(config, issue_numbers, runner=runner)
    fresh_contexts = [context for context in contexts if context.number not in already_announced]
    if fresh_contexts:
        record_session_issues(
            config.root,
            session_id,
            [context.number for context in fresh_contexts],
            "announced",
            runtime=runtime,
        )
        context_parts.append(format_issue_cache_context(fresh_contexts, include_details=False))
    if commit_context:
        context_parts.append(commit_context)
    if context_parts:
        if commit_context:
            record_commit_prefix_announced(config.root, session_id, runtime=runtime)
        emit_user_prompt_context(context_parts, stdout=stdout)
    return 0


def record_stop_issue_references(
    *,
    project_dir: Path | None,
    session_id: str,
    scan_text: str,
    stop_hook_active: bool = False,
    stdout: TextIO | None = None,
    runner: CommandRunner | None = None,
) -> int:
    """Keep Stop silent and avoid carrying issue refs into the next prompt."""

    # Stop hook JSON output is reserved for block decisions. Provider/cache
    # context injection is prompt-local only.
    _ = project_dir, session_id, scan_text, stop_hook_active, stdout, runner
    return 0


# =============================================================================
# Module-level helpers used by the handlers
# =============================================================================


def build_session_start_context(
    config: WorkflowConfig,
    plugin_root: Path,
    *,
    runtime: str,
) -> str:
    """Build the context block injected for configured workflow projects."""

    return build_session_policy_context(config, plugin_root=plugin_root, runtime=runtime)


def build_subagent_start_context(
    config: WorkflowConfig,
    plugin_root: Path,
    *,
    runtime: str,
    agent_type: str | None = None,
) -> str:
    """Build the SubagentStart context block for configured workflow projects."""

    return build_subagent_policy_context(
        config,
        plugin_root=plugin_root,
        runtime=runtime,
        agent_type=agent_type,
    )


def build_prompt_commit_context(config: WorkflowConfig, prompt_text: str) -> str:
    """Build terse commit guidance when a user prompt asks about commits."""

    if not config.commit_refs.enabled:
        return ""
    if not COMMIT_PROMPT_PATTERN.search(prompt_text):
        return ""
    if config.issues.kind not in {"github", "jira"}:
        return ""
    return build_commit_prefix_context()


def emit_user_prompt_context(context_parts: list[str], *, stdout: TextIO | None = None) -> None:
    """Emit a single UserPromptSubmit additionalContext payload."""

    emit_json(
        {
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": "\n\n".join(part for part in context_parts if part),
            }
        },
        stdout=stdout,
    )


def github_repo_for_config(
    config: WorkflowConfig,
    *,
    runner: CommandRunner | None = None,
) -> GitHubRepository | None:
    """Resolve the configured GitHub issue repository without failing hooks."""

    if config.issues.kind != "github":
        return None
    try:
        return resolve_github_repository(config.root, runner=runner)
    except (GitHubRepositoryError, OSError, subprocess.SubprocessError):
        return None


def is_provider_issue_cache_body(path: Path, config: WorkflowConfig) -> bool:
    """Return whether ``path`` is a read-only provider issue content projection."""

    if config.issues.kind == "github":
        return is_github_issue_cache_body_path(path, config.root)
    if config.issues.kind == "jira":
        return is_jira_issue_cache_body_path(path, config.root)
    return False


def is_provider_issue_cache_meta(path: Path, config: WorkflowConfig) -> bool:
    """Return whether ``path`` is an internal cache projection.

    Internal projections are the dotfiles the dispatchers own (``.meta.json``
    and, for GitHub, the ``.relationships.json`` machine source); both are
    blocked for read and write.
    """

    if config.issues.kind == "github":
        return is_github_issue_cache_meta_path(path, config.root)
    if config.issues.kind == "jira":
        return is_jira_issue_cache_meta_path(path, config.root)
    return False


def provider_cache_body_write_reason(target: EditTarget, config: WorkflowConfig) -> str | None:
    """Block writes to read-only provider cache projections (content or meta)."""

    is_body = is_provider_issue_cache_body(target.path, config)
    is_meta = is_provider_issue_cache_meta(target.path, config)
    if not (is_body or is_meta):
        return None

    if is_meta:
        return (
            "workflow cache protection blocked a write to an internal cache file "
            "(.meta.json / .relationships.json).\n\n"
            f"Target: {target.path}\n\n"
            "These files hold projection bookkeeping (freshness fingerprints, the "
            "machine relationship source) only. Never edit them; the workflow "
            "dispatchers maintain them. Use the body-file flow "
            "(`workflow issue update` / `workflow issue comment --body-file <path>`)."
        )

    if not target.path.is_file():
        return (
            "workflow cache protection blocked a write to a provider cache projection that "
            "has not been prepared yet.\n\n"
            f"Target: {target.path}\n\n"
            "Refresh the projection with the workflow fetch dispatcher "
            "(`workflow issue fetch`), then use the body-file flow — never edit cache files "
            "directly."
        )

    if target.content is None:
        return None

    return (
        "workflow cache protection blocked a write because provider cache projections are "
        "read-only.\n\n"
        f"Target: {target.path}\n\n"
        "Write the new body or comment to a caller-chosen temp file and run the matching "
        "workflow dispatcher with `--body-file <path>` (`workflow issue update` or "
        "`workflow issue comment`) instead of editing the cached file in place."
    )


def provider_cache_meta_read_reason(path: Path, config: WorkflowConfig) -> str | None:
    """Block reads of the internal ``.meta.json`` projection."""

    if not is_provider_issue_cache_meta(path, config):
        return None
    return (
        "workflow cache protection blocked reading an internal cache file "
        "(.meta.json / .relationships.json).\n\n"
        f"Target: {path}\n\n"
        "These files hold projection bookkeeping (freshness fingerprints, the machine "
        "relationship source) only — they are not issue content. Read issue.md / "
        "relationships.md / comment-*.md for the issue, or refresh with "
        "`workflow issue fetch`."
    )


def block_provider_cache_meta_read(
    *,
    project_dir: Path | None,
    path: Path | None,
    stdout: TextIO | None = None,
) -> int:
    """Block a read of the internal ``.meta.json`` cache projection."""

    if path is None:
        return 0
    config = workflow_config_for_project(project_dir)
    if config is None:
        return 0
    reason = provider_cache_meta_read_reason(path, config)
    if reason:
        emit_json({"decision": "block", "reason": reason}, stdout=stdout)
    return 0


def _ordered_issue_union(*groups: list[str], issue_id_format: str = "github") -> list[str]:
    ordered: list[str] = []
    seen: set[str] = set()
    for group in groups:
        for issue in group:
            normalized = _normalize_issue_token(issue, issue_id_format=issue_id_format)
            if normalized is None:
                continue
            if normalized in seen:
                continue
            seen.add(normalized)
            ordered.append(normalized)
    return ordered


def _normalize_issue_token(issue: str, *, issue_id_format: str) -> str | None:
    try:
        if issue_id_format == "jira":
            return normalize_jira_issue_key(issue)
        return normalize_issue_number(issue)
    except Exception:
        return None
