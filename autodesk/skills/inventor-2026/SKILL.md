---
name: Inventor 2026 API Guide
disable-model-invocation: true
description: This skill should be used when the user asks about "Inventor API", "Inventor add-in", "Inventor VBA", "Inventor C#", "Inventor .NET", "Inventor automation", "PartDocument", "AssemblyDocument", "DrawingDocument", "ComponentDefinition", "Inventor sketches", "Inventor features", "Inventor assembly constraints", "Inventor BOM", "Inventor iProperties", "Inventor ribbon customization", "Inventor transactions", or needs guidance on Autodesk Inventor 2026 API development, add-in creation, scripting, or automation.
---

# Inventor 2026 API Development Guide

This skill provides comprehensive documentation for developing add-ins and automations using the Autodesk Inventor 2026 API. The API enables automation of design tasks, custom feature creation, UI customization, and document manipulation.

## Overview

The Inventor API supports **VBA**, **C#**, and **VB.NET** for add-in development. Starting with Inventor 2025, **.NET 8** is supported.

## Reference Documentation

All reference materials are located in the following folders within this skill directory:

| Folder | Contents |
|--------|----------|
| `references/user-manual/` | Conceptual guides and tutorials |
| `references/api-reference/` | Class, method, property, and enum documentation |
| `references/samples/` | Code sample documentation |
| `references/images/` | Diagrams and screenshots |

## Core Concepts

### Object Model

Inventor uses a hierarchical object model:

```
Application
  └── Documents (collection)
       ├── PartDocument
       │    └── ComponentDefinition
       │         ├── Sketches
       │         ├── Features
       │         ├── WorkPlanes / WorkAxes / WorkPoints
       │         └── SurfaceBodies
       ├── AssemblyDocument
       │    └── ComponentDefinition
       │         ├── Occurrences
       │         └── Constraints
       └── DrawingDocument
            └── Sheets
                 ├── DrawingViews
                 ├── Dimensions
                 └── Balloons
```

See `user-manual.md` for the complete class hierarchy and `references/user-manual/InventorObjectModel.md` for detailed object relationships.

### Supported Languages

| Language | Use Case | Documentation |
|----------|----------|---------------|
| VBA | Quick automation, macros | `references/user-manual/VBA_Overview.md` |
| C# / VB.NET | Add-ins, complex solutions | `references/user-manual/CreatingAnAddIn_Overview.md` |
| .NET 8 | Modern add-ins (2025+) | `references/user-manual/PortToNetCore_Overview.md` |

## Common Development Patterns

### Getting Application Reference (C#)

```csharp
using Inventor;

// In add-in Activate method
public void Activate(ApplicationAddInSite addInSiteObject, bool firstTime)
{
    m_inventorApplication = addInSiteObject.Application;
}

// Access active document
Document doc = m_inventorApplication.ActiveDocument;
PartDocument partDoc = doc as PartDocument;
PartComponentDefinition compDef = partDoc.ComponentDefinition;
```

### Getting Application Reference (VBA)

```vb
Dim oApp As Inventor.Application
Set oApp = ThisApplication

Dim oDoc As PartDocument
Set oDoc = oApp.ActiveDocument

Dim oCompDef As PartComponentDefinition
Set oCompDef = oDoc.ComponentDefinition
```

### Creating Features

```csharp
// Create a sketch on XY plane
PlanarSketch sketch = compDef.Sketches.Add(compDef.WorkPlanes[3]);

// Draw a rectangle
TransientGeometry tg = m_inventorApplication.TransientGeometry;
Point2d pt1 = tg.CreatePoint2d(0, 0);
Point2d pt2 = tg.CreatePoint2d(10, 10);
sketch.SketchLines.AddAsTwoPointRectangle(pt1, pt2);

// Create an extrusion
Profile profile = sketch.Profiles.AddForSolid();
ExtrudeDefinition extDef = compDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(
    profile, PartFeatureOperationEnum.kNewBodyOperation);
extDef.SetDistanceExtent(5, PartFeatureExtentDirectionEnum.kPositiveExtentDirection);
ExtrudeFeature extrude = compDef.Features.ExtrudeFeatures.Add(extDef);
```

### Transaction Support

```csharp
// Wrap operations in a transaction for undo support
Transaction trans = m_inventorApplication.TransactionManager.StartTransaction(
    partDoc, "My Operation");
try
{
    // Perform operations
    trans.End();
}
catch
{
    trans.Abort();
    throw;
}
```

### Units of Measure

Inventor API uses internal database units (centimeters for length). Use `UnitsOfMeasure` for conversion:

```csharp
UnitsOfMeasure uom = partDoc.UnitsOfMeasure;

// Convert user expression to internal value
double internalVal = uom.GetValueFromExpression("25 mm");

// Convert internal value to display string
string displayStr = uom.GetStringFromValue(5.0, UnitsTypeEnum.kMillimeterLengthUnits);
```

See `references/user-manual/UOM_Overview.md` for details.

## Key Documentation Files

### Getting Started

| File | Topic |
|------|-------|
| `references/user-manual/GettingStarted.md` | API introduction |
| `references/user-manual/VBA_Overview.md` | VBA programming basics |
| `references/user-manual/CreatingAnAddIn_Overview.md` | Creating add-ins |
| `references/user-manual/UsingSDK.md` | SDK tools and utilities |

### Modeling

| File | Topic |
|------|-------|
| `references/user-manual/Sketch_Overview.md` | Creating and editing sketches |
| `references/user-manual/Features_Overview.md` | Part features (extrude, revolve, etc.) |
| `references/user-manual/WorkFeatures_Overview.md` | Work planes, axes, points |
| `references/user-manual/BRep_Overview.md` | B-Rep topology |

### Assembly

| File | Topic |
|------|-------|
| `references/user-manual/AssemblingParts_Overview.md` | Assembly constraints and joints |
| `references/user-manual/BOM_Overview.md` | Bill of Materials |
| `references/user-manual/Proxies_Overview.md` | Proxy objects |

### Drawings

| File | Topic |
|------|-------|
| `references/user-manual/DrawingViews_Overview.md` | Creating drawing views |
| `references/user-manual/DrawingDimensions_Overview.md` | Dimensions |
| `references/user-manual/Balloons_Overview.md` | Balloon annotations |

### UI Customization

| File | Topic |
|------|-------|
| `references/user-manual/RibbonUI_Overview.md` | Ribbon customization |
| `references/user-manual/UserInteraction_Overview.md` | Dialogs and selection |
| `references/user-manual/Environments_Overview.md` | Custom environments |

## API Reference Lookup

API reference files are in `references/api-reference/` with naming convention:

- `ClassName/ClassName.md` - Class overview
- `ClassName/ClassName_PropertyName.md` - Property documentation
- `ClassName/ClassName_MethodName.md` - Method documentation
- `EnumName.md` - Enumeration values

Example: To find `ExtrudeFeatures.Add()` method:
```
references/api-reference/ExtrudeFeatures/ExtrudeFeatures_Add.md
```

## Sample Code

Sample code documentation is in `references/samples/`. See `samples.md` for a complete list of available samples organized by category.

## Best Practices

1. **Use Transactions**: Wrap modifications in transactions for undo support
2. **Handle Units**: Always use `UnitsOfMeasure` for unit conversion
3. **Check Document Type**: Verify document type before casting
4. **Release COM Objects**: In VBA, set objects to Nothing when done
5. **Use Transient Geometry**: Create temporary geometry with `TransientGeometry` object
6. **Error Handling**: Always use try/catch and provide meaningful error messages
7. **Clean Up**: Remove UI elements when add-in deactivates
