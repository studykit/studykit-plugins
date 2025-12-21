# SketchPoint3D.MoveBy Method

Parent Object: [SketchPoint3D](../SketchPoint3D/SketchPoint3D.md)

## Description

Method that moves the sketch point a delta distance from its current location. Movement of a sketch point is limited by the constraints currently defined on the sketch. If a sketch is partially constrained it will perform the move within the range allowed by the constraints. Because of this, the result of a move may not always be exactly what was specified.

## Syntax

SketchPoint3D.**MoveBy**( ***Vector*** As [Vector](../Vector/Vector.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Vector | [Vector](../Vector/Vector.md) | Object that defines the delta distance to move the sketch point. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |