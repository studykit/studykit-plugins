import curses
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from ls_colors import directory_style
from markdown_preview import Style
from theme_colors import resolve
from ui import theme
import herdr_main


class DirectoryColorTests(unittest.TestCase):
    def test_native_defaults(self):
        self.assertEqual(directory_style({}, "darwin"), Style(foreground=4))
        self.assertEqual(directory_style({}, "freebsd14"), Style(foreground=4))
        self.assertEqual(directory_style({}, "linux"), Style(foreground=4, bold=True))

    def test_bsd_pairs_and_default_colors(self):
        self.assertEqual(directory_style({"LSCOLORS": "exfxcxdxbxegedabagacad"}, "darwin"), Style(foreground=4))
        self.assertEqual(directory_style({"LSCOLORS": "Cx"}, "darwin"), Style(foreground=2, bold=True))
        self.assertEqual(directory_style({"LSCOLORS": "eB"}, "darwin"), Style(foreground=4, background=1, underline=True))
        self.assertEqual(directory_style({"LSCOLORS": "xx"}, "darwin"), Style())

    def test_gnu_precedence_and_extended_colors(self):
        self.assertEqual(directory_style({"LS_COLORS": "fi=0:di=01;36", "LSCOLORS": "ex"}, "darwin"),
                         Style(foreground=6, bold=True))
        self.assertEqual(directory_style({"LS_COLORS": "di=38;5;123;48;5;234"}, "linux"),
                         Style(foreground=123, background=234))
        self.assertEqual(directory_style({"LS_COLORS": "di=38;2;255;0;0"}, "linux").foreground, 196)
        self.assertEqual(directory_style({"LS_COLORS": "di=31:di=32"}, "linux").foreground, 2)

    def test_explicit_reset_and_empty_setting(self):
        for value in ("", "0", "00", "1;34;0"):
            self.assertEqual(directory_style({"LS_COLORS": "di=" + value}, "linux"), Style())

    def test_invalid_settings_and_escape_injection(self):
        for env in ({"LS_COLORS": "di=\x1b[31m"}, {"LS_COLORS": "di=bad"},
                    {"LS_COLORS": "di=" + "1;" * 200}, {"LSCOLORS": "z?"}, {"LSCOLORS": "e"}):
            self.assertIsNone(directory_style(env, "darwin"))

    def test_curses_folder_colors_and_selection_theme(self):
        palette = resolve()
        with patch("curses.has_colors", return_value=True), patch("curses.start_color"), \
             patch("curses.use_default_colors"), patch("curses.COLORS", 256, create=True), \
             patch("curses.COLOR_PAIRS", 256, create=True), patch("curses.init_pair") as pair, \
             patch("curses.color_pair", side_effect=lambda value: value << 8):
            styles = theme(palette, Style(foreground=4, bold=True))
            pair.assert_any_call(8, 4, palette["panel_bg"])
            pair.assert_any_call(6, palette["text"], palette["selection_bg"])
            self.assertTrue(styles["folder"] & curses.A_BOLD)
            theme(palette, None)
            pair.assert_any_call(8, palette["text"], palette["panel_bg"])

    def test_adapter_passes_exported_directory_style_to_ui(self):
        env = {"HERDR_ENV": "1", "LS_COLORS": "di=01;36"}
        with patch("herdr_main.source", return_value=("pane", Path.cwd())), \
             patch("ui.Navigator") as navigator, patch("curses.wrapper"):
            self.assertEqual(herdr_main.main(env, "panel"), 0)
        self.assertEqual(navigator.call_args.kwargs["folder_style"], Style(foreground=6, bold=True))


if __name__ == "__main__":
    unittest.main()
