# ApplicationEvents.OnInitializeDocument Event

Parent Object: [ApplicationEvents](../ApplicationEvents/ApplicationEvents.md)

## Description

Event that is fired whenever a document is initialized. At the time this event fires, the document is not open yet. Calling methods or properties on the document will force it to open.

## Remarks

The OnInitializeDocument event notifies a client when a document is being initialized. Initialization of a document is essentially a low-level open. A portion of the document is opened to determine other related files but the majority of the data is not opened and loaded. For example, when you open a drawing, the referenced documents are initialized but are not fully loaded. If you perform an action within the drawing that requires access to the data within any of the referenced documents then they are automatically fully opened at that time. API calls on a document that is only initialized will also cause the document to be fully opened. When a document is opened it is always initialized, but a document can be initialized without being opened, if the additional data in the document is not needed.

## Syntax

ApplicationEvents.**OnInitializeDocument**( ***DocumentObject*** As [Document](../Document/Document.md), ***FullDocumentName*** As String, ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | The Document object that is being initialized. |
| FullDocumentName | String | Output string that specifies the fully qualified name of the document being initialized. This is supplied both before and after. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Output EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the document is initialized. Notification is sent before and after the document is initialized. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Output NameValueMap object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. This argument is ignored for this event. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |