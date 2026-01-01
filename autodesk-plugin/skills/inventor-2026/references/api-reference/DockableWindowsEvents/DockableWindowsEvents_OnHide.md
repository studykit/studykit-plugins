# DockableWindowsEvents.OnHide Event

Parent Object: [DockableWindowsEvents](../DockableWindowsEvents/DockableWindowsEvents.md)

## Description

Fires whenever a dockable window is hidden (i.e. closed).

## Syntax

DockableWindowsEvents.**OnHide**( ***DockableWindow*** As [DockableWindow](../DockableWindow/DockableWindow.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DockableWindow | [DockableWindow](../DockableWindow/DockableWindow.md) | Input DockableWindow object that specifies the window being hidden. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the window is hidden. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. This argument is currently ignored. |

## Version

Introduced in version 2012
