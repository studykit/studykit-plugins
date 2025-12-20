# CommandManager Object

## Description

The CommandManager object provides functionality that interacts with the various user interaction events. See here for an overview.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ClearPrivateEvents](../CommandManager/CommandManager_ClearPrivateEvents.md) | Clears the contents of Autodesk Inventor's internal clipboard. |
| [CreateDragContext](../CommandManager/CommandManager_CreateDragContext.md) | Method that creates a new DragContext object. |
| [CreateInteractionEvents](../CommandManager/CommandManager_CreateInteractionEvents.md) | Method that creates and returns a new InteractionEvents object. The InteractionEvents object is created for document that is currently active. |
| [CreateMiniToolbar](../CommandManager/CommandManager_CreateMiniToolbar.md) | Method that creates a MiniToolbar object. |
| [DoPreSelect](../CommandManager/CommandManager_DoPreSelect.md) | Method that causes Autodesk Inventor to go through the pre-selection protocol, including firing of corresponding event out the active InteractionEvents object if one is active. If a native Autodesk Inventor command is active and is in a selection mode, it gets the pre-select notification just like a native pre-selection happened. This method is useful when you want to perform picking outside of the graphic window. For example if you have a browser that has icons that represent selectable objects you can cause the selection behavior to happen as the user navigates through your browser and selects objects. |
| [DoSelect](../CommandManager/CommandManager_DoSelect.md) | Method that causes Autodesk Inventor to go through the selection protocol, including firing of corresponding event out the active InteractionEvents object if one is active. If a native Autodesk Inventor command is active and is in a selection mode, it gets the select notification just like a native selection happened. This method is useful when you want to perform picking outside of the graphic window. For example if you have a browser that has icons that represent selectable objects you can cause the selection behavior to happen as the user navigates through your browser and selects objects. |
| [DoStopPreSelect](../CommandManager/CommandManager_DoStopPreSelect.md) | Method that causes Autodesk Inventor to go through the stop pre-selection protocol, including firing of corresponding event out the active InteractionEvents object if one is active. If a native Autodesk Inventor command is active and is in a selection mode, it gets the stop pre-select notification just like a native stop pre-selection happened. This method is useful when you want to perform picking outside of the graphic window. For example if you have a browser that has icons that represent selectable objects you can cause the selection behavior to happen as the user navigates through your browser and selects objects. |
| [DoUnSelect](../CommandManager/CommandManager_DoUnSelect.md) | Method that causes Autodesk Inventor to go through the de-selection protocol, including firing of corresponding event out the active InteractionEvents object if one is active. If a native Autodesk Inventor command is active and is in a selection mode, it gets the de-select notification just like a native de-selection happened. This method is useful when you want to perform picking outside of the graphic window. For example if you have a browser that has icons that represent selectable objects you can cause the selection behavior to happen as the user navigates through your browser and selects objects. |
| [PeekPrivateEvent](../CommandManager/CommandManager_PeekPrivateEvent.md) | Method that queries data contained by Autodesk Inventor's internal clipboard. |
| [Pick](../CommandManager/CommandManager_Pick.md) | Method that allows the user to pick a single entity. |
| [PostPrivateEvent](../CommandManager/CommandManager_PostPrivateEvent.md) | Method that posts data onto Autodesk Inventor's internal clipboard. Certain commands that usually obtain information using a dialog, i.e. Open, Save, etc., look first to see if data is on the clipboard before displaying the dialog. If valid information is on the clipboard the command will use it instead of displaying the dialog and asking the user to specify the filename. |
| [PromptMessage](../CommandManager/CommandManager_PromptMessage.md) | This method allows the developer to put up prompt messages (unless the user has suppressed this prompt) much like the Visual Basic MsgBox functionality. |
| [StartExecutable](../CommandManager/CommandManager_StartExecutable.md) | Method that causes the specified executable to be run. Using the Parameters argument you can also pass arguments to the executable. |
| [StopActiveCommand](../CommandManager/CommandManager_StopActiveCommand.md) | Method that causes the currently running command to be terminated. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveCommand](../CommandManager/CommandManager_ActiveCommand.md) | Gets the active command (one that is currently running). |
| [CommandCategories](../CommandManager/CommandManager_CommandCategories.md) | Property that returns the collection. |
| [ControlDefinitions](../CommandManager/CommandManager_ControlDefinitions.md) | Property that returns the ControlDefinitions collection. |
| [Parent](../CommandManager/CommandManager_Parent.md) | Property that returns the parent document of the object. |
| [SelectionActive](../CommandManager/CommandManager_SelectionActive.md) | Property that informs the client if Autodesk Inventor is currently in selection mode or not. This may be used, for example, by clients to test if calling the DoSelect (and related) methods will have any effect or not. |
| [Type](../CommandManager/CommandManager_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UserInputEvents](../CommandManager/CommandManager_UserInputEvents.md) | Property that returns the object that fires events on all user input (commands, keyboard, mouse, etc.). |

## Accessed From

[Application.CommandManager](../Application/Application_CommandManager.md), [ButtonDefinition.Parent](../ButtonDefinition/ButtonDefinition_Parent.md), [ComboBoxDefinition.Parent](../ComboBoxDefinition/ComboBoxDefinition_Parent.md), [CommandCategory.Parent](../CommandCategory/CommandCategory_Parent.md), [ControlDefinition.Parent](../ControlDefinition/ControlDefinition_Parent.md), [InteractionEvents.Parent](../InteractionEvents/InteractionEvents_Parent.md), [MacroControlDefinition.Parent](../MacroControlDefinition/MacroControlDefinition_Parent.md), [UserInputEvents.Parent](../UserInputEvents/UserInputEvents_Parent.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add commands to the application menu](../../sample-programs/AddButtonToAppMenu_Sample.md) | Demonstrates adding command to the application menu. |
| [Single selection - simple](../../sample-programs/CommandManager_Pick_Sample.md) | The following sample demonstrates getting a single selection from the user. |
| [Replace content center part](../../sample-programs/ContentCenterPartReplace_Sample.md) | This sample demonstrates how to replace the content part referenced by an assembly occurrence. |
| [Copy a sketch](../../sample-programs/CopySketch_Sample.md) | This sample demonstrates copying the contents of a sketch into another sketch via the API. |
| [Print list of all Inventor Commands](../../sample-programs/DumpControlDefinitions_Sample.md) | This sample prints the internal names and descriptions of all commands (aka ControlDefinitions) in Inventor. |
| [Creation of an override environment for a document](../../sample-programs/EnvironmentManager_OverrideEnvironment_Sample.md) | A new ribbon tab is created and associated with the override environment. |
| [Post Private Event Sample](../../sample-programs/PostPrivateEventSample_Sample.md) | This sample demonstrates how to use the PostPrivateEvent to configure the options for placing a part component. |
| [Create a ribbon panel in an existing tab](../../sample-programs/RibbonPanels_Add_Sample.md) | Demonstrates creating a new ribbon panel within an existing ribbon tab. |
| [Window Selection](../../sample-programs/SelectEventsObject_WindowSelectEnabled_Sample.md) | This sample demonstrates using the selection events to window-select multiple edges. Selection is dependent on events and VB only supports events within a class module. |
| [Copy sketch contents](../../sample-programs/Sketch_CopyContentsTo_Sample.md) | This sample shows how to copy the contents of one sketch to another. |
| [Cancel a double click](../../sample-programs/UserInputEventsSink_OnDoubleClick_Sample.md) | Demonstrates how to receive (and in this case, cancel) a double click from a user. |
| [OnDrag Event - dragging a WorkPoint](../../sample-programs/UserInputEventsSink_OnDrag_Sample.md) | This sample demonstrates the use of the OnDrag event to drag fixed work points when no command is active. This sample only allows drags parallel to the X-Y plane. This sample is dependent on events and VB only supports events within a class module. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |