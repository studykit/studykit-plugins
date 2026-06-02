#!/usr/bin/env python3
# /// script
# dependencies = ["python-frontmatter", "PyYAML"]
# ///
"""Unified issue dispatcher.

Single entry point for every workflow issue operation. Each subcommand
imports the matching module from :mod:`issue.legacy` and calls its
``main(argv)`` with a translated argument vector; the heavy lifting still
lives in the per-intent legacy modules. The verb table below is the
public surface that callers (skills, agents, hook-injected context)
should target — direct ``workflow issue_*.py`` invocations are no longer
documented.

Verb mapping
------------

==============================  =======================================
``issue.py <verb>``             Legacy entry point
==============================  =======================================
``new ...``                     ``issue_new.main(["publish", ...])``
``update ...``                  ``issue_update.main(["update", ...])``
``fetch ...``                   ``issue_fetch.main([...])``
``comment ...``                 ``issue_comments.main(["append", ...])``
``link ...``                    ``issue_link.main([...])``
``state <ref> <target> [opts]`` ``issue_fields.main([<target>, <ref>, ...])``
``assign <ref> <user>``         ``issue_fields.main(["assign", <ref>, <user>])``
``unassign <ref>``              ``issue_fields.main(["unassign", <ref>])``
``set-type <ref> <type>``       ``issue_fields.main(["set-type", <ref>, <type>])``
==============================  =======================================

Pass ``--help`` after any verb to surface the active backend's option
surface for that intent.
"""

from __future__ import annotations

import sys
from typing import TextIO

from workflow_command import CommandRunner

from issue.legacy import (
    issue_attach,
    issue_comments,
    issue_new,
    issue_fetch,
    issue_fields,
    issue_link,
    issue_update,
)


_VERBS = (
    "new",
    "update",
    "fetch",
    "comment",
    "attach",
    "link",
    "state",
    "assign",
    "unassign",
    "set-type",
)


_USAGE = (
    "usage: issue.py <verb> [args...]\n"
    "\n"
    "verbs:\n"
    "  new        create a new issue (legacy: issue_new publish)\n"
    "  update     update title / body / labels / state (legacy: issue_update update)\n"
    "  fetch      fetch one or more issues into the cache (legacy: issue_fetch)\n"
    "  comment    append a comment from a body file (legacy: issue_comments append)\n"
    "  attach     attach local file(s) to an issue (Jira provider only)\n"
    "  link       add / remove / replace relationships (legacy: issue_link)\n"
    "  state      change lifecycle state (e.g. `state <ref> close`)\n"
    "  assign     assign an issue to a user (e.g. `assign <ref> me`)\n"
    "  unassign   clear all assignees (e.g. `unassign <ref>`)\n"
    "  set-type   swap the workflow type label (e.g. `set-type <ref> bug`)\n"
    "\n"
    "Run `issue.py <verb> --help` to see backend-specific options.\n"
)


def _print_usage(stream: TextIO) -> None:
    stream.write(_USAGE)


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
        _print_usage(out)
        return 0 if args else 2

    verb, rest = args[0], args[1:]

    if verb not in _VERBS:
        err.write(f"issue.py: unknown verb '{verb}'\n\n")
        _print_usage(err)
        return 2

    kwargs = {"stdout": out, "stderr": err, "runner": runner}

    if verb == "new":
        return issue_new.main(["publish", *rest], **kwargs)
    if verb == "update":
        return issue_update.main(["update", *rest], **kwargs)
    if verb == "fetch":
        return issue_fetch.main(rest, **kwargs)
    if verb == "comment":
        return issue_comments.main(["append", *rest], **kwargs)
    if verb == "attach":
        return issue_attach.main(rest, **kwargs)
    if verb == "link":
        return issue_link.main(rest, **kwargs)
    if verb == "state":
        return _run_state(rest, kwargs=kwargs, stderr=err)
    if verb in {"assign", "unassign", "set-type"}:
        return issue_fields.main([verb, *rest], **kwargs)

    raise AssertionError(f"unreachable verb dispatch: {verb}")


def _run_state(rest: list[str], *, kwargs: dict, stderr: TextIO) -> int:
    """Translate ``state <ref> <target> [opts]`` into legacy field argv.

    ``--help`` for the ``state`` verb is forwarded to the legacy fields
    module so the active backend's full set of lifecycle subparsers
    (``close``, ``reopen``, configured Jira state-transition verbs) is
    surfaced via ``issue_fields.main(["--help"])``.
    """
    if rest and rest[0] in {"-h", "--help"}:
        return issue_fields.main(["--help"], **kwargs)
    if len(rest) < 2:
        stderr.write(
            "issue.py state: expected `<issue-ref> <target>` "
            "(e.g. `issue.py state 123 close`).\n"
            "Run `issue.py state --help` to see configured lifecycle verbs.\n"
        )
        return 2
    ref, target, *opts = rest
    return issue_fields.main([target, ref, *opts], **kwargs)


if __name__ == "__main__":
    raise SystemExit(main())
