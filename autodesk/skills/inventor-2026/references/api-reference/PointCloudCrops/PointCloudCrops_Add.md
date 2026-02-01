# PointCloudCrops.Add Method

Parent Object: [PointCloudCrops](../PointCloudCrops/PointCloudCrops.md)

## Description

Method that adds a crop to the point cloud and the result PointCloudCrop is returned.

## Syntax

PointCloudCrops.**Add**( ***BoundingBox*** As [OrientedBox](../OrientedBox/OrientedBox.md), [***KeepInside***] As Boolean ) As [PointCloudCrop](../PointCloudCrop/PointCloudCrop.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BoundingBox | [OrientedBox](../OrientedBox/OrientedBox.md) | Input OrientedBox object that defines the bounding volume. The TransientGeometry.CreateOrientedBox can be used to create an OrientedBox object. |
| KeepInside | Boolean | Optional input Boolean that specifies whether keep the point cloud points in the BoundingBox. |

## Version

Introduced in version 2016
