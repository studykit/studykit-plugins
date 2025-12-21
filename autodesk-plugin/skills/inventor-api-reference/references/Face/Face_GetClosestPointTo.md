# Face.GetClosestPointTo Method

Parent Object: [Face](../Face/Face.md)

## Description

Method that returns a point on the face that is closest to the input point. A single point is returned even if multiple equidistant points are found. To get the u-v parameters of the returned point on the face, use Face.Evaluator.GetParamAtPoint method.

## Syntax

Face.**GetClosestPointTo**( ***InputPoint*** As [Point](../Point/Point.md) ) As [Point](../Point/Point.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| InputPoint | [Point](../Point/Point.md) | Point object that specifies the point for which the closest point on the face is to be located. If the input point lies on the Face, the coordinates of the input point are returned. |

## Version

Introduced in version 11
