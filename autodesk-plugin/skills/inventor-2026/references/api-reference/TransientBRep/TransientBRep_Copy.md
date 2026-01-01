# TransientBRep.Copy Method

Parent Object: [TransientBRep](../TransientBRep/TransientBRep.md)

## Description

Method that creates a copy of the input SurfaceBody, Face, or Edge object.

## Remarks

The resulting copy is a transient SurfaceBody. If a SurfaceBody object was input then the entire body is copied. If a Face object is input then the output body will contain only that single face. If an Edge object is input then the output body will contain a Wire which will contain a single edge.

## Syntax

TransientBRep.**Copy**( ***Entity*** As Object ) As [SurfaceBody](../SurfaceBody/SurfaceBody.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Entity | Object | The input B-Rep entity, which can be a SurfaceBody, Face, or Edge object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Imprint bodies within an assembly.](../../sample-programs/ImprintUsingOccurrences_Sample.md) | This sample demonstrates creating imprinted bodies from two selected occurrences in an assembly. |
| [Selection of Surface Graphics Primitives](../../sample-programs/SelectSurfaceGraphicsPrimitives_Sample.md) | This demonstrates the ability to select client graphic primitives, by creating SurfaceGraphics and showing how you can select B-Rep entities within the graphics. You must have a part or assembly open and select a part of sat file which will be read in and displayed as client graphics. Depending on our responses to the program it will create the graphics so that only the node is selectable (which is all that was supported before), so that all of the primitives are selected, or so that only certain primitives are selectable (every other face in this case). |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |

## Version

Introduced in version 2009
