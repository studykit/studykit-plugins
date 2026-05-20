#!/usr/bin/env python3
# /// script
# dependencies = ["python-frontmatter", "PyYAML"]
# ///
"""Jira Issues body-less field mutation entrypoint."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, TextIO

from workflow_command import CommandRunner
from workflow_config import WorkflowConfig, WorkflowConfigError, load_workflow_config
from workflow_env import workflow_project_dir_from_env
from workflow_jira_data_center_client import resolve_jira_data_center_site
from workflow_jira_issue_provider import (
    JIRA_ARTIFACT_ISSUE_TYPES,
    JiraDataCenterIssueNativeProvider,
    _jira_configured_artifact_issue_types,
    _jira_issue_provider_settings,
    get_jira_myself,
)
from workflow_jira_issue_refs import JiraProviderError, normalize_jira_issue_key
from workflow_providers import ProviderContext, ProviderRequest


class JiraIssueFieldsError(RuntimeError):
    """Raised when a Jira issue field mutation cannot proceed."""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=workflow_project_dir_from_env(), help="project path")
    parser.add_argument("--type", default="task", help="workflow artifact type")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    subparsers = parser.add_subparsers(dest="verb", required=True)

    p_close = subparsers.add_parser("close", help="close an issue")
    p_close.add_argument("issue", help="Jira issue key")
    p_close.add_argument("--reason", choices=("completed", "not_planned"), default="completed")
    p_close.add_argument("--comment", help="optional comment posted alongside the close")

    p_reopen = subparsers.add_parser("reopen", help="reopen an issue")
    p_reopen.add_argument("issue", help="Jira issue key")
    p_reopen.add_argument("--comment", help="optional comment posted alongside the reopen")

    p_assign = subparsers.add_parser("assign", help="assign an issue to a user")
    p_assign.add_argument("issue", help="Jira issue key")
    p_assign.add_argument("user", help='Jira DC username or the literal "me"')

    p_unassign = subparsers.add_parser("unassign", help="clear the assignee")
    p_unassign.add_argument("issue", help="Jira issue key")

    p_set_type = subparsers.add_parser("set-type", help="set the Jira issuetype via the artifact mapping")
    p_set_type.add_argument("issue", help="Jira issue key")
    p_set_type.add_argument("new_type", metavar="type", help="workflow artifact type whose Jira issuetype to apply")

    return parser


def fields_payload(
    *,
    project: Path,
    artifact_type: str,
    verb: str,
    issue: str,
    reason: str | None = None,
    comment: str | None = None,
    user: str | None = None,
    new_type: str | None = None,
    runner: CommandRunner | None = None,
) -> dict[str, Any]:
    config = _load_jira_issue_config(project)
    try:
        site = resolve_jira_data_center_site(config.root)
        issue_key = normalize_jira_issue_key(issue)
    except (WorkflowConfigError, JiraProviderError) as exc:
        raise JiraIssueFieldsError(str(exc)) from exc

    provider = JiraDataCenterIssueNativeProvider(runner=runner)
    context = ProviderContext(project=config.root, artifact_type=artifact_type)

    if verb in {"close", "reopen"}:
        state = verb
        if comment:
            payload: dict[str, Any] = {
                "issue": issue_key,
                "freshness_check": True,
                "body": comment,
                "state": state,
            }
            operation = "add_comment"
        else:
            payload = {"issue": issue_key, "freshness_check": True, "state": state}
            operation = "update"
        response = provider.call(
            ProviderRequest(
                role="issue",
                kind="jira",
                operation=operation,
                context=context,
                payload=payload,
            )
        )
        return {
            "operation": f"lifecycle_{verb}",
            "role": "issue",
            "kind": "jira",
            "site": site.to_json(),
            "issue": issue_key,
            "key": issue_key,
            "reason": reason if verb == "close" else None,
            "provider": dict(response.payload),
        }

    if verb == "assign":
        if not user:
            raise JiraIssueFieldsError("assign requires a user")
        resolved = user
        if resolved.strip().lower() == "me":
            resolved = get_jira_myself(site, runner=runner)
        payload = {"issue": issue_key, "freshness_check": True, "assignee": resolved}
    elif verb == "unassign":
        payload = {"issue": issue_key, "freshness_check": True, "unassign": True}
    elif verb == "set-type":
        if not new_type or not new_type.strip():
            raise JiraIssueFieldsError("set-type requires a non-empty type")
        artifact = new_type.strip().lower()
        try:
            settings = _jira_issue_provider_settings(config.root)
        except Exception as exc:
            raise JiraIssueFieldsError(str(exc)) from exc
        configured = _jira_configured_artifact_issue_types(settings).get(artifact)
        native = configured or JIRA_ARTIFACT_ISSUE_TYPES.get(artifact)
        if not native:
            raise JiraIssueFieldsError(
                f"no Jira issuetype mapping for workflow type '{new_type}'. "
                f"Configure providers.issues.artifact_issue_types.{artifact} in .workflow/config.yml."
            )
        payload = {"issue": issue_key, "freshness_check": True, "issuetype": native}
    else:
        raise JiraIssueFieldsError(f"unsupported verb: {verb}")

    response = provider.call(
        ProviderRequest(
            role="issue",
            kind="jira",
            operation="update",
            context=context,
            payload=payload,
        )
    )
    return {
        "operation": f"fields_{verb.replace('-', '_')}",
        "role": "issue",
        "kind": "jira",
        "site": site.to_json(),
        "issue": issue_key,
        "key": issue_key,
        "provider": dict(response.payload),
    }


def _load_jira_issue_config(project: Path) -> WorkflowConfig:
    try:
        config = load_workflow_config(project)
    except WorkflowConfigError as exc:
        raise JiraIssueFieldsError(str(exc)) from exc
    if config is None:
        raise JiraIssueFieldsError(".workflow/config.yml was not found")
    if config.issues.kind != "jira":
        raise JiraIssueFieldsError(
            f"Jira issue field updates require configured issue provider kind jira, found {config.issues.kind}"
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
        payload = fields_payload(
            project=args.project,
            artifact_type=args.type,
            verb=args.verb,
            issue=args.issue,
            reason=getattr(args, "reason", None),
            comment=getattr(args, "comment", None),
            user=getattr(args, "user", None),
            new_type=getattr(args, "new_type", None),
            runner=runner,
        )
    except Exception as exc:
        print(f"Jira issue fields error: {exc}", file=errors)
        return 2

    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=False), file=output)
    else:
        provider_payload = payload.get("provider") or {}
        status = provider_payload.get("status")
        if status == "blocked":
            print(
                f"{payload.get('key')} blocked: {provider_payload.get('reason')} "
                f"reread_required={provider_payload.get('reread_required')}",
                file=output,
            )
        else:
            print(
                f"{payload.get('key')} {payload.get('operation')} "
                f"verified={provider_payload.get('verified')}",
                file=output,
            )
    if (payload.get("provider") or {}).get("status") == "blocked":
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
