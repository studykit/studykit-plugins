import curses
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import herdr_main
from popup_size import PopupSize
from ui import Navigator


class LayoutTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name).resolve()
        (self.root / "file.txt").write_text("\n".join(str(i) for i in range(100)))
        self.callback = Mock(return_value=True)
        self.mode = Mock(return_value="popup")
        self.nav = Navigator(self.root, "source", False, "",
                             layout_loader=self.mode, on_layout=self.callback)
        self.nav.query = "file"
        self.nav.rebuild()
        self.nav.activate()
        self.nav.preview_scroll = 30
        self.nav.horizontal = 8

    def test_popup_overlay_transitions_exit_with_complete_snapshot(self):
        view = self.nav.export_state()
        for current, key, expected in (("popup", "2", "overlay"), ("overlay", "1", "popup")):
            self.mode.return_value = current
            self.nav.key("\x17", None)
            self.assertFalse(self.nav.key(key, None))
            self.callback.assert_called_with(expected, PopupSize(), view)
            self.assertEqual(self.nav.export_state(), view)
            self.assertFalse(self.nav.layout_dialog)

    def test_cancel_and_same_layout_do_not_touch_the_host(self):
        view = self.nav.export_state()
        for key in ("\x1b", "1"):
            self.nav.key("\x17", None)
            self.assertTrue(self.nav.key(key, None))
        self.callback.assert_not_called()
        self.assertEqual(self.nav.export_state(), view)

    def test_host_failure_preserves_view_and_keeps_navigator_open(self):
        self.callback.side_effect = RuntimeError("host unavailable")
        view = self.nav.export_state()
        self.nav.key("\x17", None)
        self.assertTrue(self.nav.key("2", None))
        self.assertEqual(self.nav.export_state(), view)
        self.assertIn("host unavailable", self.nav.message)
        self.assertEqual(self.nav.layout, "popup")

    def test_dialog_consumes_navigation_and_requires_exit_from_search(self):
        view = self.nav.export_state()
        self.nav.key("\x17", None)
        for key in ("j", curses.KEY_DOWN, "\t", "\x19"):
            self.nav.key(key, None)
        self.assertEqual(self.nav.export_state(), view)
        self.nav.key("\x1b", None)
        self.nav.key("\t", None)  # In the preview, "/" finds text instead.
        self.nav.key("/", None)
        self.nav.key("\x17", None)
        self.assertFalse(self.nav.layout_dialog)
        self.assertTrue(self.nav.searching)
        self.callback.assert_not_called()

    def test_size_dialog_is_popup_only_and_reads_current_host_layout(self):
        self.mode.return_value = "overlay"
        self.nav.key("\x19", None)
        self.assertIsNone(self.nav.size_draft)
        self.mode.return_value = "popup"
        self.nav.key("\x19", None)
        self.assertEqual(self.nav.size_draft, PopupSize())

    def test_slash_starts_search_and_remains_a_path_separator_in_search(self):
        self.nav.query = ""
        self.nav.key("\t", None)
        self.nav.key("/", None)
        self.nav.key("/", None)
        self.assertTrue(self.nav.searching)
        self.assertEqual(self.nav.query, "/")


class TerminalResizeTests(unittest.TestCase):
    def test_missed_resize_reconciles_with_the_pty_and_repaints(self):
        import terminal_input
        screen = Mock()
        screen.getmaxyx.return_value = (50, 160)
        with patch("terminal_input.os.get_terminal_size", return_value=(75, 50)), \
                patch("terminal_input.curses.resizeterm") as resize:
            terminal_input.sync_size(screen)
            resize.assert_called_once_with(50, 75)
            screen.clearok.assert_called_once_with(True)
            resize.reset_mock()
            screen.getmaxyx.return_value = (50, 75)
            terminal_input.sync_size(screen)
            resize.assert_not_called()


class LayoutAdapterTests(unittest.TestCase):
    def test_removed_split_mode_is_rejected_before_any_host_action(self):
        with patch("herdr_main.call") as call, patch("herdr_main.prepare_resize") as reopen:
            with self.assertRaises(ValueError):
                herdr_main.change_layout({}, "source", "split", PopupSize(), {})
            with self.assertRaises(ValueError):
                herdr_main.open_panel({}, "herdr", "source", Path("/tmp"), False,
                                      PopupSize(), placement="split")
        call.assert_not_called()
        reopen.assert_not_called()

    def test_popup_boundaries_reopen_with_requested_mode(self):
        for env, mode in (({"HERDR_PANE_ID": "navigator"}, "popup"), ({}, "overlay")):
            with patch("herdr_main.call") as call, patch("herdr_main.prepare_resize") as reopen:
                self.assertTrue(herdr_main.change_layout(env, "source", mode, PopupSize(), {"root": "/tmp"}))
            call.assert_not_called()
            reopen.assert_called_once_with(env, "source", PopupSize(), {"root": "/tmp"}, mode)

    def test_popup_launch_uses_manifest_without_pane_target_or_placement_override(self):
        with patch("herdr_main.call") as call:
            herdr_main.open_panel({"HERDR_PLUGIN_ID": "plugin"}, "herdr", "source", Path("/tmp"),
                                  False, PopupSize(), placement="popup")
        args = call.call_args.args
        self.assertEqual(args[args.index("--entrypoint") + 1], "popup")
        self.assertNotIn("--target-pane", args)
        self.assertNotIn("--placement", args)
        self.assertIn("LENS_SOURCE_PANE=source", args)

    def test_overlay_launch_uses_native_overlay_manifest_without_split_controls(self):
        import tomllib
        manifest = tomllib.loads((Path(__file__).resolve().parents[1] / "herdr-plugin.toml").read_text())
        entries = {entry["id"]: entry["placement"] for entry in manifest["panes"]}
        self.assertEqual(entries, {"navigator": "overlay", "popup": "popup"})
        with patch("herdr_main.call") as call:
            herdr_main.open_panel({"HERDR_PLUGIN_ID": "plugin"}, "herdr", "source", Path("/tmp"),
                                  False, PopupSize(), placement="overlay")
        args = call.call_args.args
        self.assertEqual(args[args.index("--entrypoint") + 1], "navigator")
        for flag in ("--placement", "--target-pane", "--direction", "--width", "--height"):
            self.assertNotIn(flag, args)

    def test_layout_uses_the_host_surface(self):
        self.assertEqual(herdr_main.current_layout({"HERDR_PANE_ID": "navigator"}), "overlay")
        self.assertEqual(herdr_main.current_layout({}), "popup")
        for placement in ("left", "right", "overlay"):
            self.assertEqual(herdr_main.current_layout(
                {"HERDR_PANE_ID": "navigator", "LENS_PLACEMENT": placement}), placement)
        self.assertEqual(herdr_main.current_layout(
            {"HERDR_PANE_ID": "navigator", "LENS_PLACEMENT": "popup"}), "overlay")

    def test_half_layouts_are_offered_by_key_and_command(self):
        nav = Navigator(Path(tempfile.gettempdir()), "source", False, "",
                        layout_loader=Mock(return_value="overlay"), on_layout=Mock(return_value=True))
        nav.key("\x17", None)
        self.assertFalse(nav.key("3", None))
        nav.on_layout.assert_called_with("left", PopupSize(), nav.export_state())
        self.assertFalse(nav.run_command("layout right", None))
        nav.on_layout.assert_called_with("right", PopupSize(), nav.export_state())

    def test_helper_drops_caller_context_but_records_pane_and_process_to_wait_for(self):
        with tempfile.TemporaryDirectory() as directory:
            env = {"HERDR_PLUGIN_STATE_DIR": directory, "HERDR_PANE_ID": "navigator"}
            with patch("herdr_main.subprocess.Popen") as spawn:
                herdr_main.prepare_resize(env, "source", PopupSize(), {"root": "/tmp"}, "popup")
            helper_env = spawn.call_args.kwargs["env"]
            self.assertNotIn("HERDR_PANE_ID", helper_env)
            self.assertEqual(env["HERDR_PANE_ID"], "navigator")
            data = json.loads(next(Path(directory).glob("resize-*.json")).read_text())
            self.assertEqual(data["previous_pane"], "navigator")
            self.assertGreater(data["previous_pid"], 0)
            self.assertEqual(data["placement"], "popup")

    def test_reopen_waits_for_process_and_pane_removal_before_opening(self):
        with tempfile.TemporaryDirectory() as directory:
            env = {"HERDR_PLUGIN_STATE_DIR": directory}
            path = Path(directory) / "resize-test.json"
            path.write_text(json.dumps({"pane_id": "source", "previous_pid": 123,
                                       "previous_pane": "navigator", "placement": "popup",
                                       "size": PopupSize().as_dict(),
                                       "view": {"root": directory, "changes": False}}))
            with patch("herdr_main.os.kill", side_effect=[None, ProcessLookupError]), \
                    patch("herdr_main.time.sleep"), \
                    patch("herdr_main.call", side_effect=[{}, RuntimeError("pane_not_found"),
                                                          {"pane": {"pane_id": "source"}}]), \
                    patch("herdr_main.open_panel") as opened:
                herdr_main.reopen(env, str(path))
            opened.assert_called_once_with(env, "herdr", "source", Path(directory), False,
                                           PopupSize(), path.resolve(), placement="popup")

class WholeTabHalfTests(unittest.TestCase):
    # Top pane over a bottom row split 40:60, as Herdr reports it.
    LAYOUT = {"tab_id": "w:t1", "zoomed": True, "area": {"x": 0, "y": 0, "width": 100, "height": 30},
              "panes": [{"pane_id": "top", "rect": {"x": 0, "y": 0, "width": 100, "height": 9}},
                        {"pane_id": "left", "rect": {"x": 0, "y": 9, "width": 40, "height": 21}},
                        {"pane_id": "right", "rect": {"x": 40, "y": 9, "width": 60, "height": 21}}],
              "splits": [{"direction": "down", "ratio": 0.3, "rect": {"x": 0, "y": 0, "width": 100, "height": 30}},
                         {"direction": "right", "ratio": 0.4, "rect": {"x": 0, "y": 9, "width": 100, "height": 21}}]}

    def test_split_tree_follows_the_reported_rectangles(self):
        panes = [{**pane["rect"], "pane_id": pane["pane_id"]} for pane in self.LAYOUT["panes"]]
        self.assertEqual(herdr_main.split_tree(panes, self.LAYOUT["splits"], self.LAYOUT["area"]),
                         ("down", 0.3, "top", ("right", 0.4, "left", "right")))

    def run_half(self, placement, fail=False):
        calls = []
        def call(binary, *args):
            calls.append(args)
            if args[:2] == ("pane", "layout"):
                return {"layout": self.LAYOUT}
            if args[:2] == ("pane", "move") and "--new-tab" in args:
                return {"move_result": {"pane": {"tab_id": "w:t9"}}}
            if args[:3] == ("plugin", "pane", "open"):
                if fail:
                    raise RuntimeError("host unavailable")
                return {"plugin_pane": {"pane": {"pane_id": "lens"}}}
            return {}
        with patch("herdr_main.call", side_effect=call):
            try:
                herdr_main.open_half("herdr", "left", ["plugin", "pane", "open"], placement)
            except RuntimeError:
                pass
        return calls

    def test_other_panes_wait_aside_and_return_with_their_splits(self):
        calls = self.run_half("left")
        self.assertEqual(calls, [
            ("pane", "layout", "--pane", "left"),
            ("pane", "zoom", "left", "--off"),
            ("pane", "move", "left", "--new-tab", "--no-focus"),
            ("pane", "move", "right", "--tab", "w:t9", "--split", "right", "--target-pane", "left", "--no-focus"),
            ("plugin", "pane", "open", "--target-pane", "top"),
            ("pane", "swap", "--source-pane", "lens", "--target-pane", "top"),
            ("pane", "move", "left", "--tab", "w:t1", "--split", "down", "--target-pane", "top", "--ratio", "0.3", "--no-focus"),
            ("pane", "move", "right", "--tab", "w:t1", "--split", "right", "--target-pane", "left", "--ratio", "0.4", "--no-focus"),
            ("plugin", "pane", "focus", "lens"),
        ])
        self.assertNotIn("swap", [args[1] for args in self.run_half("right")])

    def test_failed_open_still_returns_every_pane(self):
        calls = self.run_half("right", fail=True)
        moves = [args for args in calls if args[:2] == ("pane", "move") and "w:t1" in args]
        self.assertEqual([args[2] for args in moves], ["left", "right"])


class LayoutPreferenceTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name).resolve()
        self.env = {"HERDR_ENV": "1", "HERDR_PLUGIN_ID": "studykit.lens",
                    "HERDR_PLUGIN_CONFIG_DIR": str(self.root)}

    def test_each_saved_mode_is_used_by_browse_and_changes(self):
        from layout_mode import load_layout, save_layout
        for mode in ("popup", "overlay", "left", "right"):
            save_layout(self.root, mode)
            self.assertEqual(load_layout(self.root), mode)
            for operation in ("browse", "changes"):
                with patch("herdr_main.source", return_value=("source", self.root)), \
                        patch("herdr_main.open_panel") as opened:
                    herdr_main.main(self.env, operation)
                self.assertEqual(opened.call_args.kwargs["placement"], mode)
                self.assertEqual(opened.call_args.args[4], operation == "changes")

    def test_missing_invalid_or_old_split_preference_defaults_to_popup(self):
        from layout_mode import load_layout
        self.assertEqual(load_layout(None), "popup")
        self.assertEqual(load_layout(self.root), "popup")
        for value in ('bad', '[]', 'null', '{"placement":"split"}', '{"placement":"invalid"}', '{"placement":[]}'):
            (self.root / "layout.json").write_text(value)
            self.assertEqual(load_layout(self.root), "popup")

    def test_failed_reopen_keeps_the_previous_preference(self):
        from layout_mode import load_layout, save_layout
        save_layout(self.root, "overlay")
        path = self.root / "resize-test.json"
        path.write_text(json.dumps({"pane_id": "source", "placement": "popup",
                                   "size": PopupSize().as_dict(),
                                   "view": {"root": str(self.root), "changes": False}}))
        with patch("herdr_main.call", return_value={"pane": {"pane_id": "source"}}), \
                patch("herdr_main.open_panel", side_effect=RuntimeError("host unavailable")):
            with self.assertRaises(RuntimeError):
                herdr_main.reopen({**self.env, "HERDR_PLUGIN_STATE_DIR": str(self.root)}, str(path))
        self.assertEqual(load_layout(self.root), "overlay")

    def test_popup_boundary_saves_mode_after_successful_reopen(self):
        from layout_mode import load_layout
        for mode in ("popup", "overlay"):
            path = self.root / "resize-test.json"
            path.write_text(json.dumps({"pane_id": "source", "placement": mode,
                                       "size": PopupSize().as_dict(),
                                       "view": {"root": str(self.root), "changes": False}}))
            with patch("herdr_main.call", return_value={"pane": {"pane_id": "source"}}), \
                    patch("herdr_main.open_panel"):
                herdr_main.reopen({**self.env, "HERDR_PLUGIN_STATE_DIR": str(self.root)}, str(path))
            self.assertEqual(load_layout(self.root), mode)


if __name__ == "__main__":
    unittest.main()
