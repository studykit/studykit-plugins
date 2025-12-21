# MouseEvents Object

## Description

The MouseEvents object supports a set of events that can be received by clients who are interested in mouse input from the end-user.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MouseEvents/MouseEvents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [MouseMoveEnabled](../MouseEvents/MouseEvents_MouseMoveEnabled.md) | Gets/Sets the Boolean flag indicating whether a mouse move should fire an event (OnMouseMove). Default is FALSE. |
| [Parent](../MouseEvents/MouseEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [PointInferenceEnabled](../MouseEvents/MouseEvents_PointInferenceEnabled.md) | Gets/Sets the Boolean flag indicating that Inventor should turn its special point inferencing on. |
| [PointInferences](../MouseEvents/MouseEvents_PointInferences.md) | Gets the inferencing object. |
| [Type](../MouseEvents/MouseEvents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnMouseClick](../MouseEvents/MouseEvents_OnMouseClick.md) | Event that occurs when the user presses and then releases a mouse button. |
| [OnMouseDoubleClick](../MouseEvents/MouseEvents_OnMouseDoubleClick.md) | Event that occurs when the user presses and releases a mouse button and then presses and releases it again in quick succession. |
| [OnMouseDown](../MouseEvents/MouseEvents_OnMouseDown.md) | Event that occurs then the user presses a mouse button and begins to hold it down for a perceptible time. |
| [OnMouseLeave](../MouseEvents/MouseEvents_OnMouseLeave.md) | Event that occurs when the user moves the mouse out of a view. |
| [OnMouseMove](../MouseEvents/MouseEvents_OnMouseMove.md) | Event that occurs when the user moves the mouse. The position moved to is described by the arguments of this event. |
| [OnMouseUp](../MouseEvents/MouseEvents_OnMouseUp.md) | Event that occurs when the user transitions out of a MouseDown position, releasing the mouse button. |

## Accessed From

[InteractionEvents.MouseEvents](../InteractionEvents/InteractionEvents_MouseEvents.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [OnDrag Event - dragging a WorkPoint](../../sample-programs/UserInputEventsSink_OnDrag_Sample.md) | This sample demonstrates the use of the OnDrag event to drag fixed work points when no command is active. This sample only allows drags parallel to the X-Y plane. This sample is dependent on events and VB only supports events within a class module. |

## Version

Introduced in version 5
