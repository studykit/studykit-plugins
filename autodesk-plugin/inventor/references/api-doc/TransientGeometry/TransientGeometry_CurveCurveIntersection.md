# TransientGeometry.CurveCurveIntersection Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Gets the intersection between the input curves.

## Syntax

TransientGeometry.**CurveCurveIntersection**( ***CurveOne*** As Object, ***CurveTwo*** As Object, [***Tolerance***] As Double ) As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CurveOne | Object | Input object that specifies the first curve for the intersection. The input can be any of the transient 3D curve objects (Line, LineSegment, Arc3d, EllipticalArc, Circle, EllipseFull, or a BSplineCurve). |
| CurveTwo | Object | Input object that specifies the second curve for the intersection. The input can be any of the transient 3D curve objects (Line, LineSegment, Arc3d, EllipticalArc, Circle, EllipseFull, or a BSplineCurve). |
| Tolerance | Double | Optional input Double that specifies the linear tolerance to use for intersection computation. If not specified, the default internal tolerance is used. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |