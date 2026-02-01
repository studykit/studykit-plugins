# FileUIEvents.OnFileOpenFromMRU Event

Parent Object: [FileUIEvents](../FileUIEvents/FileUIEvents.md)

## Description

Fires when a file is selected from the MRU list to open.

## Syntax

FileUIEvents.**OnFileOpenFromMRU**( ***FullFileName*** As String, ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | The full filename of the file to open. This must be an existing valid file and the HandlingCode must be set to kEventHandled in order to override the standard open behavior. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. No context information is provided for this event. See Remarks for valid NameValueMap values. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. Can supply any of the following three values:  * kEventNotHandled: Inventor continues with its standard behavior and displays the "Open" dialog to allow the end user to select a file. * kEventHandled: Indicates that the client is handling getting the filename. Requires that the client also set the FullFileName argument. * kEventCanceled: Cancels the operation. |

## Version

Introduced in version 2009
