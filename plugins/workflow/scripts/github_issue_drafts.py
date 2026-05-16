#!/usr/bin/env python3
# /// script
# dependencies = ["python-frontmatter", "PyYAML"]
# ///
"""Prepare and create GitHub-backed pending issue drafts."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import TextIO

from workflow_cache import SCHEMA_VERSION, _atomic_write_text, _format_markdown, pending_relationship_operations_from_mapping
from workflow_command import CommandRunner
from workflow_config import WorkflowConfig, WorkflowConfigError, load_workflow_config
from workflow_env import workflow_project_dir_from_env
from workflow_github import GitHubRepositoryError, resolve_github_repository
from workflow_github_issue_cache import GitHubIssueCache
from workflow_github_issue_provider import GitHubIssueNativeProvider
from workflow_providers import ProviderContext, ProviderRequest


class GitHubIssueDraftError(RuntimeError):
    """Raised when GitHub pending issue draft operations cannot proceed."""


def prepare_pending_issue_draft(
    *,
    project: Path,
    local_id: str,
    artifact_type: str,
    title: str,
    labels: tuple[str, ...] = (),
    state: str = "open",
    state_reason: str | None = None,
    replace: bool = False,
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Create a GitHub-owned pending issue draft with an empty body."""

    config = _load_github_issue_config(project)
    local_id = _required_text(local_id, "local id")
    artifact_type = _required_text(artifact_type, "artifact type")
    title = _required_text(title, "title")
    normalized_state = (state or "open").strip().lower()
    normalized_labels = tuple(label.strip() for label in labels if label.strip())
    if artifact_type not in normalized_labels:
        normalized_labels = (artifact_type, *normalized_labels)

    try:
        repo = resolve_github_repository(config.root, runner=runner)
    except GitHubRepositoryError as exc:
        raise GitHubIssueDraftError(str(exc)) from exc
    cache = GitHubIssueCache.for_project(config.root, configured_repo=repo)
    issue_file = cache.pending_issue_file(repo, local_id)
    if issue_file.exists() and not replace:
        raise GitHubIssueDraftError(f"pending issue draft already exists: {issue_file}")

    frontmatter: dict[str, object] = {
        "schema_version": SCHEMA_VERSION,
        "type": artifact_type,
        "role": "issue",
        "provider": "github",
        "title": title,
        "labels": list(normalized_labels),
        "state": normalized_state,
    }
    if state_reason:
        frontmatter["state_reason"] = state_reason.strip()

    issue_file.parent.mkdir(parents=True, exist_ok=True)
    _atomic_write_text(issue_file, _format_markdown(frontmatter, ""))

    return {
        "operation": "prepare_pending_issue",
        "role": "issue",
        "kind": "github",
        "local_id": local_id,
        "issue_file": str(issue_file),
        "artifact_type": artifact_type,
        "title": title,
        "labels": list(normalized_labels),
        "state": normalized_state,
        "body_empty": True,
        "repository": repo.to_json(),
    }


def create_pending_issue(
    *,
    project: Path,
    local_id: str,
    artifact_type: str,
    confirm_provider_create: bool = False,
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Create a GitHub issue from an existing pending issue draft."""

    if not confirm_provider_create:
        raise GitHubIssueDraftError(
            "provider issue creation requires --confirm-provider-create after explicit user approval"
        )

    config = _load_github_issue_config(project)
    provider = GitHubIssueNativeProvider(runner=runner)
    response = provider.call(
        ProviderRequest(
            role="issue",
            kind="github",
            operation="create",
            context=ProviderContext(project=config.root, artifact_type=artifact_type),
            payload={"pending_local_id": _required_text(local_id, "local id")},
        )
    )
    return dict(response.payload)


def stage_pending_issue_relationships(
    *,
    project: Path,
    local_id: str,
    parent: str | None = None,
    children: tuple[str, ...] = (),
    blocked_by: tuple[str, ...] = (),
    blocking: tuple[str, ...] = (),
    related: tuple[str, ...] = (),
    replace: bool = False,
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Stage provider-native relationships for a pending GitHub issue draft."""

    if related:
        raise GitHubIssueDraftError("related relationship staging is not supported for GitHub issue providers")

    config = _load_github_issue_config(project)
    local_id = _required_text(local_id, "local id")
    try:
        repo = resolve_github_repository(config.root, runner=runner)
    except GitHubRepositoryError as exc:
        raise GitHubIssueDraftError(str(exc)) from exc
    cache = GitHubIssueCache.for_project(config.root, configured_repo=repo)
    issue_file = cache.pending_issue_file(repo, local_id)
    if not issue_file.is_file():
        raise GitHubIssueDraftError(f"pending issue draft does not exist: {issue_file}")
    if not replace and cache.read_pending_draft_relationships(repo, local_id):
        raise GitHubIssueDraftError(f"pending relationship operations already exist for GitHub pending issue {local_id}")

    payload = _relationship_payload(
        parent=parent,
        children=children,
        blocked_by=blocked_by,
        blocking=blocking,
        related=(),
    )
    pending_location = cache.write_pending_draft_relationships(
        repo,
        local_id,
        pending_relationship_operations_from_mapping(
            payload,
            path=issue_file,
            target_kind="pending_issue",
            target_id=local_id,
        ),
        replace_existing=replace,
    )
    operations = cache.read_pending_draft_relationships(repo, local_id)
    return {
        "operation": "stage_pending_issue_relationships",
        "role": "issue",
        "kind": "github",
        "repository": repo.to_json(),
        "local_id": local_id,
        "issue_file": str(issue_file),
        "pending_location": str(pending_location),
        "operations": [operation.to_json() for operation in operations],
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=workflow_project_dir_from_env(), help="project path")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    subparsers = parser.add_subparsers(dest="command", required=True)

    prepare = subparsers.add_parser("prepare", help="prepare a bodyless pending issue draft")
    prepare.add_argument("--local-id", required=True)
    prepare.add_argument("--type", required=True, help="workflow artifact type for the draft")
    prepare.add_argument("--title", required=True)
    prepare.add_argument("--label", action="append", default=[])
    prepare.add_argument("--state", default="open")
    prepare.add_argument("--state-reason")
    prepare.add_argument("--replace", action="store_true")

    create = subparsers.add_parser("create", help="create a provider issue from a pending draft")
    create.add_argument("--type", default="task", help="workflow artifact type")
    create.add_argument(
        "--confirm-provider-create",
        action="store_true",
        help="confirm that the user explicitly approved creating a provider issue from this pending draft",
    )
    create.add_argument("local_id")

    relationships = subparsers.add_parser("stage-relationships", help="stage provider-native relationships")
    relationships.add_argument("--local-id", required=True)
    relationships.add_argument("--parent")
    relationships.add_argument("--child", action="append", default=[])
    relationships.add_argument("--blocked-by", action="append", default=[])
    relationships.add_argument("--blocking", action="append", default=[])
    relationships.add_argument("--related", action="append", default=[])
    relationships.add_argument("--replace", action="store_true")

    for child in subparsers.choices.values():
        child.add_argument("--json", action="store_true", help=argparse.SUPPRESS)

    return parser


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
        if args.command == "prepare":
            payload = prepare_pending_issue_draft(
                project=args.project,
                local_id=args.local_id,
                artifact_type=args.type,
                title=args.title,
                labels=tuple(args.label),
                state=args.state,
                state_reason=args.state_reason,
                replace=args.replace,
                runner=runner,
            )
        elif args.command == "create":
            payload = create_pending_issue(
                project=args.project,
                local_id=args.local_id,
                artifact_type=args.type,
                confirm_provider_create=args.confirm_provider_create,
                runner=runner,
            )
        elif args.command == "stage-relationships":
            payload = stage_pending_issue_relationships(
                project=args.project,
                local_id=args.local_id,
                parent=args.parent,
                children=tuple(args.child),
                blocked_by=tuple(args.blocked_by),
                blocking=tuple(args.blocking),
                related=tuple(args.related),
                replace=args.replace,
                runner=runner,
            )
        else:
            raise GitHubIssueDraftError(f"unsupported command: {args.command}")
    except Exception as exc:
        print(f"GitHub issue draft error: {exc}", file=errors)
        return 2

    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=False), file=output)
    else:
        _print_plain(payload, output)
    return 0


def _load_github_issue_config(project: Path) -> WorkflowConfig:
    try:
        config = load_workflow_config(project)
    except WorkflowConfigError as exc:
        raise GitHubIssueDraftError(str(exc)) from exc
    if config is None:
        raise GitHubIssueDraftError(".workflow/config.yml was not found")
    if config.issues.kind != "github":
        raise GitHubIssueDraftError(
            f"GitHub issue draft commands require configured issue provider kind github, found {config.issues.kind}"
        )
    return config


def _relationship_payload(
    *,
    parent: str | None,
    children: tuple[str, ...],
    blocked_by: tuple[str, ...],
    blocking: tuple[str, ...],
    related: tuple[str, ...],
) -> dict[str, object]:
    payload: dict[str, object] = {"schema_version": SCHEMA_VERSION}
    if parent:
        payload["parent"] = _required_text(parent, "parent")
    normalized_children = _normalized_refs(children)
    normalized_blocked_by = _normalized_refs(blocked_by)
    normalized_blocking = _normalized_refs(blocking)
    normalized_related = _normalized_refs(related)
    if normalized_children:
        payload["children"] = normalized_children
    dependencies: dict[str, object] = {}
    if normalized_blocked_by:
        dependencies["blocked_by"] = normalized_blocked_by
    if normalized_blocking:
        dependencies["blocking"] = normalized_blocking
    if dependencies:
        payload["dependencies"] = dependencies
    if normalized_related:
        payload["related"] = normalized_related
    if len(payload) == 1:
        raise GitHubIssueDraftError("at least one relationship value is required")
    return payload


def _required_text(value: str, name: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise GitHubIssueDraftError(f"{name} is required")
    return text


def _normalized_refs(values: tuple[str, ...]) -> list[str]:
    return [value.strip() for value in values if value.strip()]


def _print_plain(payload: dict[str, object], output: TextIO) -> None:
    operation = payload.get("operation")
    if operation == "prepare_pending_issue":
        print(f"prepared pending issue {payload.get('local_id')}: {payload.get('issue_file')}", file=output)
        return
    if operation == "stage_pending_issue_relationships":
        print(
            f"staged relationships for pending issue {payload.get('local_id')}: {payload.get('pending_location')}",
            file=output,
        )
        return
    issue = payload.get("issue")
    print(f"created issue {issue} verified={payload.get('verified')}", file=output)


if __name__ == "__main__":
    raise SystemExit(main())
