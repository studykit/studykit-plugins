import curses
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import herdr_main
import markdown_preview as md
import terminal_input
import theme_colors as colors
from ui import Navigator, theme


class ThemeTests(unittest.TestCase):
    def test_all_builtin_palettes_and_aliases(self):
        self.assertEqual(len(colors.BUILTINS), 18)
        for name in colors.BUILTINS:
            palette = colors.resolve({"theme": {"name": name}})
            self.assertEqual(palette.name, name)
            self.assertEqual(len(palette.colors), 19)
            self.assertTrue(all(-1 <= color < 256 for color in palette.colors.values()))
        self.assertEqual(colors.resolve().name, "catppuccin")
        self.assertEqual(colors.resolve({"theme": {"name": "Tokyo_Night"}}).name, "tokyo-night")
        self.assertEqual(colors.resolve({"theme": {"name": "latte"}}).name, "catppuccin-latte")

    def test_color_formats_and_defaults(self):
        self.assertEqual(colors.parse_color("#89b4fa"), colors.parse_color("rgb(137, 180, 250)"))
        self.assertEqual(colors.parse_color("#abc"), colors.parse_color("#aabbcc"))
        self.assertEqual(colors.parse_color("reset"), -1)
        self.assertEqual(colors.parse_color("lightred"), 9)
        self.assertEqual(colors.parse_color("white"), 15)
        self.assertEqual(colors.parse_color("rgb(999,0,0)"), 6)

    def test_custom_and_legacy_accent_precedence(self):
        config = {"theme": {"custom": {"text": "#123456", "panel_bg": "reset"}}, "ui": {"accent": "red"}}
        palette = colors.resolve(config)
        self.assertEqual(palette["text"], colors.parse_color("#123456"))
        self.assertEqual(palette["panel_bg"], -1)
        self.assertEqual(palette["accent"], 1)
        config["theme"]["custom"]["accent"] = "green"
        self.assertEqual(colors.resolve(config)["accent"], 2)

    def test_auto_switch_siblings_and_mode_overrides(self):
        config = {"theme": {"name": "tokyo-night", "auto_switch": True,
                            "custom": {"accent": "blue", "light": {"accent": "red"}}}}
        self.assertEqual(colors.resolve(config, "dark").name, "tokyo-night")
        self.assertEqual(colors.resolve(config, "light").name, "tokyo-night-day")
        self.assertEqual(colors.resolve(config, "light")["accent"], 1)
        config["theme"]["light_name"] = "solarized-light"
        self.assertEqual(colors.resolve(config, "light").name, "solarized-light")
        config["theme"]["light_name"] = "unknown"
        self.assertEqual(colors.resolve(config, "light").name, "catppuccin-latte")

    def test_adapter_reads_explicit_config_and_handles_invalid_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "settings.toml"
            path.write_text('[theme]\nname = "nord"\n[keys]\nprefix = "ctrl+s"\n')
            config = herdr_main.theme_config({"HERDR_CONFIG_PATH": str(path)})
            self.assertEqual(config, {"theme": {"name": "nord"}})
            path.write_text("[broken")
            self.assertEqual(herdr_main.theme_config({"HERDR_CONFIG_PATH": str(path)}), {})

    def test_terminal_theme_preserves_terminal_defaults(self):
        palette = colors.resolve({"theme": {"name": "terminal"}})
        self.assertEqual(palette["text"], -1)
        self.assertEqual(palette["panel_bg"], -1)
        self.assertEqual(colors.terminal_color(-1, 8), -1)
        self.assertEqual(colors.terminal_color(-1, 8, False, background=True), 0)
        self.assertLess(colors.terminal_color(250, 8), 8)
        with patch("curses.has_colors", return_value=True), patch("curses.start_color"), \
             patch("curses.use_default_colors"), patch("curses.COLORS", 256, create=True), \
             patch("curses.COLOR_PAIRS", 256, create=True), patch("curses.init_pair") as pair, \
             patch("curses.color_pair", side_effect=lambda value: value << 8):
            result = theme(palette)
            pair.assert_any_call(1, -1, -1)
            self.assertTrue(result["selected"] & curses.A_REVERSE)

    def test_markdown_uses_theme_heading_and_code_colors(self):
        for name in ("catppuccin", "catppuccin-latte", "terminal"):
            palette = colors.resolve({"theme": {"name": name}})
            lines = md.render("# Title\n\n```python\ndef hello():\n    return 42\n```", 50, palette)
            spans = [span for line in lines for span in line]
            self.assertTrue(any("Title" in span.text and span.style.foreground == palette["accent"] for span in spans))
            self.assertTrue(any("def" in span.text and span.style.foreground == palette["mauve"] for span in spans))
            self.assertTrue(any(span.style.background == palette["surface_dim"] for span in spans))

    def test_appearance_reports_and_refresh_retheme_without_moving_focus(self):
        self.assertEqual(terminal_input.decode("\x1b[?997;2n"), terminal_input.Appearance("light"))
        config = {"theme": {"auto_switch": True}}
        with tempfile.TemporaryDirectory() as directory:
            nav = Navigator(Path(directory), "pane", False, "", theme_loader=lambda: config)
            nav.preview_focus = True
            nav.render_width = 50
            nav.key(terminal_input.Appearance("light"), None)
            self.assertEqual(nav.palette.name, "catppuccin-latte")
            self.assertIsNone(nav.render_width)
            self.assertTrue(nav.preview_focus)
            config["theme"] = {"name": "nord"}
            nav.refresh()
            self.assertEqual(nav.palette.name, "nord")
