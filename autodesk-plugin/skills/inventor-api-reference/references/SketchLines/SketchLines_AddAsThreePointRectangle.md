# SketchLines.AddAsThreePointRectangle Method

Parent Object: [SketchLines](../SketchLines/SketchLines.md)

## Description

Method that creates four lines to represent a rectangle where the base of the rectangle is defined by two points and the height is defined by a third point. The input points for the base can be either Point2d objects defining an X-Y point in space, or an existing SketchPoint object.

## Remarks

If an existing sketch point is input, the lines will become connected to that point. The two base points define the start and end points of the base the line of the rectangle. This base line defines the length and orientation of the rectangle. The height point is always input as a Point2d object and defines the height of the rectangle. The created sketch lines are returned in an SketchEntitiesEnumerator object.

## Syntax

SketchLines.**AddAsThreePointRectangle**( ***BasePointOne*** As Object, ***BasePointTwo*** As Object, ***HeightPoint*** As [Point2d](../Point2d/Point2d.md) ) As [SketchEntitiesEnumerator](../SketchEntitiesEnumerator/SketchEntitiesEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BasePointOne | Object | Input object that defines the first base point of the rectangle. Either a SketchPoint or Point2d object can be used. If an existing sketch point is input, that lines become connected to the point. |
| BasePointTwo | Object | Input object that defines the second base point of the rectangle. Either a SketchPoint or Point2d object can be used. If an existing sketch point is input, the lines become connected to the point. |
| HeightPoint | [Point2d](../Point2d/Point2d.md) | Input Point2d object that defines the height of the rectangle. The point can be anywhere in space and the height of the rectangle is computed by finding the shortest distance of this point to an infinite line defined by the two base points. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketch Lines](../../sample-programs/Sketch_SketchLines_Sample.md) | This sample demonstrates creating lines. It uses all of the various methods to create lines, both singly and as rectangles. |

## Version

Introduced in version 5
