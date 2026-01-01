# TransientGeometry.SurfaceSurfaceIntersection Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Gets the intersection between the input surfaces.

## Syntax

TransientGeometry.**SurfaceSurfaceIntersection**( ***SurfaceOne*** As Object, ***SurfaceTwo*** As Object, [***Tolerance***] As Double ) As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SurfaceOne | Object | Input object that specifies the first surface for the intersection. The input can be any of the transient surface objects (Plane, Cone, Cylinder, EllipticalCone, EllipticalCylinder, Sphere, Torus or a BSplineSurface). |
| SurfaceTwo | Object | Input object that specifies the second surface for the intersection. The input can be any of the transient surface objects (Plane, Cone, Cylinder, EllipticalCone, EllipticalCylinder, Sphere, Torus or a BSplineSurface). |
| Tolerance | Double | Optional input Double that specifies the linear tolerance to use for intersection computation. If not specified, the default internal tolerance is used. |

## Version

Introduced in version 2012
