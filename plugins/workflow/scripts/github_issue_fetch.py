#!/usr/bin/env python3
# /// script
# dependencies = ["python-frontmatter", "PyYAML"]
# ///
"""GitHub Issues cache fetch entrypoint."""

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
from workflow_github_issue_cache import GitHubIssueCache
from workflow_github_issue_provider import GitHubIssueNativeProvider
from workflow_github_issue_refs import issue_numbers_from_references
from workflow_issue_cli_output import (
    IssueFetchContext,
    cache_hit_from_payload,
    display_project_path,
    format_issue_cache_json,
)
from workflow_providers import CACHE_POLICY_DEFAULT, CACHE_POLICY_REFRESH, ProviderContext, ProviderRequest

CACHE_FETCH_POLICIES = (CACHE_POLICY_DEFAULT, CACHE_POLICY_REFRESH)


class GitHubIssueFetchError(RuntimeError):
    """Raised when GitHub issue cache fetch cannot proceed."""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=workflow_project_dir_from_env(), help="project path")
    parser.add_argument(
        "--cache-policy",
        choices=CACHE_FETCH_POLICIES,
        default=CACHE_POLICY_DEFAULT,
        help="provider cache policy",
    )
    parser.add_argument("references", nargs="+", help="GitHub issue IDs or configured repository issue references")
    return parser


def fetch_cache_payload(
    *,
    project: Path,
    references: list[str],
    cache_policy: str = CACHE_POLICY_DEFAULT,
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Fetch configured GitHub issue references into the workflow cache."""

    config = _load_github_issue_config(project)
    try:
        repo = resolve_github_repository(config.root, runner=runner)
    except GitHubRepositoryError as exc:
        raise GitHubIssueFetchError(str(exc)) from exc

    issue_numbers = issue_numbers_from_references(references, repo=repo, allow_bare_numbers=True)
    if not issue_numbers:
        raise GitHubIssueFetchError("no configured GitHub issue references were found")

    provider = GitHubIssueNativeProvider(runner=runner)
    cache = GitHubIssueCache.for_project(config.root, configured_repo=repo)
    contexts: list[IssueFetchContext] = []
    for issue in issue_numbers:
        response = provider.call(
            ProviderRequest(
                role="issue",
                kind="github",
                operation="get",
                context=ProviderContext(
                    project=config.root,
                    artifact_type="task",
                    cache_policy=cache_policy,
                ),
                payload={
                    "issue": issue,
                    "include_body": False,
                    "include_comments": False,
                    "include_relationships": False,
                },
            )
        )
        issue_dir = cache.issue_dir(repo, issue)
        comment_paths = tuple(
            display_project_path(path, config.root) for path in cache.comment_files(repo, issue)
        )
        contexts.append(
            IssueFetchContext(
                number=issue,
                issue_dir=display_project_path(issue_dir, config.root, trailing_slash=True),
                title=str(response.payload.get("title") or ""),
                state=str(response.payload.get("state") or "").upper(),
                cache_hit=cache_hit_from_payload(response.payload, default=False),
                provider_kind="github",
                comments=comment_paths,
            )
        )

    return format_issue_cache_json(contexts)


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
        payload = fetch_cache_payload(
            project=args.project,
            references=list(args.references),
            cache_policy=args.cache_policy,
            runner=runner,
        )
    except Exception as exc:
        print(f"GitHub issue fetch error: {exc}", file=errors)
        return 2

    print(json.dumps(payload, indent=2, sort_keys=False), file=output)
    return 0


def _load_github_issue_config(project: Path) -> WorkflowConfig:
    try:
        config = load_workflow_config(project)
    except WorkflowConfigError as exc:
        raise GitHubIssueFetchError(str(exc)) from exc
    if config is None:
        raise GitHubIssueFetchError(".workflow/config.yml was not found")
    if config.issues.kind != "github":
        raise GitHubIssueFetchError(
            f"GitHub issue fetch requires configured issue provider kind github, found {config.issues.kind}"
        )
    return config


if __name__ == "__main__":
    raise SystemExit(main())
