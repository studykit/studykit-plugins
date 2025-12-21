# LineSegment2d.IntersectWithCurve Method

Parent Object: [LineSegment2d](../LineSegment2d/LineSegment2d.md)

## Description

Method that returns Point2d objects that represent the points at the intersection of the Line2d/LineSegment2d and the input curve. Returns Nothing if the curves overlap or are parallel.

## Syntax

LineSegment2d.**IntersectWithCurve**( ***Curve*** As Object, [***Tolerance***] As Double ) As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Curve | Object | Input object. This can be a Line2d, LineSegment2d, Arc2d, EllipticalArc2d, Circle2d, EllipseFull2d, or a BSplineCurve2d. |
| Tolerance | Double | Optional input Double that specifies the linear tolerance to use for intersection computation. If not specified, the default internal tolerance is used. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |