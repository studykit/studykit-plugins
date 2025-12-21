# WorkPlane.GetSize Method

Parent Object: [WorkPlane](../WorkPlane/WorkPlane.md)

## Description

Method that gets the current size of the displayed graphics for the work plane. The returned points are in the coordinate space of the workplane.

## Remarks

The work plane is functionally infinite but has a plane that is displayed to allow the user to interact with it graphically. The size and the position of the plane can be adjusted to make it easier for the user to interact with. Construction work planes are never visible to the user and don't need to have a size defined. This method will fail in the case of a construction work plane. You can determine if the work plane is a construction work plane by checking the Construction property of the WorkPlane object. The two points define the diagonal corners of the displayed rectangle. The rectangle is parallel to the X-axis of the plane.

## Syntax

WorkPlane.**GetSize**( ***Point1*** As [Point](../Point/Point.md), ***Point2*** As [Point](../Point/Point.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Point1 | [Point](../Point/Point.md) | Output Point object that defines the first corner of the work plane. |
| Point2 | [Point](../Point/Point.md) | Output Point object that defines the diagonal corner of the work plane. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |