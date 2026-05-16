#!/usr/bin/env python3
# /// script
# dependencies = ["python-frontmatter", "PyYAML"]
# ///
"""Jira issue semantic metadata update entrypoint."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, TextIO

from workflow_cache import WorkflowCacheError
from workflow_command import CommandRunner
from workflow_config import WorkflowConfig, WorkflowConfigError, load_workflow_config
from workflow_env import workflow_project_dir_from_env
from workflow_jira_data_center_client import resolve_jira_data_center_site
from workflow_jira_issue_cache import JiraDataCenterIssueCache
from workflow_jira_issue_provider import JiraDataCenterIssueNativeProvider
from workflow_jira_issue_refs import JiraProviderError, normalize_jira_issue_key
from workflow_providers import ProviderContext, ProviderRequest


class WorkflowIssueMetadataError(RuntimeError):
    """Raised when semantic Jira issue metadata cannot be updated safely."""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=workflow_project_dir_from_env(), help="project path")
    parser.add_argument("--artifact-type", default="task", help="workflow artifact type for dispatch context")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    parser.add_argument("--title", help="new semantic title")
    parser.add_argument("--workflow-type", help="new workflow type metadata value")
    parser.add_argument("--status", help="semantic status; unsupported unless mapping is configured")
    parser.add_argument("--priority", help="semantic priority; unsupported unless mapping is configured")
    parser.add_argument("issue", help="Jira issue key")
    return parser


def update_issue_metadata_payload(
    *,
    project: Path,
    issue: str,
    artifact_type: str,
    title: str | None = None,
    workflow_type: str | None = None,
    status: str | None = None,
    priority: str | None = None,
    runner: CommandRunner | None = None,
) -> dict[str, Any]:
    """Update safe semantic metadata for one Jira issue."""

    config = _load_jira_issue_config(project)
    if workflow_type is not None:
        raise WorkflowIssueMetadataError("Jira semantic type writes require explicit safe type-change config")
    if status is not None:
        raise WorkflowIssueMetadataError("Jira semantic status writes require explicit transition or field mapping config")
    if priority is not None:
        raise WorkflowIssueMetadataError("Jira semantic priority writes require explicit metadata mapping config")

    try:
        site = resolve_jira_data_center_site(config.root)
        issue_key = normalize_jira_issue_key(issue)
    except (WorkflowConfigError, JiraProviderError) as exc:
        raise WorkflowIssueMetadataError(str(exc)) from exc

    cache = JiraDataCenterIssueCache.for_project(config.root)
    try:
        cache.read_issue(site, issue_key, include_body=False, include_comments=False, include_relationships=False)
    except WorkflowCacheError as exc:
        raise WorkflowIssueMetadataError(f"refresh the Jira issue cache before metadata update: {exc}") from exc

    payload: dict[str, Any] = {"issue": issue_key, "freshness_check": True}
    if title is not None:
        payload["title"] = title
    if len(payload) == 2:
        raise WorkflowIssueMetadataError("metadata update requires at least one supported metadata value")

    provider = JiraDataCenterIssueNativeProvider(runner=runner)
    response = provider.call(
        ProviderRequest(
            role="issue",
            kind="jira",
            operation="update",
            context=ProviderContext(project=config.root, artifact_type=artifact_type),
            payload=payload,
        )
    )
    return {
        "operation": "update_issue_metadata",
        "kind": "jira",
        "issue": issue_key,
        "key": issue_key,
        "site": site.to_json(),
        "updated": _updated_fields(title=title),
        "provider": dict(response.payload),
    }


def _updated_fields(*, title: str | None) -> list[str]:
    fields = []
    if title is not None:
        fields.append("title")
    return fields


def _load_jira_issue_config(project: Path) -> WorkflowConfig:
    try:
        config = load_workflow_config(project)
    except WorkflowConfigError as exc:
        raise WorkflowIssueMetadataError(str(exc)) from exc
    if config is None:
        raise WorkflowIssueMetadataError(".workflow/config.yml was not found")
    if config.issues.kind != "jira":
        raise WorkflowIssueMetadataError(
            f"Jira issue metadata updates require configured issue provider kind jira, found {config.issues.kind}"
        )
    return config


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
        payload = update_issue_metadata_payload(
            project=args.project,
            issue=args.issue,
            artifact_type=args.artifact_type,
            title=args.title,
            workflow_type=args.workflow_type,
            status=args.status,
            priority=args.priority,
            runner=runner,
        )
    except Exception as exc:
        print(f"Jira issue metadata error: {exc}", file=errors)
        return 2

    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=False), file=output)
        return 0

    print(f"{payload.get('issue')} metadata updated: {', '.join(payload.get('updated') or [])}", file=output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
