# Plane.IntersectWithSurface Method

Parent Object: [Plane](../Plane/Plane.md)

## Description

Gets the intersection curves and points between the plane and the input surface.

## Syntax

Plane.**IntersectWithSurface**( ***Surface*** As Object, [***Tolerance***] As Double ) As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Surface | Object | Input object that specifies the surface to intersect with the plane. The input can be any of the transient surface objects (Plane, Cone, Cylinder, EllipticalCone, EllipticalCylinder, Sphere, Torus or a BSplineSurface.) |
| Tolerance | Double | Optional input Double that specifies the linear tolerance to use for intersection computation. If not specified, the default internal tolerance is used. |

## Version

Introduced in version 2012
