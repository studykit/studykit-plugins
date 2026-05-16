#!/usr/bin/env python3
# /// script
# dependencies = ["python-frontmatter", "PyYAML"]
# ///
"""GitHub Issues pending relationship stage/apply entrypoint."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import TextIO

from workflow_cache import SCHEMA_VERSION, pending_relationship_operations_from_mapping
from workflow_command import CommandRunner
from workflow_config import WorkflowConfig, WorkflowConfigError, load_workflow_config
from workflow_env import workflow_project_dir_from_env
from workflow_github import GitHubRepositoryError, resolve_github_repository
from workflow_github_issue_cache import GitHubIssueCache
from workflow_github_issue_provider import GitHubIssueNativeProvider
from workflow_github_issue_refs import issue_numbers_from_references
from workflow_providers import CACHE_POLICY_REFRESH, ProviderContext, ProviderRequest


class GitHubIssueRelationshipsError(RuntimeError):
    """Raised when pending GitHub issue relationships cannot be applied."""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=workflow_project_dir_from_env(), help="project path")
    parser.add_argument("--type", default="task", help="workflow artifact type")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    parser.add_argument("--stage", action="store_true", help="stage relationship intent instead of applying pending files")
    parser.add_argument("--parent")
    parser.add_argument("--child", action="append", default=[])
    parser.add_argument("--blocked-by", action="append", default=[])
    parser.add_argument("--blocking", action="append", default=[])
    parser.add_argument("--related", action="append", default=[])
    parser.add_argument("--replace", action="store_true", help="replace existing pending relationships when staging")
    parser.add_argument("issues", nargs="+", help="GitHub issue IDs or configured repository issue references")
    return parser


def stage_relationships_payload(
    *,
    project: Path,
    issues: list[str],
    parent: str | None = None,
    children: tuple[str, ...] = (),
    blocked_by: tuple[str, ...] = (),
    blocking: tuple[str, ...] = (),
    related: tuple[str, ...] = (),
    replace: bool = False,
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Stage relationship intent for an existing GitHub issue."""

    if related:
        raise GitHubIssueRelationshipsError("related relationship staging is not supported for GitHub issue providers")
    config = _load_github_issue_config(project)
    repo, issue_numbers = _github_relationship_context(config, issues, runner=runner)
    if len(issue_numbers) != 1:
        raise GitHubIssueRelationshipsError("relationship staging requires exactly one issue ref")

    issue = issue_numbers[0]
    cache = GitHubIssueCache.for_project(config.root, configured_repo=repo)
    provider = GitHubIssueNativeProvider(runner=runner)
    if not cache.has_issue_projection(repo, issue):
        provider.call(
            ProviderRequest(
                role="issue",
                kind="github",
                operation="get",
                context=ProviderContext(project=config.root, artifact_type="task", cache_policy=CACHE_POLICY_REFRESH),
                payload={"issue": issue},
            )
        )
    if not replace and cache.read_pending_issue_relationships(repo, issue):
        raise GitHubIssueRelationshipsError(f"pending relationship operations already exist for GitHub issue #{issue}")

    payload = _relationship_payload(
        parent=parent,
        children=children,
        blocked_by=blocked_by,
        blocking=blocking,
        related=(),
    )
    issue_file = cache.issue_file(repo, issue)
    pending_location = cache.write_pending_issue_relationships(
        repo,
        issue,
        pending_relationship_operations_from_mapping(payload, path=issue_file, target_kind="issue", target_id=issue),
        replace_existing=replace,
    )
    operations = cache.read_pending_issue_relationships(repo, issue)
    return {
        "operation": "cache_stage_pending_relationships",
        "role": "issue",
        "kind": "github",
        "repository": repo.to_json(),
        "issue": issue,
        "issue_file": str(issue_file),
        "pending_location": str(pending_location),
        "operations": [operation.to_json() for operation in operations],
    }


def apply_pending_relationships_payload(
    *,
    project: Path,
    issues: list[str],
    artifact_type: str,
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Apply pending local relationship files to GitHub issues."""

    config = _load_github_issue_config(project)
    repo, issue_numbers = _github_relationship_context(config, issues, runner=runner)
    provider = GitHubIssueNativeProvider(runner=runner)
    results = []
    for issue in issue_numbers:
        response = provider.call(
            ProviderRequest(
                role="issue",
                kind="github",
                operation="apply_relationships",
                context=ProviderContext(project=config.root, artifact_type=artifact_type),
                payload={"issue": issue, "from_pending": True},
            )
        )
        results.append(dict(response.payload))

    return {
        "operation": "cache_apply_pending_relationships",
        "role": "issue",
        "kind": "github",
        "repository": repo.to_json(),
        "issues": results,
    }


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
        if args.stage:
            payload = stage_relationships_payload(
                project=args.project,
                issues=list(args.issues),
                parent=args.parent,
                children=tuple(args.child),
                blocked_by=tuple(args.blocked_by),
                blocking=tuple(args.blocking),
                related=tuple(args.related),
                replace=args.replace,
                runner=runner,
            )
        else:
            payload = apply_pending_relationships_payload(
                project=args.project,
                issues=list(args.issues),
                artifact_type=args.type,
                runner=runner,
            )
    except Exception as exc:
        print(f"GitHub issue relationship error: {exc}", file=errors)
        return 2

    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=False), file=output)
        return 0

    if payload.get("operation") == "cache_stage_pending_relationships":
        print(f"#{payload.get('issue')} staged: {payload.get('pending_location')}", file=output)
        return 0

    for item in payload.get("issues", []):
        if isinstance(item, dict):
            print(f"#{item.get('issue')} applied={item.get('applied')}", file=output)
    return 0


def _github_relationship_context(config: WorkflowConfig, issues: list[str], *, runner: CommandRunner | None = None):
    try:
        repo = resolve_github_repository(config.root, runner=runner)
    except GitHubRepositoryError as exc:
        raise GitHubIssueRelationshipsError(str(exc)) from exc

    issue_numbers = issue_numbers_from_references(issues, repo=repo, allow_bare_numbers=True)
    if not issue_numbers:
        raise GitHubIssueRelationshipsError("no configured-repository GitHub issue references were found")
    return repo, issue_numbers


def _load_github_issue_config(project: Path) -> WorkflowConfig:
    try:
        config = load_workflow_config(project)
    except WorkflowConfigError as exc:
        raise GitHubIssueRelationshipsError(str(exc)) from exc
    if config is None:
        raise GitHubIssueRelationshipsError(".workflow/config.yml was not found")
    if config.issues.kind != "github":
        raise GitHubIssueRelationshipsError(
            f"GitHub issue relationship commands require configured issue provider kind github, found {config.issues.kind}"
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
        payload["parent"] = _required_ref(parent, "parent")
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
        raise GitHubIssueRelationshipsError("at least one relationship value is required")
    return payload


def _required_ref(value: str, name: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise GitHubIssueRelationshipsError(f"{name} relationship ref is required")
    return text


def _normalized_refs(values: tuple[str, ...]) -> list[str]:
    return [value.strip() for value in values if value.strip()]


if __name__ == "__main__":
    raise SystemExit(main())
