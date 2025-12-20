# MouseEvents.OnMouseUp Event

Parent Object: [MouseEvents](../MouseEvents/MouseEvents.md)

## Description

Event that occurs when the user transitions out of a MouseDown position, releasing the mouse button.

## Syntax

MouseEvents.**OnMouseUp**( ***Button*** As [MouseButtonEnum](../MouseButtonEnum.md), ***ShiftKeys*** As [ShiftStateEnum](../ShiftStateEnum.md), ***ModelPosition*** As [Point](../Point/Point.md), ***ViewPosition*** As [Point2d](../Point2d/Point2d.md), ***View*** As [View](../View/View.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Button | [MouseButtonEnum](../MouseButtonEnum.md) | Returns an enumerated constant that identifies the button that was clicked to cause the event. The constants correspond to the left button (bit 0), right button (bit 1), and middle button (bit 2). These bits correspond to the values 1, 2, and 4, respectively. Only one of the bits is set, indicating the button that caused the event. |
| ShiftKeys | [ShiftStateEnum](../ShiftStateEnum.md) | Returns an enumerated constant that corresponds to the state of the SHIFT, CTRL, and ALT keys when the button specified in the button argument is clicked. The constants correspond to one or more of those three keys being down. Each of these keys corresponds to a bit: SHIFT key (bit 0), the CTRL key (bit 1), and the ALT key (bit 2). These bits correspond to the values 1, 2, and 4, respectively. Combinations of these are provided as conveniences in the enumerator. For example, if only the ALT key was down, the constant kShiftStateAlt would be returned corresponding to the integer 4. If CTRL and ALT were pressed, the constant kShiftStateCtrlAlt would be returned whose integer value would be 6. |
| ModelPosition | [Point](../Point/Point.md) | Returns the coordinates that specify the current location of the mouse pointer in model space and are returned in centimeters. |
| ViewPosition | [Point2d](../Point2d/Point2d.md) | Returns the coordinates that specify the current location of the mouse pointer in window space and are returned in pixels. |
| View | [View](../View/View.md) | Returns the View object where the mouse was pressed. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |