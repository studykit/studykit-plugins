# WeldmentComponentDefinition.FindUsingRay Method

Parent Object: [WeldmentComponentDefinition](../WeldmentComponentDefinition/WeldmentComponentDefinition.md)

## Description

Method that fires a ray through the part or assembly and returns the entities intersected by the ray. The objects intersected by the ray are returned in the order in which they are intersected, with the first entities returned being those closest to the clipping plane.

## Syntax

WeldmentComponentDefinition.**FindUsingRay**( ***RayStartPoint*** As [Point](../Point/Point.md), ***RayDirection*** As [UnitVector](../UnitVector/UnitVector.md), ***Radius*** As Double, ***FoundEntities*** As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md), ***LocationPoints*** As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md), [***FindFirstOnly***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| RayStartPoint | [Point](../Point/Point.md) | Input object that defines the start point of the ray in model space. |
| RayDirection | [UnitVector](../UnitVector/UnitVector.md) | Input object that defines the direction of the ray. The ray is infinite in the direction defined. |
| Radius | Double | Input Double that defines the radius of the ray. This value is specified in centimeters. Defining a radius for a ray allows the intersection to be within a given tolerance. This radius essentially results in the definition of a cylinder whose axis lies along the axis defined by the RayStartPoint and RayDirection. The intersection result is between the cylinder and the model's entities. A value higher than zero is recommended, though not explicitly required. |
| FoundEntities | [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md) | Output that returns the entities that were intersected by the ray. |
| LocationPoints | [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md) | Output that returns a set of Point objects. One Point object is returned for each entity in the FoundEntities list. The point defines the coordinate of the intersection between the ray and the corresponding entity. |
| FindFirstOnly | Boolean | Optional input Boolean that specifies whether to find just the first entity in the ray's path. If False (the default) then all entities found are returned. |

## Version

Introduced in version 8

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |