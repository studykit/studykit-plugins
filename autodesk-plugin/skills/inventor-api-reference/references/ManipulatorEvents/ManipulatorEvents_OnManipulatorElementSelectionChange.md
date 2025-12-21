# ManipulatorEvents.OnManipulatorElementSelectionChange Event

Parent Object: [ManipulatorEvents](../ManipulatorEvents/ManipulatorEvents.md)

## Description

Fires when a manipulator element is selected.

## Syntax

ManipulatorEvents.**OnManipulatorElementSelectionChange**( ***SelectedManipulatorElement*** As [ManipulatorElementEnum](../ManipulatorElementEnum.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SelectedManipulatorElement | [ManipulatorElementEnum](../ManipulatorElementEnum.md) | The ManipulatorElementEnum that indicates the selected manipulator element. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the manipulator element selection is changed. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 2017
