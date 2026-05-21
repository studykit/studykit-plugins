#!/usr/bin/env python3
# /// script
# dependencies = ["python-frontmatter", "PyYAML"]
# ///
"""GitHub Issues relationship apply entrypoint.

Builds add/remove/replace relationship intent from CLI flags and asks the
provider to apply it directly. No flag means no provider call (no-op).
"""

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
from issue.github.cache import GitHubIssueCache
from issue.github.provider import GitHubIssueNativeProvider
from issue.github.refs import issue_numbers_from_references
from issue.cli_output import flatten_provider_envelope
from workflow_providers import ProviderContext, ProviderRequest


class GitHubIssueRelationshipsError(RuntimeError):
    """Raised when GitHub issue relationships cannot be applied."""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=workflow_project_dir_from_env(), help="project path")
    parser.add_argument("--type", default="task", help="workflow artifact type")
    parent_group = parser.add_mutually_exclusive_group()
    parent_group.add_argument("--parent", help="add parent (errors if a parent already exists)")
    parent_group.add_argument("--replace-parent", dest="replace_parent", help="set parent, replacing any existing parent")
    parent_group.add_argument(
        "--remove-parent",
        dest="remove_parent",
        action="store_true",
        help="remove the current parent (no-op when no parent exists)",
    )
    parser.add_argument("--child", action="append", default=[], help="add a sub-issue (repeatable)")
    parser.add_argument("--remove-child", dest="remove_child", action="append", default=[], help="remove a sub-issue (repeatable)")
    parser.add_argument("--blocked-by", action="append", default=[], help="add a blocked-by dependency (repeatable)")
    parser.add_argument(
        "--remove-blocked-by",
        dest="remove_blocked_by",
        action="append",
        default=[],
        help="remove a blocked-by dependency (repeatable)",
    )
    parser.add_argument("--blocking", action="append", default=[], help="add a blocking dependency (repeatable)")
    parser.add_argument(
        "--remove-blocking",
        dest="remove_blocking",
        action="append",
        default=[],
        help="remove a blocking dependency (repeatable)",
    )
    parser.add_argument("--related", action="append", default=[], help="add a related ref (repeatable)")
    parser.add_argument(
        "--remove-related",
        dest="remove_related",
        action="append",
        default=[],
        help="remove a related ref (repeatable)",
    )
    parser.add_argument("issue", help="GitHub issue id or configured repository issue reference")
    return parser


def apply_relationships_payload(
    *,
    project: Path,
    issue_ref: str,
    artifact_type: str,
    intent: dict[str, object],
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Apply a single GitHub issue's relationship intent directly."""

    config = _load_github_issue_config(project)
    repo, issue_numbers = _github_relationship_context(config, [issue_ref], runner=runner)
    if len(issue_numbers) != 1:
        raise GitHubIssueRelationshipsError("relationship apply requires exactly one issue ref")
    issue = issue_numbers[0]

    provider = GitHubIssueNativeProvider(runner=runner)
    response = provider.call(
        ProviderRequest(
            role="issue",
            kind="github",
            operation="apply_relationships",
            context=ProviderContext(project=config.root, artifact_type=artifact_type),
            payload={"issue": issue, "relationship_intent": intent},
        )
    )
    cache = GitHubIssueCache.for_project(config.root, configured_repo=repo)
    return flatten_provider_envelope(
        response.payload,
        project=config.root,
        issue_file=cache.issue_file(repo, issue),
    )


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

    intent = _intent_from_args(args)
    try:
        payload = apply_relationships_payload(
            project=args.project,
            issue_ref=args.issue,
            artifact_type=args.type,
            intent=intent,
            runner=runner,
        )
    except Exception as exc:
        print(f"GitHub issue relationship error: {exc}", file=errors)
        return 2

    print(json.dumps(payload, indent=2, sort_keys=False), file=output)
    return 0


def _intent_from_args(args: argparse.Namespace) -> dict[str, object]:
    intent: dict[str, object] = {}
    if args.parent:
        intent["parent_add"] = args.parent
    if args.replace_parent:
        intent["parent_replace"] = args.replace_parent
    if args.remove_parent:
        intent["parent_remove"] = True
    if args.blocked_by:
        intent["blocked_by_add"] = list(args.blocked_by)
    if args.remove_blocked_by:
        intent["blocked_by_remove"] = list(args.remove_blocked_by)
    if args.blocking:
        intent["blocking_add"] = list(args.blocking)
    if args.remove_blocking:
        intent["blocking_remove"] = list(args.remove_blocking)
    if args.child:
        intent["child_add"] = list(args.child)
    if args.remove_child:
        intent["child_remove"] = list(args.remove_child)
    if args.related:
        intent["related_add"] = list(args.related)
    if args.remove_related:
        intent["related_remove"] = list(args.remove_related)
    return intent


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


if __name__ == "__main__":
    raise SystemExit(main())
