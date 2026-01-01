# TriadEvents.OnMoveTriadOnlyToggle2 Event

Parent Object: [TriadEvents](../TriadEvents/TriadEvents.md)

## Description

Fires when the 'Move Triad Only' option is toggled.

## Syntax

TriadEvents.**OnMoveTriadOnlyToggle2**( ***MoveTriadOnly*** As Boolean, ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| MoveTriadOnly | Boolean | Indicates whether to move the triad independent of the object that the triad is being used to move. A value of True indicates that the triad move should not move the object. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the MoveTriadOnly is changed. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 2020
