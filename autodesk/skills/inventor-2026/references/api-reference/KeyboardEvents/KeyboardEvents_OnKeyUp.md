# KeyboardEvents.OnKeyUp Event

Parent Object: [KeyboardEvents](../KeyboardEvents/KeyboardEvents.md)

## Description

Event that occurs when the user releases a button on the keyboard . Only the keys specified in the enumerator are handled through this event. The input signifies the hardware key that was actually depressed.

## Syntax

KeyboardEvents.**OnKeyUp**( ***Key*** As Long, ***ShiftKeys*** As [ShiftStateEnum](../ShiftStateEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Key | Long | Returns a key code, such as kKeyF1 (the F1 key) or kKeyHome (the HOME key). The key codes are defined in the constant list KeyCodeEnum. |
| ShiftKeys | [ShiftStateEnum](../ShiftStateEnum.md) | Returns an enumerated constant that corresponds to the state of the SHIFT, CTRL, and ALT keys when the button specified in the button argument is clicked. The constants correspond to one or more of those three keys being down. Each of these keys corresponds to a bit: SHIFT key (bit 0), the CTRL key (bit 1), and the ALT key (bit 2). These bits correspond to the values 1, 2, and 4, respectively. Combinations of these are provided as conveniences in the enumerator. For example, if only the ALT key was down, the constant kShiftStateAlt would be returned corresponding to the integer 4. If CTRL and ALT were pressed, the constant kShiftStateCtrlAlt would be returned whose integer value would be 6. |

## Version

Introduced in version 5
