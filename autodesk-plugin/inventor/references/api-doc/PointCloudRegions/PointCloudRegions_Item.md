# PointCloudRegions.Item Property

Parent Object: [PointCloudRegions](../PointCloudRegions/PointCloudRegions.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

PointCloudRegions.**Item**( ***Index*** As Variant ) As [PointCloudRegion](../PointCloudRegion/PointCloudRegion.md)

## Property Value

This is a read only property whose value is a [PointCloudRegion](../PointCloudRegion/PointCloudRegion.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the PointCloudRegion to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the PointCloudRegion name. If an out of range index or a name of a non-existent PointCloudRegion is provided, an error occurs. |

## Version

Introduced in version 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |