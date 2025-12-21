# FileDialogEvents.OnOptionsReset Event

Parent Object: [FileDialogEvents](../FileDialogEvents/FileDialogEvents.md)

## Description

Fires when the action to reset options on the file dialog occurs, e.g. file filter type changes, etc.

## Syntax

FileDialogEvents.**OnOptionsReset**( ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Output NameValueMap object that can be used to determine the context of why the event fired. Information describing the change is passed through the context argument, as described below: Name = "FileTypeChanged", Value = Boolean value that indicates whether the file type was changed or not. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 2026
