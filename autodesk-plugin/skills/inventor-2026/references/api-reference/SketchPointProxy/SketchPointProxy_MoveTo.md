# SketchPointProxy.MoveTo Method

Parent Object: [SketchPointProxy](../SketchPointProxy/SketchPointProxy.md)

## Description

Method that moves the sketch point to an explicit X-Y location. Movement of a sketch point is limited by the constraints currently defined on the sketch. If a sketch is partially constrained it will perform the move within the range allowed by the constraints. Because of this, the result of a move may not always be exactly what was specified.

## Syntax

SketchPointProxy.**MoveTo**( ***Point*** As [Point2d](../Point2d/Point2d.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Point | [Point2d](../Point2d/Point2d.md) | Input object that defines the new position of the sketch point. |

## Version

Introduced in version 6
