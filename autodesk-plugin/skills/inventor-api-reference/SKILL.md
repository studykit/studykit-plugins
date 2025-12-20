---
name: Inventor API Reference
description: This skill should be used when the user asks about "Inventor API class", "Inventor method", "Inventor property", "Inventor enum", "Inventor enumeration", "ExtrudeFeature", "PartDocument", "AssemblyDocument", "Sketch object", "ComponentDefinition", "Inventor object model", or needs to look up specific Inventor API classes, methods, properties, enumerations, or object definitions. Provides access to Autodesk Inventor API Reference Manual.
version: 0.1.0
---

# Inventor API Reference

This skill provides access to the Autodesk Inventor API Reference Manual, containing detailed documentation for all API classes, methods, properties, and enumerations.

## Overview

The API Reference contains:

- **Object Model**: Complete hierarchy of all Inventor API objects
- **Classes/Objects**: Object definitions with properties and methods (stored in folders)
- **Enumerations**: Constant value definitions (stored as individual .md files)

## Reference Files

All API reference documentation is located relative to the plugin root:
```
inventor/references/api-doc/
```

### Object Model Hierarchy

Read this file to understand the complete API object hierarchy:
- **`inventor/references/api-doc/InventorObjectModel.md`**

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

1. **Understand object hierarchy**: Read `inventor/references/api-doc/InventorObjectModel.md` first
2. **Find the class**: Navigate to `inventor/references/api-doc/ClassName/ClassName.md`
3. **Find specific members**: Read `inventor/references/api-doc/ClassName/ClassName_MemberName.md`
4. **Find enum values**: Read `inventor/references/api-doc/EnumName.md` directly

## Search Examples

To find API information, search within `inventor/references/api-doc/`:

- Object model overview: `InventorObjectModel.md`
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
