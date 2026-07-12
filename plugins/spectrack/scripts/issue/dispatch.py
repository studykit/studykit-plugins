#!/usr/bin/env python3
"""Unified issue dispatch core.

Every workflow issue operation routes through :func:`main`, the verb
router invoked by the ``issue`` package entry point (``issue/__main__.py``,
run by the ``spectrack`` launcher). The shared,
provider-agnostic dispatch boilerplate — load ``.spectrack/config.yml``,
resolve the backend for ``providers.issues.kind``, assemble the argparse
surface, and execute the intent — lives once in :func:`run_intent`.
Per-provider behavior lives in :mod:`issue.github` and :mod:`issue.jira`
and is reached through :func:`issue.backend.get_backend`.

Verb mapping
------------

==============================  =======================================
``issue <verb>``                Intent / translated argv
==============================  =======================================
``new ...``                     ``DRAFTS`` with ``["publish", ...]``
``update ...``                  ``WRITEBACK`` with ``["update", ...]``
``fetch ...``                   ``FETCH`` with ``[...]``
``search ...``                  ``SEARCH`` with ``[...]``
``comment ...``                 ``COMMENTS`` with ``["append", ...]`` for legacy calls,
                                or ``["append"|"update"|"resume", ...]`` when explicit
``resume ...``                  ``RESUME`` with ``[...]``
``history ...``                 ``HISTORY`` with ``[...]`` (GitHub only)
``attach ...``                  ``ATTACH`` with ``[...]`` (Jira only)
``link ...``                    ``RELATIONSHIPS`` with ``[...]``
``labels ...``                  ``LABELS`` with ``[...]`` (GitHub only)
``state <ref> <target> [opts]`` ``FIELDS`` with ``[<target>, <ref>, ...]``
``assign <ref> <user>``         ``FIELDS`` with ``["assign", <ref>, <user>]``
``unassign <ref>``              ``FIELDS`` with ``["unassign", <ref>]``
``set-type <ref> <type>``       ``FIELDS`` with ``["set-type", <ref>, <type>]``
==============================  =======================================

Pass ``--help`` after any verb to surface the active backend's option
surface for that intent.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import TextIO

from command import CommandRunner
from config import WorkflowConfigError, load_workflow_config
from env import workflow_project_dir_from_env

from issue.backend import IssueBackendError, get_backend


@dataclass(frozen=True)
class IntentSpec:
    """Declarative binding from an issue intent to its backend methods.

    ``add_args`` / ``run`` name the ``add_<intent>_args`` /
    ``run_<intent>`` pair on the resolved :class:`issue.backend.IssueBackend`
    driver. ``label`` is the error-message prefix surfaced on a clean
    failure. The two flags capture the only per-intent deviations from the
    shared dispatch path:

    - ``require_jira`` — the intent exists only on the Jira backend, so a
      non-Jira provider is refused and the backend is resolved as ``jira``.
    - ``state_verbs`` — ``add_args`` accepts a ``state_verbs`` keyword (the
      Jira backend's configured lifecycle transitions); discovered and
      passed only when the active backend opts in.
    """

    label: str
    add_args: str
    run: str
    require_jira: bool = False
    state_verbs: bool = False


FETCH = IntentSpec("issue fetch", "add_fetch_args", "run_fetch")
SEARCH = IntentSpec("issue search", "add_search_args", "run_search")
COMMENTS = IntentSpec("issue comment", "add_comments_args", "run_comments")
RESUME = IntentSpec("issue resume", "add_resume_args", "run_resume")
HISTORY = IntentSpec("issue history", "add_history_args", "run_history")
DRAFTS = IntentSpec("issue draft", "add_drafts_args", "run_drafts")
WRITEBACK = IntentSpec("issue update", "add_writeback_args", "run_writeback")
RELATIONSHIPS = IntentSpec(
    "issue relationship", "add_relationships_args", "run_relationships"
)
FIELDS = IntentSpec("issue fields", "add_fields_args", "run_fields", state_verbs=True)
ATTACH = IntentSpec("issue attach", "add_attach_args", "run_attach", require_jira=True)
LABELS = IntentSpec("issue labels", "add_labels_args", "run_labels")


def run_intent(
    spec: IntentSpec,
    argv: list[str] | None = None,
    *,
    stdout: TextIO | None = None,
    stderr: TextIO | None = None,
    runner: CommandRunner | None = None,
) -> int:
    """Run a single issue intent against the configured backend.

    Resolves the project from ``--project`` (or the workflow env default),
    loads the config, selects the backend, lets the backend register its
    intent options on a shared parser, and dispatches to the backend's
    ``run_<intent>`` driver. Returns the process exit code.
    """

    out = stdout or sys.stdout
    err = stderr or sys.stderr

    base_parser = argparse.ArgumentParser(add_help=False)
    base_parser.add_argument(
        "--project",
        type=Path,
        default=workflow_project_dir_from_env(),
    )
    base_known, _ = base_parser.parse_known_args(argv)
    project = base_known.project or workflow_project_dir_from_env()

    try:
        config = load_workflow_config(project)
    except WorkflowConfigError as exc:
        print(f"{spec.label} error: {exc}", file=err)
        return 2
    if config is None:
        print(
            f"{spec.label} error: .spectrack/config.yml was not found "
            "(run `setup.py build-config` to configure first)",
            file=err,
        )
        return 2

    if spec.require_jira and config.issues.kind != "jira":
        print(
            f"{spec.label} error: attachments are only supported by the Jira "
            f"issue provider (configured provider: {config.issues.kind})",
            file=err,
        )
        return 2

    try:
        backend = get_backend("jira" if spec.require_jira else config.issues.kind)
    except IssueBackendError as exc:
        print(f"{spec.label} error: {exc}", file=err)
        return 2

    # Some intents are provider-scoped (e.g. `labels` is GitHub-only). When the
    # active backend does not implement the intent, refuse cleanly rather than
    # raising an AttributeError.
    if not hasattr(backend, spec.add_args) or not hasattr(backend, spec.run):
        print(
            f"{spec.label} error: the {config.issues.kind} issue provider does "
            "not support this command",
            file=err,
        )
        return 2

    parser = argparse.ArgumentParser(prog="issue")
    parser.add_argument(
        "--project",
        type=Path,
        default=workflow_project_dir_from_env(),
        help="project path",
    )
    add_args = getattr(backend, spec.add_args)
    # The Jira backend's fields parser accepts dynamic state-transition verbs
    # via a keyword argument; the GitHub backend does not. Pass them only when
    # the active backend opts in, keeping the call generic.
    if (
        spec.state_verbs
        and getattr(backend, "kind", "") == "jira"
        and hasattr(backend, "discover_state_verbs")
    ):
        add_args(parser, state_verbs=backend.discover_state_verbs(config))
    else:
        add_args(parser)
    args = parser.parse_args(argv)

    return getattr(backend, spec.run)(
        args,
        config=config,
        runner=runner,
        stdout=out,
        stderr=err,
    )


# (verb, one-line description, only). ``only`` scopes the verb to a single
# provider in `issue --help`: None lists it for every provider, "jira" or
# "github" list it only when the configured provider matches.
_VERB_HELP: tuple[tuple[str, str, str | None], ...] = (
    ("new", "create a new issue", None),
    ("update", "update title / body / labels / state", None),
    ("fetch", "fetch one or more issues into the cache", None),
    ("search", "search issues with the backend's native query", None),
    ("comment", "append / update / resume (upsert Resume) a comment from a body file", None),
    ("resume", "find the current Resume comment for an issue", None),
    ("history", "show issue body or comment edit history", "github"),
    ("attach", "add/get issue file attachments", "jira"),
    ("link", "add / remove / replace relationships", None),
    ("labels", "list configured issue-type labels", "github"),
    ("state", "change lifecycle state (e.g. `state <ref> close`)", None),
    ("assign", "assign an issue to a user (e.g. `assign <ref> me`)", None),
    ("unassign", "clear all assignees (e.g. `unassign <ref>`)", None),
    ("set-type", "swap the workflow type label (e.g. `set-type <ref> bug`)", None),
)

_VERBS = tuple(name for name, _desc, _only in _VERB_HELP)


def _build_usage(provider: str | None) -> str:
    rows = [
        (name, desc)
        for name, desc, only in _VERB_HELP
        if only is None or provider == only
    ]
    width = max(len(name) for name, _desc in rows)
    verb_lines = "".join(f"  {name.ljust(width)}   {desc}\n" for name, desc in rows)
    return (
        "usage: issue <verb> [args...]\n"
        "\n"
        "verbs:\n"
        f"{verb_lines}"
        "\n"
        "Run `issue <verb> --help` for each verb's usage.\n"
    )


def _active_provider(argv: list[str]) -> str | None:
    """Resolve the configured issue provider kind for usage filtering.

    Returns ``None`` when the project or config cannot be resolved, in which
    case the usage falls back to the provider-neutral verb set.
    """

    base = argparse.ArgumentParser(add_help=False)
    base.add_argument("--project", type=Path, default=None)
    try:
        known, _ = base.parse_known_args(argv)
    except SystemExit:
        return None
    project = known.project or workflow_project_dir_from_env()
    try:
        config = load_workflow_config(project)
    except Exception:
        return None
    if config is None:
        return None
    kind = getattr(getattr(config, "issues", None), "kind", None)
    return str(kind).strip().lower() if kind else None


def _print_usage(stream: TextIO, provider: str | None = None) -> None:
    stream.write(_build_usage(provider))


def main(
    argv: list[str] | None = None,
    *,
    stdout: TextIO | None = None,
    stderr: TextIO | None = None,
    runner: CommandRunner | None = None,
) -> int:
    out = stdout or sys.stdout
    err = stderr or sys.stderr
    args = list(sys.argv[1:] if argv is None else argv)

    if not args or args[0] in {"-h", "--help"}:
        _print_usage(out, _active_provider(args))
        return 0 if args else 2

    verb, rest = args[0], args[1:]

    if verb not in _VERBS:
        err.write(f"issue: unknown verb '{verb}'\n\n")
        _print_usage(err, _active_provider(args))
        return 2

    kwargs = {"stdout": out, "stderr": err, "runner": runner}

    if verb == "new":
        return run_intent(DRAFTS, ["publish", *rest], **kwargs)
    if verb == "update":
        return run_intent(WRITEBACK, ["update", *rest], **kwargs)
    if verb == "fetch":
        return run_intent(FETCH, rest, **kwargs)
    if verb == "search":
        return run_intent(SEARCH, rest, **kwargs)
    if verb == "comment":
        if rest and rest[0] in {"append", "update", "resume"}:
            return run_intent(COMMENTS, rest, **kwargs)
        return run_intent(COMMENTS, ["append", *rest], **kwargs)
    if verb == "resume":
        return run_intent(RESUME, rest, **kwargs)
    if verb == "history":
        return run_intent(HISTORY, rest, **kwargs)
    if verb == "attach":
        return run_intent(ATTACH, rest, **kwargs)
    if verb == "link":
        return run_intent(RELATIONSHIPS, rest, **kwargs)
    if verb == "labels":
        return run_intent(LABELS, rest, **kwargs)
    if verb == "state":
        return _run_state(rest, kwargs=kwargs, stderr=err)
    if verb in {"assign", "unassign", "set-type"}:
        return run_intent(FIELDS, [verb, *rest], **kwargs)

    raise AssertionError(f"unreachable verb dispatch: {verb}")


def _run_state(rest: list[str], *, kwargs: dict, stderr: TextIO) -> int:
    """Translate ``state <ref> <target> [opts]`` into fields-intent argv.

    ``--help`` for the ``state`` verb is forwarded to the fields intent so
    the active backend's full set of lifecycle subparsers (``close``,
    ``reopen``, configured Jira state-transition verbs) is surfaced.
    """
    if rest and rest[0] in {"-h", "--help"}:
        return run_intent(FIELDS, ["--help"], **kwargs)
    if len(rest) < 2:
        stderr.write(
            "issue state: expected `<issue-ref> <target>` "
            "(e.g. `issue state 123 close`).\n"
            "Run `issue state --help` to see configured lifecycle verbs.\n"
        )
        return 2
    ref, target, *opts = rest
    return run_intent(FIELDS, [target, ref, *opts], **kwargs)
