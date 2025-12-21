# UserInputEvents.OnActivateCommand Event

Parent Object: [UserInputEvents](../UserInputEvents/UserInputEvents.md)

## Description

The OnActivateCommand event notifies the client when a command has been invoked.

## Syntax

UserInputEvents.**OnActivateCommand**( ***CommandName*** As String, ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CommandName | String | The internal name of the command. This is the same name as the internal name of the ControlDefinition object associated with this command. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. No context information is provided for this event. |

## Version

Introduced in version 10
