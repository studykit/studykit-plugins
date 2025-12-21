# WorkAxis.GetSize Method

Parent Object: [WorkAxis](../WorkAxis/WorkAxis.md)

## Description

Method that gets the current size of the displayed graphics for the work axis. The returned points are in model coordinate space.

## Remarks

The work axis is functionally infinite but has a line that is displayed to allow the user to interact with it graphically. The size and the position of the line can be adjusted to make it easier for the user to interact with. Construction work axes are never visible to the user and don't need to have a size defined. This method will fail in the case of a construction work axis. You can determine if the work axis is a construction work axis by checking the Construction property of the WorkAxis object. The two points define the end points of the displayed line.

## Syntax

WorkAxis.**GetSize**( ***Point1*** As [Point](../Point/Point.md), ***Point2*** As [Point](../Point/Point.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Point1 | [Point](../Point/Point.md) | Output Point object that defines the first end point of the work axis. |
| Point2 | [Point](../Point/Point.md) | Output Point object that defines the other end point of the work axis. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |