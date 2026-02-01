# Inventor API Reference

This skill provides access to the Autodesk Inventor API Reference Manual, containing detailed documentation for all API classes, methods, properties, and enumerations.

## Overview

The API Reference contains:

- **Classes/Objects**: Object definitions with properties and methods (stored in folders)
- **Enumerations**: Constant value definitions (stored as individual .md files)

## Reference Files

All API reference documentation is located in the [references/api-reference/](references/api-reference/) folder.

### Class Documentation (Folders)

Each class is stored as a **folder** containing multiple files:
- `ClassName/ClassName.md` - Main class description, methods list, properties list
- `ClassName/ClassName_PropertyName.md` - Individual property documentation
- `ClassName/ClassName_MethodName.md` - Individual method documentation

Example for `ExtrudeFeature`:
```
references/api-reference/ExtrudeFeature/
├── ExtrudeFeature.md              # Main class doc
├── ExtrudeFeature_Operation.md    # Operation property
├── ExtrudeFeature_Profile.md      # Profile property
└── ExtrudeFeature_Extent.md       # Extent property
```

### Enum Documentation (Files)

Enums are individual `.md` files at the root level:
```
references/api-reference/PartFeatureExtentEnum.md
references/api-reference/PartFeatureOperationEnum.md
references/api-reference/DocumentTypeEnum.md
```

## Usage Workflow

To answer questions about specific API elements:

1. **Find the class**: Navigate to [references/api-reference/ClassName/ClassName.md](references/api-reference/)
2. **Find specific members**: Read `references/api-reference/ClassName/ClassName_MemberName.md`
3. **Find enum values**: Read `references/api-reference/EnumName.md` directly

## Search Examples

To find API information, search within the [references/api-reference/](references/api-reference/) folder:

- Class documentation: `ClassName/ClassName.md`
- Property/method detail: `ClassName/ClassName_MemberName.md`
- Enum values: `*Enum.md` files


## Related Skills

- For conceptual understanding, see `inventor-user-manual` skill
- For working code examples, see `inventor-samples` skill
