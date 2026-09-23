import curses
from pathlib import Path
import io
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import markdown_preview as md
import terminal_input as terminal
from ui import Navigator, clean


class InputTests(unittest.TestCase):
    def test_sgr_mouse_both_wheel_directions_and_modifiers(self):
        self.assertEqual(terminal.decode("\x1b[<64;40;12M"), terminal.Mouse(39, 11, "up"))
        self.assertEqual(terminal.decode("\x1b[<65;40;12M"), terminal.Mouse(39, 11, "down"))
        self.assertEqual(terminal.decode("\x1b[<69;40;12M"), terminal.Mouse(39, 11, "down"))
        self.assertEqual(terminal.decode("\x1b[<0;2;3M"), terminal.Mouse(1, 2, "click"))
        self.assertIsNone(terminal.decode("\x1b[<0;2;3m"))
        self.assertIsNone(terminal.decode("\x1b[<32;2;3M"))

    def test_arrows_and_page_keys_without_keypad(self):
        for sequence, key in (("\x1b[A", curses.KEY_UP), ("\x1bOB", curses.KEY_DOWN),
                              ("\x1b[1;5C", curses.KEY_RIGHT), ("\x1b[6~", curses.KEY_NPAGE),
                              ("\x1b[Z", curses.KEY_BTAB)):
            self.assertEqual(terminal.decode(sequence), key)

    def test_reader_restores_blocking_mode(self):
        screen = Mock()
        screen.get_wch.side_effect = list("\x1b[<65;40;12M")
        self.assertEqual(terminal.read(screen), terminal.Mouse(39, 11, "down"))
        screen.timeout.assert_called_with(-1)
        screen.get_wch.side_effect = ["\x1b", curses.error()]
        self.assertEqual(terminal.read(screen), "\x1b")
        screen.timeout.assert_called_with(-1)


class PreviewTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        (self.root / "README.md").write_text("# Hello\n\n**World**\n")
        (self.root / "plain.txt").write_text("\n".join(str(i) for i in range(60)))
        self.nav = Navigator(self.root, "pane", False, "")

    def test_search_requires_slash_and_enter_only_applies(self):
        for char in "random\x13":
            self.nav.key(char, None)
        self.assertEqual(self.nav.query, "")
        self.nav.key("/", None)
        for char in "readme":
            self.nav.key(char, None)
        self.assertTrue(self.nav.searching)
        self.assertEqual(self.nav.items[0].path, "README.md")
        self.nav.key("\n", None)
        self.assertFalse(self.nav.searching)
        self.assertEqual(self.nav.active, "")
        self.nav.key("x", None)
        self.nav.key("\x7f", None)
        self.assertEqual(self.nav.query, "readme")
        self.nav.key("\n", None)
        self.assertEqual(self.nav.active, "README.md")

    def test_search_cancel_restores_filter_and_does_not_close(self):
        self.nav.query = "readme"
        self.nav.key("/", None)
        self.nav.key("\x15", None)
        self.nav.key("x", None)
        self.assertTrue(self.nav.key("\x1b", None))
        self.assertEqual(self.nav.query, "readme")
        self.assertFalse(self.nav.searching)

    def test_raw_mouse_scroll_preview_and_clamps(self):
        self.nav.load("plain.txt")
        self.nav.divider, self.nav.body = 30, 10
        self.nav.handle_mouse(terminal.Mouse(40, 10, "down"))
        self.assertFalse(self.nav.preview_focus)
        self.assertEqual(self.nav.preview_scroll, 3)
        self.nav.handle_mouse(terminal.Mouse(40, 10, "up"))
        self.assertEqual(self.nav.preview_scroll, 0)
        self.nav.preview_scroll = 49
        self.nav.handle_mouse(terminal.Mouse(40, 10, "down"))
        self.assertEqual(self.nav.preview_scroll, 50)

    def test_shared_preview_keys_preserve_focus_tree_and_active_file(self):
        self.nav.load("plain.txt")
        self.nav.body = 10
        self.nav.selected = 1
        self.nav.scroll = 1
        for focused in (False, True):
            self.nav.preview_focus = focused
            self.nav.preview_scroll = 20
            for key, expected in (("\x0e", 21), ("\x10", 20), ("\x06", 30), ("\x02", 20)):
                self.nav.key(key, None)
                self.assertEqual(self.nav.preview_scroll, expected)
                self.assertEqual(self.nav.preview_focus, focused)
                self.assertEqual((self.nav.selected, self.nav.scroll), (1, 1))
                self.assertEqual(self.nav.active, "plain.txt")
        self.nav.preview_focus = False
        self.nav.key("j", None)
        self.assertEqual(self.nav.selected, 2)
        self.assertEqual(self.nav.preview_scroll, 20)

    def test_shared_preview_keys_clamp_rendered_lines_and_empty_content(self):
        self.nav.body = 10
        for key in ("\x0e", "\x10", "\x06", "\x02"):
            self.nav.key(key, None)
            self.assertEqual(self.nav.preview_scroll, 0)
        (self.root / "long.md").write_text("Long paragraph with words. " * 100)
        self.nav.load("long.md")
        self.nav.prepare_preview(25)
        limit = len(self.nav.rendered) - self.nav.body
        self.nav.preview_scroll = limit - 1
        self.nav.key("\x06", None)
        self.assertEqual(self.nav.preview_scroll, limit)
        self.nav.key("\x0e", None)
        self.assertEqual(self.nav.preview_scroll, limit)
        self.nav.preview_scroll = 1
        self.nav.key("\x02", None)
        self.nav.key("\x10", None)
        self.assertEqual(self.nav.preview_scroll, 0)
        self.assertFalse(self.nav.preview_focus)

    def test_shared_preview_keys_do_not_override_input_modes(self):
        self.nav.load("plain.txt")
        self.nav.body = 10
        for mode in ("/", "\x0f", "\x17"):
            self.nav.key(mode, None)
            self.nav.preview_scroll = 20
            for key in ("\x0e", "\x10", "\x06", "\x02"):
                self.nav.key(key, None)
                self.assertEqual(self.nav.preview_scroll, 20)
            self.nav.key("\x1b", None)

    def test_wheel_targets_pointer_without_changing_focus(self):
        self.nav.load("plain.txt")
        self.nav.divider, self.nav.body = 30, 10
        for focus in (False, True):
            for x in (10, 40):
                self.nav.preview_focus = focus
                self.nav.preview_scroll = 20
                self.nav.selected = 0
                self.nav.key(terminal.Mouse(x, 10, "down"), None)
                self.assertEqual(self.nav.preview_focus, focus)
                self.assertEqual(self.nav.preview_scroll, 23 if x == 40 else 20)
                self.assertEqual(self.nav.selected, 0 if x == 40 else len(self.nav.items) - 1)
                self.nav.key(terminal.Mouse(x, 10, "up"), None)
                self.assertEqual(self.nav.preview_focus, focus)
                self.assertEqual(self.nav.preview_scroll, 20)
                self.assertEqual(self.nav.selected, 0)
                self.assertEqual(self.nav.active, "plain.txt")

    def test_wheel_keeps_search_input_and_is_ignored_in_dialogs(self):
        self.nav.load("plain.txt")
        self.nav.divider, self.nav.body = 30, 10
        self.nav.key("/", None)
        self.nav.key("p", None)
        self.nav.key(terminal.Mouse(40, 10, "down"), None)
        self.assertTrue(self.nav.searching)
        self.assertFalse(self.nav.preview_focus)
        self.assertEqual(self.nav.query, "p")
        self.assertEqual(self.nav.preview_scroll, 3)
        self.nav.key("\x1b", None)
        for mode in ("\x0f", "\x17"):
            self.nav.key(mode, None)
            self.nav.key(terminal.Mouse(40, 10, "down"), None)
            self.assertEqual(self.nav.preview_scroll, 3)
            self.nav.key("\x1b", None)

    def test_narrow_wheel_only_scrolls_visible_panel(self):
        self.nav.load("plain.txt")
        self.nav.narrow, self.nav.body = True, 10
        self.nav.selected = 0
        self.nav.key(terminal.Mouse(80, 10, "down"), None)
        self.assertFalse(self.nav.preview_focus)
        self.assertEqual(self.nav.preview_scroll, 0)
        self.assertEqual(self.nav.selected, len(self.nav.items) - 1)
        self.nav.key("\t", None)
        self.nav.key(terminal.Mouse(10, 10, "down"), None)
        self.assertTrue(self.nav.preview_focus)
        self.assertEqual(self.nav.preview_scroll, 3)

    def test_click_still_focuses_preview_or_tree(self):
        self.nav.divider = 30
        self.nav.key(terminal.Mouse(40, 10, "click"), None)
        self.assertTrue(self.nav.preview_focus)
        self.nav.key(terminal.Mouse(10, 4, "click"), None)
        self.assertFalse(self.nav.preview_focus)

    def test_markdown_render_cached_by_width_and_reload(self):
        self.nav.load("README.md")
        with patch("markdown_preview.render", return_value=[[md.Span("Rendered")]]) as render:
            self.nav.prepare_preview(60)
            self.nav.prepare_preview(60)
            render.assert_called_once()
            self.assertEqual(self.nav.content, ["Rendered"])
            self.nav.prepare_preview(40)
            self.assertEqual(render.call_count, 2)
            self.nav.load("README.md")
            self.nav.prepare_preview(40)
            self.assertEqual(render.call_count, 3)

    def test_preview_less_line_page_and_half_page_keys(self):
        self.nav.load("plain.txt")
        self.nav.preview_focus = True
        self.nav.body = 10
        for keys, amount in ((["j", "e", "\x0e", "\n", "\r", curses.KEY_ENTER], 1),
                             (["k", "y", "\x10"], -1),
                             ([" ", "f", "\x06"], 10), (["b", "\x02"], -10),
                             (["d"], 5), (["u", "\x15"], -5)):
            for key in keys:
                with self.subTest(key=key):
                    self.nav.preview_scroll = 20
                    self.nav.key(key, None)
                    self.assertEqual(self.nav.preview_scroll, 20 + amount)
                    self.assertTrue(self.nav.preview_focus)
                    self.assertEqual(self.nav.query, "")

    def test_preview_less_boundaries_and_small_viewport(self):
        self.nav.load("plain.txt")
        self.nav.preview_focus = True
        self.nav.body = 10
        for key in ("G", ">"):
            self.nav.key(key, None)
            self.assertEqual(self.nav.preview_scroll, 50)
            self.nav.key(" ", None)
            self.assertEqual(self.nav.preview_scroll, 50)
        for key in ("g", "<"):
            self.nav.key(key, None)
            self.assertEqual(self.nav.preview_scroll, 0)
            self.nav.key("k", None)
            self.assertEqual(self.nav.preview_scroll, 0)
        self.nav.body = 1
        self.nav.key("d", None)
        self.assertEqual(self.nav.preview_scroll, 1)
        self.nav.body = 100
        self.nav.key("G", None)
        self.assertEqual(self.nav.preview_scroll, 0)

    def test_unbound_pager_keys_do_not_change_files_or_search(self):
        self.nav.load("plain.txt")
        self.nav.preview_scroll = 10
        keys = "efbydugG<>"
        for key in keys:
            self.nav.key(key, None)
        self.assertEqual(self.nav.selected, 0)
        self.assertEqual(self.nav.preview_scroll, 10)
        self.assertEqual(self.nav.query, "")
        self.nav.key("/", None)
        for key in keys:
            self.nav.key(key, None)
        self.assertEqual(self.nav.query, keys)
        self.assertEqual(self.nav.preview_scroll, 10)

    def test_tree_jk_moves_and_clamps_without_searching(self):
        self.nav.key("j", None)
        self.assertEqual(self.nav.selected, 1)
        self.nav.key("j", None)
        self.assertEqual(self.nav.selected, 2)
        self.nav.key("j", None)
        self.assertEqual(self.nav.selected, 2)
        self.nav.key("k", None)
        self.nav.key("k", None)
        self.assertEqual(self.nav.selected, 0)
        self.assertEqual(self.nav.query, "")
        self.assertFalse(self.nav.preview_focus)

    def test_tree_hl_expands_enters_collapses_and_moves_to_parent(self):
        (self.root / "folder" / "nested").mkdir(parents=True)
        (self.root / "folder" / "nested" / "file.txt").write_text("content")
        self.nav.refresh()
        self.nav.selected = next(i for i, row in enumerate(self.nav.items) if row.path == "folder")
        for key, selected in (("l", "folder"), ("l", "folder/nested"),
                              ("l", "folder/nested"), ("l", "folder/nested/file.txt"),
                              ("l", "folder/nested/file.txt"), ("h", "folder/nested"),
                              ("h", "folder/nested"), ("h", "folder"), ("h", "folder")):
            self.nav.key(key, None)
            self.assertEqual(self.nav.items[self.nav.selected].path, selected)
        self.assertEqual(self.nav.expanded, set())
        self.assertFalse(self.nav.preview_focus)

    def test_tree_space_previews_in_changes_mode_without_vimdiff(self):
        for changes in (False, True):
            self.nav.changes = changes
            self.nav.preview_focus = False
            self.nav.selected = next(i for i, row in enumerate(self.nav.items) if row.path == "plain.txt")
            with patch.object(self.nav, "show_diff") as diff, patch.object(self.nav, "edit") as edit:
                self.nav.key(" ", None)
                diff.assert_not_called()
                edit.assert_not_called()
            self.assertEqual(self.nav.active, "plain.txt")
            self.assertFalse(self.nav.preview_focus)
            self.nav.key(" ", None)
            self.assertEqual(self.nav.preview_scroll, 0)
            self.assertFalse(self.nav.preview_focus)
            self.nav.key("\t", None)
            self.assertTrue(self.nav.preview_focus)
            self.nav.key(" ", None)
            self.assertGreater(self.nav.preview_scroll, 0)

    def test_space_keeps_tree_selection_and_following_keys_navigate_files(self):
        self.nav.selected = next(i for i, row in enumerate(self.nav.items) if row.path == "plain.txt")
        selected = self.nav.selected
        self.nav.key(" ", None)
        self.assertEqual(self.nav.selected, selected)
        self.assertEqual(self.nav.active, "plain.txt")
        self.nav.key("j", None)
        self.assertEqual(self.nav.items[self.nav.selected].path, "README.md")
        self.assertEqual(self.nav.active, "plain.txt")
        self.assertEqual(self.nav.preview_scroll, 0)
        self.nav.key(" ", None)
        self.assertEqual(self.nav.active, "README.md")
        self.assertFalse(self.nav.preview_focus)
        self.nav.key("\n", None)
        self.assertTrue(self.nav.preview_focus)

    def test_tree_folder_icons_distinguish_parent_collapsed_and_expanded(self):
        (self.root / "한글 폴더").mkdir()
        (self.root / "한글 폴더" / "child.txt").write_text("content")
        self.nav.refresh()
        for expanded, marker in ((False, "▸  "), (True, "▾  ")):
            with self.subTest(expanded=expanded):
                self.nav.expanded = {"한글 폴더"} if expanded else set()
                self.nav.rebuild()
                with patch("ui.band") as band, patch("ui.put"), patch.object(self.nav, "panel"):
                    self.nav.draw_tree(Mock(), 0, 50, 20)
                labels = [call.args[3] for call in band.call_args_list]
                self.assertTrue(any("↑  .." in label for label in labels))
                self.assertTrue(any(marker + "한글 폴더" in label for label in labels))
                file_labels = [label for label in labels if label.endswith(("plain.txt", "child.txt"))]
                self.assertTrue(file_labels)
                self.assertTrue(all("" not in label and "" not in label for label in file_labels))

    def test_search_results_do_not_show_folder_icons_for_parent_path(self):
        (self.root / "folder").mkdir()
        (self.root / "folder" / "child.txt").write_text("content")
        self.nav.refresh()
        self.nav.query = "child"
        self.nav.rebuild()
        with patch("ui.band") as band, patch("ui.put"), patch.object(self.nav, "panel"):
            self.nav.draw_tree(Mock(), 0, 50, 20)
        label = next(call.args[3] for call in band.call_args_list if "folder/child.txt" in call.args[3])
        self.assertNotIn("", label)
        self.assertNotIn("", label)

    def test_folder_glyphs_reach_terminal_output_without_allowing_controls(self):
        self.assertEqual(clean("\x1b\x00\u202e"), "   ")
        (self.root / "folder").mkdir()
        (self.root / "folder" / "file.txt").write_text("content")
        self.nav.refresh()
        screen = Mock()
        screen.getmaxyx.return_value = (30, 100)
        for expanded, marker in ((False, "▸  folder"), (True, "▾  folder")):
            screen.reset_mock()
            self.nav.expanded = {"folder"} if expanded else set()
            self.nav.rebuild()
            self.nav.draw_tree(screen, 0, 50, 25)
            output = [call.args[2] for call in screen.addstr.call_args_list]
            self.assertTrue(any(marker in line for line in output))
            self.assertTrue(any("↑  .." in line for line in output))

    def test_tree_keys_are_text_in_search_and_ignored_in_resize_dialog(self):
        self.nav.key("\x19", None)
        for key in "hjkl ":
            self.nav.key(key, None)
        self.assertEqual(self.nav.selected, 0)
        self.assertEqual(self.nav.active, "")
        self.nav.key("\x1b", None)
        self.nav.key("/", None)
        for key in "hjkl ":
            self.nav.key(key, None)
        self.assertEqual(self.nav.query, "hjkl ")
        self.assertEqual(self.nav.active, "")

    def test_tree_space_ignores_folders_and_empty_results(self):
        (self.root / "folder").mkdir()
        (self.root / "folder" / "file.txt").write_text("content")
        self.nav.refresh()
        self.nav.selected = next(i for i, row in enumerate(self.nav.items) if row.path == "folder")
        self.nav.key(" ", None)
        self.assertEqual(self.nav.active, "")
        self.assertFalse(self.nav.preview_focus)
        self.nav.query = "no-match"
        self.nav.rebuild()
        for key in "hjkl ":
            self.nav.key(key, None)
        self.assertEqual(self.nav.active, "")
        self.assertEqual(self.nav.query, "no-match")

    def test_preview_less_keys_leave_modal_and_action_shortcuts_intact(self):
        self.nav.load("plain.txt")
        self.nav.preview_focus = True
        self.nav.key("\x19", None)
        self.nav.key("G", None)
        self.assertEqual(self.nav.preview_scroll, 0)
        self.nav.key("\x1b", None)
        with patch.object(self.nav, "show_diff") as diff, patch.object(self.nav, "edit") as edit:
            self.nav.key("\x04", None)
            self.nav.key("\x05", None)
            diff.assert_called_once_with(None)
            edit.assert_called_once_with(None)

    def test_preview_less_keys_use_rendered_markdown_length(self):
        (self.root / "long.md").write_text("A paragraph with words. " * 100)
        self.nav.refresh()
        self.nav.load("long.md")
        self.nav.prepare_preview(25)
        self.nav.preview_focus = True
        self.nav.body = 10
        self.nav.key("G", None)
        self.assertGreater(self.nav.preview_scroll, 0)
        self.assertEqual(self.nav.preview_scroll, len(self.nav.rendered) - 10)

    def test_missing_dependency_and_failed_render_fall_back(self):
        self.nav.load("README.md")
        with patch("markdown_preview.render", side_effect=ImportError("rich")) as render:
            self.nav.prepare_preview(60)
            render.assert_called_once()
        self.assertEqual(self.nav.content[0], "# Hello")
        self.nav.load("README.md")
        with patch("markdown_preview.render", side_effect=ValueError("render failed")) as render:
            self.nav.prepare_preview(60)
            self.nav.prepare_preview(60)
            render.assert_called_once()
        self.assertIsNone(self.nav.rendered)
        self.assertEqual(self.nav.content[0], "# Hello")
        self.nav.load("plain.txt")
        with patch("markdown_preview.render") as render:
            self.nav.prepare_preview(60)
            render.assert_not_called()

    def test_ansi_styles_and_terminal_control_removal(self):
        lines = md.parse_ansi("\x1b[1;38;5;117mTitle\x1b[0m\n\x1b[2J\x1b]8;;https://example.com\x07Link\x1b]8;;\x1b\\")
        self.assertEqual(lines[0][0], md.Span("Title", md.Style(foreground=117, bold=True)))
        self.assertEqual(lines[1], [md.Span("Link")])
        self.assertNotIn("\x1b", str(lines))

    def test_rich_formats_markdown_without_external_commands(self):
        with patch("subprocess.run", side_effect=AssertionError("External renderer")), patch("sys.stdout", new_callable=io.StringIO) as output:
            rendered = md.render("# Hello\n\n**World**\n", 50)
            self.assertEqual(output.getvalue(), "")
        text = "\n".join("".join(span.text for span in line) for line in rendered)
        self.assertIn("Hello", text)
        self.assertIn("World", text)
        self.assertNotIn("**World**", text)
        self.assertTrue(any(span.style != md.Style() for line in rendered for span in line))

    def test_rich_tables_code_unicode_and_width(self):
        from rich.cells import cell_len
        source = "# 문서\n\n| Name | Value |\n|---|---|\n| 한글 | 값 |\n\n```python\ndef hello():\n    return 42\n```\n\n" + "Long paragraph with words. " * 12
        for width in (24, 70):
            rendered = md.render(source, width)
            lines = ["".join(span.text for span in line) for line in rendered]
            self.assertIn("문서", "\n".join(lines))
            self.assertIn("한글", "\n".join(lines))
            self.assertIn("return", "\n".join(lines))
            self.assertTrue(all(cell_len(line) <= width for line in lines))

    def test_rich_drops_file_control_sequences(self):
        rendered = md.render("Hello\x1b[2J\x1b]52;c;secret\x07\x00 world", 40)
        text = "\n".join("".join(span.text for span in line) for line in rendered)
        self.assertIn("Hello world", text)
        self.assertNotIn("secret", text)
        self.assertTrue(all(char.isprintable() or char == "\n" for char in text))

    def test_render_output_is_bounded(self):
        with patch.object(md, "MAX_RENDER_BYTES", 10):
            with self.assertRaisesRegex(ValueError, "preview limit"):
                md.render("# Too much output", 40)
