# PlaneAndTangentWorkPlaneDef.GetData Method

Parent Object: [PlaneAndTangentWorkPlaneDef](../PlaneAndTangentWorkPlaneDef/PlaneAndTangentWorkPlaneDef.md)

## Description

Method that gets all of the data defining a work that is parallel to the plane and tangent to the input face.

## Syntax

PlaneAndTangentWorkPlaneDef.**GetData**( ***Plane*** As Object, ***Face*** As [Face](../Face/Face.md), ***ProximityPoint*** As [Point](../Point/Point.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Plane | Object | Output object that represents a plane. This object can be a planar Face, WorkPlane, or Sketch object. The work plane is parallel to this plane. |
| Face | [Face](../Face/Face.md) | Output Face object that indicates the tangent surface. This face will be a cylinder, cone, or sphere. |
| ProximityPoint | [Point](../Point/Point.md) | Output object that indicates which of the possible two solutions was used when calculating the tangent plane. The original proximity point itself is not stored. The point returned is calculated as an arbitrary point along the tangent between the face and plane. |

## Version

Introduced in version 4
