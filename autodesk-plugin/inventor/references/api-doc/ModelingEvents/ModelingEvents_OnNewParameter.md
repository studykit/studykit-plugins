# ModelingEvents.OnNewParameter Event

Parent Object: [ModelingEvents](../ModelingEvents/ModelingEvents.md)

## Description

The OnNewParameter event notifies the client when a new parameter is created.

## Remarks

New parameters can be created explicitly by the end-user using the Add button on the Parameters dialog and they are also created implicitly as the result of placing dimension constraints and constructing features. This event provides notification is both cases.

## Syntax

ModelingEvents.**OnNewParameter**( ***DocumentObject*** As [Document](../Document/Document.md), ***Parameter*** As [Parameter](../Parameter/Parameter.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | The Document object the parameter is contained within. |
| Parameter | [Parameter](../Parameter/Parameter.md) | The Parameter object that has just been created. When the BeforeOrAfter argument is kBefore, the value of this argument is Nothing since the Parameter does not yet exist. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating when the event is being fired. Notification is sent before and after the parameter has been created. Generally, you should only perform query operations in Inventor when the value of this argument is kBefore. Inventor is not in a state to correctly handle edit operations after that point. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |