# CommandManager.CreateInteractionEvents Method

Parent Object: [CommandManager](../CommandManager/CommandManager.md)

## Description

Method that creates and returns a new InteractionEvents object. The InteractionEvents object is created for document that is currently active.

## Syntax

CommandManager.**CreateInteractionEvents**() As [InteractionEvents](../InteractionEvents/InteractionEvents.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Basic Selection Using Interaction Events](../../sample-programs/InteractionEventsSink_Sample.md) | This sample demonstrates using the selection events to select a face. Selection is dependent on events and VB only supports events within a class module. |
| [InteractionGraphics](../../sample-programs/InteractionGraphics_Sample.md) | The sample creates overlay graphics. |
| [Using measure events](../../sample-programs/MeasureEventsSink_OnMeasure_Sample.md) | This sample demonstrates using the measure events to measure distance and angle. Interactive measure is dependent on events and VB only supports events within a class module. To use the sample copy the InteractiveMeasureDistance and InteractiveMeasureAngle subs into a code module. Create a new class module called clsMeasure and copy all of the rest of the code into it. |
| [Window Selection](../../sample-programs/SelectEventsObject_WindowSelectEnabled_Sample.md) | This sample demonstrates using the selection events to window-select multiple edges. Selection is dependent on events and VB only supports events within a class module. |
| [OnDrag Event - dragging a WorkPoint](../../sample-programs/UserInputEventsSink_OnDrag_Sample.md) | This sample demonstrates the use of the OnDrag event to drag fixed work points when no command is active. This sample only allows drags parallel to the X-Y plane. This sample is dependent on events and VB only supports events within a class module. |

## Version

Introduced in version 5
