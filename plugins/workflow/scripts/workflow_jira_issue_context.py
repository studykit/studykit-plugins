#!/usr/bin/env python3
"""Jira issue cache context readers for prompt-time hook injection."""

from __future__ import annotations

from collections.abc import Sequence

from workflow_command import CommandRunner
from workflow_config import WorkflowConfig
from workflow_issue_cli_output import IssueFetchContext, cache_hit_from_payload, display_project_path
from workflow_jira_data_center_client import resolve_jira_data_center_site
from workflow_jira_issue_cache import JiraDataCenterIssueCache
from workflow_jira_issue_refs import normalize_jira_issue_key
from workflow_providers import CACHE_POLICY_DEFAULT, ProviderContext, ProviderRequest


def cache_jira_issue_references(
    config: WorkflowConfig,
    issue_keys: Sequence[str],
    *,
    cache_policy: str = CACHE_POLICY_DEFAULT,
    runner: CommandRunner | None = None,
    strict: bool = False,
) -> list[IssueFetchContext]:
    """Read Jira issues through the provider cache path and return hook context."""

    from workflow_jira_issue_provider import JiraDataCenterIssueNativeProvider

    provider = JiraDataCenterIssueNativeProvider(runner=runner)
    site = resolve_jira_data_center_site(config.root)
    cache = JiraDataCenterIssueCache.for_project(config.root)
    contexts: list[IssueFetchContext] = []

    for key in issue_keys:
        try:
            normalized = normalize_jira_issue_key(key)
            response = provider.call(
                ProviderRequest(
                    role="issue",
                    kind="jira",
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
            issue_dir = cache.issue_dir(site, normalized)
            contexts.append(
                IssueFetchContext(
                    number=normalized,
                    issue_dir=display_project_path(issue_dir, config.root, trailing_slash=True),
                    title=str(response.payload.get("title") or ""),
                    state=str(response.payload.get("state") or "").upper(),
                    cache_hit=cache_hit_from_payload(response.payload, default=False),
                    provider_kind="jira",
                    issue_file="snapshot.md",
                )
            )
        except Exception:
            if strict:
                raise
            continue

    return contexts
