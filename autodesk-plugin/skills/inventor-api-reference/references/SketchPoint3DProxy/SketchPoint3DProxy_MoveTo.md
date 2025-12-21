# SketchPoint3DProxy.MoveTo Method

Parent Object: [SketchPoint3DProxy](../SketchPoint3DProxy/SketchPoint3DProxy.md)

## Description

Method that moves the sketch point to an explicit x-y-z location. Movement of a sketch point is limited by the constraints currently defined on the sketch. If a sketch is partially constrained it will perform the move within the range allowed by the constraints. Because of this, the result of a move may not always be exactly what was specified.

## Syntax

SketchPoint3DProxy.**MoveTo**( ***Point*** As [Point](../Point/Point.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Point | [Point](../Point/Point.md) | Object that defines the new position of the sketch point. |

## Version

Introduced in version 11
