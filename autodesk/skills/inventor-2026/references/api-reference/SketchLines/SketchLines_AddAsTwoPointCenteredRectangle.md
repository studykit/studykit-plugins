# SketchLines.AddAsTwoPointCenteredRectangle Method

Parent Object: [SketchLines](../SketchLines/SketchLines.md)

## Description

Method that creates four lines to represent a rectangle where the center of the rectangle is defined by a point and the corner of the rectangle is defined by the second point and the rectangle is aligned with the sketch x and y axes. The input points can be either Point2d objects defining an x-y point in space, or an existing SketchPoint object. If an existing sketch point is input, the lines will become connected to that point. The created sketch lines are returned in a SketchEntitiesEnumerator object. This includes the four lines representing the rectangle and the two internal construction lines.

## Syntax

SketchLines.**AddAsTwoPointCenteredRectangle**( ***CenterPoint*** As Object, ***CornerPoint*** As Object ) As [SketchEntitiesEnumerator](../SketchEntitiesEnumerator/SketchEntitiesEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CenterPoint | Object | Input object that specifies the center of the rectangle. This can either be a SketchPoint or a Point2d object. |
| CornerPoint | Object | Input object that specifies a corner of the rectangle. This can either be a SketchPoint or a Point2d object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create Centerpoint Rectangles](../../sample-programs/CenterPointRectangle_Sample.md) | Creates a new sketch containing rectangles created using the two new center point rectangle commands. |

## Version

Introduced in version 2013
