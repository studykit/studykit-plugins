# PointCloudPlane.GetPlaneRectangle Method

Parent Object: [PointCloudPlane](../PointCloudPlane/PointCloudPlane.md)

## Description

Method that gets the full definition of a bounded rectangular plane.

## Syntax

PointCloudPlane.**GetPlaneRectangle**( ***Plane*** As [Plane](../Plane/Plane.md), ***LengthDirection*** As [UnitVector](../UnitVector/UnitVector.md), ***Length*** As Double, ***Height*** As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Plane | [Plane](../Plane/Plane.md) | Output Plane object that defines the position and orientation of the plane. The Plane object is boundless. The origin point of this plane is at the center of the bounded plane. |
| LengthDirection | [UnitVector](../UnitVector/UnitVector.md) | Output UnitVector object that specifies the direction that the length of the plane goes in. This vector will also be perpendicular to the plane normal vector. |
| Length | Double | The length of the plane in centimeters. This is the entire length of the bounded plane. |
| Height | Double | The height of the plane in centimeters. This is the entire height of the bounded plane. |

## Version

Introduced in version 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |