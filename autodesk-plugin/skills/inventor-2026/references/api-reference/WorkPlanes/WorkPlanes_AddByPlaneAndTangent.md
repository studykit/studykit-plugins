# WorkPlanes.AddByPlaneAndTangent Method

Parent Object: [WorkPlanes](../WorkPlanes/WorkPlanes.md)

## Description

Method that creates a new work plane that is parallel to the input plane and tangent to the input surface. Valid geometry for the face includes cylinders, cones, and spheres. This method is not currently supported when creating a work plane within an assembly.

## Syntax

WorkPlanes.**AddByPlaneAndTangent**( ***Plane*** As Object, ***Face*** As [Face](../Face/Face.md), ***ProximityPoint*** As [Point](../Point/Point.md), [***Construction***] As Boolean ) As [WorkPlane](../WorkPlane/WorkPlane.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Plane | Object | Input object that represents a Plane. This object can be a planar Face, WorkPlane, or Sketch object. |
| Face | [Face](../Face/Face.md) | Input Face object that indicates the tangent surface. This face must either be a cylinder whose axis is parallel to the plane, a cone that is positioned such that a valid tangent exists, or a sphere. |
| ProximityPoint | [Point](../Point/Point.md) | Input Point object that indicates which of the possible two solutions to use. For cylinders and spheres the plane can be on either side of the surface. Which solution to use will be determined by which side the proximity point is closest to. This point is only used for the initial computation. During a recompute the plane will remain on the same side of the tangent surface regardless of its position relative to the originally specified point. |
| Construction | Boolean | Optional Input Boolean that specifies whether to create the work plane as a construction plane or not. The default is False, which indicates to create a standard work plane, not a construction work plane. A construction work plane is hidden from the user and is not displayed graphically or listed in the browser. |

## Version

Introduced in version 4
