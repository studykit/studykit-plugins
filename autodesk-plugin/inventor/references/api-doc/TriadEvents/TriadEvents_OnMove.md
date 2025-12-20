# TriadEvents.OnMove Event

Parent Object: [TriadEvents](../TriadEvents/TriadEvents.md)

## Description

Event that occurs when the triad moves as a result of a drag, a reposition or user entering values for translation or rotation. A 'reposition' move is always immediately followed by the OnEndMove event.

## Syntax

TriadEvents.**OnMove**( ***SelectedTriadSegment*** As [TriadSegmentEnum](../TriadSegmentEnum.md), ***ShiftKeys*** As [ShiftStateEnum](../ShiftStateEnum.md), ***CoordinateSystem*** As [Matrix](../Matrix/Matrix.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SelectedTriadSegment | [TriadSegmentEnum](../TriadSegmentEnum.md) | Returns a TriadSegmentEnum indicating the segment of the triad that was selected for this move operation. |
| ShiftKeys | [ShiftStateEnum](../ShiftStateEnum.md) | Returns an enumerated constant that corresponds to the state of the SHIFT, CTRL, and ALT keys when the drag operation occurs. The constants correspond to one or more of those three keys being down. Each of these keys corresponds to a bit: SHIFT key (bit 0), the CTRL key (bit 1), and the ALT key (bit 2). These bits correspond to the values 1, 2, and 4, respectively. Combinations of these are provided as conveniences in the enumerator. For example, if only the ALT key was down, the constant kShiftStateAlt would be returned corresponding to the integer 4. If CTRL and ALT were pressed, the constant kShiftStateCtrlAlt would be returned whose integer value would be 6. |
| CoordinateSystem | [Matrix](../Matrix/Matrix.md) | Returns a Matrix object indicating the triad's current position in model space. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Returns the NameValueMap object with information regarding the context in which the move occurred. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |