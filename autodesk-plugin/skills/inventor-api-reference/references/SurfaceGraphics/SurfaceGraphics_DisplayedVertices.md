# SurfaceGraphics.DisplayedVertices Property

Parent Object: [SurfaceGraphics](../SurfaceGraphics/SurfaceGraphics.md)

## Description

Read-only property that returns a SurfaceGraphicsVertexList object. This list provides access to all vertices that are currently displayed. Vertices can be added to or removed from the list. The vertices added to the list must be from the surface body associated with the SurfaceGraphics, else an error will occur.

## Syntax

SurfaceGraphics.**DisplayedVertices**() As [SurfaceGraphicsVertexList](../SurfaceGraphicsVertexList/SurfaceGraphicsVertexList.md)

## Property Value

This is a read only property whose value is a [SurfaceGraphicsVertexList](../SurfaceGraphicsVertexList/SurfaceGraphicsVertexList.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Selection of Surface Graphics Primitives](../../sample-programs/SelectSurfaceGraphicsPrimitives_Sample.md) | This demonstrates the ability to select client graphic primitives, by creating SurfaceGraphics and showing how you can select B-Rep entities within the graphics. You must have a part or assembly open and select a part of sat file which will be read in and displayed as client graphics. Depending on our responses to the program it will create the graphics so that only the node is selectable (which is all that was supported before), so that all of the primitives are selected, or so that only certain primitives are selectable (every other face in this case). |

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |