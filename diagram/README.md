# Diagram Plugin

Create, explain, validate, and render diagrams as code with one skill that covers three
engines:

- **PlantUML** — UML (sequence, class, activity, state, use case, timing, …), Gantt, mind
  map, WBS, network, JSON/YAML, C4-PlantUML, and more
- **D2** — architecture and flow diagrams, SQL tables, grid layouts, themes, sketch style
- **Structurizr DSL** — C4 model workspaces with system landscape, context, container,
  component, deployment, and dynamic views

The skill picks the engine you name, the one an existing file or Markdown block already
uses, or the best fit for what you asked to draw.

Supported hosts: Claude Code and Codex.

## Installation

Install `diagram` from the Studykit marketplace in Claude Code or Codex.

## Prerequisites

| Engine | Needs |
|---|---|
| PlantUML | The `plantuml` CLI (`brew install plantuml`). Without it, a pinned PlantUML jar is downloaded to `~/.cache/studykit-diagram/` on first use, which needs Java. |
| D2 | `brew install d2` |
| Structurizr | `brew install structurizr`. PNG/SVG output also uses PlantUML. |

An online PlantUML check is available as a last resort. It sends the diagram source to the
public plantuml.com server, so the skill asks before using it.

## Usage

The skill has three modes. It infers the mode from your request when you do not give one.

- **create** — write a standalone `.puml`, `.d2`, or `.dsl` file, or a fenced
  `plantuml` / `d2` / `structurizr` block in a Markdown file, then validate it. D2 and
  Structurizr diagrams are also rendered to PNG.
- **reference** — explain syntax with a minimal example, without writing files.
- **check** — validate a source file, or every diagram block in a Markdown file, and
  explain any failure.

Claude Code:

```text
/diagram:diagram create sequence diagram of order processing
/diagram:diagram reference d2 sql_table syntax
/diagram:diagram check docs/architecture.md
```

Codex: mention `$diagram`, or just ask.

You can also ask naturally:

> Draw a C4 container diagram for our checkout system in Structurizr
> Show me the PlantUML syntax for a Gantt chart
> Validate the diagrams in this Markdown file
