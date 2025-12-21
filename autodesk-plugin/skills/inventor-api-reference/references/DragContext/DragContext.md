# DragContext Object

## Description

The DragContext object provides methods that allow a user to move an object similar to the standard Inventor Assembly Drag.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CancelDrag](../DragContext/DragContext_CancelDrag.md) | Method called when the user wants to cancel the drag operation. |
| [Drag](../DragContext/DragContext_Drag.md) | Method called to drag a part to the given position. The Point parameter is the current position of the mouse in model space. This is the same as ModelPosition in OnDrag. |
| [EndDrag](../DragContext/DragContext_EndDrag.md) | Method called when the drag is finished. Use this call to commit the drag changes. |
| [StartDrag](../DragContext/DragContext_StartDrag.md) | Method called at the beginning of the drag to initialize drag environment. This method must be called before any Drag or TryMove call. |
| [TryMove](../DragContext/DragContext_TryMove.md) | Method that tries to position the object at the exact location given. Returns false if object could not be placed at the exact transform given. |

## Accessed From

[CommandManager.CreateDragContext](../CommandManager/CommandManager_CreateDragContext.md)

## Version

Introduced in version 2011
