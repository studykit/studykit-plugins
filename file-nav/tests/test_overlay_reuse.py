import fcntl
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import herdr_main
from popup_size import PopupSize


class OverlayReuseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.env = {"HERDR_PLUGIN_ID": "studykit.file-nav",
                    "HERDR_PLUGIN_STATE_DIR": str(self.root),
                    "HERDR_SOCKET_PATH": "/session-a/herdr.sock",
                    "HERDR_PLUGIN_CONTEXT_JSON": json.dumps({"tab_id": "w1:t1"})}
        self.panes = {}
        self.created = 0
        self.focused = []
        self.zoomed = []
        self.on_create = lambda: None
        self.calls = patch("herdr_main.call", side_effect=self.call).start()
        self.addCleanup(patch.stopall)

    def call(self, binary, *args):
        if args[:3] == ("plugin", "pane", "open"):
            self.on_create()
            self.created += 1
            pane_id = f"w1:p{self.created + 1}"
            self.panes[pane_id] = {"plugin_id": self.env["HERDR_PLUGIN_ID"], "entrypoint": "navigator",
                                  "pane": {"pane_id": pane_id, "terminal_id": f"terminal-{self.created}",
                                           "tab_id": "w1:t1"}}
            return {"plugin_pane": self.panes[pane_id]}
        if args[:2] == ("pane", "get"):
            if args[2] == "source":
                return {"pane": {"tab_id": "w1:t1"}}
            if args[2] not in self.panes:
                raise RuntimeError("pane_not_found")
            return {"pane": self.panes[args[2]]["pane"]}
        if args[:3] == ("plugin", "pane", "focus"):
            if args[3] not in self.panes:
                raise RuntimeError("plugin_pane_not_found")
            self.focused.append(args[3])
            return {"plugin_pane": self.panes[args[3]]}
        if args[:2] == ("pane", "zoom"):
            self.assertEqual(args[3], "--on")
            self.zoomed.append(args[2])
            return {}
        self.fail(f"Unexpected host command: {args}")

    def open(self, source="source", **kwargs):
        return herdr_main.open_panel(self.env, "herdr", source, self.root, False,
                                     PopupSize(), placement="overlay", **kwargs)

    def test_repeated_action_from_overlay_or_source_reuses_the_same_terminal(self):
        initial = self.open()["plugin_pane"]
        pane_id = initial["pane"]["pane_id"]
        for source in (pane_id, "source", pane_id):
            self.assertEqual(self.open(source)["plugin_pane"], initial)
        self.assertEqual(self.created, 1)
        self.assertEqual(self.zoomed, [pane_id] * 3)

    def test_focused_overlay_created_before_tracking_is_adopted(self):
        initial = self.open()["plugin_pane"]
        slot, _ = herdr_main.overlay_slot(self.env, "herdr", "source")
        slot.write_text("invalid previous record")
        pane_id = initial["pane"]["pane_id"]
        self.open(pane_id)
        self.assertEqual(self.created, 1)
        self.assertEqual(json.loads(slot.read_text())["pane_id"], pane_id)

    def test_closed_overlay_is_recreated(self):
        initial = self.open()["plugin_pane"]["pane"]["pane_id"]
        del self.panes[initial]
        replacement = self.open()["plugin_pane"]["pane"]["pane_id"]
        self.assertNotEqual(replacement, initial)
        self.assertEqual(self.created, 2)

    def test_reused_pane_id_with_a_different_terminal_is_not_focused(self):
        pane_id = self.open()["plugin_pane"]["pane"]["pane_id"]
        self.panes[pane_id]["pane"]["terminal_id"] = "unrelated-terminal"
        self.open()
        self.assertNotIn(pane_id, self.focused)
        self.assertEqual(self.created, 2)

    def test_moved_overlay_does_not_steal_focus_from_another_tab(self):
        pane_id = self.open()["plugin_pane"]["pane"]["pane_id"]
        self.panes[pane_id]["pane"]["tab_id"] = "w1:t2"
        self.open()
        self.assertNotIn(pane_id, self.focused)
        self.assertEqual(self.created, 2)

    def test_host_failure_does_not_launch_a_duplicate(self):
        self.open()
        self.calls.side_effect = RuntimeError("host unavailable")
        with self.assertRaisesRegex(RuntimeError, "host unavailable"):
            self.open()
        self.assertEqual(self.created, 1)

    def test_lookup_and_creation_share_an_exclusive_lock(self):
        path, _ = herdr_main.overlay_slot(self.env, "herdr", "source")
        def assert_locked():
            with path.open("a+") as stream:
                with self.assertRaises(BlockingIOError):
                    fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        self.on_create = assert_locked
        self.open()
        inode = path.stat().st_ino
        self.open()
        self.assertEqual(path.stat().st_ino, inode)
        self.assertEqual(self.created, 1)

    def test_slot_is_scoped_to_both_host_session_and_tab(self):
        first, _ = herdr_main.overlay_slot(self.env, "herdr", "source")
        second, _ = herdr_main.overlay_slot({**self.env, "HERDR_SOCKET_PATH": "/session-b/herdr.sock"}, "herdr", "source")
        third, _ = herdr_main.overlay_slot({**self.env, "HERDR_PLUGIN_CONTEXT_JSON": '{"tab_id":"w1:t2"}'}, "herdr", "source")
        self.assertEqual(len({first, second, third}), 3)

    def test_missing_context_tab_uses_live_source_metadata(self):
        original = herdr_main.overlay_slot(self.env, "herdr", "source")
        self.env.pop("HERDR_PLUGIN_CONTEXT_JSON")
        self.assertEqual(herdr_main.overlay_slot(self.env, "herdr", "source"), original)

    def test_another_plugin_is_not_reused_as_file_navigator(self):
        self.panes["other"] = {"plugin_id": "another.plugin", "entrypoint": "navigator", "pane": {}}
        self.open("other")
        self.assertEqual(self.created, 1)
        self.assertEqual(self.zoomed, [])

    def test_unused_resume_file_is_consumed_when_an_overlay_already_exists(self):
        self.open()
        resume = self.root / "resize-test.json"
        resume.write_text("{}")
        self.open(resume=resume)
        self.assertFalse(resume.exists())
        self.assertEqual(self.created, 1)


if __name__ == "__main__":
    unittest.main()
