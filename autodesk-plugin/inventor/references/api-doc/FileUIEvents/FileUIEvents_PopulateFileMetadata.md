# FileUIEvents.PopulateFileMetadata Method

Parent Object: [FileUIEvents](../FileUIEvents/FileUIEvents.md)

## Description

Method that fires the OnPopulateFileMetadata event with the input arguments and returns the values specified in the event. This method should be called just before showing the file naming dialog to the user.

## Syntax

FileUIEvents.**PopulateFileMetadata**( ***FileMetadataObjects*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***Formulae*** As String, ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FileMetadataObjects | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectsEnumerator that contains FileMetadata objects with the proposed file names and properties. The input enumerator contains one FileMetadata object for every file being generated. The properties of the FileMetadata objects can be set to the desired values. |
| Formulae | String | Input String that specifies XML-based formulae for generating file name, display name and file properties. This can be a null string. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input/output NameValueMap object that can be used to determine the context of why the event fired. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Input HandlingCodeEnum that indicates how you are handling the event:  \* kEventNotHandled: Inventor continues with its standard behavior and displays the file-naming dialog to the end-user.  \* kEventHandled: Indicates that the client has specified file names and/or properties for the files and Inventor should use these to display in its dialog to the user.  \* kEventCanceled: This code is return as a signal that an unexpected failure has occurred. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |