# TriadEvents.OnSegmentSelectionChange Event

Parent Object: [TriadEvents](../TriadEvents/TriadEvents.md)

## Description

Event that occurs every time a segment of a triad is selected.

## Syntax

TriadEvents.**OnSegmentSelectionChange**( ***SelectedTriadSegment*** As [TriadSegmentEnum](../TriadSegmentEnum.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SelectedTriadSegment | [TriadSegmentEnum](../TriadSegmentEnum.md) | Returns a TriadSegmentEnum indicating the segment of the triad that was selected for this operation. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the triad segment selection is changed. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output  that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |