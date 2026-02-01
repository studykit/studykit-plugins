# PointClouds.Item Property

Parent Object: [PointClouds](../PointClouds/PointClouds.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

PointClouds.**Item**( ***Index*** As Variant ) As [PointCloud](../PointCloud/PointCloud.md)

## Property Value

This is a read only property whose value is a [PointCloud](../PointCloud/PointCloud.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the point cloud to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the point cloud name. If an out of range index or a name of a non-existent point cloud is provided, an error will occur. |

## Version

Introduced in version 2016
