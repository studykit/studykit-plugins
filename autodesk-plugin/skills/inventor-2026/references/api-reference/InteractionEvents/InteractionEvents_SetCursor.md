# InteractionEvents.SetCursor Method

Parent Object: [InteractionEvents](../InteractionEvents/InteractionEvents.md)

## Description

Sets the cursor for the command in which this interaction takes place.

## Syntax

InteractionEvents.**SetCursor**( ***CursorType*** As [CursorTypeEnum](../CursorTypeEnum.md), [***Cursor***] As Variant, [***CursorHotSpot***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CursorType | [CursorTypeEnum](../CursorTypeEnum.md) | Specify the CursorTypeEnum indicating the cursor type. |
| Cursor | Variant | Input the cursor.  When the CursorType is specified as kCursorTypeCustom, this is required to be set as String indicating a cursor file(.cur, .ani) name or IPictureDisp object(32x32 pixels). If the CursorType is specified as kCursorTypeWindows, this is required to be set as Long indicating the Windows cursor ID, below table shows the map between the Long value and Windows cursor ID:  | Long value | Windows Cursor Id | | --- | --- | | 0 | IDC\_ARROW | | 1 | IDC\_ARROW | | 2 | IDC\_CROSS | | 3 | IDC\_IBEAM | | 4 | IDC\_ARROW | | 5 | IDC\_SIZEALL | | 6 | IDC\_SIZENESW | | 7 | IDC\_SIZENS | | 8 | IDC\_SIZENWSE | | 9 | IDC\_SIZEWE | | 10 | IDC\_UPARROW | | 11 | IDC\_WAIT | | 12 | IDC\_NO | | 13 | IDC\_WAIT | | 14 | IDC\_HELP | | 15 | IDC\_SIZEALL |     This is an optional argument whose default value is null. |
| CursorHotSpot | Variant | Specify the CursorHotSpotEnum indicating the hotspot location relative to the cursor.   This is an optional argument whose default value is null. |

## Version

Introduced in version 9
