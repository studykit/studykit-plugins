# RuledSurfaceFeatures.Item Property

Parent Object: [RuledSurfaceFeatures](../RuledSurfaceFeatures/RuledSurfaceFeatures.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

RuledSurfaceFeatures.**Item**( ***Index*** As Variant ) As [RuledSurfaceFeature](../RuledSurfaceFeature/RuledSurfaceFeature.md)

## Property Value

This is a read only property whose value is a [RuledSurfaceFeature](../RuledSurfaceFeature/RuledSurfaceFeature.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the RuledSurfaceFeature to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the RuledSurfaceFeature name. If an out of range index or a name of a non-existent RuledSurfaceFeature is provided, an error will occur. |

## Version

Introduced in version 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |