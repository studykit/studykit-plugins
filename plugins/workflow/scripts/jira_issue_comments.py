#!/usr/bin/env python3
# /// script
# dependencies = ["python-frontmatter", "PyYAML"]
# ///
"""Append a Jira-backed issue comment from an opaque caller-owned body file."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import TextIO

import frontmatter as frontmatter_lib

from workflow_command import CommandRunner
from workflow_config import WorkflowConfig, WorkflowConfigError, load_workflow_config
from workflow_env import workflow_project_dir_from_env
from workflow_jira_issue_provider import JiraDataCenterIssueNativeProvider
from workflow_jira_issue_refs import normalize_jira_issue_key
from workflow_providers import ProviderContext, ProviderRequest


_FRONTMATTER_HANDLER = frontmatter_lib.YAMLHandler()


class JiraIssueCommentsError(RuntimeError):
    """Raised when a Jira issue comment append cannot proceed."""


def append_comment(
    *,
    project: Path,
    artifact_type: str,
    issue: str,
    body_file: Path,
    state: str | None = None,
    state_reason: str | None = None,
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Post one comment from an opaque body file to one Jira issue."""

    config = _load_jira_issue_config(project)
    artifact_type = _required_text(artifact_type, "artifact type")
    issue_key = normalize_jira_issue_key(issue)

    body_path = body_file.expanduser()
    if not body_path.is_file():
        raise JiraIssueCommentsError(f"body file does not exist: {body_path}")
    body = _strip_body_frontmatter(body_path.read_text(encoding="utf-8"))

    payload: dict[str, object] = {
        "issue": issue_key,
        "body": body,
        "freshness_check": True,
    }
    if state:
        payload["state"] = state.strip().lower()
    if state_reason:
        payload["state_reason"] = state_reason.strip()

    provider = JiraDataCenterIssueNativeProvider(runner=runner)
    response = provider.call(
        ProviderRequest(
            role="issue",
            kind="jira",
            operation="add_comment",
            context=ProviderContext(project=config.root, artifact_type=artifact_type),
            payload=payload,
        )
    )

    provider_payload = dict(response.payload)
    if provider_payload.get("status") == "blocked":
        provider_payload["body_file"] = str(body_path)
        provider_payload["body_file_removed"] = False
        return provider_payload

    cache_payload = provider_payload.get("cache") if isinstance(provider_payload.get("cache"), dict) else {}
    issue_file = (
        cache_payload.get("snapshot") if isinstance(cache_payload, dict) else None
    )
    body_removed = False
    try:
        body_path.unlink()
    except OSError:
        body_removed = False
    else:
        body_removed = True

    return {
        "operation": "append_comment",
        "kind": "jira",
        "issue": provider_payload.get("issue") or provider_payload.get("key"),
        "key": provider_payload.get("key"),
        "comment": provider_payload.get("comment"),
        "state_changed": bool(provider_payload.get("state_changed")),
        "state": provider_payload.get("state"),
        "issue_file": issue_file,
        "body_file": str(body_path),
        "body_file_removed": body_removed,
        "cache_refreshed": bool(provider_payload.get("cache_refreshed")),
        "cache": cache_payload,
    }


def _strip_body_frontmatter(body: str) -> str:
    if not _FRONTMATTER_HANDLER.detect(body):
        return body
    try:
        _frontmatter_text, remainder = _FRONTMATTER_HANDLER.split(body)
    except Exception:
        return body
    return remainder.lstrip("\n")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--project",
        type=Path,
        default=workflow_project_dir_from_env(),
        help="project path",
    )
    parser.add_argument("--json", action="store_true", help="emit JSON")
    subparsers = parser.add_subparsers(dest="command", required=True)

    append = subparsers.add_parser(
        "append",
        help="append a comment to one Jira issue from a body file",
    )
    append.add_argument("--type", default="task", help="workflow artifact type")
    append.add_argument("--issue", required=True, help="Jira issue key")
    append.add_argument(
        "--body-file",
        type=Path,
        required=True,
        help="path to the opaque body content file (leading YAML frontmatter is stripped)",
    )
    append.add_argument(
        "--state",
        help="workflow verb keyed in providers.issues.state_transitions (free-form)",
    )
    append.add_argument(
        "--state-reason",
        choices=["completed", "not_planned", "reopened"],
    )

    for child in subparsers.choices.values():
        child.add_argument("--json", action="store_true", help=argparse.SUPPRESS)
    return parser


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
        if args.command == "append":
            payload = append_comment(
                project=args.project,
                artifact_type=args.type,
                issue=args.issue,
                body_file=args.body_file,
                state=args.state,
                state_reason=args.state_reason,
                runner=runner,
            )
        else:
            raise JiraIssueCommentsError(f"unsupported command: {args.command}")
    except Exception as exc:
        print(f"Jira issue comment append error: {exc}", file=errors)
        return 2

    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=False), file=output)
    else:
        _print_plain(payload, output)
    if payload.get("status") == "blocked":
        return 3
    return 0


def _load_jira_issue_config(project: Path) -> WorkflowConfig:
    try:
        config = load_workflow_config(project)
    except WorkflowConfigError as exc:
        raise JiraIssueCommentsError(str(exc)) from exc
    if config is None:
        raise JiraIssueCommentsError(".workflow/config.yml was not found")
    if config.issues.kind != "jira":
        raise JiraIssueCommentsError(
            f"Jira issue comment append requires configured issue provider kind jira, found {config.issues.kind}"
        )
    return config


def _required_text(value: str, name: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise JiraIssueCommentsError(f"{name} is required")
    return text


def _print_plain(payload: dict[str, object], output: TextIO) -> None:
    if payload.get("status") == "blocked":
        print(
            f"{payload.get('issue')} blocked: {payload.get('reason')} "
            f"reread_required={payload.get('reread_required')}",
            file=output,
        )
        return
    print(
        f"appended comment to issue {payload.get('issue')} "
        f"state_changed={payload.get('state_changed')} "
        f"cache={payload.get('issue_file')}",
        file=output,
    )


if __name__ == "__main__":
    raise SystemExit(main())
