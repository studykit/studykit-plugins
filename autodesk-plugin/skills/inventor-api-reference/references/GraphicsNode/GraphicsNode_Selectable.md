# GraphicsNode.Selectable Property

Parent Object: [GraphicsNode](../GraphicsNode/GraphicsNode.md)

## Description

Property that specifies whether the GraphicsNode object can be selected when the Select command is running in Inventor.

## Syntax

GraphicsNode.**Selectable**() As Boolean

## Property Value

This is a read/write property whose value is a Boolean.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client Graphics - Draw Range Box](../../sample-programs/ClientGraphics_Sample.md) | This sample demonstrates the use of client graphics to draw the range box of selected entities. |
| [Selection of Surface Graphics Primitives](../../sample-programs/SelectSurfaceGraphicsPrimitives_Sample.md) | This demonstrates the ability to select client graphic primitives, by creating SurfaceGraphics and showing how you can select B-Rep entities within the graphics. You must have a part or assembly open and select a part of sat file which will be read in and displayed as client graphics. Depending on our responses to the program it will create the graphics so that only the node is selectable (which is all that was supported before), so that all of the primitives are selected, or so that only certain primitives are selectable (every other face in this case). |

## Version

Introduced in version 5
