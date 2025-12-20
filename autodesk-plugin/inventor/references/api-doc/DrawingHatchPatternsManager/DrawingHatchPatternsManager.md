# DrawingHatchPatternsManager Object

## Description

DrawingHatchPatternsManager Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ExportHatchPatterns](../DrawingHatchPatternsManager/DrawingHatchPatternsManager_ExportHatchPatterns.md) | Method that exports hatch patterns to a PAT file. If a file with the same name already exists, it will be overwritten. |
| [GetHatchPatternDefinitions](../DrawingHatchPatternsManager/DrawingHatchPatternsManager_GetHatchPatternDefinitions.md) | Method that gets the hatch pattern definitions from a PAT file. |
| [LoadHatchPatterns](../DrawingHatchPatternsManager/DrawingHatchPatternsManager_LoadHatchPatterns.md) | Method that loads hatch patterns from a PAT file. If a hatch pattern has the same name as specified in the PatternDefinitionNames is already loaded, it will be replaced. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DrawingHatchPatternsManager/DrawingHatchPatternsManager_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Count](../DrawingHatchPatternsManager/DrawingHatchPatternsManager_Count.md) | Gets the number of items in this collection. |
| [Item](../DrawingHatchPatternsManager/DrawingHatchPatternsManager_Item.md) | Allows integer-indexed access to items in the collection. |
| [Parent](../DrawingHatchPatternsManager/DrawingHatchPatternsManager_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../DrawingHatchPatternsManager/DrawingHatchPatternsManager_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[DrawingDocument.DrawingHatchPatternsManager](../DrawingDocument/DrawingDocument_DrawingHatchPatternsManager.md), [DrawingHatchPattern.Parent](../DrawingHatchPattern/DrawingHatchPattern_Parent.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Drawing Sketch Hatch Region Sample](../../sample-programs/DrawingSketchHatchRegionSample_Sample.md) | This sample demonstrates how to create a sketch hatch region in drawing. |

## Version

Introduced in version 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |