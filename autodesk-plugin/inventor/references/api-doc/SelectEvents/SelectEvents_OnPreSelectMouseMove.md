# SelectEvents.OnPreSelectMouseMove Event

Parent Object: [SelectEvents](../SelectEvents/SelectEvents.md)

## Description

Event that occurs while an object is in pre-select mode and the user is moving the mouse. This allows you to receive mouse input relative to the pre-selected object.

## Syntax

SelectEvents.**OnPreSelectMouseMove**( ***PreSelectEntity*** As Object, ***ModelPosition*** As [Point](../Point/Point.md), ***ViewPosition*** As [Point2d](../Point2d/Point2d.md), ***View*** As [View](../View/View.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PreSelectEntity | Object | Input argument that specifies the object currently pre-selected. |
| ModelPosition | [Point](../Point/Point.md) | Returns the coordinates that result from projecting the current location of the mouse onto the selected entity. This is returned in centimeters relative to model space. |
| ViewPosition | [Point2d](../Point2d/Point2d.md) | Returns the coordinates that specify the current location of the mouse pointer in window space and are returned in pixels. |
| View | [View](../View/View.md) | Returns the View object where the selection took place. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |