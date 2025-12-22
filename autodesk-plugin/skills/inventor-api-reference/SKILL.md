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

All API reference documentation is located in the [references/](references/) folder.

### Class Documentation (Folders)

Each class is stored as a **folder** containing multiple files:
- `ClassName/ClassName.md` - Main class description, methods list, properties list
- `ClassName/ClassName_PropertyName.md` - Individual property documentation
- `ClassName/ClassName_MethodName.md` - Individual method documentation

Example for `ExtrudeFeature`:
```
references/ExtrudeFeature/
├── ExtrudeFeature.md              # Main class doc
├── ExtrudeFeature_Operation.md    # Operation property
├── ExtrudeFeature_Profile.md      # Profile property
└── ExtrudeFeature_Extent.md       # Extent property
```

### Enum Documentation (Files)

Enums are individual `.md` files at the root level:
```
references/PartFeatureExtentEnum.md
references/PartFeatureOperationEnum.md
references/DocumentTypeEnum.md
```

## Usage Workflow

To answer questions about specific API elements:

1. **Find the class**: Navigate to [references/ClassName/ClassName.md](references/)
2. **Find specific members**: Read `references/ClassName/ClassName_MemberName.md`
3. **Find enum values**: Read `references/EnumName.md` directly

## Search Examples

To find API information, search within the [references/](references/) folder:

- Class documentation: `ClassName/ClassName.md`
- Property/method detail: `ClassName/ClassName_MemberName.md`
- Enum values: `*Enum.md` files


## Related Skills

- For conceptual understanding, see `inventor-user-manual` skill
- For working code examples, see `inventor-samples` skill
