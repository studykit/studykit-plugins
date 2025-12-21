# SelectEvents.OnPreSelect Event

Parent Object: [SelectEvents](../SelectEvents/SelectEvents.md)

## Description

Fires signaling that a particular object has been indicated as a potential candidate for selection.

## Remarks

This event is fired before the object is highlighted, giving the programmer the opportunity to apply further custom filtering. By responding with False to the DoHighlight argument, the object will not be available for selection and the UI behaves as if the object was never considered for selection.

## Syntax

SelectEvents.**OnPreSelect**( ***PreSelectEntity*** As Object, ***DoHighlight*** As Boolean, ***MorePreSelectEntities*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***SelectionDevice*** As [SelectionDeviceEnum](../SelectionDeviceEnum.md), ***ModelPosition*** As [Point](../Point/Point.md), ***ViewPosition*** As [Point2d](../Point2d/Point2d.md), ***View*** As [View](../View/View.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PreSelectEntity | Object | Input/Output. When called, Inventor returns the entity the mouse is currently over. The client though has a chance to change this entity to some other, if so desired. The entity passed back from the call is the one Inventor will highlight for the pre-select. |
| DoHighlight | Boolean | Input value that specifies whether the entity should be available for selection or not. If True, this signifies a successful pre-selection and the entity is highlighted by Inventor. |
| MorePreSelectEntities | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input argument through which you can supply a group of objects that are logically pre-selected along with the one that Inventor found on its own. This argument is ignored if DoHighLight is False. Inventor passes in an empty collection that you can add additional entities to. |
| SelectionDevice | [SelectionDeviceEnum](../SelectionDeviceEnum.md) | Returns a constant denoting whether the selection was made via a pick in a graphics window or was it by a pick in the browser or by some other means. An object can also be selected programmatically by calling the selection simulation methods on the CommandManager. A value of kGraphicsWindowSelection indicates it was selected in a graphic window. For all other values the View, ModelPosition, and ViewPosition arguments are meaningless. |
| ModelPosition | [Point](../Point/Point.md) | Returns the coordinates that result from projecting the click point onto the selected entity. This is returned in centimeters relative to model space. Applicable only when the SelectionDevice argument is kGraphicsWindowSelection. |
| ViewPosition | [Point2d](../Point2d/Point2d.md) | Returns the coordinates that specify the current location of the mouse pointer in window space and are returned in pixels. Applicable only when the SelectionDevice argument is kGraphicsWindowSelection. |
| View | [View](../View/View.md) | Returns the View  object where the selection took place. Applicable only when the SelectionDevice argument is kGraphicsWindowSelection. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |