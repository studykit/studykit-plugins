# FileDialogEvents.OnOptions Event

Parent Object: [FileDialogEvents](../FileDialogEvents/FileDialogEvents.md)

## Description

Event that fires when the user clicks the Options button on the file dialog. This event can be used to put up customized option pages.

## Syntax

FileDialogEvents.**OnOptions**( ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Output NameValueMap object that can be used to determine the context of why the event fired. This argument is currently empty. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. |

## Version

Introduced in version 2008
