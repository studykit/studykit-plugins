#!/usr/bin/env python3
# /// script
# dependencies = ["python-frontmatter", "PyYAML"]
# ///
"""Update an existing GitHub-backed issue body from an opaque caller-owned body file."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import TextIO

from workflow_command import CommandRunner
from workflow_config import WorkflowConfig, WorkflowConfigError, load_workflow_config
from workflow_env import workflow_project_dir_from_env
from workflow_github import GitHubRepositoryError, resolve_github_repository
from workflow_github_issue_provider import GitHubIssueNativeProvider
from workflow_github_issue_refs import issue_numbers_from_references
from workflow_providers import ProviderContext, ProviderRequest


class GitHubIssueWritebackError(RuntimeError):
    """Raised when GitHub issue body update cannot proceed."""


def update_issue(
    *,
    project: Path,
    artifact_type: str,
    issue: str,
    body_file: Path,
    title: str | None = None,
    labels: tuple[str, ...] = (),
    state: str | None = None,
    state_reason: str | None = None,
    relationship_intent: dict[str, object] | None = None,
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Update one GitHub issue body from an opaque caller-owned body file."""

    config = _load_github_issue_config(project)
    artifact_type = _required_text(artifact_type, "artifact type")
    try:
        repo = resolve_github_repository(config.root, runner=runner)
    except GitHubRepositoryError as exc:
        raise GitHubIssueWritebackError(str(exc)) from exc

    issue_numbers = issue_numbers_from_references([issue], repo=repo, allow_bare_numbers=True)
    if len(issue_numbers) != 1:
        raise GitHubIssueWritebackError(
            f"expected exactly one configured GitHub issue reference, got {len(issue_numbers)}"
        )
    issue_number = issue_numbers[0]

    body_path = body_file.expanduser()
    if not body_path.is_file():
        raise GitHubIssueWritebackError(f"body file does not exist: {body_path}")
    body = body_path.read_text(encoding="utf-8")
    _reject_body_with_frontmatter(body, body_path)

    normalized_labels = tuple(label.strip() for label in labels if label.strip())

    payload: dict[str, object] = {
        "issue": issue_number,
        "body": body,
        "freshness_check": True,
    }
    if title is not None:
        payload["title"] = title
    if normalized_labels:
        payload["labels"] = list(normalized_labels)
    if state:
        payload["state"] = state.strip().lower()
    if state_reason:
        payload["state_reason"] = state_reason.strip()

    provider = GitHubIssueNativeProvider(runner=runner)
    response = provider.call(
        ProviderRequest(
            role="issue",
            kind="github",
            operation="update",
            context=ProviderContext(project=config.root, artifact_type=artifact_type),
            payload=payload,
        )
    )

    provider_payload = dict(response.payload)
    if provider_payload.get("status") == "blocked":
        provider_payload["body_file"] = str(body_path)
        provider_payload["body_file_removed"] = False
        return provider_payload

    cache_payload = provider_payload.get("cache") if isinstance(provider_payload.get("cache"), dict) else {}
    issue_file = cache_payload.get("issue_file") if isinstance(cache_payload, dict) else None
    body_removed = False
    try:
        body_path.unlink()
    except OSError:
        body_removed = False
    else:
        body_removed = True

    result: dict[str, object] = {
        "operation": "update_issue",
        "kind": "github",
        "issue": provider_payload.get("issue"),
        "verified": bool(provider_payload.get("verified")),
        "state_changed": bool(provider_payload.get("state_changed")),
        "state": provider_payload.get("state"),
        "issue_file": issue_file,
        "body_file": str(body_path),
        "body_file_removed": body_removed,
        "cache_refreshed": bool(provider_payload.get("cache_refreshed")),
        "cache": cache_payload,
    }

    if relationship_intent:
        relationships_response = provider.call(
            ProviderRequest(
                role="issue",
                kind="github",
                operation="apply_relationships",
                context=ProviderContext(project=config.root, artifact_type=artifact_type),
                payload={
                    "issue": provider_payload.get("issue"),
                    "relationship_intent": relationship_intent,
                },
            )
        )
        result["relationships"] = dict(relationships_response.payload)

    return result


def _reject_body_with_frontmatter(body: str, path: Path) -> None:
    stripped = body.lstrip("﻿")
    if stripped.startswith("---\n") or stripped.startswith("---\r\n") or stripped.strip() == "---":
        raise GitHubIssueWritebackError(
            f"body file must not contain frontmatter; remove the YAML delimiter: {path}"
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--project",
        type=Path,
        default=workflow_project_dir_from_env(),
        help="project path",
    )
    parser.add_argument("--json", action="store_true", help="emit JSON")
    subparsers = parser.add_subparsers(dest="command", required=True)

    update = subparsers.add_parser(
        "update",
        help="update one GitHub issue body from a body file",
    )
    update.add_argument("--type", default="task", help="workflow artifact type")
    update.add_argument("--issue", required=True, help="GitHub issue id or configured reference")
    update.add_argument(
        "--body-file",
        type=Path,
        required=True,
        help="path to the opaque body content file (no frontmatter)",
    )
    update.add_argument("--title")
    update.add_argument("--label", action="append", default=[])
    update.add_argument("--state", choices=["open", "closed"])
    update.add_argument(
        "--state-reason",
        choices=["completed", "not_planned", "reopened"],
    )
    parent_group = update.add_mutually_exclusive_group()
    parent_group.add_argument("--parent", help="add parent (errors if a parent already exists)")
    parent_group.add_argument(
        "--replace-parent",
        dest="replace_parent",
        help="set parent, replacing any existing parent",
    )
    parent_group.add_argument(
        "--remove-parent",
        dest="remove_parent",
        action="store_true",
        help="remove the current parent (no-op when no parent exists)",
    )
    update.add_argument("--child", action="append", default=[], help="add a sub-issue (repeatable)")
    update.add_argument(
        "--remove-child",
        dest="remove_child",
        action="append",
        default=[],
        help="remove a sub-issue (repeatable)",
    )
    update.add_argument(
        "--blocked-by",
        action="append",
        default=[],
        help="add a blocked-by dependency (repeatable)",
    )
    update.add_argument(
        "--remove-blocked-by",
        dest="remove_blocked_by",
        action="append",
        default=[],
        help="remove a blocked-by dependency (repeatable)",
    )
    update.add_argument(
        "--blocking",
        action="append",
        default=[],
        help="add a blocking dependency (repeatable)",
    )
    update.add_argument(
        "--remove-blocking",
        dest="remove_blocking",
        action="append",
        default=[],
        help="remove a blocking dependency (repeatable)",
    )
    update.add_argument("--related", action="append", default=[], help="add a related ref (repeatable)")
    update.add_argument(
        "--remove-related",
        dest="remove_related",
        action="append",
        default=[],
        help="remove a related ref (repeatable)",
    )

    for child in subparsers.choices.values():
        child.add_argument("--json", action="store_true", help=argparse.SUPPRESS)
    return parser


def _update_relationship_intent(args: argparse.Namespace) -> dict[str, object]:
    intent: dict[str, object] = {}
    if getattr(args, "parent", None):
        intent["parent_add"] = args.parent
    if getattr(args, "replace_parent", None):
        intent["parent_replace"] = args.replace_parent
    if getattr(args, "remove_parent", False):
        intent["parent_remove"] = True
    if getattr(args, "blocked_by", None):
        intent["blocked_by_add"] = list(args.blocked_by)
    if getattr(args, "remove_blocked_by", None):
        intent["blocked_by_remove"] = list(args.remove_blocked_by)
    if getattr(args, "blocking", None):
        intent["blocking_add"] = list(args.blocking)
    if getattr(args, "remove_blocking", None):
        intent["blocking_remove"] = list(args.remove_blocking)
    if getattr(args, "child", None):
        intent["child_add"] = list(args.child)
    if getattr(args, "remove_child", None):
        intent["child_remove"] = list(args.remove_child)
    if getattr(args, "related", None):
        intent["related_add"] = list(args.related)
    if getattr(args, "remove_related", None):
        intent["related_remove"] = list(args.remove_related)
    return intent


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
        if args.command == "update":
            payload = update_issue(
                project=args.project,
                artifact_type=args.type,
                issue=args.issue,
                body_file=args.body_file,
                title=args.title,
                labels=tuple(args.label),
                state=args.state,
                state_reason=args.state_reason,
                relationship_intent=_update_relationship_intent(args),
                runner=runner,
            )
        else:
            raise GitHubIssueWritebackError(f"unsupported command: {args.command}")
    except Exception as exc:
        print(f"GitHub issue update error: {exc}", file=errors)
        return 2

    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=False), file=output)
    else:
        _print_plain(payload, output)
    if payload.get("status") == "blocked":
        return 3
    return 0


def _load_github_issue_config(project: Path) -> WorkflowConfig:
    try:
        config = load_workflow_config(project)
    except WorkflowConfigError as exc:
        raise GitHubIssueWritebackError(str(exc)) from exc
    if config is None:
        raise GitHubIssueWritebackError(".workflow/config.yml was not found")
    if config.issues.kind != "github":
        raise GitHubIssueWritebackError(
            f"GitHub issue update requires configured issue provider kind github, found {config.issues.kind}"
        )
    return config


def _required_text(value: str, name: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise GitHubIssueWritebackError(f"{name} is required")
    return text


def _print_plain(payload: dict[str, object], output: TextIO) -> None:
    if payload.get("status") == "blocked":
        print(
            f"#{payload.get('issue')} blocked: {payload.get('reason')} "
            f"reread_required={payload.get('reread_required')}",
            file=output,
        )
        return
    print(
        f"updated issue {payload.get('issue')} "
        f"state_changed={payload.get('state_changed')} "
        f"cache={payload.get('issue_file')}",
        file=output,
    )


if __name__ == "__main__":
    raise SystemExit(main())
