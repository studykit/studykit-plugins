# UserInputEvents.OnStopPreSelect Event

Parent Object: [UserInputEvents](../UserInputEvents/UserInputEvents.md)

## Description

Fires when the user hovers away from an Inventor object and it is no longer highlighted.

## Syntax

UserInputEvents.**OnStopPreSelect**( ***ModelPosition*** As [Point](../Point/Point.md), ***ViewPosition*** As [Point2d](../Point2d/Point2d.md), ***View*** As [View](../View/View.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ModelPosition | [Point](../Point/Point.md) | Returns the coordinates that result from projecting the click point onto the selected entity. This is returned in centimeters relative to model space. Applicable only when the SelectionDevice argument is kGraphicsWindowSelection. |
| ViewPosition | [Point2d](../Point2d/Point2d.md) | Returns the coordinates that specify the current location of the mouse pointer in window space and are returned in pixels. Applicable only when the SelectionDevice argument is kGraphicsWindowSelection. |
| View | [View](../View/View.md) | Returns the View object where the selection took place. Applicable only when the SelectionDevice argument is kGraphicsWindowSelection. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |