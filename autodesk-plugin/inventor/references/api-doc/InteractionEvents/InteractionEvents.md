# InteractionEvents Object

## Description

The InteractionEvents object provides the ability to obtain input from the user. This includes selecting objects, various mouse inputs, and using the keyboard.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CreateMiniToolbar](../InteractionEvents/InteractionEvents_CreateMiniToolbar.md) | Method that creates a MiniToolbar object associated with the parent InteractionEvents. |
| [GetCursor](../InteractionEvents/InteractionEvents_GetCursor.md) | Gets the cursor for the command in which this interaction takes place. |
| [SetCursor](../InteractionEvents/InteractionEvents_SetCursor.md) | Sets the cursor for the command in which this interaction takes place. |
| [Start](../InteractionEvents/InteractionEvents_Start.md) | Starts this object inside Inventor. This will cause the OnActivate to fire initiating the activity linked with this object. |
| [Stop](../InteractionEvents/InteractionEvents_Stop.md) | Stops this object inside Inventor. This will cause the OnTerminate to fire halting all activity linked with this object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AllowCommandAliases](../InteractionEvents/InteractionEvents_AllowCommandAliases.md) | Gets/Sets the Boolean flag indicating whether command aliases are allowed while the interaction command is active. |
| [Application](../InteractionEvents/InteractionEvents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [InteractionDisabled](../InteractionEvents/InteractionEvents_InteractionDisabled.md) | Gets/Sets the Boolean flag that disables this object's Selection, Mouse and Keyboard Events. Setting this to True, continues to honor the SelectionActive flag. |
| [InteractionGraphics](../InteractionEvents/InteractionEvents_InteractionGraphics.md) | Gets the Interaction Graphics object. |
| [KeyboardEvents](../InteractionEvents/InteractionEvents_KeyboardEvents.md) | Gets the Keyboard Events object. |
| [ManipulatorEvents](../InteractionEvents/InteractionEvents_ManipulatorEvents.md) | Gets the ManipulatorEvents object. |
| [MeasureEvents](../InteractionEvents/InteractionEvents_MeasureEvents.md) | Gets the Measure Events object. |
| [MouseEvents](../InteractionEvents/InteractionEvents_MouseEvents.md) | Gets the Mouse Events object. |
| [Name](../InteractionEvents/InteractionEvents_Name.md) | Gets/Sets the name for the command in which this interaction takes place. |
| [Parent](../InteractionEvents/InteractionEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [SelectEvents](../InteractionEvents/InteractionEvents_SelectEvents.md) | Gets the Selection Events object. |
| [StatusBarText](../InteractionEvents/InteractionEvents_StatusBarText.md) | Gets/Sets the status bar message for the command in which this interaction takes place. |
| [TargetDocument](../InteractionEvents/InteractionEvents_TargetDocument.md) | Gets the Document which is the context in which this interaction takes place. |
| [TriadEvents](../InteractionEvents/InteractionEvents_TriadEvents.md) | Gets the TriadEvents object. |
| [Type](../InteractionEvents/InteractionEvents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnActivate](../InteractionEvents/InteractionEvents_OnActivate.md) | Event that notifies the command that control has been passed to it. This event is fired when the command initially starts, (when the Start method has been called). |
| [OnHelp](../InteractionEvents/InteractionEvents_OnHelp.md) | Event that fires to signal the client to present help for the associated activity. |
| [OnResume](../InteractionEvents/InteractionEvents_OnResume.md) | Event that notifies the command to resume execution after being suspended. |
| [OnSuspend](../InteractionEvents/InteractionEvents_OnSuspend.md) | Event that notifies the InteractionEvents object to temporarily suspend itself. This happens when the user selects a command that stacks on the current command. Invocation of any of the view commands will cause the stacking behavior. |
| [OnTerminate](../InteractionEvents/InteractionEvents_OnTerminate.md) | Event that notifies the command has been terminated. This can happen when the user selects another command or presses escape. It can be forced by calling the Stop method on the InteractionEvents object as well. |

## Accessed From

[CommandManager.CreateInteractionEvents](../CommandManager/CommandManager_CreateInteractionEvents.md), [KeyboardEvents.Parent](../KeyboardEvents/KeyboardEvents_Parent.md), [ManipulatorEvents.Parent](../ManipulatorEvents/ManipulatorEvents_Parent.md), [MeasureEvents.Parent](../MeasureEvents/MeasureEvents_Parent.md), [MouseEvents.Parent](../MouseEvents/MouseEvents_Parent.md), [SelectEvents.Parent](../SelectEvents/SelectEvents_Parent.md), [TriadEvents.Parent](../TriadEvents/TriadEvents_Parent.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Basic Selection Using Interaction Events](../../sample-programs/InteractionEventsSink_Sample.md) | This sample demonstrates using the selection events to select a face. Selection is dependent on events and VB only supports events within a class module. |
| [Using measure events](../../sample-programs/MeasureEventsSink_OnMeasure_Sample.md) | This sample demonstrates using the measure events to measure distance and angle. Interactive measure is dependent on events and VB only supports events within a class module. To use the sample copy the InteractiveMeasureDistance and InteractiveMeasureAngle subs into a code module. Create a new class module called clsMeasure and copy all of the rest of the code into it. |
| [Window Selection](../../sample-programs/SelectEventsObject_WindowSelectEnabled_Sample.md) | This sample demonstrates using the selection events to window-select multiple edges. Selection is dependent on events and VB only supports events within a class module. |
| [OnDrag Event - dragging a WorkPoint](../../sample-programs/UserInputEventsSink_OnDrag_Sample.md) | This sample demonstrates the use of the OnDrag event to drag fixed work points when no command is active. This sample only allows drags parallel to the X-Y plane. This sample is dependent on events and VB only supports events within a class module. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |