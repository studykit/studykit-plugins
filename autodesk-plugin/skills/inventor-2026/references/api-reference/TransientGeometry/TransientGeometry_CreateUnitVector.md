# TransientGeometry.CreateUnitVector Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new UnitVector object.

## Syntax

TransientGeometry.**CreateUnitVector**( [***XCoord***] As Double, [***YCoord***] As Double, [***ZCoord***] As Double ) As [UnitVector](../UnitVector/UnitVector.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| XCoord | Double | Input Double that specifies the UnitVector's X-coordinate. |
| YCoord | Double | Input Double that specifies the UnitVector's Y-coordinate.   This is an optional argument whose default value is 0.0. |
| ZCoord | Double | Input Double that specifies the UnitVector's Z-coordinate.   This is an optional argument whose default value is 1.0. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Offset a 2D sketch](../../sample-programs/Sketch_OffsetSketchEntitiesUsingDistance_Sample.md) | This sample demonstrates the creation of offsets in 2d sketches. Two ways of creating the offset are shown - one uses a distance and the other uses the input point. |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |
| [Create curve primitives](../../sample-programs/TransientGeometry_Sample.md) | This sample demonstrates the creation of curve primitives (lines, arcs, circles, etc.) using client graphics. |

## Version

Introduced in version 4
