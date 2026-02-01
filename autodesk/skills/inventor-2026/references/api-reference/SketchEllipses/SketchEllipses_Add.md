# SketchEllipses.Add Method

Parent Object: [SketchEllipses](../SketchEllipses/SketchEllipses.md)

## Description

Method that creates a new sketch ellipse.

## Syntax

SketchEllipses.**Add**( ***CenterPoint*** As Object, ***MajorAxisVector*** As [UnitVector2d](../UnitVector2d/UnitVector2d.md), ***MajorRadius*** As Double, ***MinorRadius*** As Double ) As [SketchEllipse](../SketchEllipse/SketchEllipse.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CenterPoint | Object | Input object that defines the center point. This can be either a SketchPoint or Point2d object. In the case where a SketchPoint object is input, the ellipse will be attached to the point. |
| MajorAxisVector | [UnitVector2d](../UnitVector2d/UnitVector2d.md) | Input UnitVector2d that defines the direction of the major axis. |
| MajorRadius | Double | Input Double that defines the major radius in centimeters. |
| MinorRadius | Double | Input Double that defines the minor radius in centimeters. |

## Version

Introduced in version 5
