# SelectEvents.OnUnSelect Event

Parent Object: [SelectEvents](../SelectEvents/SelectEvents.md)

## Description

Event that occurs when the user unselects an entity. This is done in the user interface by pressing the Shift button and selecting a previously selected entity.

## Syntax

SelectEvents.**OnUnSelect**( ***UnSelectedEntities*** As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md), ***SelectionDevice*** As [SelectionDeviceEnum](../SelectionDeviceEnum.md), ***ModelPosition*** As [Point](../Point/Point.md), ***ViewPosition*** As [Point2d](../Point2d/Point2d.md), ***View*** As [View](../View/View.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| UnSelectedEntities | [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md) | Input ObjectsEnumerator that specifies the object(s) (un)selected by the user to be taken out of the selection set being built. |
| SelectionDevice | [SelectionDeviceEnum](../SelectionDeviceEnum.md) | Input constant denoting whether the (un)selection was made via a pick in a graphics window or was it by a pick in the browser or by some other means. An object can also be selected programmatically by calling the selection simulation methods on the CommandManager. A value of kGraphicsWindowSelection indicates it was (un)selected in a graphic window. For all other values the View, ModelPosition, and ViewPosition arguments are meaningless. |
| ModelPosition | [Point](../Point/Point.md) | Returns the coordinates that result from projecting the click point onto the (un)selected entity. This is returned in centimeters relative to model space. Applicable only when the SelectionDevice argument is kGraphicsWindowSelection. |
| ViewPosition | [Point2d](../Point2d/Point2d.md) | Returns the coordinates that specify the current location of the mouse pointer in window space and are returned in pixels. Applicable only when the SelectionDevice argument is kGraphicsWindowSelection. |
| View | [View](../View/View.md) | Returns the View object where the selection took place. Applicable only when the SelectionDevice argument is kGraphicsWindowSelection. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |