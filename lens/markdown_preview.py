"""Render Markdown with Rich in memory and retain only safe text styling."""
from __future__ import annotations

from dataclasses import dataclass, replace
import io
import re
import secrets
from theme_colors import resolve as resolve_theme


MAX_RENDER_BYTES = 8 * 1024 * 1024
FOOTNOTE_DEFINITION = re.compile(r"\[\^[^\]\s]+\]:")
BLOCK_ID = re.compile(r"(?:^|[ \t])\^[A-Za-z0-9-]+[ \t]*$")
BLOCK_ID_LINE = re.compile(r"\^[A-Za-z0-9-]+")


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
    link: str = ""  # A web address, or FILE_LINK and a vault file, a Ctrl-click follows.


ESCAPES = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]|\x1b\][^\x07\x1b]*(?:\x07|\x1b\\)")
HYPERLINK = re.compile(r"\x1b\]8;[^;\x07\x1b]*;([^\x07\x1b]*)")
WEB_ADDRESS = re.compile(r"https?://\S+", re.I)
# Internal links carry `FILE_LINK/absolute/path#subpath`; never emitted to the terminal.
FILE_LINK = "lens-file:"
URI_SCHEME = re.compile(r"[A-Za-z][A-Za-z0-9+.-]*:")


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
    link = ""

    def append(value):
        for i, line in enumerate(value.split("\n")):
            if i:
                lines.append([])
            cleaned = "".join(char for char in line.expandtabs(4) if char.isprintable())
            if cleaned:
                if lines[-1] and (lines[-1][-1].style, lines[-1][-1].link) == (style, link):
                    lines[-1][-1] = Span(lines[-1][-1].text + cleaned, style, link)
                else:
                    lines[-1].append(Span(cleaned, style, link))

    end = 0
    for escape in ESCAPES.finditer(text):
        append(text[end:escape.start()])
        token = escape[0]
        if token.startswith("\x1b[") and token.endswith("m"):
            style = sgr(style, token[2:-1])
        elif hyperlink := HYPERLINK.match(token):
            target = hyperlink[1]
            link = target if WEB_ADDRESS.fullmatch(target) or target.startswith(FILE_LINK) else ""
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


def preview_tokens(text: str, vault=None, depth=0, seen=frozenset()):
    """Markdown tokens; with an obsidian_embeds.Vault, embeds of notes and images too."""
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
    tokens = hide_block_ids(tokens)
    if vault is None:
        return tokens
    internal_links(tokens, vault)
    return transclude(tokens, vault, depth, seen)


def internal_links(tokens, vault):
    """Resolve wiki links and Markdown links to vault files now, while each note's own
    folder is known; an embedded note's links are relative to that note."""
    from urllib.parse import unquote
    from obsidian_embeds import split_target

    for token in tokens:
        for child in token.children or []:
            if child.type == "wikilink":
                target = child.meta["target"]
            elif child.type == "link_open":
                target = str(child.attrs.get("href", ""))
                if URI_SCHEME.match(target):
                    continue  # Web and mail addresses are not vault files.
                target = unquote(target)
            else:
                continue
            name, subpath = split_target(target)
            # `[[#Heading]]` points into the note that holds it.
            path = vault.find(name) if name else vault.current
            if path is not None:
                child.meta = {**(child.meta or {}), "file": f"{FILE_LINK}{path}#{subpath}"}


def hide_block_ids(tokens):
    """Drop Obsidian's `^block-id` markers, as its reading view does."""
    result, index = [], 0
    while index < len(tokens):
        window = tokens[index:index + 3]
        if ([token.type for token in window] == ["paragraph_open", "inline", "paragraph_close"]
                and BLOCK_ID_LINE.fullmatch(window[1].content.strip())):
            index += 3  # An ID on its own line, naming the block above.
            continue
        token = tokens[index]
        last = (token.children or [None])[-1] if token.type == "inline" else None
        if last is not None and last.type == "text" and (marker := BLOCK_ID.search(last.content)):
            last.content = last.content[:marker.start()]
        result.append(token)
        index += 1
    return result


def embed_paragraph(tokens):
    """The embeds of a paragraph that holds nothing else, else None."""
    if [token.type for token in tokens] != ["paragraph_open", "inline", "paragraph_close"]:
        return None
    children = tokens[1].children or []
    embeds = [child for child in children if child.type == "obsidian_embed"]
    rest = all(child.type in ("obsidian_embed", "softbreak", "hardbreak")
               or (child.type == "text" and not child.content.strip()) for child in children)
    return embeds if embeds and rest else None


def transclude(tokens, vault, depth, seen):
    # Only an embed alone in its paragraph is replaced, as Obsidian shows it as a block;
    # one inside a sentence, list text or table cell keeps its placeholder.
    from markdown_it.token import Token
    import obsidian_embeds as embeds

    def placeholder(embed, opening):
        inline = Token("inline", "", 0, content=embed.content, map=opening.map,
                       level=opening.level + 1, children=[embed])
        return [Token("paragraph_open", "p", 1, map=opening.map, level=opening.level, block=True),
                inline, Token("paragraph_close", "p", -1, level=opening.level, block=True)]

    result, index = [], 0
    while index < len(tokens):
        found = embed_paragraph(tokens[index:index + 3])
        if found is None:
            result.append(tokens[index])
            index += 1
            continue
        opening = tokens[index]
        index += 3
        for embed in found:
            name, subpath = embeds.split_target(embed.meta["target"])
            path = vault.find(name)
            suffix = path.suffix.lower() if path else ""
            if suffix in embeds.IMAGE_SUFFIXES:
                try:
                    changed = path.stat().st_mtime_ns  # A new key re-renders an edited image.
                except OSError:
                    result += placeholder(embed, opening)
                    continue
                width, height = embeds.image_size(embed.meta.get("alias", "")) or (0, 0)
                result.append(Token("obsidian_image", "img", 0, content=embed.content, map=opening.map,
                                    level=opening.level, block=True,
                                    info="\n".join(map(str, (path, width, height, changed)))))
                continue
            key = (path, subpath)
            text = (vault.note(path, subpath) if suffix in embeds.NOTE_SUFFIXES
                    and depth < embeds.MAX_DEPTH and key not in seen else None)
            if text is None:
                result += placeholder(embed, opening)
                continue
            title = embed.meta.get("alias") or embed.meta["target"]
            result.append(Token("obsidian_note_open", "section", 1, meta={"title": title},
                                level=opening.level, block=True))
            result += preview_tokens(clean_source(text), vault.at(path), depth + 1, seen | {key})
            result.append(Token("obsidian_note_close", "section", -1, level=opening.level, block=True))
    return result


def clean_source(text: str) -> str:
    # Do not interpret file-supplied terminal escapes as renderer output.
    text = ESCAPES.sub("", text)
    return "".join(char for char in text if char.isprintable() or char in "\n\t")


def diagram_key(token):
    """(language, source) for a fenced block in a known diagram language, else None."""
    from diagram_preview import fence_language
    if token.type == "obsidian_image":
        return ("image", token.info)
    language = fence_language(token.info) if token.type == "fence" else None
    return (language, token.content) if language else None


def diagram_blocks(text: str, vault=None) -> list[tuple[str, str]]:
    return [key for token in preview_tokens(clean_source(text), vault) if (key := diagram_key(token))]


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


def link_tokens(tokens):
    """Keep Rich's `text (destination)` link layout, but tag both parts of a web link
    with its address; Rich only emits hyperlinks when it drops the destination."""
    from markdown_it.token import Token

    def styled(tag, children, href=None):
        opened = [Token("link_open", "a", 1, attrs={"href": href})] if href else []
        closed = [Token("link_close", "a", -1)] if href else []
        # Rich styles an unknown token by its tag; a `link_open` type would read as a real link.
        return [*opened, Token(f"styled_{tag}_open", tag, 1), *children,
                Token(f"styled_{tag}_close", tag, -1), *closed]

    for token in tokens:
        children, token.children, link = token.children or [], token.children and [], None
        for child in children:
            if child.type == "link_open":
                link = (str(child.attrs.get("href", "")), [], (child.meta or {}).get("file"))
            elif child.type == "link_close" and link:
                href, inner, file = link
                web = href if WEB_ADDRESS.fullmatch(href) else file
                token.children += [*styled("link", inner, web), Token("text", "", 0, content=" ("),
                                   *styled("link_url", [Token("text", "", 0, content=href)], web),
                                   Token("text", "", 0, content=")")]
                link = None
            elif link:
                link[1].append(child)
            elif child.type == "wikilink" and (child.meta or {}).get("file"):
                token.children += [Token("link_open", "a", 1, attrs={"href": child.meta["file"]}), child,
                                   Token("link_close", "a", -1)]
            else:
                token.children.append(child)
    return tokens


def render(text: str, width: int, colors=None, vault=None) -> list[list[Span]]:
    return render_diagrams(text, width, colors, vault=vault)[0]


def render_diagrams(text: str, width: int, colors=None, diagrams=None, vault=None):
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
        markdown = markdown_type()("", code_theme=CodeTheme(), hyperlinks=True)
        markdown.markup = text
        markdown.parsed, found = replace_diagrams(link_tokens(preview_tokens(text, vault)), diagrams or {}, marker)
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
