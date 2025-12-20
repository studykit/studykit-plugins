# ManipulatorEvents.ApplyDrag Method

Parent Object: [ManipulatorEvents](../ManipulatorEvents/ManipulatorEvents.md)

## Description

Drives manipulator to move as if it is dragged by end user.

## Syntax

ManipulatorEvents.**ApplyDrag**( ***ManipulatorElement*** As [ManipulatorElementEnum](../ManipulatorElementEnum.md), ***DragValue*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ManipulatorElement | [ManipulatorElementEnum](../ManipulatorElementEnum.md) | The ManipulatorElementEnum that indicates the direction to drag. |
| DragValue | Variant | Input Variant to specify the translation, rotation or scaling value for the drag . For scaling this can be numeric value, for translation this can be Vector and for rotation this can be numeric value or String. If a numeric value is provided for rotation it is in radians, and if a String is provided the units can be specified as part of the string or it will default to current angle units of the document. |

## Version

Introduced in version 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |