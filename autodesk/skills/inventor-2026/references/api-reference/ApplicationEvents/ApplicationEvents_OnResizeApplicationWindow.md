# ApplicationEvents.OnResizeApplicationWindow Event

Parent Object: [ApplicationEvents](../ApplicationEvents/ApplicationEvents.md)

## Description

Fires after application main window is resized, or layout is recalculated.

## Syntax

ApplicationEvents.**OnResizeApplicationWindow**( ***ApplicationObject*** As [Application](../Application/Application.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ApplicationObject | [Application](../Application/Application.md) | The Application object which window has been resized. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the application window is resized. This notification is currently only provided after the application window has been resized. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired.   Name=”WindowState”, Value= WindowsSizeEnum. This indicates the current application window state. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 2017
