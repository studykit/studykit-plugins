#!/usr/bin/env python3
# /// script
# dependencies = ["python-frontmatter", "PyYAML"]
# ///
"""Jira issue relationship apply entrypoint.

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
from issue.cli_output import flatten_provider_envelope
from workflow_jira_data_center_client import resolve_jira_data_center_site
from issue.jira.cache import JiraDataCenterIssueCache
from issue.jira.provider import JiraDataCenterIssueNativeProvider
from issue.jira.refs import JiraProviderError, jira_issue_keys_from_references, normalize_jira_issue_key
from workflow_providers import ProviderContext, ProviderRequest


class JiraIssueRelationshipsError(RuntimeError):
    """Raised when Jira issue relationships cannot be applied."""


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
    epic_group = parser.add_mutually_exclusive_group()
    epic_group.add_argument(
        "--epic",
        help="add Epic Link (errors if an Epic Link already exists)",
    )
    epic_group.add_argument(
        "--replace-epic",
        dest="replace_epic",
        help="set Epic Link, replacing any existing Epic Link",
    )
    epic_group.add_argument(
        "--remove-epic",
        dest="remove_epic",
        action="store_true",
        help="remove the current Epic Link (no-op when no Epic Link exists)",
    )
    parser.add_argument("--child", action="append", default=[], help="add a child (repeatable)")
    parser.add_argument("--remove-child", dest="remove_child", action="append", default=[], help="remove a child (repeatable)")
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
    parser.add_argument("issue", help="Jira issue key")
    return parser


def apply_relationships_payload(
    *,
    project: Path,
    issue_ref: str,
    artifact_type: str,
    intent: dict[str, object],
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Apply a single Jira issue's relationship intent directly."""

    config = _load_jira_issue_config(project)
    site, issue_keys = _jira_relationship_context(config, [issue_ref])
    if len(issue_keys) != 1:
        raise JiraIssueRelationshipsError("relationship apply requires exactly one issue ref")
    issue_key = issue_keys[0]

    provider = JiraDataCenterIssueNativeProvider(runner=runner)
    response = provider.call(
        ProviderRequest(
            role="issue",
            kind="jira",
            operation="apply_relationships",
            context=ProviderContext(project=config.root, artifact_type=artifact_type),
            payload={"issue": issue_key, "relationship_intent": intent},
        )
    )
    cache = JiraDataCenterIssueCache.for_project(config.root)
    return flatten_provider_envelope(
        response.payload,
        project=config.root,
        issue_file=cache.issue_file(site, issue_key),
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
        print(f"Jira issue relationship error: {exc}", file=errors)
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
    if args.epic:
        intent["epic_add"] = args.epic
    if args.replace_epic:
        intent["epic_replace"] = args.replace_epic
    if args.remove_epic:
        intent["epic_remove"] = True
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


if __name__ == "__main__":
    raise SystemExit(main())
