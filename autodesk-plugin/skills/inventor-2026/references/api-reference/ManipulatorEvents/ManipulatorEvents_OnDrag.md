# ManipulatorEvents.OnDrag Event

Parent Object: [ManipulatorEvents](../ManipulatorEvents/ManipulatorEvents.md)

## Description

Fires fires when the manipulator moves as a result of a drag, reposition or user entering values for translation, rotation and scaling.

## Syntax

ManipulatorEvents.**OnDrag**( ***SelectedManipulatorElement*** As [ManipulatorElementEnum](../ManipulatorElementEnum.md), ***DragValue*** As Variant, ***ManipulatorTransform*** As [Matrix](../Matrix/Matrix.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SelectedManipulatorElement | [ManipulatorElementEnum](../ManipulatorElementEnum.md) | Returns a ManipulatorElementEnum indicating the element of the manipulator that was selected for this drag operation. |
| DragValue | Variant | Returns the value of the translation, rotation or scaling in the drag. This returns Vector for translation, numeric value in radians for rotation and numeric value for scaling. |
| ManipulatorTransform | [Matrix](../Matrix/Matrix.md) | Input the Matrix object that indicates the transformation of the Manipulator against its original position and orientation. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 2017
