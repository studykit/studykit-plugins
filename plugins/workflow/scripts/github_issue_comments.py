#!/usr/bin/env python3
# /// script
# dependencies = ["python-frontmatter", "PyYAML"]
# ///
"""GitHub Issues pending comment append entrypoint."""

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


class GitHubIssueCommentsError(RuntimeError):
    """Raised when pending GitHub issue comments cannot be appended."""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=workflow_project_dir_from_env(), help="project path")
    parser.add_argument("--type", default="task", help="workflow artifact type")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    parser.add_argument("issues", nargs="+", help="GitHub issue IDs or configured repository issue references")
    return parser


def append_pending_comments_payload(
    *,
    project: Path,
    issues: list[str],
    artifact_type: str,
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Append pending local comment files to GitHub issues."""

    config = _load_github_issue_config(project)
    try:
        repo = resolve_github_repository(config.root, runner=runner)
    except GitHubRepositoryError as exc:
        raise GitHubIssueCommentsError(str(exc)) from exc

    issue_numbers = issue_numbers_from_references(issues, repo=repo, allow_bare_numbers=True)
    if not issue_numbers:
        raise GitHubIssueCommentsError("no configured GitHub issue references were found")

    provider = GitHubIssueNativeProvider(runner=runner)
    results = []
    for issue in issue_numbers:
        response = provider.call(
            ProviderRequest(
                role="issue",
                kind="github",
                operation="add_comment",
                context=ProviderContext(project=config.root, artifact_type=artifact_type),
                payload={"issue": issue, "from_pending": True},
            )
        )
        results.append(dict(response.payload))

    return {
        "operation": "cache_append_pending_comments",
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
        payload = append_pending_comments_payload(
            project=args.project,
            issues=list(args.issues),
            artifact_type=args.type,
            runner=runner,
        )
    except Exception as exc:
        print(f"GitHub issue pending comment append error: {exc}", file=errors)
        return 2

    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=False), file=output)
        return 0

    for item in payload["issues"]:
        if isinstance(item, dict):
            if item.get("status") == "blocked":
                print(
                    f"#{item.get('issue')} blocked: {item.get('reason')} "
                    f"reread_required={item.get('reread_required')}",
                    file=output,
                )
            else:
                print(f"#{item.get('issue')} appended={item.get('appended')}", file=output)
    return 0


def _load_github_issue_config(project: Path) -> WorkflowConfig:
    try:
        config = load_workflow_config(project)
    except WorkflowConfigError as exc:
        raise GitHubIssueCommentsError(str(exc)) from exc
    if config is None:
        raise GitHubIssueCommentsError(".workflow/config.yml was not found")
    if config.issues.kind != "github":
        raise GitHubIssueCommentsError(
            f"GitHub issue comment append requires configured issue provider kind github, found {config.issues.kind}"
        )
    return config


if __name__ == "__main__":
    raise SystemExit(main())
