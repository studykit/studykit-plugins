# UserInputEvents Object

## Description

The UserInputEvents object provides input event notification. For example, use of the context menu.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../UserInputEvents/UserInputEvents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../UserInputEvents/UserInputEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../UserInputEvents/UserInputEvents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnActivateCommand](../UserInputEvents/UserInputEvents_OnActivateCommand.md) | The OnActivateCommand event notifies the client when a command has been invoked. |
| [OnContextualMiniToolbar](../UserInputEvents/UserInputEvents_OnContextualMiniToolbar.md) | Fires before contextual commands are displayed to the user in the graphics window when the user selects an object. |
| [OnDeleteKeyUp](../UserInputEvents/UserInputEvents_OnDeleteKeyUp.md) | Fires when the user performs a delete key click when no command is active. |
| [OnDoubleClick](../UserInputEvents/UserInputEvents_OnDoubleClick.md) | Event that is sent when the user double-clicks in the window. |
| [OnDrag](../UserInputEvents/UserInputEvents_OnDrag.md) | The OnDrag event notifies the client whenever the end-user performs a drag operation in the graphics window. Using this event, the client can override Inventor's standard drag behavior. |
| [OnLinearMarkingMenu](../UserInputEvents/UserInputEvents_OnLinearMarkingMenu.md) | Fires before the overflow context menu is displayed to the user. |
| [OnPreSelect](../UserInputEvents/UserInputEvents_OnPreSelect.md) | Fires when the user hovers over an Inventor object, and it is a potential candidate for selection. |
| [OnRadialMarkingMenu](../UserInputEvents/UserInputEvents_OnRadialMarkingMenu.md) | Fires before the marking menu is displayed to the user or before the user gestures using the right mouse button. |
| [OnSelect](../UserInputEvents/UserInputEvents_OnSelect.md) | Fires when the user selects an object by clicking. |
| [OnStopPreSelect](../UserInputEvents/UserInputEvents_OnStopPreSelect.md) | Fires when the user hovers away from an Inventor object and it is no longer highlighted. |
| [OnTerminateCommand](../UserInputEvents/UserInputEvents_OnTerminateCommand.md) | The OnTerminateCommand event notifies the client when a command has been terminated. |
| [OnUnSelect](../UserInputEvents/UserInputEvents_OnUnSelect.md) | Event that occurs when the user unselects an entity. This is done in the user interface by pressing the Shift button and selecting a previously selected entity. |

## Accessed From

[CommandManager.UserInputEvents](../CommandManager/CommandManager_UserInputEvents.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [OnDrag Event - dragging a WorkPoint](../../sample-programs/UserInputEventsSink_OnDrag_Sample.md) | This sample demonstrates the use of the OnDrag event to drag fixed work points when no command is active. This sample only allows drags parallel to the X-Y plane. This sample is dependent on events and VB only supports events within a class module. |

## Version

Introduced in version 4
