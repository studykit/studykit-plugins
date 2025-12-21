# DrawingHatchPatternsManager.Item Property

Parent Object: [DrawingHatchPatternsManager](../DrawingHatchPatternsManager/DrawingHatchPatternsManager.md)

## Description

Allows integer-indexed access to items in the collection.

## Syntax

DrawingHatchPatternsManager.**Item**( ***Index*** As Variant ) As [DrawingHatchPattern](../DrawingHatchPattern/DrawingHatchPattern.md)

## Property Value

This is a read only property whose value is a [DrawingHatchPattern](../DrawingHatchPattern/DrawingHatchPattern.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the DrawingHatchPattern to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the DrawingHatchPattern name. If an out of range index or a name of a non-existent DrawingHatchPattern is provided, an error will occur. |

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