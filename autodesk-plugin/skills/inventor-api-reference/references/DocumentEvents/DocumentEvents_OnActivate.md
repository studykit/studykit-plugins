# DocumentEvents.OnActivate Event

Parent Object: [DocumentEvents](../DocumentEvents/DocumentEvents.md)

## Description

The OnActivate event notifies a client when the document is activated.

## Remarks

When a document is activated it is the top-level document currently available for edit in the user-interface. In-place activating a document within the context of an assembly does not cause it to be the active document. In this case the document being in-place activated becomes the active edit object, but not the active document. The top-level assembly that the edit is taking place within remains the active document.

## Syntax

DocumentEvents.**OnActivate**( ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input indicating if the event is being fired before (kBefore) or after (kAfter). Notification is sent before and after the document is activated. BeforeOrAfter is kAbort if the native processing was ABORTED. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. This argument is ignored for this event. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |