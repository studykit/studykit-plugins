# Sketch.RotateSketchObjects Method

Parent Object: [Sketch](../Sketch/Sketch.md)

## Description

Method that rotates a collection of sketch objects by a specified angle. If the Copy argument is set to True, the newly created objects are returned.

## Syntax

Sketch.**RotateSketchObjects**( ***SketchObjects*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***CenterPoint*** As [Point2d](../Point2d/Point2d.md), ***Angle*** As Double, [***Copy***] As Boolean, [***RemoveConstraints***] As Boolean ) As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SketchObjects | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection that contains the sketch elements to rotate. The collection must contain at least one object and can be any SketchEntity, a TextBox or an Image. |
| CenterPoint | [Point2d](../Point2d/Point2d.md) | Input Point2d object that defines the center point to rotate the elements about. |
| Angle | Double | Input Double that defines the angle to rotate the elements by in radians. |
| Copy | Boolean | Optional input Boolean that specifies whether to copy the sketch elements to the new location or to rotate them. If not specified, a default value of False is used indicating that the elements will be rotated. |
| RemoveConstraints | Boolean | Optional input Boolean that specifies whether to remove or retain some of the constraints that constrain the input sketch entities to other geometry. If not specified, a default value of False is used indicating that the constraints will be retained.   This is an optional argument whose default value is False. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |