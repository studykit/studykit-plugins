# PlanarSketchProxy.MoveSketchObjects Method

Parent Object: [PlanarSketchProxy](../PlanarSketchProxy/PlanarSketchProxy.md)

## Description

Method that moves a collection of sketch objects by a specified vector. If the Copy argument is set to True, the newly created objects are returned.

## Syntax

PlanarSketchProxy.**MoveSketchObjects**( ***SketchObjects*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***Vector*** As [Vector2d](../Vector2d/Vector2d.md), [***Copy***] As Boolean, [***RemoveConstraints***] As Boolean ) As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SketchObjects | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection that contains the sketch elements to move. The collection must contain at least one object and can be any SketchEntity, a TextBox or an Image. |
| Vector | [Vector2d](../Vector2d/Vector2d.md) | Input Vector2d object that defines the delta distance to move the sketch elements. |
| Copy | Boolean | Optional input Boolean that specifies whether to copy the sketch elements to the new location or to move them. If not specified, a default value of False is used indicating that the elements will be moved. |
| RemoveConstraints | Boolean | Optional input Boolean that specifies whether to remove or retain some of the constraints that constrain the input sketch entities to other geometry. If not specified, a default value of False is used indicating that the constraints will be retained.   This is an optional argument whose default value is False. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |