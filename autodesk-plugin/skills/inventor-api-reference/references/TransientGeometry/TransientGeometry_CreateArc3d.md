# TransientGeometry.CreateArc3d Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new Arc3d object. The object created is a transient mathematical object and is not displayed graphically.

## Syntax

TransientGeometry.**CreateArc3d**( ***Center*** As [Point](../Point/Point.md), ***Normal*** As [UnitVector](../UnitVector/UnitVector.md), ***ReferenceVector*** As [UnitVector](../UnitVector/UnitVector.md), ***Radius*** As Double, ***StartAngle*** As Double, ***SweepAngle*** As Double ) As [Arc3d](../Arc3d/Arc3d.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Center | [Point](../Point/Point.md) | Input Point object that defines the center of the arc. |
| Normal | [UnitVector](../UnitVector/UnitVector.md) | Input UnitVector that specifies the axis of the arc. The direction of this vector will also determine the direction of the start and sweep angles. Their direction is defined using the right\-hand rule relative to this vector. |
| ReferenceVector | [UnitVector](../UnitVector/UnitVector.md) | Input UnitVector that specifies the zero angle direction the start angle is relative to. Any vector is valid except one that is parallel to the axis vector. |
| Radius | Double | Input Double that specifies the radius of the arc. |
| StartAngle | Double | Input Double that specifies the start angle of the arc. An angle of 0 is along the direction specified by the reference vector. The direction of the angle is defined using the right\-hand rule around the axis vector. |
| SweepAngle | Double | Input Double that specifies the sweep angle of the arc. The sweep direction is defined using the right\-hand rule around the axis vector. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |
| [Create curve primitives](../../sample-programs/TransientGeometry_Sample.md) | This sample demonstrates the creation of curve primitives (lines, arcs, circles, etc.) using client graphics. |

## Version

Introduced in version 11
