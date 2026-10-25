#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""File rule, queue, and adapter regressions; not a host hook-delivery test."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


PLUGIN = Path(__file__).resolve().parents[1]
CLI = PLUGIN / "scripts/guard_hook.py"
CODEX_HOOK = PLUGIN / "hooks/scripts/hook_codex.py"


def rule(pattern, name, kind="agent"):
    return {"glob": pattern, "action": {"kind": kind, "name": name}}


class FileReviewTests(unittest.TestCase):
    def test_codex_stop_refreshes_sidebar_after_mcp_completion_without_herdr_env(self):
        self.configure("codex", [rule("main.py", "reviewer")])
        calls = self.project / "herdr-calls.jsonl"
        binary = self.project / "herdr-probe"
        binary.write_text(f"#!{sys.executable}\nimport json,sys\n"
                          f"with open({str(calls)!r}, 'a') as stream:\n"
                          "    stream.write(json.dumps(sys.argv[1:]) + '\\n')\n")
        binary.chmod(0o755)
        presentation = {"HERDR_ENV": "1", "HERDR_PANE_ID": "fixture:p1", "HERDR_BIN_PATH": str(binary)}
        self.env.update(presentation)
        self.record("codex", self.write("main.py"))
        checkpoint = self.checkpoint("codex", "show")
        self.assertIn("guard_pending=Guard · 1 pending", json.loads(calls.read_text().splitlines()[-1]))
        for key in presentation:
            self.env.pop(key)
        before = calls.read_text()
        self.assertEqual(self.checkpoint("codex", "complete", checkpoint["token"]),
                         {"cleared": 1, "remaining": 0})
        self.assertEqual(calls.read_text(), before)
        self.env.update(presentation)
        self.event("codex", "Stop")
        self.assertEqual(json.loads(calls.read_text().splitlines()[-1])[-2:],
                         ["--clear-token", "guard_pending"])

    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="guard-file-review-")
        self.addCleanup(temporary.cleanup)
        self.project = Path(temporary.name).resolve()
        self.env = {key: value for key, value in os.environ.items()
                    if not key.startswith(("GUARD_", "CLAUDE_", "CODEX_", "HERDR_"))}
        self.env.update(PYTHONDONTWRITEBYTECODE="1", GUARD_TRACE="1",
                        GUARD_PROJECT_DIR=str(self.project),
                        CLAUDE_PROJECT_DIR=str(self.project), GUARD_SETTINGS_SKILL="1")

    def configure(self, host, rules=None, **extra):
        path = self.project / f".{host}/guard.local.json"
        path.parent.mkdir(exist_ok=True)
        value = dict(extra)
        if rules is not None:
            value["file_review_rules"] = rules
        path.write_text(json.dumps(value))
        return path

    def write(self, name, content="changed\n"):
        path = self.project / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        return path

    def run_script(self, host, script, args=(), payload=None):
        result = subprocess.run(
            [sys.executable, str(script), *args], cwd=self.project,
            env=dict(self.env, GUARD_HOST=host), input=json.dumps(payload or {}),
            text=True, capture_output=True, timeout=15)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        trace = self.project / f".{host}/guard/trace.log"
        if trace.exists():
            self.assertNotIn('"exception"', trace.read_text())
        return result

    def cli(self, host, *args):
        return self.run_script(host, CLI, args)

    def event(self, host, event, tool="Write", inputs=None, turn="turn-1"):
        payload = {"session_id": "session", "prompt_id": turn, "turn_id": turn,
                   "cwd": str(self.project), "hook_event_name": event,
                   "tool_name": tool, "tool_input": inputs or {}, "tool_response": {},
                   "tool_use_id": "write-call"}
        if host == "codex":
            return self.run_script(host, CODEX_HOOK, payload=payload)
        verb = {"PostToolUse": "post-edit", "PreToolUse": "pre-search",
                "UserPromptSubmit": "prompt", "Stop": "stop"}[event]
        return self.run_script(host, CLI, [verb], payload)

    def record(self, host, path, turn="turn-1"):
        if host == "codex":
            self.event(host, "UserPromptSubmit", turn=turn)
        return self.event(host, "PostToolUse", inputs={"file_path": str(path)}, turn=turn)

    def checkpoint(self, host, *args):
        return json.loads(self.cli(host, "file-checkpoint", *args,
                                   "--session", "session", "--host", host).stdout)

    def test_rules_route_any_file_type_without_switches_on_both_hosts(self):
        paths = {name: self.write(name) for name in
                 ("main.py", "src/deep/main.py", "config.json", "Makefile", "guide.md", "skip.txt")}
        for host in ("claude", "codex"):
            self.configure(host, [rule("**/*.py", "source-review"),
                                  rule("**/*.json", "config-review", "skill"),
                                  rule("Makefile", "build-review", "skill"),
                                  rule("**/*.md", "project-doc-review")],
                           **{"comment-corrector": "off", "doc-auditor": "off"})
            for path in paths.values():
                self.record(host, path)
            result = self.checkpoint(host, "show")
            actual = {Path(path).relative_to(self.project).as_posix(): (g["kind"], g["name"])
                      for g in result["groups"] for path in g["paths"]}
            self.assertEqual(actual, {
                "main.py": ("agent", "source-review"),
                "src/deep/main.py": ("agent", "source-review"),
                "config.json": ("skill", "config-review"),
                "Makefile": ("skill", "build-review"),
                "guide.md": ("agent", "project-doc-review")})
            self.assertTrue(all(not g["conditional"] for g in result["groups"]))

    def test_specificity_and_exclusions_apply_before_dispatch(self):
        for host in ("claude", "codex"):
            self.configure(host, [rule("docs/**", "broad"), rule("docs/**/*.md", "docs"),
                                  rule("**/AGENTS.md", "instructions"),
                                  rule("docs/a.py", "first"), rule("docs/a.py", "second")],
                           files_exclude=["docs/generated/**", "**/draft.md"])
            for name in ("docs/AGENTS.md", "docs/deep/a.md", "docs/a.py",
                         "docs/generated/a.py", "docs/generated/a.md", "docs/draft.md"):
                self.record(host, self.write(name))
            groups = self.checkpoint(host, "show")["groups"]
            self.assertEqual({g["name"] for g in groups}, {"instructions", "docs", "first"})
            self.assertEqual(sum(len(g["paths"]) for g in groups), 3)

    def test_old_rules_and_switches_are_silently_ignored(self):
        for host in ("claude", "codex"):
            self.configure(host, doc_review_rules=[rule("**", "old-review")],
                           **{"comment-corrector": "on", "doc-auditor": "on"})
            for name in ("guide.md", "main.py"):
                self.record(host, self.write(name))
            self.assertEqual(self.checkpoint(host, "show")["files"], {})
            shown = self.cli(host, "settings", "show").stdout
            self.assertIn("file_review_rules: (none)", shown)
            self.assertNotIn("doc_review_rules", shown)
            self.assertNotIn("migrat", shown)

    def test_exclusions_apply_to_every_file_type_and_negation_is_ordered(self):
        names = ("sources/Main.java", "sources/README.md", "sources/config.json",
                 "sources/Makefile", "sources/src/Keep.java", "sources/src/Drop.java",
                 "sources/keep.md", "sources/no-review.txt", "outside.py")
        for host in ("claude", "codex"):
            self.configure(host, [rule("**/*.java", "comments"), rule("**/*.md", "docs"),
                                  rule("**/*.json", "config"), rule("**/Makefile", "build"),
                                  rule("**/*.py", "python")],
                           files_exclude=["sources/**", "!sources/src/**/*.java",
                                          "sources/src/Drop.java", "!sources/keep.md",
                                          "!sources/no-review.txt"])
            for name in names:
                self.record(host, self.write(name))
            result = self.checkpoint(host, "show")
            relative = {Path(path).relative_to(self.project).as_posix() for path in result["files"]}
            self.assertEqual(relative, {"sources/src/Keep.java", "sources/keep.md", "outside.py"})
            # Changing exclusion order must reconcile already queued files as well.
            self.cli(host, "settings", "set", "files_exclude",
                     "!sources/src/**/*.java,sources/**", "--session", "session")
            result = self.checkpoint(host, "show")
            self.assertEqual(set(result["files"]), {str(self.project / "outside.py")})

    def test_only_plural_exclusion_key_is_used(self):
        for host in ("claude", "codex"):
            config = self.configure(host, [rule("**", "review")],
                                    doc_exclude=["**"], file_exclude=["**"])
            for name in ("main.py", "guide.md", "config.json", "Makefile"):
                self.record(host, self.write(name))
            self.assertEqual(len(self.checkpoint(host, "show")["files"]), 4)
            self.cli(host, "settings", "set", "files_exclude", "**,!**/*.py",
                     "--session", "session")
            self.assertEqual(json.loads(config.read_text())["files_exclude"], ["**", "!**/*.py"])
            self.assertEqual(set(self.checkpoint(host, "show")["files"]),
                             {str(self.project / "main.py")})
            shown = self.cli(host, "settings", "show").stdout
            self.assertNotIn("doc_exclude", shown)
            self.assertNotIn("file_exclude:", shown)

    def test_literal_bang_and_empty_negation_do_not_restore_other_files(self):
        for host in ("claude", "codex"):
            self.configure(host, [rule("**/*.py", "review")],
                           files_exclude=["\\!skip.py", "!", ""])
            for name in ("!skip.py", "keep.py"):
                self.record(host, self.write(name))
            self.assertEqual(set(self.checkpoint(host, "show")["files"]),
                             {str(self.project / "keep.py")})

    def test_settings_reconcile_existing_queue_and_reject_invalid_rules(self):
        for host in ("claude", "codex"):
            config = self.configure(host, [rule("**", "all")])
            for name in ("main.py", "guide.md"):
                self.record(host, self.write(name))
            new_rules = [rule("**/*.py", "new-source", "skill")]
            result = self.cli(host, "settings", "set", "file_review_rules",
                              json.dumps(new_rules), "--session", "session")
            self.assertEqual(result.stderr, "")
            groups = self.checkpoint(host, "show")["groups"]
            self.assertEqual([g["name"] for g in groups], ["new-source"])
            before = config.read_bytes()
            for invalid in ([rule("**", "guard:audit-files", "skill")],
                            [{"glob": "**", "action": None}], "wrong-type"):
                result = self.cli(host, "settings", "set", "file_review_rules", json.dumps(invalid))
                self.assertIn("must be a JSON list", result.stderr)
                self.assertEqual(config.read_bytes(), before)
            self.cli(host, "settings", "set", "file_review_rules", "[]", "--session", "session")
            self.assertEqual(self.checkpoint(host, "show")["files"], {})

    def test_completion_preserves_later_edits_and_clear_invalidates_tokens(self):
        for host in ("claude", "codex"):
            self.configure(host, [rule("**/*.py", "source")])
            path = self.write("main.py", "before\n")
            self.record(host, path)
            initial = self.checkpoint(host, "show")
            path.write_text("after\n")
            self.record(host, path, turn="turn-2")
            self.assertEqual(self.checkpoint(host, "complete", initial["token"])["remaining"], 1)
            current = self.checkpoint(host, "show")
            self.assertEqual(self.checkpoint(host, "complete", current["token"])["remaining"], 0)
            self.record(host, path)
            token = self.checkpoint(host, "show")["token"]
            self.checkpoint(host, "clear")
            result = subprocess.run([sys.executable, str(CLI), "file-checkpoint", "complete", token,
                                     "--session", "session", "--host", host],
                                    cwd=self.project, env=dict(self.env, GUARD_HOST=host),
                                    text=True, capture_output=True)
            self.assertNotEqual(result.returncode, 0)

    def test_shell_writes_record_custom_extensions_without_blocking(self):
        subprocess.run(["git", "init", "-q", str(self.project)], check=True)
        for host in ("claude", "codex"):
            self.configure(host, [rule("**/*.json", "json-review", "skill")],
                           files_exclude=["**", "!settings.json"])
            shell = "Bash"  # Both hosts normalize shell hook events to this name.
            target = self.write("settings.json", "before\n")
            self.event(host, "UserPromptSubmit")
            self.event(host, "PreToolUse", shell, {"command": "write files"})
            target.write_text("after\n")
            # An unindexed Markdown file under `wiki/ref/` is an ordinary write now.
            self.write("wiki/ref/page.md", "External page\n")
            result = self.event(host, "PostToolUse", shell, {"command": "write files"})
            self.assertEqual(result.stdout, "")
            groups = self.checkpoint(host, "show")["groups"]
            self.assertEqual([g["name"] for g in groups], ["json-review"])
            self.assertTrue(groups[0]["conditional"])
            (self.project / "wiki/ref/page.md").unlink()

    def test_codex_native_apply_patch_command_records_add_and_move_destinations(self):
        self.configure("codex", [rule("**/*.py", "project-source-review")])
        added = self.write("added.py")
        moved = self.write("nested/moved.py")
        patch = ("*** Begin Patch\n*** Add File: added.py\n+changed\n"
                 "*** Update File: original.py\n*** Move to: nested/moved.py\n"
                 "@@\n-before\n+after\n*** End Patch")
        self.event("codex", "UserPromptSubmit")
        self.event("codex", "PostToolUse", "apply_patch", {"command": patch})
        groups = self.checkpoint("codex", "show")["groups"]
        self.assertEqual(len(groups), 1)
        self.assertEqual(set(groups[0]["paths"]), {str(added), str(moved)})
        self.assertEqual(groups[0]["name"], "project-source-review")
        self.assertFalse(groups[0]["conditional"])

    def test_codex_shell_command_containing_patch_text_keeps_conditional_provenance(self):
        subprocess.run(["git", "init", "-q", str(self.project)], check=True)
        self.configure("codex", [rule("**/*.py", "project-source-review")])
        target = self.write("shell.py", "before\n")
        patch_text = "*** Begin Patch\n*** Update File: shell.py\n@@\n-before\n+after\n*** End Patch"
        self.event("codex", "UserPromptSubmit")
        self.event("codex", "PreToolUse", "Bash", {"command": patch_text})
        target.write_text("after\n")
        self.event("codex", "PostToolUse", "Bash", {"command": patch_text})
        groups = self.checkpoint("codex", "show")["groups"]
        self.assertEqual(len(groups), 1)
        self.assertEqual(groups[0]["paths"], [str(target)])
        self.assertTrue(groups[0]["conditional"])


if __name__ == "__main__":
    unittest.main()
