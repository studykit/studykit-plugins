#!/usr/bin/env python3
"""GitHub issue cache context readers for prompt-time hook injection."""

from __future__ import annotations

from collections.abc import Sequence

from command import CommandRunner
from config import WorkflowConfig
from issue.github.gh import GitHubRepository, normalize_issue_number
from issue.cli_output import IssueFetchContext, cache_refreshed_from_payload, display_project_path
from issue.github.cache import GitHubIssueCache
from issue.providers import CACHE_POLICY_DEFAULT, ProviderContext, ProviderRequest


def cache_github_issue_references(
    config: WorkflowConfig,
    issue_numbers: Sequence[str],
    *,
    repo: GitHubRepository,
    cache_policy: str = CACHE_POLICY_DEFAULT,
    runner: CommandRunner | None = None,
    strict: bool = False,
) -> list[IssueFetchContext]:
    """Read GitHub issues through the provider cache path and return hook context."""

    from issue.github.provider import GitHubIssueNativeProvider

    provider = GitHubIssueNativeProvider(runner=runner)
    cache = GitHubIssueCache.for_project(config.root, configured_repo=repo)
    contexts: list[IssueFetchContext] = []

    for number in issue_numbers:
        try:
            normalized = normalize_issue_number(number)
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
                        "issue": normalized,
                        "include_body": False,
                        "include_comments": False,
                        "include_relationships": False,
                    },
                )
            )
            issue_dir = cache.issue_dir(repo, normalized)
            comment_paths = tuple(
                display_project_path(path, config.root) for path in cache.comment_files(repo, normalized)
            )
            contexts.append(
                IssueFetchContext(
                    number=normalized,
                    issue_dir=display_project_path(issue_dir, config.root, trailing_slash=True),
                    title=str(response.payload.get("title") or ""),
                    state=str(response.payload.get("state") or "").upper(),
                    cache_refreshed=cache_refreshed_from_payload(response.payload, default=True),
                    provider_kind="github",
                    comments=comment_paths,
                )
            )
        except Exception:
            if strict:
                raise
            continue

    return contexts
