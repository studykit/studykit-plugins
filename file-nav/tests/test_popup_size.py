import curses
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import herdr_main
from popup_size import PopupSize, load_size, save_size
from ui import Navigator


class SizeTests(unittest.TestCase):
    def test_percentages_are_bounded_and_validated(self):
        self.assertEqual(PopupSize(40, 100).adjust(-5, 5), PopupSize(40, 100))
        for invalid in (0, 101, "80", True):
            with self.assertRaises(ValueError):
                PopupSize(invalid, 80)

    def test_remembers_size_and_recovers_from_invalid_settings(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(load_size(root), PopupSize())
            save_size(root, PopupSize(85, 80))
            self.assertEqual(load_size(root), PopupSize(85, 80))
            (root / "popup-size.json").write_text('{"width": 900, "height": 80}')
            self.assertEqual(load_size(root), PopupSize())


class NavigatorResizeTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / "file.txt").write_text("\n".join(str(i) for i in range(60)))
        self.callback = Mock()
        self.nav = Navigator(self.root, "source", False, "", on_resize=self.callback)

    def test_resize_preserves_search_selection_focus_and_scroll(self):
        self.nav.query = "file"
        self.nav.rebuild()
        self.nav.activate()
        self.nav.preview_scroll = 30
        self.nav.horizontal = 8
        self.nav.key("\x17", None)
        self.nav.key("2", None)
        self.assertFalse(self.nav.key("\n", None))
        size, state = self.callback.call_args.args
        self.assertEqual(size, PopupSize(85, 80))
        restored = Navigator(self.root, "source", False, "", size=size)
        restored.restore_state(state)
        self.assertEqual(restored.query, "file")
        self.assertEqual(restored.active, "file.txt")
        self.assertTrue(restored.preview_focus)
        self.assertEqual(restored.preview_scroll, 30)
        self.assertEqual(restored.horizontal, 8)

    def test_cancel_does_not_change_size_or_query(self):
        self.nav.query = "file"
        self.nav.key("\x17", None)
        self.nav.key(curses.KEY_LEFT, None)
        self.nav.key("\x1b", None)
        self.assertEqual(self.nav.size, PopupSize())
        self.assertEqual(self.nav.query, "file")
        self.callback.assert_not_called()

    def test_resize_failure_keeps_navigator_open(self):
        self.callback.side_effect = OSError("disk full")
        self.nav.key("\x17", None)
        self.nav.key("1", None)
        self.assertTrue(self.nav.key("\n", None))
        self.assertIn("disk full", self.nav.message)

    def test_arrow_keys_adjust_dimensions_without_moving_selection(self):
        self.nav.key("\x17", None)
        self.nav.key(curses.KEY_LEFT, None)
        self.nav.key(curses.KEY_DOWN, None)
        self.assertEqual(self.nav.size_draft, PopupSize(91, 87))
        self.assertEqual(self.nav.selected, 0)


class ResizeAdapterTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name).resolve()
        self.env = {"HERDR_PLUGIN_ID": "studykit.file-nav", "HERDR_ENV": "1",
                    "HERDR_PLUGIN_STATE_DIR": str(self.directory),
                    "HERDR_PLUGIN_CONFIG_DIR": str(self.directory / "config")}
        self.payload = {"pane_id": "source", "size": {"width": 85, "height": 80},
                        "view": {"root": str(self.directory), "changes": False}}
        self.path = self.directory / "resize-test.json"
        self.path.write_text(json.dumps(self.payload))

    def test_open_passes_dimensions_and_resume_file(self):
        with patch("herdr_main.call") as call:
            herdr_main.open_panel(self.env, "herdr", "source", self.directory, False,
                                  PopupSize(85, 80), self.path)
        args = call.call_args.args
        self.assertEqual(args[args.index("--width") + 1], "85%")
        self.assertEqual(args[args.index("--height") + 1], "80%")
        self.assertIn(f"FILE_NAV_RESUME={self.path}", args)

    def test_reopen_waits_for_old_popup_then_saves_size(self):
        with patch("herdr_main.call", return_value={"pane": {"pane_id": "source"}}), \
             patch("herdr_main.open_panel", side_effect=[RuntimeError("ui_busy"), {}]) as opened, \
             patch("herdr_main.time.sleep"):
            herdr_main.reopen(self.env, str(self.path))
        self.assertEqual(opened.call_count, 2)
        self.assertEqual(load_size(self.directory / "config"), PopupSize(85, 80))
        self.assertTrue(self.path.exists())  # The new popup consumes the resume file.

    def test_focus_change_cancels_without_opening_another_panes_popup(self):
        with patch("herdr_main.call", return_value={"pane": {"pane_id": "other"}}), \
             patch("herdr_main.open_panel") as opened:
            with self.assertRaisesRegex(RuntimeError, "focus moved"):
                herdr_main.reopen(self.env, str(self.path))
        opened.assert_not_called()
        self.assertFalse(self.path.exists())

    def test_unrelated_errors_do_not_retry_or_save_size(self):
        with patch("herdr_main.call", return_value={"pane": {"pane_id": "source"}}), \
             patch("herdr_main.open_panel", side_effect=RuntimeError("plugin disabled")) as opened:
            with self.assertRaisesRegex(RuntimeError, "plugin disabled"):
                herdr_main.reopen(self.env, str(self.path))
        self.assertEqual(opened.call_count, 1)
        self.assertFalse(self.path.exists())
        self.assertFalse((self.directory / "config" / "popup-size.json").exists())

    def test_resume_file_must_be_owned_by_this_plugin(self):
        with self.assertRaisesRegex(ValueError, "Invalid"):
            herdr_main.resume_path(self.env, str(self.directory.parent / "resize-other.json"))


if __name__ == "__main__":
    unittest.main()
