# MarkFeatures.Item Property

Parent Object: [MarkFeatures](../MarkFeatures/MarkFeatures.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

MarkFeatures.**Item**( ***Index*** As Variant ) As [MarkFeature](../MarkFeature/MarkFeature.md)

## Property Value

This is a read only property whose value is a [MarkFeature](../MarkFeature/MarkFeature.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the MarkFeature to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the MarkFeature name. If an out of range index or a name of a non-existent MarkFeature is provided, an error will occur. |

## Version

Introduced in version 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |