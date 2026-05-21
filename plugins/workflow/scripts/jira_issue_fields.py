#!/usr/bin/env python3
# /// script
# dependencies = ["python-frontmatter", "PyYAML"]
# ///
"""Jira Issues body-less field mutation entrypoint."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any, TextIO

from workflow_command import CommandRunner
from workflow_config import WorkflowConfig, WorkflowConfigError, load_workflow_config
from workflow_env import workflow_project_dir_from_env
from issue.cli_output import flatten_provider_envelope
from workflow_jira_data_center_client import resolve_jira_data_center_site
from issue.jira.provider import (
    JIRA_ARTIFACT_ISSUE_TYPES,
    JiraDataCenterIssueNativeProvider,
    _jira_configured_artifact_issue_types,
    _jira_issue_provider_settings,
    get_jira_myself,
)
from issue.jira.refs import JiraProviderError, normalize_jira_issue_key
from workflow_providers import ProviderContext, ProviderRequest


_RESERVED_VERBS = frozenset({"assign", "unassign", "set-type"})

_LIFECYCLE_NOTE = (
    "Lifecycle verbs come from providers.issues.state_transitions; "
    "configure one with `workflow_setup.py build-config "
    "--jira-state-transition <verb>=<transition>`."
)


class JiraIssueFieldsError(RuntimeError):
    """Raised when a Jira issue field mutation cannot proceed."""


class _JiraFieldsParser(argparse.ArgumentParser):
    """Argparse parser that surfaces friendly errors for unknown verbs."""

    def __init__(self, *args: Any, state_verbs: Iterable[str] = (), **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._state_verbs: tuple[str, ...] = tuple(state_verbs)

    def error(self, message: str) -> None:  # type: ignore[override]
        match = re.match(r"argument verb: invalid choice: '([^']+)'", message)
        if match:
            verb = match.group(1)
            self.print_usage(sys.stderr)
            hint = self._unknown_verb_hint(verb)
            self.exit(2, hint)
        super().error(message)

    def _unknown_verb_hint(self, verb: str) -> str:
        reserved = ", ".join(sorted(_RESERVED_VERBS))
        configured = ", ".join(self._state_verbs) if self._state_verbs else "(none configured)"
        return (
            f"{self.prog}: error: unknown verb '{verb}'.\n"
            f"  reserved verbs: {reserved}\n"
            f"  configured lifecycle verbs: {configured}\n"
            f"  to add this verb, configure providers.issues.state_transitions.{verb} "
            f"in .workflow/config.yml (see `workflow_setup.py build-config "
            f"--jira-state-transition {verb}=<transition>`).\n"
        )


def build_base_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--project", type=Path, default=workflow_project_dir_from_env())
    parser.add_argument("--type", default="task")
    return parser


def build_parser(state_verbs: Iterable[str] = ()) -> argparse.ArgumentParser:
    verbs = tuple(state_verbs)
    parser = _JiraFieldsParser(
        description=f"{__doc__} {_LIFECYCLE_NOTE}",
        state_verbs=verbs,
    )
    parser.add_argument("--project", type=Path, default=workflow_project_dir_from_env(), help="project path")
    parser.add_argument("--type", default="task", help="workflow artifact type")
    subparsers = parser.add_subparsers(dest="verb", required=True)

    p_assign = subparsers.add_parser("assign", help="assign an issue to a user")
    p_assign.add_argument("issue", help="Jira issue key")
    p_assign.add_argument("user", help='Jira DC username or the literal "me"')

    p_unassign = subparsers.add_parser("unassign", help="clear the assignee")
    p_unassign.add_argument("issue", help="Jira issue key")

    p_set_type = subparsers.add_parser("set-type", help="set the Jira issuetype via the artifact mapping")
    p_set_type.add_argument("issue", help="Jira issue key")
    p_set_type.add_argument("new_type", metavar="type", help="workflow artifact type whose Jira issuetype to apply")

    for verb in verbs:
        sub = subparsers.add_parser(verb, help=f"apply the '{verb}' state transition")
        sub.add_argument("issue", help="Jira issue key")
        sub.add_argument("--comment", help="optional comment posted alongside the transition")

    return parser


def _discover_state_verbs(project: Path) -> list[str]:
    try:
        config = load_workflow_config(project)
    except WorkflowConfigError:
        return []
    if config is None or config.issues.kind != "jira":
        return []
    try:
        settings = _jira_issue_provider_settings(project)
    except Exception:
        return []
    raw = settings.get("state_transitions") or settings.get("stateTransitions")
    if not isinstance(raw, Mapping):
        return []
    verbs: list[str] = []
    for key, value in raw.items():
        verb = str(key).strip()
        if not verb or verb in _RESERVED_VERBS:
            continue
        text = str(value).strip() if value is not None else ""
        if not text:
            continue
        verbs.append(verb)
    return sorted(set(verbs))


def fields_payload(
    *,
    project: Path,
    artifact_type: str,
    verb: str,
    issue: str,
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

    if verb not in _RESERVED_VERBS:
        if comment:
            payload: dict[str, Any] = {
                "issue": issue_key,
                "freshness_check": True,
                "body": comment,
                "state": verb,
            }
            operation = "add_comment"
        else:
            payload = {"issue": issue_key, "freshness_check": True, "state": verb}
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
        return flatten_provider_envelope(response.payload, project=config.root)

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
    return flatten_provider_envelope(response.payload, project=config.root)


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
    base_args, _ = build_base_parser().parse_known_args(argv)
    project = base_args.project or workflow_project_dir_from_env()
    state_verbs = _discover_state_verbs(project)
    parser = build_parser(state_verbs)
    args = parser.parse_args(argv)
    output = stdout or sys.stdout
    errors = stderr or sys.stderr

    try:
        payload = fields_payload(
            project=args.project,
            artifact_type=args.type,
            verb=args.verb,
            issue=args.issue,
            comment=getattr(args, "comment", None),
            user=getattr(args, "user", None),
            new_type=getattr(args, "new_type", None),
            runner=runner,
        )
    except Exception as exc:
        print(f"Jira issue fields error: {exc}", file=errors)
        return 2

    print(json.dumps(payload, indent=2, sort_keys=False), file=output)
    if payload.get("status") == "blocked":
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
