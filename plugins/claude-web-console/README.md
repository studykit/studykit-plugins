# claude-web-console

Mirror your Claude Code conversation into a **local web page** and render
**renderable fenced code blocks** as rich output. Assistant text streams live;
diagrams render when a message finishes.

**Claude Code only.**

## What it renders

- ` ```plantuml ` fenced blocks → diagrams, rendered by a **local** PlantUML
  server (nothing leaves your machine).
- ` ```math ` fenced blocks and `$$ … $$` / `$ … $` → math, rendered with KaTeX.
- Everything else → Markdown.

New renderers key off the fenced block's info-string, so more types can be added.

## Requirements

- Claude Code with this plugin enabled.
- Python 3 (the web server uses only the standard library) and `uv`.
- Optional, for PlantUML diagrams: a Java runtime and a `plantuml.jar`. Without
  them, Markdown and math still render; diagrams show an "engine unavailable"
  placeholder.

## Install

Enable `claude-web-console` from the `studykit-plugins` marketplace.

## Use

1. In a Claude Code session, run the command:

   ```
   /web-console
   ```

   This starts the local web server (and the PlantUML engine if Java + a jar are
   available) and opens the viewer in your browser.

2. Keep chatting. Your prompts and Claude's responses appear in the page in real
   time; PlantUML and math blocks render as rich output.

If the server is not running, the plugin stays completely silent and never
affects your conversation.

## Configuration

Set these environment variables before running `/web-console` to override
defaults:

| Variable | Purpose | Default |
| --- | --- | --- |
| `CLAUDE_WEB_CONSOLE_PORT` | Web server port | `8477` |
| `CLAUDE_WEB_CONSOLE_PLANTUML_PORT` | Local PlantUML server port | `8478` |
| `CLAUDE_WEB_CONSOLE_PLANTUML_JAR` | Path to your `plantuml.jar` | auto-detected |

## Notes

- Rendering libraries load from a public CDN; your conversation text is served
  only from the local server and is not sent anywhere.
- The viewer is currently read-only.
