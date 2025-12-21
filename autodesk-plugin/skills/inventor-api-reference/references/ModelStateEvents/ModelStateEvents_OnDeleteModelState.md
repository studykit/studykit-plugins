# ModelStateEvents.OnDeleteModelState Event

Parent Object: [ModelStateEvents](../ModelStateEvents/ModelStateEvents.md)

## Description

Event that fires when a model state is deleted.

## Syntax

ModelStateEvents.**OnDeleteModelState**( ***DocumentObject*** As [Document](../Document/Document.md), ***ModelState*** As Object, ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | The Document object the deleted object is within. |
| ModelState | Object | The model state that is being deleted. When the value of the BeforeOrAfter argument is kBefore, the model state provided is the object before being deleted. When the value is kAfter, a model state is also provided but since the actual model state has been deleted calling any methods or properties on the object will fail. The only thing that is valid to do with the object at this time is to compare it's identity with a reference previously saved. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating when the event is being fired. Notification is sent before and after the object is deleted. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |