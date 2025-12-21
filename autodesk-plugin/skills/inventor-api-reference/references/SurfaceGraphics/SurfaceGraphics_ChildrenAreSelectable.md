# SurfaceGraphics.ChildrenAreSelectable Property

Parent Object: [SurfaceGraphics](../SurfaceGraphics/SurfaceGraphics.md)

## Description

Read-write property that gets and sets whether the children elements of the surface graphics are selectable.

## Syntax

SurfaceGraphics.**ChildrenAreSelectable**() As Boolean

## Property Value

This is a read/write property whose value is a Boolean.

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