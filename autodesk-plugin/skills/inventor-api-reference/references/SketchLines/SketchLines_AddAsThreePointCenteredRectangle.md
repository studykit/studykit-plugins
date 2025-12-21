# SketchLines.AddAsThreePointCenteredRectangle Method

Parent Object: [SketchLines](../SketchLines/SketchLines.md)

## Description

Method that creates four lines to represent a rectangle where the center of the rectangle is defined by a point, the length and orientation is defined by a second point, and the width defined by a third point.

## Remarks

The input points are illustrated in the picture below. The width point can be anywhere along the green line since it’s the distance between this point and the line defined by the center and edge point that defines the width.

![](../images/AddAsThreePointCenteredRectangle.png)

The first two input points can be either Point2d objects defining an x-y point in space, or an existing SketchPoint object. If an existing sketch point is input, the lines will become connected to that point. The created sketch lines are returned in a SketchEntitiesEnumerator object. This includes the four lines representing the rectangle and the two internal construction lines.

## Syntax

SketchLines.**AddAsThreePointCenteredRectangle**( ***CenterPoint*** As Object, ***EdgePoint*** As Object, ***WidthPoint*** As [Point2d](../Point2d/Point2d.md) ) As [SketchEntitiesEnumerator](../SketchEntitiesEnumerator/SketchEntitiesEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CenterPoint | Object | Input object that specifies the center of the rectangle. This can either be a SketchPoint or a Point2d object. |
| EdgePoint | Object | Input object that specifies a point on the edge of the rectangle that defines the orientation and length of the rectangle. |
| WidthPoint | [Point2d](../Point2d/Point2d.md) | Input Point2d that defines the width of the rectangle. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create Centerpoint Rectangles](../../sample-programs/CenterPointRectangle_Sample.md) | Creates a new sketch containing rectangles created using the two new center point rectangle commands. |

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |