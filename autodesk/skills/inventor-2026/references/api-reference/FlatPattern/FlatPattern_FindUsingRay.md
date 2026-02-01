# FlatPattern.FindUsingRay Method

Parent Object: [FlatPattern](../FlatPattern/FlatPattern.md)

## Description

Method that fires a ray through the flat pattern and returns the entities intersected by the ray. The objects intersected by the ray are returned in the order in which they are intersected, with the first entities returned being those closest to the clipping plane.

## Remarks

There is also a precedence in the type of entities returned. The entities returned can be Vertex, Edge, or Face objects. The precedence is in that order. If the ray intersects a vertex, then that vertex is returned and none of the edges or faces that connect to that vertex are returned. If the ray intersects an edge, then that edge is returned and none of the faces that connect to the edge are returned. If the ray intersects a face, then that face is returned. If desired, you can use the functionality provided by the B-Rep portion of the API to obtain the various associated objects from the entity returned. For example if you need a face but an edge is returned, you can use the Faces property of the Edge object to get the associated faces. The start point defines the physical starting point from which to determine intersections. Any intersections behind the start point are ignored. However, the ray is infinite from the start point, so all intersections in the direction of the ray will be returned. Note: As of Autodesk Inventor 5.3 Service Pack 2, the FindUsingRay method has superseded LocateUsingRay. Please update your applications accordingly.

## Syntax

FlatPattern.**FindUsingRay**( ***RayStartPoint*** As [Point](../Point/Point.md), ***RayDirection*** As [UnitVector](../UnitVector/UnitVector.md), ***Radius*** As Double, ***FoundEntities*** As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md), ***LocationPoints*** As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md), [***FindFirstOnly***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| RayStartPoint | [Point](../Point/Point.md) | Input Point object that defines the start point of the ray in model space. |
| RayDirection | [UnitVector](../UnitVector/UnitVector.md) | Input UnitVector object that defines the direction of the ray. The ray is infinite in the direction defined. |
| Radius | Double | Input Double that defines the radius of the ray. This value is specified in centimeters. Defining a radius for a ray allows the intersection to be within a given tolerance. This radius essentially results in the definition of a cylinder whose axis lies along the axis defined by the RayStartPoint and RayDirection. The intersection result is between the cylinder and the model's entities. A value higher than zero is recommended, though not explicitly required. |
| FoundEntities | [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md) | Output ObjectsEnumerator that returns the entities that were intersected by the ray. |
| LocationPoints | [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md) | Output ObjectsEnumerator that returns a set of Point objects. One Point object is returned for each entity in the FoundEntities list. The point defines the coordinate of the intersection between the ray and the corresponding entity. |
| FindFirstOnly | Boolean | Optional input Boolean that specifies whether to find just the first entity in the ray's path. If False (the default) then all entities found are returned. |

## Version

Introduced in version 2010
