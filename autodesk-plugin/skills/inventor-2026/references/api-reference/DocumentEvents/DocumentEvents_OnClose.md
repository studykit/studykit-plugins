# DocumentEvents.OnClose Event

Parent Object: [DocumentEvents](../DocumentEvents/DocumentEvents.md)

## Description

The Onclose event notifies a client when the document is closed.

## Syntax

DocumentEvents.**OnClose**( ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input indicating when the event is being fired. Notification is sent before and after the document is closed. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. This event provides additional information through the Context argument as described below: Name = "HealthStatusEnum", Value = The health status of the document. If this value is anything other than kUpToDateHealth you know the Document object returned is not in a state where you can use most of its methods or properties. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 4
