# SketchDrivenPatternFeatures.Item Property

Parent Object: [SketchDrivenPatternFeatures](../SketchDrivenPatternFeatures/SketchDrivenPatternFeatures.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

SketchDrivenPatternFeatures.**Item**( ***Index*** As Variant ) As [SketchDrivenPatternFeature](../SketchDrivenPatternFeature/SketchDrivenPatternFeature.md)

## Property Value

This is a read only property whose value is a [SketchDrivenPatternFeature](../SketchDrivenPatternFeature/SketchDrivenPatternFeature.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the SketchDrivenPatternFeature to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the SketchDrivenPatternFeature name. If an out of range index or a name of a non-existent SketchDrivenPatternFeature is provided, an error occurs. |

## Version

Introduced in version 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |