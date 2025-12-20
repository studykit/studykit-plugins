# ExtrudeFeatures.Item Property

Parent Object: [ExtrudeFeatures](../ExtrudeFeatures/ExtrudeFeatures.md)

## Description

Returns the specified object from the collection.

## Syntax

ExtrudeFeatures.**Item**( ***Index*** As Variant ) As [ExtrudeFeature](../ExtrudeFeature/ExtrudeFeature.md)

## Property Value

This is a read only property whose value is an [ExtrudeFeature](../ExtrudeFeature/ExtrudeFeature.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the feature to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the feature name. If an out of range index or a name of a non-existent feature is provided, an error occurs. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketch Share](../../sample-programs/PlanarSketch_Shared_Sample.md) | This sample demonstrates setting a sketch so it is shared. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |