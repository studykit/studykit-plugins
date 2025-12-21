# PresentationEvents.OnDelete Event

Parent Object: [PresentationEvents](../PresentationEvents/PresentationEvents.md)

## Description

Event that fires just before and after an entity is deleted.

## Syntax

PresentationEvents.**OnDelete**( ***DocumentObject*** As [PresentationDocument](../PresentationDocument/PresentationDocument.md), ***PublicationObj*** As [Publication](Publication.md), ***pEntity*** As Object, ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [PresentationDocument](../PresentationDocument/PresentationDocument.md) | Input PresentationDocument object that indicates the document in which the change occurred. |
| PublicationObj | [Publication](Publication.md) | The Publication object in the document. |
| pEntity | Object | The entity that was just deleted. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the entity is deleted. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |