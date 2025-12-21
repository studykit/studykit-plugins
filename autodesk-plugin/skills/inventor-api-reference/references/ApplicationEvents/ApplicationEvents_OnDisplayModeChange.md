# ApplicationEvents.OnDisplayModeChange Event

Parent Object: [ApplicationEvents](../ApplicationEvents/ApplicationEvents.md)

## Description

The OnDisplayModeChange event notifies a client when the display mode of a view has changed.

## Remarks

The display mode defines whether the view is displayed as wireframe, shaded with hidden edges, or shaded with no hidden edges shown. The current display mode of the view can be determined by using the DisplayMode property of the View object returned by the ViewObject argument.

## Syntax

ApplicationEvents.**OnDisplayModeChange**( ***ViewObject*** As [View](../View/View.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ViewObject | [View](../View/View.md) | The View object whose display mode is being changed. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the view mode is changed. Notification is sent before and after the display mode is changed. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. The value of this argument is currently ignored for this event. This argument is ignored for this event. |

## Version

Introduced in version 9
