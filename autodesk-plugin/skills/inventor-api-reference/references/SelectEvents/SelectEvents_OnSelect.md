# SelectEvents.OnSelect Event

Parent Object: [SelectEvents](../SelectEvents/SelectEvents.md)

## Description

Event that occurs when the user selects an entity.

## Syntax

SelectEvents.**OnSelect**( ***JustSelectedEntities*** As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md), ***SelectionDevice*** As [SelectionDeviceEnum](../SelectionDeviceEnum.md), ***ModelPosition*** As [Point](../Point/Point.md), ***ViewPosition*** As [Point2d](../Point2d/Point2d.md), ***View*** As [View](../View/View.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| JustSelectedEntities | [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md) | Returns the object(s) that were just selected by the user. This may be the only one selected so far or the latest one in a series during this selection process. Multiple objects may be returned if the user does a window (area) select. |
| SelectionDevice | [SelectionDeviceEnum](../SelectionDeviceEnum.md) | Input constant denoting whether the selection was made via a pick in a graphics window or was it by a pick in the browser or by some other means. An object can also be selected programmatically by calling the selection simulation methods on the CommandManager. A value of kGraphicsWindowSelection indicates it was selected in a graphic window. For all other values the View, ModelPosition, and ViewPosition arguments are meaningless. |
| ModelPosition | [Point](../Point/Point.md) | Returns the coordinates that result from projecting the click point onto the selected entity. This is returned in centimeters relative to model space. Applicable only when the SelectionDevice argument is kGraphicsWindowSelection. |
| ViewPosition | [Point2d](../Point2d/Point2d.md) | Returns the coordinates that specify the current location of the mouse pointer in window space and are returned in pixels. Applicable only when the SelectionDevice argument is kGraphicsWindowSelection. |
| View | [View](../View/View.md) | Returns the View object where the selection took place. Applicable only when the SelectionDevice argument is kGraphicsWindowSelection. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Basic Selection Using Interaction Events](../../sample-programs/InteractionEventsSink_Sample.md) | This sample demonstrates using the selection events to select a face. Selection is dependent on events and VB only supports events within a class module. |

## Version

Introduced in version 5
