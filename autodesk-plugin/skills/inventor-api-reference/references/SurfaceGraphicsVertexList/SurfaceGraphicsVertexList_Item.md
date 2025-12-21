# SurfaceGraphicsVertexList.Item Property

Parent Object: [SurfaceGraphicsVertexList](../SurfaceGraphicsVertexList/SurfaceGraphicsVertexList.md)

## Description

Returns a SurfaeGraphicsVertex object.

## Syntax

SurfaceGraphicsVertexList.**Item**( ***Index*** As Variant ) As [SurfaceGraphicsVertex](../SurfaceGraphicsVertex/SurfaceGraphicsVertex.md)

## Property Value

This is a read only property whose value is a [SurfaceGraphicsVertex](../SurfaceGraphicsVertex/SurfaceGraphicsVertex.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Specifies which SurfaeGraphicsVertex object to return. This can be a Long, which specifies the index in the list, or it can be the Vertex object referenced by a SurfaceGraphicsVertex object. The property will fail in the case where an Index is provided that does not identify an existing SurfaeGraphicsVertex object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Selection of Surface Graphics Primitives](../../sample-programs/SelectSurfaceGraphicsPrimitives_Sample.md) | This demonstrates the ability to select client graphic primitives, by creating SurfaceGraphics and showing how you can select B-Rep entities within the graphics. You must have a part or assembly open and select a part of sat file which will be read in and displayed as client graphics. Depending on our responses to the program it will create the graphics so that only the node is selectable (which is all that was supported before), so that all of the primitives are selected, or so that only certain primitives are selectable (every other face in this case). |

## Version

Introduced in version 2013
