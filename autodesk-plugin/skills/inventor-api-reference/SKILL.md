---
name: Inventor API Reference
description: This skill should be used when the user asks about "Inventor API class", "Inventor method", "Inventor property", "Inventor enum", "Inventor enumeration", "ExtrudeFeature", "PartDocument", "AssemblyDocument", "Sketch object", "ComponentDefinition", "Inventor object model", or needs to look up specific Inventor API classes, methods, properties, enumerations, or object definitions. Provides access to Autodesk Inventor API Reference Manual.
version: 0.1.0
---

# Inventor API Reference

This skill provides access to the Autodesk Inventor API Reference Manual, containing detailed documentation for all API classes, methods, properties, and enumerations.

## Overview

The API Reference contains:

- **Classes/Objects**: Object definitions with properties and methods (stored in folders)
- **Enumerations**: Constant value definitions (stored as individual .md files)

## Reference Files

All API reference documentation is located in:
```
${CLAUDE_PLUGIN_ROOT}/inventor/references/api-doc/
```

### Class Documentation (Folders)

Each class is stored as a **folder** containing multiple files:
- `ClassName/ClassName.md` - Main class description, methods list, properties list
- `ClassName/ClassName_PropertyName.md` - Individual property documentation
- `ClassName/ClassName_MethodName.md` - Individual method documentation

Example for `ExtrudeFeature`:
```
inventor/references/api-doc/ExtrudeFeature/
├── ExtrudeFeature.md              # Main class doc
├── ExtrudeFeature_Operation.md    # Operation property
├── ExtrudeFeature_Profile.md      # Profile property
└── ExtrudeFeature_Extent.md       # Extent property
```

### Enum Documentation (Files)

Enums are individual `.md` files at the root level:
```
inventor/references/api-doc/PartFeatureExtentEnum.md
inventor/references/api-doc/PartFeatureOperationEnum.md
inventor/references/api-doc/DocumentTypeEnum.md
```

## Usage Workflow

To answer questions about specific API elements:

1. **Find the class**: Navigate to `inventor/references/api-doc/ClassName/ClassName.md`
2. **Find specific members**: Read `inventor/references/api-doc/ClassName/ClassName_MemberName.md`
3. **Find enum values**: Read `inventor/references/api-doc/EnumName.md` directly

## Search Examples

To find API information, search within `inventor/references/api-doc/`:

- Class documentation: `ClassName/ClassName.md`
- Property/method detail: `ClassName/ClassName_MemberName.md`
- Enum values: `*Enum.md` files

## Common Object Categories

| Category | Key Objects |
|----------|-------------|
| Documents | `PartDocument`, `AssemblyDocument`, `DrawingDocument` |
| Part Features | `ExtrudeFeature`, `RevolveFeature`, `HoleFeature`, `FilletFeature` |
| Assembly | `ComponentOccurrence`, `MateConstraint`, `AssemblyJoint` |
| Sketches | `PlanarSketch`, `Sketch3D`, `SketchLine`, `SketchCircle` |
| Drawing | `Sheet`, `DrawingView`, `GeneralDimension`, `Balloon` |

## Related Skills

- For conceptual understanding, see `inventor-user-manual` skill
- For working code examples, see `inventor-samples` skill
