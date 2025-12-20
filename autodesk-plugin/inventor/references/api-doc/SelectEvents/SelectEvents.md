# SelectEvents Object

## Description

The SelectEvents object supports a set of events that are fired when the user is selecting geometry. These events are fired when the user is selecting items from various UI elements such as the graphics window or the browser.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddSelectionFilter](../SelectEvents/SelectEvents_AddSelectionFilter.md) | Adds a new filter (indication of the type of object(s) of interest) to the existing list of filters. |
| [AddToSelectedEntities](../SelectEvents/SelectEvents_AddToSelectedEntities.md) | Adds an entity to the selected entities collection. |
| [AddWindowSelectionFilter](../SelectEvents/SelectEvents_AddWindowSelectionFilter.md) | Adds a new filter (indication of the type of object(s) of interest) to the list of filters for Window Select (defaults to same filter list specified by AddSelectionFilter). |
| [ClearSelectionFilter](../SelectEvents/SelectEvents_ClearSelectionFilter.md) | Clears out the filter list. |
| [ClearWindowSelectionFilter](../SelectEvents/SelectEvents_ClearWindowSelectionFilter.md) | Clears out the window selection filter list. |
| [RemoveFromSelectedEntities](../SelectEvents/SelectEvents_RemoveFromSelectedEntities.md) | Removes entities from the selected entities collection. |
| [ResetSelections](../SelectEvents/SelectEvents_ResetSelections.md) | Resets the set of selections being recorded by this object to an empty set. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SelectEvents/SelectEvents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Enabled](../SelectEvents/SelectEvents_Enabled.md) | Gets/Sets the flag indicating whether the selection is enabled. |
| [ExpressSelectionEnabled](../SelectEvents/SelectEvents_ExpressSelectionEnabled.md) | Gets/Sets the flag indicating whether express selection is enabled which controls the behavior of selection when an assembly is open in Express mode. If the assembly is not in Express mode this property has no effect. |
| [IgnoreProfileInnerLoops](../SelectEvents/SelectEvents_IgnoreProfileInnerLoops.md) | Gets and sets whether to ignore inner loops during 2d and 3d sketch profile selection. This property defaults to False. |
| [MouseMoveEnabled](../SelectEvents/SelectEvents_MouseMoveEnabled.md) | Gets/Sets the flag indicating whether a mouse move should fire an event (OnPreSelectMouseMove). Default is TRUE. |
| [Parent](../SelectEvents/SelectEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [PreSelectBurnThrough](../SelectEvents/SelectEvents_PreSelectBurnThrough.md) | Gets/Sets the flag indicating whether the preselected items will burn through. |
| [RestrictSelectionToOccurrence](../SelectEvents/SelectEvents_RestrictSelectionToOccurrence.md) | Read-write property that gets and sets the ComponentOccurrence to which the selection should be restricted. |
| [RestrictWindowSelectionToOccurrence](../SelectEvents/SelectEvents_RestrictWindowSelectionToOccurrence.md) | Read-write property that gets and sets the ComponentOccurrence the window selection should be restricted to. |
| [SelectedEntities](../SelectEvents/SelectEvents_SelectedEntities.md) | Gets an ObjectsEnumerator that presents all of the selected objects so far. |
| [SingleSelectEnabled](../SelectEvents/SelectEvents_SingleSelectEnabled.md) | Gets/Sets the flag indicating whether single select is enabled. |
| [Type](../SelectEvents/SelectEvents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [WindowSelectEnabled](../SelectEvents/SelectEvents_WindowSelectEnabled.md) | Gets/Sets the flag indicating whether window select is enabled. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnPreSelect](../SelectEvents/SelectEvents_OnPreSelect.md) | Fires signaling that a particular object has been indicated as a potential candidate for selection. |
| [OnPreSelectMouseMove](../SelectEvents/SelectEvents_OnPreSelectMouseMove.md) | Event that occurs while an object is in pre-select mode and the user is moving the mouse. This allows you to receive mouse input relative to the pre-selected object. |
| [OnSelect](../SelectEvents/SelectEvents_OnSelect.md) | Event that occurs when the user selects an entity. |
| [OnStopPreSelect](../SelectEvents/SelectEvents_OnStopPreSelect.md) | Event that occurs when the currently pre-selected entity stops being displayed in pre-selection highlight--happens usually when the user has moved his/her mouse away from the vicinity of the pre-selected entity. This way, the client programmer has the ability to display additional graphics on pre-select and with the OnStopPreSelect knows when to stop displaying this additional graphics. An example can be seen in the Sketch trim command. As you move the mouse over some sketch graphics, you see the preview of what the result will be if you select the object and when you move away this trimmed preview is taken away. |
| [OnUnSelect](../SelectEvents/SelectEvents_OnUnSelect.md) | Event that occurs when the user unselects an entity. This is done in the user interface by pressing the Shift button and selecting a previously selected entity. |

## Accessed From

[InteractionEvents.SelectEvents](../InteractionEvents/InteractionEvents_SelectEvents.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Basic Selection Using Interaction Events](../../sample-programs/InteractionEventsSink_Sample.md) | This sample demonstrates using the selection events to select a face. Selection is dependent on events and VB only supports events within a class module. |
| [Window Selection](../../sample-programs/SelectEventsObject_WindowSelectEnabled_Sample.md) | This sample demonstrates using the selection events to window-select multiple edges. Selection is dependent on events and VB only supports events within a class module. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |