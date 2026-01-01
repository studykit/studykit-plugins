# Line.IntersectWithCurve Method

Parent Object: [Line](../Line/Line.md)

## Description

Method that returns Point objects that represent the points at the intersection of the Line/LineSegment and the input curve. Returns Nothing if the curves overlap or are parallel.

## Syntax

Line.**IntersectWithCurve**( ***Curve*** As Object, [***Tolerance***] As Double ) As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Curve | Object | Input object. This can be a Line, LineSegment, Arc3d, EllipticalArc, Circle, EllipseFull, or a BSplineCurve. |
| Tolerance | Double | Optional input Double that specifies the linear tolerance to use for intersection computation. If not specified, the default internal tolerance is used. |

## Version

Introduced in version 2008
