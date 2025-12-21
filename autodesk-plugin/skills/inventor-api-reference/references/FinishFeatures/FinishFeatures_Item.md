# FinishFeatures.Item Property

Parent Object: [FinishFeatures](../FinishFeatures/FinishFeatures.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

FinishFeatures.**Item**( ***Index*** As Variant ) As [FinishFeature](../FinishFeature/FinishFeature.md)

## Property Value

This is a read only property whose value is a [FinishFeature](../FinishFeature/FinishFeature.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the FinishFeature to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the FinishFeature name. If an out of range index or a name of a non-existent FinishFeature is provided, an error will occur. |

## Version

Introduced in version 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |