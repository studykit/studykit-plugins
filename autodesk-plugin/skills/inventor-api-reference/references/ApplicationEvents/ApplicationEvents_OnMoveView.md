# ApplicationEvents.OnMoveView Event

Parent Object: [ApplicationEvents](../ApplicationEvents/ApplicationEvents.md)

## Description

Fires after view window is moved.

## Syntax

ApplicationEvents.**OnMoveView**( ***ViewObject*** As [View](../View/View.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ViewObject | [View](../View/View.md) | The view that has been moved. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the view is moved. This notification is currently only provided after the view has been moved. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 2017
