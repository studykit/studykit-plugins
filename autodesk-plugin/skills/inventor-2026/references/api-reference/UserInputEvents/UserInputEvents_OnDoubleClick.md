# UserInputEvents.OnDoubleClick Event

Parent Object: [UserInputEvents](../UserInputEvents/UserInputEvents.md)

## Description

Event that is sent when the user double-clicks in the window.

## Syntax

UserInputEvents.**OnDoubleClick**( ***SelectedEntities*** As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md), ***SelectionDevice*** As [SelectionDeviceEnum](../SelectionDeviceEnum.md), ***Button*** As [MouseButtonEnum](../MouseButtonEnum.md), ***ShiftKeys*** As [ShiftStateEnum](../ShiftStateEnum.md), ***ModelPosition*** As [Point](../Point/Point.md), ***ViewPosition*** As [Point2d](../Point2d/Point2d.md), ***View*** As [View](../View/View.md), ***AdditionalInfo*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SelectedEntities | [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md) | Enumerator of entities selected by double click. Count of SelectedEntities will be 0 if user double-clicks in space. If any of the selected objects are not supported by the API, no notification is sent. |
| SelectionDevice | [SelectionDeviceEnum](../SelectionDeviceEnum.md) |  |
| Button | [MouseButtonEnum](../MouseButtonEnum.md) | Returns an enumerated constant that identifies the button that was clicked to cause the event. The constants correspond to the left button (bit 0), right button (bit 1), and middle button (bit 2). These bits correspond to the values 1, 2, and 4, respectively. Only one of the bits is set, indicating the button that caused the event. |
| ShiftKeys | [ShiftStateEnum](../ShiftStateEnum.md) | Returns an enumerated constant that corresponds to the state of the SHIFT, CTRL, and ALT keys when the button specified in the button argument is clicked. The constants correspond to one or more of those three keys being down. Each of these keys corresponds to a bit: SHIFT key (bit 0), the CTRL key (bit 1), and the ALT key (bit 2). These bits correspond to the values 1, 2, and 4, respectively. Combinations of these are provided as conveniences in the enumerator. For example, if only the ALT key was down, the constant kShiftStateAlt would be returned corresponding to the integer 4. If CTRL and ALT were pressed, the constant kShiftStateCtrlAlt would be returned whose integer value would be 6. |
| ModelPosition | [Point](../Point/Point.md) | Returns the coordinates that specify the current location of the mouse pointer in model space and are returned in centimeters. Model Returns Nothing if user double-clicks in browser. |
| ViewPosition | [Point2d](../Point2d/Point2d.md) | Returns the coordinates that specify the current location of the mouse pointer in window space and are returned in pixels. Model Returns Nothing if user double-clicks in browser. |
| View | [View](../View/View.md) | Returns the View object where the mouse was pressed. |
| AdditionalInfo | [NameValueMap](../NameValueMap/NameValueMap.md) |  |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Returning kEventCanceled or kEventHandled as the HandlingCode cancels regular Inventor behavior. |

## Version

Introduced in version 2009
