# ManipulatorEvents.OnStartDrag Event

Parent Object: [ManipulatorEvents](../ManipulatorEvents/ManipulatorEvents.md)

## Description

Fires when a manipulator element is selected.

## Syntax

ManipulatorEvents.**OnStartDrag**( ***SelectedManipulatorElement*** As [ManipulatorElementEnum](../ManipulatorElementEnum.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SelectedManipulatorElement | [ManipulatorElementEnum](../ManipulatorElementEnum.md) | Returns a ManipulatorElementEnum indicating the element of the manipulator that was selected for this drag operation. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the manipulator element move. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. Name=”UserDrag”,Value=Boolean. This indicates whether this event is fired because of user drags manipulator, this returns False if this is fired because of calling ApplyDrag method. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 2017
