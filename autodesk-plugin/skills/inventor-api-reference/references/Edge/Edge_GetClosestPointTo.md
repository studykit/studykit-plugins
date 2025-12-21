# Edge.GetClosestPointTo Method

Parent Object: [Edge](../Edge/Edge.md)

## Description

Method that returns a point on the edge that is closest to the input point. A single point is returned even if multiple equidistant points are found. To get the u parameter of the returned point on the edge, use Edge.Evaluator.GetParamAtPoint method.

## Syntax

Edge.**GetClosestPointTo**( ***InputPoint*** As [Point](../Point/Point.md) ) As [Point](../Point/Point.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| InputPoint | [Point](../Point/Point.md) | Point object that specifies the point for which the closest point on the edge is to be located. If the input point lies on the Edge, the coordinates of the input point are returned. |

## Version

Introduced in version 11
