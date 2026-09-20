import curses
import json
from pathlib import Path
import stat
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import core
import herdr_main
import view_state as store
from ui import Navigator


class StateFixture(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name).resolve()
        self.root = self.base / "project"
        self.root.mkdir()
        (self.root / "folder").mkdir()
        (self.root / "folder" / "file.txt").write_text("\n".join(f"line {i}" for i in range(120)))
        (self.root / "other.txt").write_text("other")
        self.directory = self.base / "state"
        self.nav = Navigator(self.root, "pane", False, "",
                             on_state=lambda view: store.save_view(self.directory, view))

    def prepare_view(self):
        self.nav.expanded = {"folder"}
        self.nav.rebuild()
        self.nav.selected = next(i for i, row in enumerate(self.nav.items) if row.path == "folder/file.txt")
        self.nav.load("folder/file.txt")
        self.nav.scroll = 1
        self.nav.preview_scroll = 25
        self.nav.horizontal = 8
        self.nav.preview_focus = True
        return self.nav.export_state()


class StorageTests(StateFixture):
    def test_roundtrip_atomic_private_metadata_only(self):
        view = self.prepare_view()
        store.save_view(self.directory, view)
        self.assertEqual(store.load_view(self.directory, self.root), view)
        path = store.state_path(self.directory, self.root)
        self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o600)
        self.assertNotIn("line 119", path.read_text())
        self.assertEqual(list(path.parent.iterdir()), [path])

    def test_roots_are_isolated_and_symlink_aliases_share_state(self):
        view = self.prepare_view()
        store.save_view(self.directory, view)
        other = self.base / "other"
        other.mkdir()
        self.assertIsNone(store.load_view(self.directory, other))
        store.save_view(self.directory, {"root": str(other), "query": "other"})
        self.assertEqual(store.load_view(self.directory, self.root), view)
        alias = self.base / "alias"
        alias.symlink_to(self.root, target_is_directory=True)
        self.assertEqual(store.load_view(self.directory, alias), view)

    def test_missing_corrupt_oversized_and_wrong_version_are_ignored(self):
        self.assertIsNone(store.load_view(None, self.root))
        self.assertIsNone(store.load_view(self.directory, self.root))
        self.nav.checkpoint()
        path = store.state_path(self.directory, self.root)
        invalid = [b"not json", b"[]", b"null", b"\xff", b'{"version": 99}',
                   json.dumps({"version": True, "view": self.nav.export_state()}).encode(),
                   json.dumps({"version": 1, "view": {"root": str(self.base)}}).encode()]
        for raw in invalid:
            path.write_bytes(raw)
            self.assertIsNone(store.load_view(self.directory, self.root))
        path.write_bytes(b" " * 101)
        with patch.object(store, "MAX_STATE_BYTES", 100):
            self.assertIsNone(store.load_view(self.directory, self.root))

    def test_malformed_fields_and_unsafe_relative_paths_are_rejected(self):
        view = self.prepare_view()
        cases = {"root": ["", "relative", None], "changes": [1, "false"],
                 "query": [[], "x" * 4097], "active": ["../secret", "/secret", "a\0b"],
                 "expanded": ["folder", [None], ["../secret"], ["/secret"]],
                 "preview_scroll": [-1, True, "20", 1_000_000_001],
                 "selected": ["../other", {}], "preview_focus": ["true"]}
        for field, values in cases.items():
            for value in values:
                with self.subTest(field=field, value=value):
                    self.assertIsNone(store.normalize({**view, field: value}, self.root))
        self.assertIsNotNone(store.normalize({**view, "selected": ".."}, self.root))

    def test_failed_replace_keeps_previous_snapshot_and_removes_temporary(self):
        view = self.prepare_view()
        store.save_view(self.directory, view)
        with patch("view_state.os.replace", side_effect=OSError("disk full")):
            with self.assertRaises(OSError):
                store.save_view(self.directory, {**view, "query": "new"})
        self.assertEqual(store.load_view(self.directory, self.root), view)
        self.assertEqual(len(list((self.directory / "views").iterdir())), 1)

    def test_write_limit_keeps_existing_snapshot(self):
        view = self.prepare_view()
        store.save_view(self.directory, view)
        with patch.object(store, "MAX_STATE_BYTES", 10):
            with self.assertRaisesRegex(ValueError, "save limit"):
                store.save_view(self.directory, view)
        self.assertEqual(store.load_view(self.directory, self.root), view)


class NavigatorStateTests(StateFixture):
    def test_restore_complete_view_in_a_different_pane(self):
        view = self.prepare_view()
        self.nav.checkpoint()
        nav = Navigator(self.root, "different-pane", False, "")
        self.assertTrue(nav.restore_state(store.load_view(self.directory, self.root)))
        self.assertEqual(nav.export_state(), view)
        self.assertIn("Restored", nav.message)

    def test_filters_and_visibility_restore_without_reentering_search(self):
        self.prepare_view()
        self.nav.query = "file"
        self.nav.include_ignored = True
        self.nav.changes = True
        self.nav.searching = True
        nav = Navigator(self.root, "pane", False, "")
        nav.restore_state(self.nav.export_state())
        self.assertEqual(nav.query, "file")
        self.assertTrue(nav.include_ignored)
        self.assertTrue(nav.changes)
        self.assertFalse(nav.searching)

    def test_deleted_file_and_folder_do_not_restore_stale_preview(self):
        view = self.prepare_view()
        (self.root / "folder" / "file.txt").unlink()
        (self.root / "folder").rmdir()
        nav = Navigator(self.root, "pane", False, "")
        nav.restore_state(view)
        self.assertEqual(nav.expanded, set())
        self.assertEqual(nav.selected, 0)
        self.assertEqual(nav.active, "")
        self.assertFalse(nav.preview_focus)
        self.assertEqual(nav.preview_scroll, 0)

    def test_markdown_offset_is_not_clamped_to_source_line_count(self):
        (self.root / "long.md").write_text("A long paragraph with words. " * 400)
        view = {**self.nav.export_state(), "active": "long.md", "preview_scroll": 30}
        nav = Navigator(self.root, "pane", False, "")
        nav.restore_state(view)
        self.assertEqual(len(nav.content), 1)
        screen = Mock()
        screen.getmaxyx.return_value = (40, 140)
        with patch.object(nav, "style", return_value=0), patch.object(nav, "draw_content"), \
                patch.object(nav, "draw_tree"):
            nav.draw(screen)
        self.assertGreater(len(nav.rendered), 60)
        self.assertEqual(nav.preview_scroll, 30)

    def test_file_content_is_reread_and_scroll_clamped_on_draw(self):
        view = self.prepare_view()
        (self.root / "folder" / "file.txt").write_text("updated\n")
        nav = Navigator(self.root, "pane", False, "")
        nav.restore_state(view)
        self.assertEqual(nav.source_text, "updated\n")
        screen = Mock()
        screen.getmaxyx.return_value = (40, 140)
        with patch.object(nav, "style", return_value=0), patch.object(nav, "draw_content"), \
                patch.object(nav, "draw_tree"):
            nav.draw(screen)
        self.assertEqual(nav.preview_scroll, 0)
        self.assertEqual(nav.horizontal, 0)

    def test_malformed_wrong_root_and_failed_scan_leave_view_unchanged(self):
        original = self.prepare_view()
        for state in ({}, None, {**original, "root": str(self.base)}):
            self.assertFalse(self.nav.restore_state(state))
            self.assertEqual(self.nav.export_state(), original)
        with patch("ui.scan", side_effect=OSError("not readable")):
            self.assertFalse(self.nav.restore_state({**original, "include_ignored": True}))
        self.assertEqual(self.nav.export_state(), original)

    def test_checkpoint_skips_duplicates_and_recovers_from_write_failure(self):
        callback = Mock(side_effect=[OSError("disk full"), None, None])
        self.nav.on_state = callback
        self.nav.checkpoint()
        self.assertIn("disk full", self.nav.message)
        self.nav.checkpoint()
        self.nav.checkpoint()
        self.assertEqual(callback.call_count, 2)
        self.nav.selected = 1
        self.nav.checkpoint()
        self.assertEqual(callback.call_count, 3)

    def test_root_change_saves_departing_root_without_redirecting_it(self):
        view = self.prepare_view()
        self.assertTrue(self.nav.change_root(self.base))
        self.assertEqual(store.load_view(self.directory, self.root), view)
        self.nav.checkpoint()
        self.assertEqual(store.load_view(self.directory, self.base)["root"], str(self.base))
        self.assertEqual(store.load_view(self.directory, self.root), view)

    def test_run_checkpoints_before_waiting_and_on_exit(self):
        self.prepare_view()
        self.nav.preview_focus = False
        self.nav.body = 10
        keys = iter(("\x06", "\x03"))
        observed = []

        def read(screen):
            observed.append(store.load_view(self.directory, self.root)["preview_scroll"])
            return next(keys)

        with patch("curses.curs_set"), patch("ui.theme", return_value={}), \
                patch("terminal_input.enable"), patch("terminal_input.disable"), \
                patch("terminal_input.read", side_effect=read), patch.object(self.nav, "draw"):
            self.nav.run(Mock())
        self.assertEqual(observed, [25, 35])
        self.assertEqual(store.load_view(self.directory, self.root)["preview_scroll"], 35)


class AdapterStateTests(StateFixture):
    def panel(self, inspect, extra=None):
        env = {"HERDR_ENV": "1", "HERDR_PLUGIN_STATE_DIR": str(self.directory), **(extra or {})}
        with patch("herdr_main.source", return_value=("pane", self.root)), \
                patch("curses.wrapper", side_effect=lambda run: inspect(run.__self__)):
            return herdr_main.main(env, "panel")

    def test_close_then_reopen_restores_by_root(self):
        view = self.prepare_view()
        self.panel(lambda nav: nav.restore_state(view))
        self.assertEqual(store.load_view(self.directory, self.root), view)
        self.panel(lambda nav: self.assertEqual(nav.export_state(), view))

    def test_explicit_changes_action_overrides_saved_browse_mode(self):
        self.nav.checkpoint()
        self.panel(lambda nav: self.assertTrue(nav.changes), {"FILE_NAV_CHANGES": "1"})

    def test_panel_restores_ignored_view_without_default_scan(self):
        self.nav.toggle_ignored()
        self.nav.checkpoint()
        with patch("ui.scan", wraps=core.scan) as scan:
            self.panel(lambda nav: self.assertTrue(nav.include_ignored))
        scan.assert_called_once_with(self.root, include_ignored=True, include_status=False)

    def test_resize_snapshot_has_precedence_over_saved_view(self):
        self.nav.checkpoint()
        view = self.prepare_view()
        self.directory.mkdir(exist_ok=True)
        path = self.directory / "resize-test.json"
        path.write_text(json.dumps({"view": view}))
        self.panel(lambda nav: self.assertEqual(nav.export_state(), view),
                   {"FILE_NAV_RESUME": str(path)})
        self.assertFalse(path.exists())

    def test_wrapper_exception_still_checkpoints_current_state(self):
        def fail(nav):
            nav.query = "file"
            raise RuntimeError("terminal closed")

        with self.assertRaisesRegex(RuntimeError, "terminal closed"):
            self.panel(fail)
        self.assertEqual(store.load_view(self.directory, self.root)["query"], "file")


if __name__ == "__main__":
    unittest.main()
