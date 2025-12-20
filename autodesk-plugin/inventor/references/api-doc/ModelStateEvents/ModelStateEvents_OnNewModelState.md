# ModelStateEvents.OnNewModelState Event

Parent Object: [ModelStateEvents](../ModelStateEvents/ModelStateEvents.md)

## Description

Event that fires when a model state is created.

## Syntax

ModelStateEvents.**OnNewModelState**( ***DocumentObject*** As [Document](../Document/Document.md), ***ModelState*** As [ModelState](../ModelState/ModelState.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | The Document object the model state is being created within. |
| ModelState | [ModelState](../ModelState/ModelState.md) | The new ModelState object that has just been created. When the BeforeOrAfter argument is kBefore, this argument is Nothing since the model state has not yet been created. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating when the event is being fired. Notification is sent before and after the object is created. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |