# UserInputEvents.OnTerminateCommand Event

Parent Object: [UserInputEvents](../UserInputEvents/UserInputEvents.md)

## Description

The OnTerminateCommand event notifies the client when a command has been terminated.

## Remarks

There are several things that cause a command to be terminated. When a command finishes it will terminate. For example when you execute the Extrude command, after the extrusion has finished the command terminates. Starting another command while one command is active will cause the active command to terminate. An exception to this is the viewing commands. They just temporarily suspend the active command rather than terminate it. Pressing the escape key will terminate the current command.

## Syntax

UserInputEvents.**OnTerminateCommand**( ***CommandName*** As String, ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CommandName | String | The internal name of the command. This is the same name as the internal name of the ControlDefinition object associated with this command. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. No context information is provided for this event. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |