# WorkPlane.SetSize Method

Parent Object: [WorkPlane](../WorkPlane/WorkPlane.md)

## Description

Method that sets the current size of the displayed graphics for the work plane.

## Remarks

The input points should be in the coordinate space of the workplane. The work plane is functionally infinite but has a plane that is displayed to allow the user to interact with it graphically. The size and the position of the plane can be adjusted to make it easier for the user to interact with. Construction work planes are never visible to the user and don't need to have a size defined. This method will fail in the case of a construction work plane. You can determine if the work plane is a construction work plane by checking the Construction property of the WorkPlane object. This method will also fail if the AutoResize property is set to True. The two points define the diagonal corners of the displayed rectangle. The rectangles sides are parallel to the X and Y axes of the plane.

## Syntax

WorkPlane.**SetSize**( ***Point1*** As [Point](../Point/Point.md), ***Point2*** As [Point](../Point/Point.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Point1 | [Point](../Point/Point.md) | Input  object that defines the first corner of the work plane. |
| Point2 | [Point](../Point/Point.md) | Input  object that defines the diagonal corner of the work plane. |

## Version

Introduced in version 4
