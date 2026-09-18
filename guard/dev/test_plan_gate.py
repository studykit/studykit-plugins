#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Plan gate CLI regression tests; these do not verify host hook delivery.

Run: uv run --script guard/dev/test_plan_gate.py
"""

from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


CLI = Path(__file__).resolve().parents[1] / "scripts" / "guard_hook.py"


class PlanGateTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix="guard-plan-test-")
        self.addCleanup(temp.cleanup)
        self.project = Path(temp.name)
        self.config = self.project / ".claude" / "guard.local.json"
        self.config.parent.mkdir()
        self.env = {
            key: value for key, value in os.environ.items()
            if not key.startswith(("GUARD_", "CLAUDE_", "HERDR_", "CODEX_"))
        }
        self.env.update(
            GUARD_HOST="claude",
            GUARD_PROJECT_DIR=str(self.project),
            CLAUDE_PROJECT_DIR=str(self.project),
            CLAUDE_CODE_SESSION_ID="plan-test",
            GUARD_TRACE="1",
            PYTHONDONTWRITEBYTECODE="1",
        )

    def configure(self, **values):
        self.config.write_text(json.dumps(values), encoding="utf-8")

    def run_cli(self, *args, payload=None):
        result = subprocess.run(
            [sys.executable, str(CLI), *args],
            input=json.dumps(payload) if payload is not None else "",
            text=True, capture_output=True, cwd=self.project, env=self.env,
            timeout=15,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        trace = self.project / ".claude" / "guard" / "trace.log"
        if trace.exists():
            self.assertNotIn('"exception"', trace.read_text())
        return result.stdout

    def approve(self, plan="Implement the requested change", **fields):
        payload = {
            "session_id": "plan-test",
            "tool_name": "ExitPlanMode",
            "tool_response": {"plan": plan},
        }
        payload.update(fields)
        output = self.run_cli("exit-plan", payload=payload)
        return json.loads(output) if output else None

    def test_unconfigured_plans_pass_without_a_fallback(self):
        self.assertIsNone(self.approve())
        self.configure(plan_review={})
        self.assertIsNone(self.approve())
        self.assertIn("plan_review: (unset) — no plan review", self.run_cli("settings", "show"))

    def test_only_the_configured_agent_or_skill_is_requested(self):
        for kind in ("agent", "skill"):
            with self.subTest(kind=kind):
                self.configure(plan_review={"kind": kind, "name": "my-reviewer"})
                decision = self.approve()
                self.assertEqual(decision["decision"], "block")
                self.assertIn(f"`my-reviewer` {kind}", decision["reason"])
                self.assertIn("guard-plan-audited <plan file path>", decision["reason"])
                self.assertNotIn("guard:audit-plan", decision["reason"])

    def test_recorded_plan_passes_but_revised_plan_is_reviewed_again(self):
        self.configure(plan_review={"kind": "agent", "name": "my-reviewer"})
        plan = self.project / "plan.md"
        plan.write_text("Implement the requested change\n")
        self.assertIsNotNone(self.approve())
        self.run_cli("plan-audited", str(plan))
        self.assertIsNone(self.approve())
        decision = self.approve("Implement a different approach")
        self.assertIn("has changed since it was audited", decision["reason"])

    def test_clearing_reviewer_skips_even_a_revised_plan(self):
        self.configure(plan_review={"kind": "skill", "name": "my-reviewer"})
        self.assertIsNotNone(self.approve())
        self.configure(plan_review={})
        self.assertIsNone(self.approve("Revised plan"))

    def test_settings_can_register_clear_and_remove_reviewer(self):
        self.env["GUARD_SETTINGS_SKILL"] = "1"
        action = json.dumps({"kind": "skill", "name": "my-reviewer"})
        self.run_cli("settings", "set", "plan_review", action)
        self.assertIn("plan_review: skill:my-reviewer", self.run_cli("settings", "show"))
        self.assertIsNotNone(self.approve())
        self.run_cli("settings", "set", "plan_review", "{}")
        self.assertIsNone(self.approve())
        self.run_cli("settings", "set", "plan_review", action)
        self.run_cli("settings", "unset", "plan_review")
        self.assertNotIn("plan_review", json.loads(self.config.read_text()))
        self.assertIsNone(self.approve())

    def test_project_default_and_session_toggle_control_review(self):
        self.configure(**{"audit-plan": "off", "plan_review": {
            "kind": "agent", "name": "my-reviewer"}})
        self.assertIsNone(self.approve())
        self.run_cli("plan-toggle-cli", "on")
        self.assertIsNotNone(self.approve())
        self.run_cli("plan-toggle-cli", "off")
        self.assertIsNone(self.approve())

    def test_invalid_action_blocks_without_substituting_a_reviewer(self):
        for action in ({"kind": "reviewer", "name": "x"},
                       {"kind": "agent"}, {"kind": "skill", "name": "bad name"}):
            with self.subTest(action=action):
                self.configure(plan_review=action)
                decision = self.approve()
                self.assertEqual(decision["decision"], "block")
                self.assertIn("plan_review", decision["reason"])
                self.assertNotIn("guard:audit-plan", decision["reason"])
        self.run_cli("plan-toggle-cli", "off")
        self.assertIsNone(self.approve())

    def test_wrong_json_type_keeps_loader_skip_behavior(self):
        self.configure(plan_review="my-reviewer")
        self.assertIsNone(self.approve())
        self.assertIn("not a JSON object, ignored at use", self.run_cli("settings", "show"))

    def test_missing_plan_skips_and_input_plan_is_a_fallback(self):
        self.configure(plan_review={"kind": "skill", "name": "my-reviewer"})
        self.assertIsNone(self.approve(""))
        self.assertIsNotNone(self.approve("", tool_input={"plan": "Plan from input"}))


if __name__ == "__main__":
    unittest.main()
