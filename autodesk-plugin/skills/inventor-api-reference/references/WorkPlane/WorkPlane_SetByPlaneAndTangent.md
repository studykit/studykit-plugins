# WorkPlane.SetByPlaneAndTangent Method

Parent Object: [WorkPlane](../WorkPlane/WorkPlane.md)

## Description

Method that redefines the work plane to be parallel to the input plane and tangent to the input surface.

## Remarks

This method is not valid when the work plane exists in an Assembly component definition.

## Syntax

WorkPlane.**SetByPlaneAndTangent**( ***Plane*** As Object, ***Face*** As [Face](../Face/Face.md), ***ProximityPoint*** As [Point](../Point/Point.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Plane | Object | Input object that represents a Plane. This object can be a planar Face, WorkPlane, or Sketch object. |
| Face | [Face](../Face/Face.md) | Input Face object that indicates the tangent surface. This face must either be a cylinder whose axis is parallel to the line, a cone that is positioned such that a valid tangent exists, or a sphere. |
| ProximityPoint | [Point](../Point/Point.md) | Input Point object that indicates which of the possible two solutions to use. Valid geometry for the face includes cylinders, cones, and spheres. For cylinders and spheres the plane can be on either side of the surface. Which solution to use will be determined by which side the proximity point is closest to. This point is only used for the initial computation. During a recompute the plane will remain on the same side of the tangent surface regardless of its position relative to the originally specified point. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |