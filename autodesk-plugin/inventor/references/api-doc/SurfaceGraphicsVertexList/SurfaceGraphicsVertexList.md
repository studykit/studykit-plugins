# SurfaceGraphicsVertexList Object

## Description

The SurfaceGraphicsVertexList object contains a list of vertices currently displayed by a SurfaceGraphics primitive and allows you to add vertices to the list.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../SurfaceGraphicsVertexList/SurfaceGraphicsVertexList_Add.md) | Method that specifies additional vertices to be displayed. |
| [Clear](../SurfaceGraphicsVertexList/SurfaceGraphicsVertexList_Clear.md) | Method that removes all the vertices from the list. No vertices will be displayed after the method is called. |
| [Remove](../SurfaceGraphicsVertexList/SurfaceGraphicsVertexList_Remove.md) | Method that remove a vertex from the Vertexlist. The vertex will no longer be displayed. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SurfaceGraphicsVertexList/SurfaceGraphicsVertexList_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../SurfaceGraphicsVertexList/SurfaceGraphicsVertexList_Count.md) | Read-only property that returns the number of SurfaceGraphicsVertex objects in the list. |
| [Item](../SurfaceGraphicsVertexList/SurfaceGraphicsVertexList_Item.md) | Returns a SurfaeGraphicsVertex object. |
| [Type](../SurfaceGraphicsVertexList/SurfaceGraphicsVertexList_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SurfaceGraphics.DisplayedVertices](../SurfaceGraphics/SurfaceGraphics_DisplayedVertices.md)

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