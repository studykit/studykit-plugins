# ManipulatorEvents.OnEndDrag Event

Parent Object: [ManipulatorEvents](../ManipulatorEvents/ManipulatorEvents.md)

## Description

Fires when the user ends an intermediate drag of the manipulator.

## Syntax

ManipulatorEvents.**OnEndDrag**( ***SelectedManipulatorElement*** As [ManipulatorElementEnum](../ManipulatorElementEnum.md), ***DragValue*** As Variant, ***ManipulatorTransform*** As [Matrix](../Matrix/Matrix.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SelectedManipulatorElement | [ManipulatorElementEnum](../ManipulatorElementEnum.md) | Returns a ManipulatorElementEnum indicating the element of the manipulator that was selected for this drag operation. |
| DragValue | Variant | Returns the value of the translation, rotation or scaling in the drag. This returns Vector for translation, numeric value in radians for rotation and numeric value for scaling. |
| ManipulatorTransform | [Matrix](../Matrix/Matrix.md) | Input the Matrix object that indicates the transformation of the Manipulator against its original position and orientation. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the manipulator element move. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 2017
