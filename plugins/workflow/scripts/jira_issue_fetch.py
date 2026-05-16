#!/usr/bin/env python3
# /// script
# dependencies = ["python-frontmatter", "PyYAML"]
# ///
"""Jira issue cache fetch entrypoint."""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Mapping
from pathlib import Path
from typing import TextIO

from workflow_command import CommandRunner
from workflow_config import WorkflowConfig, WorkflowConfigError, load_workflow_config
from workflow_env import workflow_project_dir_from_env
from workflow_issue_cli_output import (
    IssueFetchContext,
    cache_hit_from_payload,
    display_project_path,
    format_issue_cache_context_from_payload,
    format_issue_cache_json,
)
from workflow_jira_data_center_client import resolve_jira_data_center_site
from workflow_jira_issue_cache import JiraDataCenterIssueCache
from workflow_jira_issue_provider import JiraDataCenterIssueNativeProvider
from workflow_jira_issue_refs import JiraProviderError, jira_issue_keys_from_references, normalize_jira_issue_key
from workflow_providers import CACHE_POLICY_DEFAULT, CACHE_POLICY_REFRESH, ProviderContext, ProviderRequest
from workflow_relationship_renderers import render_relationship_summary

CACHE_FETCH_POLICIES = (CACHE_POLICY_DEFAULT, CACHE_POLICY_REFRESH)


class JiraIssueFetchError(RuntimeError):
    """Raised when Jira issue cache fetch cannot proceed."""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=workflow_project_dir_from_env(), help="project path")
    parser.add_argument(
        "--cache-policy",
        choices=CACHE_FETCH_POLICIES,
        default=CACHE_POLICY_DEFAULT,
        help="provider cache policy",
    )
    parser.add_argument("--json", action="store_true", help="emit JSON")
    parser.add_argument("references", nargs="+", help="Jira issue keys or text containing configured Jira issue keys")
    return parser


def fetch_cache_payload(
    *,
    project: Path,
    references: list[str],
    cache_policy: str = CACHE_POLICY_DEFAULT,
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Fetch configured Jira issue references into the workflow cache."""

    config = _load_jira_issue_config(project)
    try:
        site = resolve_jira_data_center_site(config.root)
    except (WorkflowConfigError, JiraProviderError) as exc:
        raise JiraIssueFetchError(str(exc)) from exc

    issue_keys = jira_issue_keys_from_references(references)
    if not issue_keys:
        raise JiraIssueFetchError("no Jira issue references were found")

    provider = JiraDataCenterIssueNativeProvider(runner=runner)
    cache = JiraDataCenterIssueCache.for_project(config.root)
    contexts: list[IssueFetchContext] = []
    for issue in issue_keys:
        try:
            issue_key = normalize_jira_issue_key(issue)
        except JiraProviderError as exc:
            raise JiraIssueFetchError(str(exc)) from exc
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
                    "issue": issue_key,
                    "include_body": False,
                    "include_comments": False,
                    "include_relationships": False,
                },
            )
        )
        issue_dir = cache.issue_dir(site, issue_key)
        relationship_summary = _cached_relationship_summary(cache, site, issue_key)
        contexts.append(
            IssueFetchContext(
                number=issue_key,
                issue_dir=display_project_path(issue_dir, config.root, trailing_slash=True),
                title=str(response.payload.get("title") or ""),
                state=str(response.payload.get("state") or "").upper(),
                cache_hit=cache_hit_from_payload(response.payload, default=False),
                relationship_summary=relationship_summary,
                provider_kind="jira",
                issue_file="snapshot.md",
            )
        )

    return format_issue_cache_json(
        contexts,
        provider_kind="jira",
        cache_policy=cache_policy,
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

    try:
        payload = fetch_cache_payload(
            project=args.project,
            references=list(args.references),
            cache_policy=args.cache_policy,
            runner=runner,
        )
    except Exception as exc:
        print(f"Jira issue fetch error: {exc}", file=errors)
        return 2

    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=False), file=output)
        return 0

    print(format_issue_cache_context_from_payload(payload), file=output)
    return 0


def _load_jira_issue_config(project: Path) -> WorkflowConfig:
    try:
        config = load_workflow_config(project)
    except WorkflowConfigError as exc:
        raise JiraIssueFetchError(str(exc)) from exc
    if config is None:
        raise JiraIssueFetchError(".workflow/config.yml was not found")
    if config.issues.kind != "jira":
        raise JiraIssueFetchError(
            f"Jira issue fetch requires configured issue provider kind jira, found {config.issues.kind}"
        )
    return config


def _cached_relationship_summary(cache: JiraDataCenterIssueCache, site, issue_key: str) -> str:
    try:
        cached = cache.read_issue(site, issue_key, include_body=False, include_comments=False, include_relationships=True)
    except Exception:
        return ""
    relationships = cached.get("relationships") if isinstance(cached, Mapping) else {}
    if not isinstance(relationships, Mapping):
        return ""
    return render_relationship_summary("jira", relationships)


if __name__ == "__main__":
    raise SystemExit(main())
