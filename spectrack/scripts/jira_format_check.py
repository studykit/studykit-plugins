#!/usr/bin/env python3
"""Report mechanically detectable Jira wiki-markup hazards in one draft file."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

_CJK = r"\u3400-\u4dbf\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7a3"
_RULES: tuple[tuple[str, str, re.Pattern[str], str], ...] = (
    ("markdown-heading", "error", re.compile(r"^\s{0,3}#{2,6}\s+"), "Markdown heading; use hN. heading"),
    ("markdown-numbered-list", "error", re.compile(r"^\s*\d+\.\s+"), "Markdown numbered list; use # item"),
    ("markdown-task-list", "error", re.compile(r"^\s*[-*+]\s+\[[ xX]\]\s+"), "Markdown task list; use Jira task-list markup"),
    ("markdown-quote", "error", re.compile(r"^\s*>\s?"), "Markdown quote; use bq. or {quote}"),
    ("markdown-table-separator", "error", re.compile(r"^\s*\|?\s*:?-{3,}"), "Markdown table separator; use Jira table rows"),
    ("markdown-link", "error", re.compile(r"(?<!\\)\[[^]\n]+\]\([^\s)]+\)"), "Markdown link; use [label|url]"),
    ("markdown-bold", "error", re.compile(r"(?<!\\)\*\*[^*\n]+\*\*"), "Markdown bold; use *bold*"),
    ("markdown-inline-code", "error", re.compile(r"(?<!\\)`[^`\n]+`"), "Markdown inline code; use {{text}}"),
)
_FENCE = re.compile(r"^\s*```")
_JIRA_CODE_START = re.compile(r"^\s*\{(?:code|noformat)(?::[^}]*)?\}\s*$", re.IGNORECASE)
_JIRA_CODE_END = re.compile(r"^\s*\{(?:code|noformat)\}\s*$", re.IGNORECASE)
_CJK_BEFORE_MONOSPACE = re.compile(rf"[{_CJK}]\{{\{{")
_CJK_AFTER_MONOSPACE = re.compile(rf"\}}\}}[{_CJK}]")
_STRIKETHROUGH_RISK = re.compile(r"(?<![\\\w])-\S(?:[^\s]*\S)?-(?!\w)")


def scan_text(text: str) -> list[dict[str, Any]]:
    """Return findings with stable codes and one-based line numbers.

    The checker deliberately reports only syntax patterns that are objective or
    known rendering hazards. It does not decide whether ambiguous prose should
    be rewritten; the format-corrector agent retains that responsibility.
    """

    findings: list[dict[str, Any]] = []
    in_fenced_block = False
    in_jira_code_block = False
    for line_number, line in enumerate(text.splitlines(), start=1):
        if _FENCE.match(line):
            findings.append(_finding("markdown-fenced-code", "error", line_number, "Markdown fence; use {code}...{code}"))
            in_fenced_block = not in_fenced_block
            continue
        if in_fenced_block:
            continue
        if in_jira_code_block:
            if _JIRA_CODE_END.match(line):
                in_jira_code_block = False
            continue
        if _JIRA_CODE_START.match(line):
            in_jira_code_block = True
            continue

        matched_codes: set[str] = set()
        for code, severity, pattern, message in _RULES:
            if pattern.search(line):
                findings.append(_finding(code, severity, line_number, message))
                matched_codes.add(code)
        if _CJK_BEFORE_MONOSPACE.search(line) or _CJK_AFTER_MONOSPACE.search(line):
            findings.append(_finding("cjk-monospace-spacing", "warning", line_number, "CJK text touches {{...}}; add spacing outside the delimiters"))
        if "markdown-table-separator" not in matched_codes and _STRIKETHROUGH_RISK.search(line):
            findings.append(_finding("jira-strikethrough-risk", "warning", line_number, "outer-edge hyphen may render as strikethrough; inspect and escape when needed"))
    return findings


def _finding(code: str, severity: str, line: int, message: str) -> dict[str, Any]:
    return {"code": code, "severity": severity, "line": line, "message": message}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("draft", type=Path, help="absolute or relative path to one Jira draft file")
    args = parser.parse_args(argv)
    try:
        text = args.draft.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"jira format check error: {exc}", file=sys.stderr)
        return 2
    findings = scan_text(text)
    print(json.dumps({"path": str(args.draft.resolve()), "findings": findings}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
