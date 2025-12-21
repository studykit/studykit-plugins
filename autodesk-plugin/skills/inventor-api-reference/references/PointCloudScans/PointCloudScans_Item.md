# PointCloudScans.Item Property

Parent Object: [PointCloudScans](../PointCloudScans/PointCloudScans.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

PointCloudScans.**Item**( ***Index*** As Variant ) As [PointCloudScan](../PointCloudScan/PointCloudScan.md)

## Property Value

This is a read only property whose value is a [PointCloudScan](../PointCloudScan/PointCloudScan.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the PointCloudScan to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the PointCloudScan name. If an out of range index or a name of a non-existent PointCloudScan is provided, an error occurs. |

## Version

Introduced in version 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |