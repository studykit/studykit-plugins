# EdgeLoop.IsOuterEdgeLoop Property

Parent Object: [EdgeLoop](../EdgeLoop/EdgeLoop.md)

## Description

Gets whether this EdgeLoop is an external loop, or a loop that encloses material as opposed to a void.

## Syntax

EdgeLoop.**IsOuterEdgeLoop**() As Boolean

## Property Value

This is a read only property whose value is a Boolean.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |

## Version

Introduced in version 4
