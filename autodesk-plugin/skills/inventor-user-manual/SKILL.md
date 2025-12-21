---
name: Inventor User Manual
description: This skill should be used when the user asks about "Inventor API concepts", "how to use Inventor API", "VBA programming in Inventor", "creating Inventor add-ins", "Inventor sketches", "Inventor features", "Inventor assembly", "Inventor drawings", "Inventor BOM", "iLogic programming", "Inventor customization", "Inventor automation basics", or needs to understand Inventor API architecture, object model, and development workflows. Provides comprehensive guidance from Autodesk Inventor API User's Manual.
version: 0.1.0
---

# Inventor API User's Manual

This skill provides access to Autodesk Inventor's official API User's Manual documentation, covering concepts, workflows, and programming guidance for Inventor automation and customization.

## Overview

The Inventor API User's Manual contains comprehensive documentation for:

- **API Fundamentals**: Programming concepts, object model, and development setup
- **Object Model**: Complete hierarchy of all Inventor API objects
- **Part & Assembly Modeling**: Sketches, features, assemblies, BOM
- **Drawings**: Views, dimensions, balloons, tables
- **User Interface Customization**: Ribbon, dialogs, browser, environments
- **Custom Data**: iProperties, attributes
- **Transactions**: Undo support, change processing

## Reference Files Location

All user manual documentation is located in the `references/` folder within this skill directory. Reference files using relative paths like `references/GettingStarted.md`.

## Document Categories

### API Overviews

Foundational documents for getting started:

| File | Content |
|------|---------|
| `GettingStarted.md` | API introduction, object model, programming basics |
| `VBA_Overview.md` | VBA programming in Inventor |
| `CreatingAnAddIn_Overview.md` | Creating C#/VB.NET add-ins |
| `ConvertingToRegFree_Overview.md` | Registry-free add-in deployment |
| `PortToNetCore_Overview.md` | Migrating to .NET 8 (Inventor 2025+) |
| `UsingSDK.md` | SDK installation and tools |

### General Concepts

Core concepts applicable across all Inventor programming:

| File | Content |
|------|---------|
| `UOM_Overview.md` | Units of measure, conversion |
| `TransientGeometry_Overview.md` | Geometry objects, matrices, vectors |
| `Proxies_Overview.md` | Proxy objects in assemblies |
| `FileAndDocReferences_Overview.md` | File references, document management |
| `ConsistentMaterials_Overview.md` | Materials and appearances |

### Object Model Hierarchy

Read this file to understand the complete API object hierarchy:
- **`InventorObjectModel.md`**

This document contains:
- Object relationships and inheritance
- Document types (Part, Assembly, Drawing, Presentation)
- Feature types and their collections
- Constraint types (Mate, Angle, Tangent, etc.)
- Sketch objects (2D and 3D)
- Work features (WorkPlane, WorkAxis, WorkPoint)
- B-Rep topology (Face, Edge, Vertex)
- User interface objects
- Transient geometry objects

### Part and Assembly Modeling

Core modeling operations:

| File | Content |
|------|---------|
| `Sketch_Overview.md` | Creating and editing sketches |
| `SketchConstraints_Overview.md` | Geometric and dimensional constraints |
| `Features_Overview.md` | Extrude, revolve, sweep, loft, etc. |
| `WorkFeatures_Overview.md` | Work planes, axes, points |
| `BRep_Overview.md` | B-Rep topology (faces, edges, vertices) |
| `AssemblingParts_Overview.md` | Assembly constraints, joints, occurrences |
| `BOM_Overview.md` | Bill of Materials programming |
| `ModelStates_Overview.md` | Level of Detail, Design Views |

### Drawings

Drawing document automation:

| File | Content |
|------|---------|
| `DrawingViews_Overview.md` | Creating and manipulating drawing views |
| `DrawingDimensions_Overview.md` | Dimension placement and formatting |
| `Balloons_Overview.md` | Balloon annotations |
| `CustomTables_Overview.md` | Custom table creation |

### User Interface Customization

Extending Inventor's UI:

| File | Content |
|------|---------|
| `RibbonUI_Overview.md` | Ribbon tabs, panels, buttons |
| `UserInteraction_Overview.md` | Dialogs, selection, input |
| `Browser_Overview.md` | Custom browser panes |
| `BrowserNodes_Overview.md` | Custom tree nodes |
| `Environments_Overview.md` | Custom environments |
| `TriadEvents_Overview.md` | 3D Move/Rotate tool |
| `ViewFrames_Overview.md` | View manipulation |

### Custom Data

Storing custom data in documents:

| File | Content |
|------|---------|
| `DocumentProperties_Overview.md` | iProperties (built-in and custom) |
| `Attributes_Overview.md` | Attribute sets for custom data |

### Transaction Support

Undo/redo and change management:

| File | Content |
|------|---------|
| `Transactions_Overview.md` | Transaction grouping for undo |
| `ChangeProcessor_Overview.md` | Change processor for complex operations |

### Miscellaneous

Additional specialized topics:

| File | Content |
|------|---------|
| `CustomGraphics_Overview.md` | Drawing custom 3D graphics |
| `DataIO_Overview.md` | File translation (STEP, IGES, etc.) |
| `Apprentice_Overview.md` | Apprentice Server for lightweight access |
| `ClientViews_Overview.md` | Custom view rendering |
| `UserFunctions_Overview.md` | User-defined functions |
| `FormattedTextTags_Overview.md` | Text formatting codes |

## Usage Workflow

To answer questions about Inventor API concepts:

1. Identify the topic category from the user's question
2. Read the relevant overview document from `references/`
3. Extract relevant code examples and explanations
4. Provide clear guidance with working code samples

## Code Example Patterns

### Connecting to Inventor (C#)

```csharp
using Inventor;

// In add-in Activate method
Inventor.Application inventorApp = addInSiteObject.Application;

// Access active document
Document doc = inventorApp.ActiveDocument;
```

### Common Object Model Navigation

```
Application
  └─ Documents (collection)
       └─ PartDocument / AssemblyDocument / DrawingDocument
            └─ ComponentDefinition
                 ├─ Sketches (collection)
                 ├─ Features (collection)
                 ├─ WorkPlanes / WorkAxes / WorkPoints
                 └─ Occurrences (assembly only)
```

## Best Practices

When working with Inventor API:

1. **Use Transactions**: Wrap modifications in transactions for undo support
2. **Handle Units**: Use `UnitsOfMeasure` object for unit conversion
3. **Check Document Type**: Verify document type before accessing type-specific properties
4. **Release COM Objects**: In Python, set objects to None when done
5. **Use Transient Geometry**: Create temporary geometry with `TransientGeometry` object

## Additional Resources

For detailed information on specific topics, read the corresponding file from `references/`.

The `TOC.md` file provides a complete table of contents with links to all documents.

For API reference (classes, methods, enums), see the `inventor-api-reference` skill.
For sample code, see the `inventor-samples` skill.
