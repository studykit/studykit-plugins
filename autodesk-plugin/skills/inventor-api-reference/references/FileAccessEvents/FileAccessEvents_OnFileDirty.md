# FileAccessEvents.OnFileDirty Event

Parent Object: [FileAccessEvents](../FileAccessEvents/FileAccessEvents.md)

## Description

The OnFileDirty event notifies a client when a document is about to become to dirty.

## Remarks

A document becomes dirty when a change is made to a clean document. A clean document is defined as a document that has not changed since it was last saved. Examples of clean documents are documents that have just been opened and documents that have just been saved. In both cases, a save operation is not needed because the file on disk is the same as the open document. Any change to the open document causes it to be different than the version on disk. When the document changes state of going from clean to dirty this notification is sent. Any subsequent changes to the document do not result in the OnFileDirty notification being sent because the document is already dirty. If the document is saved it will become clean, (the in-memory version of the document matches the version on disk), and the next change will again cause the OnFileDirty event notification to be made. Some of the actions that cause a document to become dirty can be controlled through the Save tab of the Application Options dialog and will impact when this notification is sent.

## Syntax

FileAccessEvents.**OnFileDirty**( ***RelativeFileName*** As String, ***LibraryName*** As String, ***CustomLogicalName***() As Byte, ***FullFileName*** As String, ***DocumentObject*** As [Document](../Document/Document.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| RelativeFileName | String | The relative filename of the document. This is typically just the filename but may also include relative path information. |
| LibraryName | String | If the document is a library part, this argument provides the name of the library as defined in the active project. If it is not a library part this will be an empty string. |
| CustomLogicalName | Byte | An array of Bytes that is used by data management systems as a way to associated additional information with a file reference. In the case where a custom logical name was assigned to a reference and the associated document, this argument will return that value. |
| FullFileName | String | The full filename of the document. |
| DocumentObject | [Document](../Document/Document.md) | Input object being dirtied. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating when the event is being fired. This notification is currently only provided before the document is dirtied so this is always kBefore. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. Additional information is provided through this argument to help in understanding the context of the notification.  Name = "AffectedFiles". Value = An array of Strings that contains a list of full filenames of the files being dirtied. Typically this will contain a single filename, but in the case of referenced files, changing one document can also cause others to become dirty. For example, editing a part in the context of the assembly can cause other parts to reposition within other assemblies and in the case of adaptivity can cause parts to update. Each of these documents becomes dirty as a result of editing the single part. This list returns the filenames of the files affected. An OnFileDirty event notification is also made for each document as it is dirtied.  Name = "ReasonsForChange". Value = A value from the CommandTypesEnum list, which represents the different categories of changes that can be made. Typically this will be a single value from the list but it can represent multiple values that have been combined together so you need to use bitwise operations to check for a specific change.  Name = "Reason". Value = Returns "Update" or "FilesOpened" indicating the dirty reason.  Name = "DirtyByRecompute". Value = A Boolean value indicates if the dirty is caused by recompute only. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. This event supports the ability to cancel the dirty by aborting the actions that caused the change. By setting this argument to kEventCanceled Inventor will abort the change. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |