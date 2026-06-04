#!/usr/bin/env python3
"""Jira issue cache context readers for prompt-time hook injection."""

from __future__ import annotations

from collections.abc import Sequence

from command import CommandRunner
from config import WorkflowConfig
from issue.cli_output import IssueFetchContext, cache_refreshed_from_payload, display_project_path
from issue.jira.cache import JiraDataCenterIssueCache
from issue.jira.refs import normalize_jira_issue_key
from issue.jira.client import resolve_jira_data_center_site
from issue.providers import CACHE_POLICY_DEFAULT, ProviderContext, ProviderRequest


def cache_jira_issue_references(
    config: WorkflowConfig,
    issue_keys: Sequence[str],
    *,
    cache_policy: str = CACHE_POLICY_DEFAULT,
    runner: CommandRunner | None = None,
    strict: bool = False,
) -> list[IssueFetchContext]:
    """Read Jira issues through the provider cache path and return hook context."""

    from issue.jira.provider import JiraDataCenterIssueNativeProvider

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
            comment_paths = tuple(
                display_project_path(path, config.root) for path in cache.comment_files(site, normalized)
            )
            relationships_path = cache.relationships_file(site, normalized)
            relationships_display = (
                display_project_path(relationships_path, config.root)
                if relationships_path.is_file()
                else None
            )
            attachments_path = cache.attachments_file(site, normalized)
            attachments_display = (
                display_project_path(attachments_path, config.root)
                if attachments_path.is_file()
                else None
            )
            contexts.append(
                IssueFetchContext(
                    number=normalized,
                    issue_dir=display_project_path(issue_dir, config.root, trailing_slash=True),
                    title=str(response.payload.get("title") or ""),
                    state=str(response.payload.get("state") or "").upper(),
                    cache_refreshed=cache_refreshed_from_payload(response.payload, default=True),
                    provider_kind="jira",
                    comments=comment_paths,
                    relationships=relationships_display,
                    attachments=attachments_display,
                )
            )
        except Exception:
            if strict:
                raise
            continue

    return contexts
