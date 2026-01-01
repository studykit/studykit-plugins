# LineAndTangentWorkPlaneDef.GetData Method

Parent Object: [LineAndTangentWorkPlaneDef](../LineAndTangentWorkPlaneDef/LineAndTangentWorkPlaneDef.md)

## Description

Method that gets all of the data defining a work that passes through the line and is tangent to the input face.

## Syntax

LineAndTangentWorkPlaneDef.**GetData**( ***Line*** As Object, ***Face*** As [Face](../Face/Face.md), ***ProximityPoint*** As [Point](../Point/Point.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Line | Object | Output object that represents a line. This object can be a linear Edge, WorkAxis, or SketchLine object. The work plane passes through this line. |
| Face | [Face](../Face/Face.md) | Output Face object that indicates the tangent surface. This face will be a cylinder, cone, or sphere. |
| ProximityPoint | [Point](../Point/Point.md) | Output object that indicates which of the possible two solutions was used when calculating the tangent plane. The proximity point itself is not stored. The point returned is calculated as an arbitrary point along the tangent between the face and plane. |

## Version

Introduced in version 4
