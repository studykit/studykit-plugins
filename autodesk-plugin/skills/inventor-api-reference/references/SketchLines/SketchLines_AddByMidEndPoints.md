# SketchLines.AddByMidEndPoints Method

Parent Object: [SketchLines](../SketchLines/SketchLines.md)

## Description

Method that creates a new sketch line based on the mid and end points. The new sketch line is returned.

## Syntax

SketchLines.**AddByMidEndPoints**( ***MidPoint*** As Object, ***EndPoint*** As Object ) As [SketchLine](../SketchLine/SketchLine.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| MidPoint | Object | Input object that defines the mid point of the line. This can be either a Point2d object defining an x-y point in space, or an existing SketchPoint object. If an existing sketch point is input, a MidpointContraint will be created between the SketchPoint and the new sketch line. |
| EndPoint | Object | Input object that defines the end point of the line. This can be either a Point2d object defining an x-y point in space, or an existing SketchPoint object. If an existing sketch point is input, that point becomes the line’s end point. |

## Version

Introduced in version 2025.2
