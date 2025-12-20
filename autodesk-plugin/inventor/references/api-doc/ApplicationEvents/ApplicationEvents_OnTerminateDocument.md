# ApplicationEvents.OnTerminateDocument Event

Parent Object: [ApplicationEvents](../ApplicationEvents/ApplicationEvents.md)

## Description

The OnTerminateDocument event notifies a client when a document is being terminated. Termination of a document is a complete close of the document. A document terminate corresponds with a document initialize.

## Syntax

ApplicationEvents.**OnTerminateDocument**( ***DocumentObject*** As [Document](../Document/Document.md), ***FullDocumentName*** As String, ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | When the BeforeOrAfter argument is kBefore this returns the Document object that is being terminated. When BeforeOrAfter is kAfter this returns Nothing since the document is no longer available. |
| FullDocumentName | String | Output string that specifies the fully qualified name of the document being terminated. This is supplied both before and after. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Output EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the document is terminated. Notification is sent before and after the document is terminated. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Output NameValueMap object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |