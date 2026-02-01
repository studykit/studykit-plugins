# Line.IntersectWithSurface Method

Parent Object: [Line](../Line/Line.md)

## Description

Method that returns Point objects that represent the points at the intersection of the Line/LineSegment and the input surface. Returns Nothing if the Line/LineSegment lies on the surface or it is parallel to the surface.

## Syntax

Line.**IntersectWithSurface**( ***Surface*** As Object, [***Tolerance***] As Double ) As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Surface | Object | Input object. This can be a Plane, Cone, Cylinder, EllipticalCone, EllipticalCylinder, Sphere, Torus or a BSplineSurface. |
| Tolerance | Double | Optional input Double that specifies the linear tolerance to use for intersection computation. If not specified, the default internal tolerance is used. |

## Version

Introduced in version 2008
