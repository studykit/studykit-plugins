# KeyboardEvents Object

## Description

The KeyboardEvents object supports a set of events that can be received by the client when a key on the keyboard is pressed while the InteractionEvents object has been started AND the InteractionDisabled flag is set to False.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../KeyboardEvents/KeyboardEvents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../KeyboardEvents/KeyboardEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../KeyboardEvents/KeyboardEvents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnKeyDown](../KeyboardEvents/KeyboardEvents_OnKeyDown.md) | Event that occurs when the user presses a button on the keyboard. Only the keys specified in the enumerator are handled through this event. The input signifies the hardware key that was actually depressed. |
| [OnKeyPress](../KeyboardEvents/KeyboardEvents_OnKeyPress.md) | Event that occurs when the user presses and releases an ANSI key on the keyboard. The ANSI value of the key pressed is returned. |
| [OnKeyUp](../KeyboardEvents/KeyboardEvents_OnKeyUp.md) | Event that occurs when the user releases a button on the keyboard . Only the keys specified in the enumerator are handled through this event. The input signifies the hardware key that was actually depressed. |

## Accessed From

[InteractionEvents.KeyboardEvents](../InteractionEvents/InteractionEvents_KeyboardEvents.md)

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |