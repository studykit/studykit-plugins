# SelectEvents.OnStopPreSelect Event

Parent Object: [SelectEvents](../SelectEvents/SelectEvents.md)

## Description

Event that occurs when the currently pre-selected entity stops being displayed in pre-selection highlight--happens usually when the user has moved his/her mouse away from the vicinity of the pre-selected entity. This way, the client programmer has the ability to display additional graphics on pre-select and with the OnStopPreSelect knows when to stop displaying this additional graphics. An example can be seen in the Sketch trim command. As you move the mouse over some sketch graphics, you see the preview of what the result will be if you select the object and when you move away this trimmed preview is taken away.

## Syntax

SelectEvents.**OnStopPreSelect**( ***ModelPosition*** As [Point](../Point/Point.md), ***ViewPosition*** As [Point2d](../Point2d/Point2d.md), ***View*** As [View](../View/View.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ModelPosition | [Point](../Point/Point.md) | Returns the coordinates that result from projecting the click point onto the selected entity. This is returned in centimeters relative to model space. Applicable only when the SelectionDevice argument is kGraphicsWindowSelection. |
| ViewPosition | [Point2d](../Point2d/Point2d.md) | Returns the coordinates that specify the current location of the mouse pointer in window space and are returned in pixels. Applicable only when the SelectionDevice argument is kGraphicsWindowSelection. |
| View | [View](../View/View.md) | Returns the View object where the selection took place. Applicable only when the SelectionDevice argument is kGraphicsWindowSelection. |

## Version

Introduced in version 5
