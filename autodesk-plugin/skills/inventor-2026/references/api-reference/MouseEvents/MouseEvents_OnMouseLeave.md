# MouseEvents.OnMouseLeave Event

Parent Object: [MouseEvents](../MouseEvents/MouseEvents.md)

## Description

Event that occurs when the user moves the mouse out of a view.

## Syntax

MouseEvents.**OnMouseLeave**( ***Button*** As [MouseButtonEnum](../MouseButtonEnum.md), ***ShiftKeys*** As [ShiftStateEnum](../ShiftStateEnum.md), ***View*** As [View](../View/View.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Button | [MouseButtonEnum](../MouseButtonEnum.md) | Returns an enumerated constant that identifies the button that was clicked to cause the event. The constants correspond to the left button (bit 0), right button (bit 1), and middle button (bit 2). These bits correspond to the values 1, 2, and 4, respectively. Only one of the bits is set, indicating the button that caused the event. |
| ShiftKeys | [ShiftStateEnum](../ShiftStateEnum.md) | Returns an enumerated constant that corresponds to the state of the SHIFT, CTRL, and ALT keys when the button specified in the button argument is clicked. The constants correspond to one or more of those three keys being down. Each of these keys corresponds to a bit: SHIFT key (bit 0), the CTRL key (bit 1), and the ALT key (bit 2). These bits correspond to the values 1, 2, and 4, respectively. Combinations of these are provided as conveniences in the enumerator. For example, if only the ALT key was down, the constant kShiftStateAlt would be returned corresponding to the integer 4. If CTRL and ALT were pressed, the constant kShiftStateCtrlAlt would be returned whose integer value would be 6. |
| View | [View](../View/View.md) | Returns the View object the mouse was moved out of. |

## Version

Introduced in version 5
