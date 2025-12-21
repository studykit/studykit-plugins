# FileManagerEvents.OnFileCopy Event

Parent Object: [FileManagerEvents](../FileManagerEvents/FileManagerEvents.md)

## Description

Event that fires whenever a file is moved or copied using the MoveFile or CopyFile methods of the FileManager object.

## Syntax

FileManagerEvents.**OnFileCopy**( ***SourceFullFileName*** As String, ***DestinationFullFileName*** As String, ***Copy*** As Boolean, ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SourceFullFileName | String | The full file name of the file to copy/move. |
| DestinationFullFileName | String | The full file name of the destination to copy/move to. |
| Copy | Boolean | Indicates whether this is a 'copy' (True) or a 'move' (False). |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | This event supports a veto (HandlingCode = kEventCanceled) |

## Version

Introduced in version 2009
