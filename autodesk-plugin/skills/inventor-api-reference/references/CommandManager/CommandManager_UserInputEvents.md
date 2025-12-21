# CommandManager.UserInputEvents Property

Parent Object: [CommandManager](../CommandManager/CommandManager.md)

## Description

Property that returns the object that fires events on all user input (commands, keyboard, mouse, etc.).

## Syntax

CommandManager.**UserInputEvents**() As [UserInputEvents](../UserInputEvents/UserInputEvents.md)

## Property Value

This is a read only property whose value is a [UserInputEvents](../UserInputEvents/UserInputEvents.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Cancel a double click](../../sample-programs/UserInputEventsSink_OnDoubleClick_Sample.md) | Demonstrates how to receive (and in this case, cancel) a double click from a user. |
| [OnDrag Event - dragging a WorkPoint](../../sample-programs/UserInputEventsSink_OnDrag_Sample.md) | This sample demonstrates the use of the OnDrag event to drag fixed work points when no command is active. This sample only allows drags parallel to the X-Y plane. This sample is dependent on events and VB only supports events within a class module. |

## Version

Introduced in version 6
