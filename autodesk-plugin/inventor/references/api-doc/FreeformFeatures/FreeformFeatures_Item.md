# FreeformFeatures.Item Property

Parent Object: [FreeformFeatures](../FreeformFeatures/FreeformFeatures.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

FreeformFeatures.**Item**( ***Index*** As Variant ) As [FreeformFeature](../FreeformFeature/FreeformFeature.md)

## Property Value

This is a read only property whose value is a [FreeformFeature](../FreeformFeature/FreeformFeature.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the FreeformFeature to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the FreeformFeature name. If an out of range index or a name of a non-existent FreeformFeature is provided, an error will occur. |

## Version

Introduced in version 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |