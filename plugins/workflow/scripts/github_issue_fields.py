#!/usr/bin/env python3
# /// script
# dependencies = ["python-frontmatter", "PyYAML"]
# ///
"""GitHub Issues body-less field mutation entrypoint."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, TextIO

from workflow_cache import WorkflowCacheError
from workflow_command import CommandRunner
from workflow_config import WorkflowConfig, WorkflowConfigError, load_workflow_config
from workflow_env import workflow_project_dir_from_env
from workflow_github import (
    GitHubRepositoryError,
    get_github_login,
    resolve_github_repository,
)
from workflow_github_issue_cache import GitHubIssueCache
from workflow_github_issue_provider import GitHubIssueNativeProvider
from workflow_github_issue_refs import issue_numbers_from_references
from workflow_providers import ProviderContext, ProviderRequest


class GitHubIssueFieldsError(RuntimeError):
    """Raised when a GitHub issue field mutation cannot proceed."""


_GITHUB_TYPE_LABELS = {"task", "bug", "spike", "epic", "review", "usecase", "research"}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=workflow_project_dir_from_env(), help="project path")
    parser.add_argument("--type", default="task", help="workflow artifact type")
    subparsers = parser.add_subparsers(dest="verb", required=True)

    p_close = subparsers.add_parser("close", help="close an issue")
    p_close.add_argument("issue", help="GitHub issue reference")
    p_close.add_argument("--reason", choices=("completed", "not_planned"), default="completed")
    p_close.add_argument("--comment", help="optional comment posted alongside the close")

    p_reopen = subparsers.add_parser("reopen", help="reopen an issue")
    p_reopen.add_argument("issue", help="GitHub issue reference")
    p_reopen.add_argument("--comment", help="optional comment posted alongside the reopen")

    p_assign = subparsers.add_parser("assign", help="assign an issue to a user")
    p_assign.add_argument("issue", help="GitHub issue reference")
    p_assign.add_argument("user", help='GitHub login or the literal "me"')

    p_unassign = subparsers.add_parser("unassign", help="clear all assignees")
    p_unassign.add_argument("issue", help="GitHub issue reference")

    p_set_type = subparsers.add_parser("set-type", help="swap the workflow type label")
    p_set_type.add_argument("issue", help="GitHub issue reference")
    p_set_type.add_argument("new_type", metavar="type", help="new workflow type label")

    return parser


def fields_payload(
    *,
    project: Path,
    artifact_type: str,
    verb: str,
    issue: str,
    reason: str | None = None,
    comment: str | None = None,
    user: str | None = None,
    new_type: str | None = None,
    runner: CommandRunner | None = None,
) -> dict[str, Any]:
    config = _load_github_issue_config(project)
    try:
        repo = resolve_github_repository(config.root, runner=runner)
    except GitHubRepositoryError as exc:
        raise GitHubIssueFieldsError(str(exc)) from exc

    issue_numbers = issue_numbers_from_references([issue], repo=repo, allow_bare_numbers=True)
    if len(issue_numbers) != 1:
        raise GitHubIssueFieldsError("fields update requires exactly one GitHub issue ref")
    issue_number = issue_numbers[0]

    provider = GitHubIssueNativeProvider(runner=runner)

    if verb in {"close", "reopen"}:
        payload: dict[str, Any] = {
            "issue": issue_number,
            "freshness_check": True,
            "freshness_target": "issue",
        }
        if verb == "close" and reason is not None:
            payload["reason"] = reason
        if comment is not None:
            payload["comment"] = comment
        response = provider.call(
            ProviderRequest(
                role="issue",
                kind="github",
                operation=verb,
                context=ProviderContext(project=config.root, artifact_type=artifact_type),
                payload=payload,
            )
        )
        return {
            "operation": f"lifecycle_{verb}",
            "role": "issue",
            "kind": "github",
            "repository": repo.to_json(),
            "issue": issue_number,
            "provider": dict(response.payload),
        }

    if verb == "assign":
        if not user:
            raise GitHubIssueFieldsError("assign requires a user")
        resolved = user
        if resolved.strip().lower() == "me":
            resolved = get_github_login(project=config.root, runner=runner)
        payload = {"issue": issue_number, "freshness_check": True, "assignee": resolved}
    elif verb == "unassign":
        payload = {"issue": issue_number, "freshness_check": True, "unassign": True}
    elif verb == "set-type":
        if not new_type or not new_type.strip():
            raise GitHubIssueFieldsError("set-type requires a non-empty type")
        cache = GitHubIssueCache.for_project(config.root, configured_repo=repo)
        try:
            cached = cache.read_issue(
                repo,
                issue_number,
                include_body=False,
                include_comments=False,
                include_relationships=False,
            )
        except WorkflowCacheError as exc:
            raise GitHubIssueFieldsError(
                f"refresh the GitHub issue cache before set-type: {exc}"
            ) from exc
        current_labels = set(_string_list(cached.get("labels")))
        new_labels = _replace_github_type_label(current_labels, new_type)
        payload = {
            "issue": issue_number,
            "freshness_check": True,
            "label_set": sorted(new_labels),
        }
    else:
        raise GitHubIssueFieldsError(f"unsupported verb: {verb}")

    response = provider.call(
        ProviderRequest(
            role="issue",
            kind="github",
            operation="update",
            context=ProviderContext(project=config.root, artifact_type=artifact_type),
            payload=payload,
        )
    )
    return {
        "operation": f"fields_{verb.replace('-', '_')}",
        "role": "issue",
        "kind": "github",
        "repository": repo.to_json(),
        "issue": issue_number,
        "provider": dict(response.payload),
    }


def _replace_github_type_label(labels: set[str], workflow_type: str) -> set[str]:
    desired = workflow_type.strip()
    if not desired:
        raise GitHubIssueFieldsError("workflow type is empty")
    labels = {label for label in labels if label not in _GITHUB_TYPE_LABELS}
    labels.add(desired)
    return labels


def _string_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        nodes = value.get("nodes")
        if isinstance(nodes, list):
            return _string_list(nodes)
        name = value.get("name")
        return [str(name)] if name else []
    if isinstance(value, list | tuple | set):
        result: list[str] = []
        for item in value:
            if isinstance(item, dict):
                name = item.get("name")
                if name:
                    result.append(str(name))
            elif item is not None:
                result.append(str(item))
        return result
    return [str(value)]


def _load_github_issue_config(project: Path) -> WorkflowConfig:
    try:
        config = load_workflow_config(project)
    except WorkflowConfigError as exc:
        raise GitHubIssueFieldsError(str(exc)) from exc
    if config is None:
        raise GitHubIssueFieldsError(".workflow/config.yml was not found")
    if config.issues.kind != "github":
        raise GitHubIssueFieldsError(
            f"GitHub issue field updates require configured issue provider kind github, found {config.issues.kind}"
        )
    return config


def main(
    argv: list[str] | None = None,
    *,
    stdout: TextIO | None = None,
    stderr: TextIO | None = None,
    runner: CommandRunner | None = None,
) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    output = stdout or sys.stdout
    errors = stderr or sys.stderr

    try:
        payload = fields_payload(
            project=args.project,
            artifact_type=args.type,
            verb=args.verb,
            issue=args.issue,
            reason=getattr(args, "reason", None),
            comment=getattr(args, "comment", None),
            user=getattr(args, "user", None),
            new_type=getattr(args, "new_type", None),
            runner=runner,
        )
    except Exception as exc:
        print(f"GitHub issue fields error: {exc}", file=errors)
        return 2

    print(json.dumps(payload, indent=2, sort_keys=False), file=output)
    if (payload.get("provider") or {}).get("status") == "blocked":
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
