# TransientGeometry.CurveSurfaceIntersection Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Gets the intersection between the input curve and the input surface.

## Syntax

TransientGeometry.**CurveSurfaceIntersection**( ***Curve*** As Object, ***Surface*** As Object, [***Tolerance***] As Double ) As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Curve | Object | Input object that specifies the curve for the intersection. The input can be any of the transient 3D curve objects (Line, LineSegment, Arc3d, EllipticalArc, Circle, EllipseFull, or a BSplineCurve). |
| Surface | Object | Input object that specifies the surface for the intersection. The input can be any of the transient surface objects (Plane, Cone, Cylinder, EllipticalCone, EllipticalCylinder, Sphere, Torus or a BSplineSurface). |
| Tolerance | Double | Optional input Double that specifies the linear tolerance to use for intersection computation. If not specified, the default internal tolerance is used. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |