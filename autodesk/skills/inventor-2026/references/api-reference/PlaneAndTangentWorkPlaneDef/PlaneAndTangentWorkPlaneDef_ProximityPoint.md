# PlaneAndTangentWorkPlaneDef.ProximityPoint Property

Parent Object: [PlaneAndTangentWorkPlaneDef](../PlaneAndTangentWorkPlaneDef/PlaneAndTangentWorkPlaneDef.md)

## Description

Property that returns the proximity point. The proximity point defines which of the two possible solutions is chosen when computing the tangent plane. This point is used for the initial computation and the specific point is not stored. During a recompute of the model the plane will remain on the same side of the tangent surface regardless of its position relative to the originally specified point. The point returned by this property is as an arbitrary point along the tangent between the face and plane.

## Syntax

PlaneAndTangentWorkPlaneDef.**ProximityPoint**() As [Point](../Point/Point.md)

## Property Value

This is a read only property whose value is a [Point](../Point/Point.md).

## Version

Introduced in version 4
