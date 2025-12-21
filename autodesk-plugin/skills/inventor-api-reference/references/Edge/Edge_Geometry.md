# Edge.Geometry Property

Parent Object: [Edge](../Edge/Edge.md)

## Description

Property that returns the underlying geometry of the edge (e.g. Arc2D, Circle, Cone etc.)

## Syntax

Edge.**Geometry**() As Object

## Property Value

This is a read only property whose value is an Object.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal face and fold features](../../sample-programs/FoldFeatures_Add_Sample.md) | This sample demonstrates the creation of sheet metal face and fold features. |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |

## Version

Introduced in version 6
