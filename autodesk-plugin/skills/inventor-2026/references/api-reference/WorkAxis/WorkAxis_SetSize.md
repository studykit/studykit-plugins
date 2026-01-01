# WorkAxis.SetSize Method

Parent Object: [WorkAxis](../WorkAxis/WorkAxis.md)

## Description

Method that sets the current size of the displayed graphics for the work axis.

## Remarks

The input points should be in model coordinate space. The work axis is functionally infinite but has a line that is displayed to allow the user to interact with it graphically. The size and the position of the line can be adjusted to make it easier for the user to interact with. Construction work axes are never visible to the user and don't need to have a size defined. This method will fail in the case of a construction work axis. You can determine if the work plane is a construction work axis by checking the Construction property of the WorkAxis object. This method will also fail if the AutoResize property is set to True. The two points define the two ends of the displayed line. The points must lie on the underlying Line geometry of the work axis.

## Syntax

WorkAxis.**SetSize**( ***Point1*** As [Point](../Point/Point.md), ***Point2*** As [Point](../Point/Point.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Point1 | [Point](../Point/Point.md) | Input Point object that defines the first end point of the work axis. |
| Point2 | [Point](../Point/Point.md) | Input Point object that defines the other end point of the work axis. |

## Version

Introduced in version 2008
