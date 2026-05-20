#!/usr/bin/env python3
# /// script
# dependencies = ["python-frontmatter", "PyYAML"]
# ///
"""Update an existing Jira-backed issue body from an opaque caller-owned body file."""

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


class JiraIssueWritebackError(RuntimeError):
    """Raised when Jira issue body update cannot proceed."""


def update_issue(
    *,
    project: Path,
    artifact_type: str,
    issue: str,
    body_file: Path,
    title: str | None = None,
    add_labels: tuple[str, ...] = (),
    remove_labels: tuple[str, ...] = (),
    set_labels: tuple[str, ...] | None = None,
    state: str | None = None,
    state_reason: str | None = None,
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Update one Jira issue body from an opaque caller-owned body file."""

    config = _load_jira_issue_config(project)
    artifact_type = _required_text(artifact_type, "artifact type")
    issue_key = normalize_jira_issue_key(issue)

    body_path = body_file.expanduser()
    if not body_path.is_file():
        raise JiraIssueWritebackError(f"body file does not exist: {body_path}")
    body = _strip_body_frontmatter(body_path.read_text(encoding="utf-8"))

    normalized_add = tuple(label.strip() for label in add_labels if label.strip())
    normalized_remove = tuple(label.strip() for label in remove_labels if label.strip())
    normalized_set: tuple[str, ...] | None
    if set_labels is None:
        normalized_set = None
    else:
        normalized_set = tuple(label.strip() for label in set_labels if label.strip())
    if normalized_set is not None and (normalized_add or normalized_remove):
        raise JiraIssueWritebackError(
            "--set-labels cannot be combined with --add-label or --remove-label"
        )

    payload: dict[str, object] = {
        "issue": issue_key,
        "body": body,
        "freshness_check": True,
    }
    if title is not None:
        payload["title"] = title
    if normalized_set is not None:
        payload["label_set"] = list(normalized_set)
    if normalized_add:
        payload["label_add"] = list(normalized_add)
    if normalized_remove:
        payload["label_remove"] = list(normalized_remove)
    if state:
        payload["state"] = state.strip().lower()
    if state_reason:
        payload["state_reason"] = state_reason.strip()

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

    provider_payload = dict(response.payload)
    if provider_payload.get("status") == "blocked":
        provider_payload["body_file"] = str(body_path)
        provider_payload["body_file_removed"] = False
        return provider_payload

    cache_payload = provider_payload.get("cache") if isinstance(provider_payload.get("cache"), dict) else {}
    issue_file = (
        cache_payload.get("issue_file") if isinstance(cache_payload, dict) else None
    )
    body_removed = False
    try:
        body_path.unlink()
    except OSError:
        body_removed = False
    else:
        body_removed = True

    return {
        "operation": "update_issue",
        "kind": "jira",
        "issue": provider_payload.get("issue") or provider_payload.get("key"),
        "key": provider_payload.get("key"),
        "verified": bool(provider_payload.get("verified")),
        "state_changed": bool(provider_payload.get("state_changed")),
        "state": provider_payload.get("state"),
        "issue_file": issue_file,
        "body_file": str(body_path),
        "body_file_removed": body_removed,
        "cache_refreshed": bool(provider_payload.get("cache_refreshed")),
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
    subparsers = parser.add_subparsers(dest="command", required=True)

    update = subparsers.add_parser(
        "update",
        help="update one Jira issue body from a body file",
    )
    update.add_argument("--type", default="task", help="workflow artifact type")
    update.add_argument("--issue", required=True, help="Jira issue key")
    update.add_argument(
        "--body-file",
        type=Path,
        required=True,
        help="path to the opaque body content file (leading YAML frontmatter is stripped)",
    )
    update.add_argument("--title")
    update.add_argument(
        "--add-label",
        dest="add_label",
        action="append",
        default=[],
        help="add a label (repeatable; cannot be combined with --set-labels)",
    )
    update.add_argument(
        "--remove-label",
        dest="remove_label",
        action="append",
        default=[],
        help="remove a label (repeatable; cannot be combined with --set-labels)",
    )
    update.add_argument(
        "--set-labels",
        dest="set_labels",
        help="replace the label set with a comma-separated list",
    )
    update.add_argument(
        "--state",
        help="workflow verb keyed in providers.issues.state_transitions (free-form)",
    )
    update.add_argument(
        "--state-reason",
        choices=["completed", "not_planned", "reopened"],
    )

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
        if args.command == "update":
            set_labels: tuple[str, ...] | None = None
            if args.set_labels is not None:
                set_labels = tuple(part for part in args.set_labels.split(","))
            payload = update_issue(
                project=args.project,
                artifact_type=args.type,
                issue=args.issue,
                body_file=args.body_file,
                title=args.title,
                add_labels=tuple(args.add_label),
                remove_labels=tuple(args.remove_label),
                set_labels=set_labels,
                state=args.state,
                state_reason=args.state_reason,
                runner=runner,
            )
        else:
            raise JiraIssueWritebackError(f"unsupported command: {args.command}")
    except Exception as exc:
        print(f"Jira issue update error: {exc}", file=errors)
        return 2

    print(json.dumps(payload, indent=2, sort_keys=False), file=output)
    if payload.get("status") == "blocked":
        return 3
    return 0


def _load_jira_issue_config(project: Path) -> WorkflowConfig:
    try:
        config = load_workflow_config(project)
    except WorkflowConfigError as exc:
        raise JiraIssueWritebackError(str(exc)) from exc
    if config is None:
        raise JiraIssueWritebackError(".workflow/config.yml was not found")
    if config.issues.kind != "jira":
        raise JiraIssueWritebackError(
            f"Jira issue update requires configured issue provider kind jira, found {config.issues.kind}"
        )
    return config


def _required_text(value: str, name: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise JiraIssueWritebackError(f"{name} is required")
    return text


if __name__ == "__main__":
    raise SystemExit(main())
