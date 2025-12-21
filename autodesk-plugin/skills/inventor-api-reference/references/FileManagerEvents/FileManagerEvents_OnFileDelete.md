# FileManagerEvents.OnFileDelete Event

Parent Object: [FileManagerEvents](../FileManagerEvents/FileManagerEvents.md)

## Description

The OnFileDelete event notifies a client whenever a file is deleted using the DeleteFile method of the FileManager object.

## Syntax

FileManagerEvents.**OnFileDelete**( ***FullFileName*** As String, ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | The full filename of the file being deleted. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. Additional information is provided through this argument to help in understanding the context of the notification. Name = "FileManagementOption". Value = A value from the FileManagementEnum list. This can represent multiple values that have been combined together so you need to use bitwise operations to check for a specific option. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |