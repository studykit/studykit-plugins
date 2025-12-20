# ApplicationEvents.OnNewDocument Event

Parent Object: [ApplicationEvents](../ApplicationEvents/ApplicationEvents.md)

## Description

Event that is fired whenever a new document is created.

## Syntax

ApplicationEvents.**OnNewDocument**( ***DocumentObject*** As [Document](../Document/Document.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | Input object that was just created. When the BeforeOrAfter argument is kBefore this argument will be Nothing because the document does not yet exist. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input indicating if the event is being fired before (kBefore) or after (kAfter) the document is created. Notification is sent before and after the document is created. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. This event provides additional information through the Context argument as described below: Name = "TemplateFilename", Value = The full filename of the file used as the template when creating the new document. Name = "NewFileName", Value = The full filename of the new file. In most cases this value will be an empty string because the filename of a new document is not specified until it is saved for the first time. The exception to this is when the Create Component command is used in an Assembly to create a new part. In this case the filename is specified as part of the command. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |