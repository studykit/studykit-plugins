# Autodesk Plugin for Claude Code

Claude Code plugin for Autodesk Inventor API development and automation.

## Overview

This plugin provides comprehensive Inventor API documentation and development assistance, enabling Claude to:

- Answer questions about Inventor API concepts and architecture
- Look up API classes, methods, properties, and enumerations
- Write working C#, VBA, and Python code for Inventor automation
- Provide sample code and best practices

## Features

### Skills (3)

| Skill | Description |
|-------|-------------|
| **inventor-user-manual** | API concepts, architecture, development workflows |
| **inventor-api-reference** | Class/method/enum lookup, object model hierarchy |
| **inventor-samples** | Working code examples and samples |

### Agent (1)

| Agent | Description |
|-------|-------------|
| **inventor-api-guide** | Autonomous API documentation search and code writing |

## Installation

### Option 1: Plugin Directory
```bash
claude --plugin-dir /path/to/autodesk-plugin
```

### Option 2: Project Plugin
Copy to your project's `.claude-plugin/` directory.

## Usage Examples

### Ask about API concepts
```
"How do I create a sketch in Inventor API?"
"What is the Inventor object model for assemblies?"
```

### Look up API reference
```
"What properties does ExtrudeFeature have?"
"Show me PartFeatureOperationEnum values"
```

### Request code
```
"Write Python code to create a 10cm cube in Inventor"
"Create C# code to traverse assembly structure"
```

## Documentation Structure

```
autodesk-plugin/
├── .claude-plugin/
│   └── plugin.json
├── agents/
│   └── inventor-api-guide.md
└── skills/
    ├── inventor-api-reference/
    │   ├── images/
    │   ├── references/
    │   └── SKILL.md
    ├── inventor-samples/
    │   ├── images/
    │   ├── references/
    │   └── SKILL.md
    └── inventor-user-manual/
        ├── images/
        ├── references/
        └── SKILL.md
```

## Supported Languages

- **C#** (.NET Add-In)
- **VBA** (Inventor macros)

## Requirements

- Autodesk Inventor 2026 (or compatible version)
- .NET 8

## Future Plans

- Fusion 360 API support
- AutoCAD API support

## License

MIT
