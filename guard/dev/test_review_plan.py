#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Cross-host CLI contracts for the explicit plan-review entry.

Run: uv run --script guard/dev/test_review_plan.py
"""

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


PLUGIN = Path(__file__).resolve().parents[1]
SCRIPT = PLUGIN / "skills" / "audit-plan" / "scripts" / "review.py"


class PlanReviewEntryTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix="guard-audit-plan-")
        self.addCleanup(temp.cleanup)
        self.project = Path(temp.name)
        self.plan = self.project / "plan with spaces.md"
        self.plan.write_text("Implement the requested change\n", encoding="utf-8")
        self.env = {k: v for k, v in os.environ.items()
                    if not k.startswith(("GUARD_", "CLAUDE_", "CODEX_", "HERDR_"))}
        self.env["PYTHONDONTWRITEBYTECODE"] = "1"

    def configure(self, host, action=None, **settings):
        path = self.project / f".{host}" / "guard.local.json"
        path.parent.mkdir(exist_ok=True)
        path.write_text(json.dumps({"plan_review": action or {}, **settings}))

    def state_path(self, host, session="parent-session"):
        return self.project / f".{host}" / "guard" / "state" / f"{session}.json"

    def call(self, host, action="prepare", *, session="parent-session", plan=None, error=False):
        args = [sys.executable, str(SCRIPT), action, str(plan or self.plan),
                "--host", host, "--project", str(self.project)]
        if session is not None:
            args += ["--session", session]
        result = subprocess.run(args, cwd=self.project, env=self.env, capture_output=True,
                                text=True, timeout=15)
        self.assertEqual(result.returncode, 1 if error else 0, result.stdout + result.stderr)
        self.assertEqual(result.stderr, "")
        return json.loads(result.stdout)

    def test_unconfigured_review_does_not_dispatch_or_stamp(self):
        for host in ("claude", "codex"):
            with self.subTest(host=host):
                self.assertEqual(self.call(host)["status"], "no_reviewer")
                self.configure(host)
                self.assertEqual(self.call(host)["status"], "no_reviewer")
                self.assertFalse(self.state_path(host).exists())

    def test_each_host_selects_only_its_own_configured_agent_or_skill(self):
        for host in ("claude", "codex"):
            for kind in ("agent", "skill"):
                with self.subTest(host=host, kind=kind):
                    reviewer = {"kind": kind, "name": f"{host}-reviewer"}
                    self.configure(host, reviewer)
                    result = self.call(host, plan=Path(self.plan.name))
                    self.assertEqual(result["status"], "review")
                    self.assertEqual(result["reviewer"], reviewer)
                    self.assertEqual(result["plan_path"], str(self.plan.resolve()))
                    self.assertFalse(self.state_path(host).exists())

    def test_final_contents_are_recorded_and_do_not_overwrite_other_state(self):
        for host in ("claude", "codex"):
            with self.subTest(host=host):
                self.configure(host, {"kind": "agent", "name": "reviewer"})
                self.call(host)
                state_path = self.state_path(host)
                state_path.parent.mkdir(parents=True)
                state_path.write_text(json.dumps({"plan_audit_paused": True,
                                                 "edited_files": ["pending.py"]}))
                self.plan.write_text("Revised plan after review\n")
                result = self.call(host, "complete")
                digest = hashlib.sha256(b"Revised plan after review").hexdigest()
                self.assertEqual(result["status"], "recorded")
                self.assertEqual(result["sha256"], digest)
                state = json.loads(state_path.read_text())
                self.assertEqual(state["plan_audited_hash"], digest)
                self.assertTrue(state["plan_audit_paused"])
                self.assertEqual(state["edited_files"], ["pending.py"])
                # A direct request must not be suppressed by the stamp or automatic mute.
                self.assertEqual(self.call(host)["status"], "review")

    def test_explicit_review_ignores_automatic_gate_default(self):
        for host in ("claude", "codex"):
            self.configure(host, {"kind": "skill", "name": "reviewer"}, **{"audit-plan": "off"})
            self.assertEqual(self.call(host)["status"], "review")

    def test_invalid_or_recursive_reviewer_is_an_error(self):
        for host in ("claude", "codex"):
            for reviewer in ({"kind": "bad", "name": "reviewer"},
                             {"kind": "skill", "name": "guard:audit-plan"},
                             {"kind": "skill", "name": "audit-plan"}):
                self.configure(host, reviewer)
                self.assertEqual(self.call(host, error=True)["status"], "error")
                self.assertFalse(self.state_path(host).exists())

    def test_unreadable_or_empty_plan_never_gets_a_completion_record(self):
        for host in ("claude", "codex"):
            for content in ("", "  \n", None):
                if content is None:
                    self.plan.unlink()
                else:
                    self.plan.write_text(content)
                for action in ("prepare", "complete"):
                    self.assertEqual(self.call(host, action, error=True)["status"], "error")
                self.assertFalse(self.state_path(host).exists())

    def test_adapter_uses_selected_host_and_calling_session(self):
        self.env.update(CODEX_THREAD_ID="codex-parent", CLAUDE_CODE_SESSION_ID="claude-parent",
                        GUARD_HOST="wrong-host", GUARD_PROJECT_DIR="/invalid/inherited/project")
        for host in ("claude", "codex"):
            self.call(host, "complete", session=None)
            self.assertTrue(self.state_path(host, f"{host}-parent").exists())
            self.call(host, "complete", session="explicit-parent")
            self.assertTrue(self.state_path(host, "explicit-parent").exists())

    def test_missing_or_unsafe_session_fails_before_writing(self):
        for host in ("claude", "codex"):
            for session in (None, "../escape", ""):
                self.assertEqual(self.call(host, "complete", session=session, error=True)["status"], "error")
            self.assertFalse((self.project / f".{host}" / "guard").exists())

    def test_failed_state_write_is_reported(self):
        for host in ("claude", "codex"):
            folder = self.project / f".{host}"
            folder.mkdir()
            (folder / "guard").write_text("Not a directory")
            result = self.call(host, "complete", error=True)
            self.assertIn("persist", result["error"])

    def test_explicit_claude_completion_releases_automatic_gate(self):
        self.configure("claude", {"kind": "agent", "name": "reviewer"})
        self.call("claude", "complete")
        env = {**self.env, "CLAUDE_PROJECT_DIR": str(self.project), "GUARD_HOST": "claude"}
        for plan, blocked in ((self.plan.read_text(), False), ("A changed plan", True)):
            payload = {"session_id": "parent-session", "tool_response": {"plan": plan}}
            result = subprocess.run(
                [sys.executable, str(PLUGIN / "scripts" / "guard_hook.py"), "exit-plan"],
                input=json.dumps(payload), text=True, capture_output=True, env=env, timeout=15,
            )
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stderr, "")
            if blocked:
                self.assertEqual(json.loads(result.stdout)["decision"], "block")
            else:
                self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
