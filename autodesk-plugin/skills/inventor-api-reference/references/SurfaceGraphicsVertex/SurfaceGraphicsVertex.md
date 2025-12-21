# SurfaceGraphicsVertex Object

## Description

surface graphics vertex object.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SurfaceGraphicsVertex/SurfaceGraphicsVertex_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Index](../SurfaceGraphicsVertex/SurfaceGraphicsVertex_Index.md) | Gets the index of the SurfaceGraphicsVertex object within the SurfaceGraphicsVertexList. |
| [Parent](../SurfaceGraphicsVertex/SurfaceGraphicsVertex_Parent.md) | Read-only property that returns the parent SurfaceGraphics object. |
| [Selectable](../SurfaceGraphicsVertex/SurfaceGraphicsVertex_Selectable.md) | Read-write property that specifies whether the surface graphics vertex can be selected or not. |
| [Type](../SurfaceGraphicsVertex/SurfaceGraphicsVertex_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Vertex](../SurfaceGraphicsVertex/SurfaceGraphicsVertex_Vertex.md) | Read-only property that returns the Vertex object associated with the SurfaceGraphicsVertex. |

## Accessed From

[SurfaceGraphicsVertexList.Item](../SurfaceGraphicsVertexList/SurfaceGraphicsVertexList_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Selection of Surface Graphics Primitives](../../sample-programs/SelectSurfaceGraphicsPrimitives_Sample.md) | This demonstrates the ability to select client graphic primitives, by creating SurfaceGraphics and showing how you can select B-Rep entities within the graphics. You must have a part or assembly open and select a part of sat file which will be read in and displayed as client graphics. Depending on our responses to the program it will create the graphics so that only the node is selectable (which is all that was supported before), so that all of the primitives are selected, or so that only certain primitives are selectable (every other face in this case). |

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |