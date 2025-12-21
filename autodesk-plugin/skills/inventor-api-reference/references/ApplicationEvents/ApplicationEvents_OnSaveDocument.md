# ApplicationEvents.OnSaveDocument Event

Parent Object: [ApplicationEvents](../ApplicationEvents/ApplicationEvents.md)

## Description

The OnSaveDocument notifies a client whenever a document is saved.

## Remarks

The notification is made when the standard Save and the Save Copy As commands are invoked. When assemblies are saved this can also cause the dependent documents to be saved and this event is also fired in those cases.

## Syntax

ApplicationEvents.**OnSaveDocument**( ***DocumentObject*** As [Document](../Document/Document.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | Input object that is being saved. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input indicating if the notification is being sent before the document is saved (kBefore), after a change is made (kAfter), or when a change has been aborted (kAbort). |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. Additional information is provided through this argument to help in understanding the context of the save. Either SaveCopyAsFileName or SaveFileName is provided depending on whether the end-user executed the Save or Save Copy As command. The TopLevelSaveFileName is always provided but in some cases will have an empty string as the value. Name = SaveCopyAsFileName, Value = The full filename of the new document being created. Name = SaveFileName, Value = The full filename of the document being saved. Name = TopLevelSaveFileName, Value = Different values are returned depending on the context of the save. When a document is saved in the context of another document (for example, a part is saved when the assembly it is in is saved) this will return the name of the top-level assembly. When the notification is made for a save copy as operation this value is the full filename of the original document that is being saved to a new name. When the notification is made for a standard save this value is the filename of the document being saved. When a document is saved for the first time, this value will be "" for the kBefore timing and the filename of the document in the kAfter timing. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. This event supports the ability to cancel the save. By setting this argument to kEventCanceled when the BeforeOrAfter argument is kBefore Inventor will abort the save. When the save is cancelled, this event is fired again but the BeforeOrAfter argument will have a value of kAbort. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |