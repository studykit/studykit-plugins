"""Render Markdown with Rich in memory and retain only safe text styling."""
from __future__ import annotations

from dataclasses import dataclass, replace
import io
import re
import secrets
from theme_colors import resolve as resolve_theme


MAX_RENDER_BYTES = 8 * 1024 * 1024
FOOTNOTE_DEFINITION = re.compile(r"\[\^[^\]\s]+\]:")


@dataclass(frozen=True)
class Style:
    foreground: int = -1
    background: int = -1
    bold: bool = False
    italic: bool = False
    underline: bool = False


@dataclass(frozen=True)
class Span:
    text: str
    style: Style = Style()


ESCAPES = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]|\x1b\][^\x07\x1b]*(?:\x07|\x1b\\)")


def sgr(style: Style, parameters: str) -> Style:
    try:
        codes = [int(item or 0) for item in parameters.split(";")]
    except ValueError:
        return style
    i = 0
    while i < len(codes):
        code = codes[i]
        if code == 0:
            style = Style()
        elif code in (1, 3, 4, 22, 23, 24):
            field = {1: "bold", 3: "italic", 4: "underline", 22: "bold", 23: "italic", 24: "underline"}[code]
            style = replace(style, **{field: code < 20})
        elif code in (39, 49):
            style = replace(style, **{"foreground" if code == 39 else "background": -1})
        elif 30 <= code <= 37 or 90 <= code <= 97:
            style = replace(style, foreground=code - (30 if code < 90 else 82))
        elif 40 <= code <= 47 or 100 <= code <= 107:
            style = replace(style, background=code - (40 if code < 100 else 92))
        elif code in (38, 48) and i + 2 < len(codes):
            color = None
            if codes[i + 1] == 5:
                color = max(0, min(255, codes[i + 2]))
                i += 2
            elif codes[i + 1] == 2 and i + 4 < len(codes):
                r, g, b = [max(0, min(255, value)) for value in codes[i + 2:i + 5]]
                color = 232 + round(r / 255 * 23) if r == g == b else 16 + 36 * round(r / 51) + 6 * round(g / 51) + round(b / 51)
                i += 4
            if color is not None:
                style = replace(style, **{"foreground" if code == 38 else "background": color})
        i += 1
    return style


def parse_ansi(text: str) -> list[list[Span]]:
    lines: list[list[Span]] = [[]]
    style = Style()

    def append(value):
        for i, line in enumerate(value.split("\n")):
            if i:
                lines.append([])
            cleaned = "".join(char for char in line.expandtabs(4) if char.isprintable())
            if cleaned:
                if lines[-1] and lines[-1][-1].style == style:
                    lines[-1][-1] = Span(lines[-1][-1].text + cleaned, style)
                else:
                    lines[-1].append(Span(cleaned, style))

    end = 0
    for escape in ESCAPES.finditer(text):
        append(text[end:escape.start()])
        token = escape[0]
        if token.startswith("\x1b[") and token.endswith("m"):
            style = sgr(style, token[2:-1])
        end = escape.end()
    append(text[end:])
    return lines


class BoundedOutput(io.StringIO):
    def __init__(self):
        super().__init__()
        self.bytes_written = 0

    def write(self, text):
        self.bytes_written += len(text.encode("utf-8"))
        if self.bytes_written > MAX_RENDER_BYTES:
            raise ValueError("Markdown output exceeded the preview limit")
        return super().write(text)


def preview_tokens(text: str):
    from markdown_it import MarkdownIt
    from markdown_it.rules_block import reference
    from obsidian_markdown import install

    def link_reference(state, start_line, end_line, silent):
        start = state.bMarks[start_line] + state.tShift[start_line]
        # Rich has no footnote renderer. Keep definitions visible instead of
        # letting URL-only footnotes disappear as ordinary link definitions.
        if FOOTNOTE_DEFINITION.match(state.src, start):
            return False
        return reference(state, start_line, end_line, silent)

    parser = MarkdownIt().enable("strikethrough").enable("table")
    parser.block.ruler.at("reference", link_reference)
    install(parser)
    tokens = parser.parse(text)
    for token in tokens:
        children = token.children or []
        for child in children:
            if child.type == "html_inline" and re.fullmatch(r"<br\s*/?>", child.content, re.I):
                child.type, child.tag, child.content = "hardbreak", "br", ""
        for current, following in zip(children, children[1:]):
            if (current.type == "softbreak" and following.type == "text"
                    and FOOTNOTE_DEFINITION.match(following.content)):
                current.type = "hardbreak"
                current.tag = "br"
    return tokens


def clean_source(text: str) -> str:
    # Do not interpret file-supplied terminal escapes as renderer output.
    text = ESCAPES.sub("", text)
    return "".join(char for char in text if char.isprintable() or char in "\n\t")


def diagram_key(token):
    """(language, source) for a fenced block in a known diagram language, else None."""
    from diagram_preview import fence_language
    language = fence_language(token.info) if token.type == "fence" else None
    return (language, token.content) if language else None


def diagram_blocks(text: str) -> list[tuple[str, str]]:
    return [key for token in preview_tokens(clean_source(text)) if (key := diagram_key(token))]


def replace_diagrams(tokens, diagrams, marker):
    # Swap each rendered diagram fence for a one-word paragraph; its rendered
    # line is later replaced by blank rows the image is drawn over.
    from markdown_it.token import Token
    result, found = [], []
    for token in tokens:
        key = diagram_key(token)
        if key not in diagrams:
            result.append(token)
            continue
        word = f"{marker}{len(found)}"
        found.append(key)
        inline = Token("inline", "", 0, content=word, map=token.map, level=token.level + 1, block=True,
                       children=[Token("text", "", 0, content=word)])
        result += [Token("paragraph_open", "p", 1, map=token.map, level=token.level, block=True), inline,
                   Token("paragraph_close", "p", -1, level=token.level, block=True)]
    return result, found


def render(text: str, width: int, colors=None) -> list[list[Span]]:
    return render_diagrams(text, width, colors)[0]


def render_diagrams(text: str, width: int, colors=None, diagrams=None):
    """Render Markdown; diagram fences whose (language, source) maps to a row count
    in `diagrams` become that many blank lines, reported as (line, key, rows)."""
    # Import lazily so a broken/missing dependency can fall back to source text.
    from rich.console import Console
    from obsidian_markdown import markdown_type
    from rich.theme import Theme
    from rich.style import Style as RichStyle
    from rich.syntax import SyntaxTheme
    from syntax_preview import token_style

    colors = colors or resolve_theme()
    c = colors.rich
    styles = {
        "markdown.h1": f"bold {c('accent')}",
        "markdown.h1.border": c("overlay0"),
        "markdown.h2": f"bold {c('accent')}",
        "markdown.h3": f"bold {c('mauve')}",
        "markdown.h4": f"bold {c('mauve')}",
        "markdown.h5": f"bold {c('mauve')}",
        "markdown.h6": f"bold {c('mauve')}",
        "markdown.code": f"{c('peach')} on {c('surface_dim')}",
        "markdown.link": f"underline {c('accent')}",
        "markdown.link_url": c("subtext0"),
        "markdown.block_quote": c("subtext0"),
        "markdown.hr": c("overlay0"),
        "markdown.table.border": c("overlay0"),
        "markdown.table.header": f"bold {c('accent')}",
        "markdown.wikilink": f"underline {c('accent')}",
        "markdown.embed": f"italic {c('subtext0')}",
        "markdown.mark": f"bold {c('text')} on {c('surface1')}",
        "markdown.checked": f"bold {c('green')}",
        "markdown.unchecked": c("subtext0"),
    }
    for color, kinds in {
        "accent": "note info todo",
        "teal": "abstract summary tldr tip hint important",
        "green": "success check done",
        "yellow": "question help faq warning caution attention",
        "red": "failure fail missing danger error bug",
        "mauve": "example",
        "subtext0": "quote cite",
    }.items():
        for kind in kinds.split():
            styles[f"markdown.callout.{kind}"] = f"bold {c(color)}"
    palette = Theme(styles)

    class CodeTheme(SyntaxTheme):
        def get_background_style(self):
            return RichStyle(bgcolor=c("surface_dim"))

        def get_style_for_token(self, token_type):
            style = token_style(token_type, colors)
            foreground = "default" if style.foreground < 0 else f"color({style.foreground})"
            return RichStyle(color=foreground, bold=style.bold, italic=style.italic, underline=style.underline)
    text = clean_source(text)
    marker = "LD" + secrets.token_hex(3)
    while marker in text:
        marker = "LD" + secrets.token_hex(3)
    with BoundedOutput() as output:
        console = Console(file=output, width=max(10, width), color_system="256",
                          force_terminal=True, force_jupyter=False, legacy_windows=False,
                          no_color=False, markup=False, highlight=False, emoji=False,
                          theme=palette)
        markdown = markdown_type()("", code_theme=CodeTheme(), hyperlinks=False)
        markdown.markup = text
        markdown.parsed, found = replace_diagrams(preview_tokens(text), diagrams or {}, marker)
        console.print(markdown)
        lines = parse_ansi(output.getvalue())
    if not found:
        return lines, []
    result, placements = [], []
    for line in lines:
        match = re.search(re.escape(marker) + r"(\d+)", "".join(span.text for span in line))
        if match and int(match[1]) < len(found):
            source = found[int(match[1])]
            placements.append((len(result), source, diagrams[source]))
            result += [[] for _ in range(diagrams[source])]
        else:
            result.append(line)
    return result, placements
