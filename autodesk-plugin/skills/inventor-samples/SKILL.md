---
name: Inventor Sample Programs
description: This skill should be used when the user asks for "Inventor API example", "Inventor sample code", "Inventor VBA sample", "how to create extrude in Inventor API", "Inventor code example", "Inventor API tutorial", or needs working code examples for Inventor automation. Provides access to official Autodesk Inventor API sample programs.
version: 0.1.0
---

# Inventor Sample Programs

This skill provides access to official Autodesk Inventor API sample programs, demonstrating practical implementations of various API features.

## Overview

The sample programs collection contains:

- **VBA Code Samples**: Ready-to-run VBA macro examples
- **Feature Creation**: Extrude, revolve, hole, fillet, etc.
- **Assembly Operations**: Constraints, joints, BOM
- **Drawing Automation**: Views, dimensions, balloons
- **UI Customization**: Ribbon, browser, dialogs

## Reference Files

All sample programs are located in the `references/` folder within this skill directory. Reference files using relative paths like `references/ExtrudeFeature_Sample.md`.

File naming convention: `ClassName_MethodName_Sample.md` or `FeatureName_Sample.md`

## Sample Categories

### Part Feature Samples

| File | Description |
|------|-------------|
| `ExtrudeFeatures_Add_Sample.md` | Create extrude features |
| `RevolveFeatures_Add_Sample.md` | Create revolve features |
| `HoleFeatures_Add_Sample.md` | Create hole features |
| `FilletFeatures_Add_Sample.md` | Create fillet features |
| `ChamferFeatures_Add_Sample.md` | Create chamfer features |
| `SweepFeatures_Add_Sample.md` | Create sweep features |
| `LoftFeatures_Add_Sample.md` | Create loft features |
| `BoundaryPatchFeatures_Add_Sample.md` | Create boundary patch |
| `CopyBodyFeature_Sample.md` | Copy body feature |

### Sketch Samples

| File | Description |
|------|-------------|
| `CenterPointRectangle_Sample.md` | Create center point rectangle |
| `CopySketch_Sample.md` | Copy sketch geometry |
| `AdvancedCurveCreation_Sample.md` | Advanced curve creation |
| `Approximate3DSketchGeometry_Sample.md` | 3D sketch approximation |
| `ArcLengthDimConstraint_Sample.md` | Arc length constraints |

### Assembly Samples

| File | Description |
|------|-------------|
| `AddOccurrence_Sample.md` | Add component occurrence |
| `AssemblyConstraints_AddMateConstraint_Sample.md` | Create mate constraint |
| `AssemblyConstraints_AddInsertConstraint_Sample.md` | Create insert constraint |
| `AssemblyRotationalJoint_Sample.md` | Create rotational joint |
| `AssemblyJointDefinition_SetOriginOneAsOffset_Sample.md` | Joint offset definition |
| `AssemblyTraverse_Sample.md` | Traverse assembly structure |
| `AssemblyComponentDefinition_AnalyzeInterference_Sample.md` | Interference analysis |
| `AddUsingiMates_Sample.md` | Add components using iMates |
| `ComponentOccurrence_Grounded_Sample.md` | Ground component |

### Drawing Samples

| File | Description |
|------|-------------|
| `Balloons_Add_Sample.md` | Add balloon annotations |
| `Balloons_Sample.md` | Balloon operations |
| `BaselineDimensionSets_Add_Sample.md` | Baseline dimension sets |
| `ChainDimensionSets_Add_Sample.md` | Chain dimension sets |
| `BendNotes_Add_Sample.md` | Add bend notes |
| `AngularGeneralDimension_CenterText_Sample.md` | Angular dimensions |
| `BreakOperations_Add_Sample.md` | Break operations |
| `AutoCADBlocks_Add_Sample.md` | Add AutoCAD blocks |

### BOM Samples

| File | Description |
|------|-------------|
| `BOM_Sample.md` | BOM operations |
| `BOMView_Export_Sample.md` | Export BOM view |
| `BalloonValueSet_ReferencedRow_Sample.md` | Balloon value sets |

### iPart/iAssembly Samples

| File | Description |
|------|-------------|
| `AddiPartMember_Sample.md` | Add iPart member |
| `AddiAssemblyMember_Sample.md` | Add iAssembly member |

### UI Customization Samples

| File | Description |
|------|-------------|
| `AddButtonToAppMenu_Sample.md` | Add button to app menu |
| `BrowserPaneObject_AddBrowserFolder_Sample.md` | Add browser folder |
| `BrowserPanes_GetNativeBrowserNodeDefinition_Sample.md` | Browser node definition |
| `CommandManager_Pick_Sample.md` | Command manager pick |
| `ChangeAppearanceUsingMiniToolbar_Sample.md` | Mini toolbar usage |
| `CreateParallelEnvironment_Sample.md` | Create environment |

### Appearance & Graphics Samples

| File | Description |
|------|-------------|
| `CreateSimpleAppearance_Sample.md` | Create appearance |
| `BrightnessAdjustSample_Sample.md` | Brightness adjustment |
| `ClientGraphics_Sample.md` | Client graphics |

### Content Center Samples

| File | Description |
|------|-------------|
| `ContentCenterPartReplace_Sample.md` | Replace content center part |

### Parameters Samples

| File | Description |
|------|-------------|
| `CustomParameterGroup_Add_Sample.md` | Custom parameter groups |

### Export Samples

| File | Description |
|------|-------------|
| `CreateRevitExportSample_Sample.md` | Export to Revit |

## Usage Workflow

To find sample code:

1. Identify the API feature or operation needed
2. Search for matching sample file in `references/`
3. Read the sample file for description and code
4. Adapt the VBA code to Python or C# if needed

## Code Conversion Tips

### VBA to Python

```vba
' VBA
Dim oDoc As PartDocument
Set oDoc = ThisApplication.ActiveDocument
```

### VBA to C#

```vba
' VBA
Dim oDoc As PartDocument
Set oDoc = ThisApplication.ActiveDocument
```

```csharp
// C#
PartDocument oDoc = (PartDocument)inventorApp.ActiveDocument;
```

## Related Skills

- For API concepts, see `inventor-user-manual` skill
- For class/method reference, see `inventor-api-reference` skill
