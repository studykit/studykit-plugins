#!/usr/bin/env python3
# /// script
# dependencies = ["python-frontmatter", "PyYAML"]
# ///
"""Jira issue pending relationship stage/apply entrypoint."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import TextIO

from workflow_cache import SCHEMA_VERSION, _atomic_write_text, _dump_yaml
from workflow_command import CommandRunner
from workflow_config import WorkflowConfig, WorkflowConfigError, load_workflow_config
from workflow_env import workflow_project_dir_from_env
from workflow_jira_data_center_client import resolve_jira_data_center_site
from workflow_jira_issue_cache import JiraDataCenterIssueCache
from workflow_jira_issue_provider import JiraDataCenterIssueNativeProvider
from workflow_jira_issue_refs import JiraProviderError, jira_issue_keys_from_references, normalize_jira_issue_key
from workflow_providers import ProviderContext, ProviderRequest


class JiraIssueRelationshipsError(RuntimeError):
    """Raised when pending Jira issue relationships cannot be applied."""


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
    parser.add_argument("--replace", action="store_true", help="replace an existing pending relationship file when staging")
    parser.add_argument("issues", nargs="+", help="Jira issue keys or text containing Jira issue keys")
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
    """Stage relationship intent for an existing Jira issue."""

    _ = runner
    config = _load_jira_issue_config(project)
    site, issue_keys = _jira_relationship_context(config, issues)
    if len(issue_keys) != 1:
        raise JiraIssueRelationshipsError("relationship staging requires exactly one issue ref")

    issue_key = issue_keys[0]
    cache = JiraDataCenterIssueCache.for_project(config.root)
    if not cache.has_issue_projection(site, issue_key):
        raise JiraIssueRelationshipsError(f"Jira issue cache projection is missing for {issue_key}; refresh the issue cache first")

    relationships_file = cache.relationships_pending_file(site, issue_key)
    if relationships_file.exists() and not replace:
        raise JiraIssueRelationshipsError(f"pending relationship file already exists: {relationships_file}")

    payload = _relationship_payload(
        parent=parent,
        children=children,
        blocked_by=blocked_by,
        blocking=blocking,
        related=related,
    )
    relationships_file.parent.mkdir(parents=True, exist_ok=True)
    _atomic_write_text(relationships_file, _dump_yaml(payload))
    operations = cache.read_pending_issue_relationships(site, issue_key)
    return {
        "operation": "cache_stage_pending_relationships",
        "role": "issue",
        "kind": "jira",
        "site": site.to_json(),
        "issue": issue_key,
        "key": issue_key,
        "pending_location": str(relationships_file),
        "relationships_file": str(relationships_file),
        "operations": [operation.to_json() for operation in operations],
    }


def apply_pending_relationships_payload(
    *,
    project: Path,
    issues: list[str],
    artifact_type: str,
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Apply pending local relationship files to Jira issues."""

    config = _load_jira_issue_config(project)
    site, issue_keys = _jira_relationship_context(config, issues)
    provider = JiraDataCenterIssueNativeProvider(runner=runner)
    results = []
    for issue_key in issue_keys:
        response = provider.call(
            ProviderRequest(
                role="issue",
                kind="jira",
                operation="apply_relationships",
                context=ProviderContext(project=config.root, artifact_type=artifact_type),
                payload={"issue": issue_key, "from_pending": True},
            )
        )
        results.append(dict(response.payload))
    return {
        "operation": "cache_apply_pending_relationships",
        "role": "issue",
        "kind": "jira",
        "site": site.to_json(),
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
        print(f"Jira issue relationship error: {exc}", file=errors)
        return 2

    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=False), file=output)
        return 0

    if payload.get("operation") == "cache_stage_pending_relationships":
        print(f"{payload.get('issue')} staged: {payload.get('pending_location')}", file=output)
        return 0

    for item in payload.get("issues", []):
        if isinstance(item, dict):
            print(f"{item.get('issue')} applied={item.get('applied')}", file=output)
    return 0


def _jira_relationship_context(config: WorkflowConfig, issues: list[str]):
    try:
        site = resolve_jira_data_center_site(config.root)
    except (WorkflowConfigError, JiraProviderError) as exc:
        raise JiraIssueRelationshipsError(str(exc)) from exc
    issue_keys = []
    for issue in jira_issue_keys_from_references(issues):
        try:
            issue_keys.append(normalize_jira_issue_key(issue))
        except JiraProviderError as exc:
            raise JiraIssueRelationshipsError(str(exc)) from exc
    if not issue_keys:
        raise JiraIssueRelationshipsError("no Jira issue references were found")
    return site, issue_keys


def _load_jira_issue_config(project: Path) -> WorkflowConfig:
    try:
        config = load_workflow_config(project)
    except WorkflowConfigError as exc:
        raise JiraIssueRelationshipsError(str(exc)) from exc
    if config is None:
        raise JiraIssueRelationshipsError(".workflow/config.yml was not found")
    if config.issues.kind != "jira":
        raise JiraIssueRelationshipsError(
            f"Jira issue relationship commands require configured issue provider kind jira, found {config.issues.kind}"
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
        raise JiraIssueRelationshipsError("at least one relationship value is required")
    return payload


def _required_ref(value: str, name: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise JiraIssueRelationshipsError(f"{name} relationship ref is required")
    return text


def _normalized_refs(values: tuple[str, ...]) -> list[str]:
    return [value.strip() for value in values if value.strip()]


if __name__ == "__main__":
    raise SystemExit(main())
