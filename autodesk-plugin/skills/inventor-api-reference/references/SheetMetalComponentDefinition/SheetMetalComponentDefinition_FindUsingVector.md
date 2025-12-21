# SheetMetalComponentDefinition.FindUsingVector Method

Parent Object: [SheetMetalComponentDefinition](../SheetMetalComponentDefinition/SheetMetalComponentDefinition.md)

## Description

Method that finds all the entities of the specified type along the specified vector using either a cylinder or cone that to define the tolerance within the defined vector.

## Syntax

SheetMetalComponentDefinition.**FindUsingVector**( ***OriginPoint*** As [Point](../Point/Point.md), ***Direction*** As [UnitVector](../UnitVector/UnitVector.md), ***ObjectTypes***() As [SelectionFilterEnum](../SelectionFilterEnum.md), [***UseCylinder***] As Boolean, [***ProximityTolerance***] As Variant, [***VisibleObjectsOnly***] As Boolean, [***LocationPoints***] As Variant ) As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| OriginPoint | [Point](../Point/Point.md) | Input Point that defines the model space location to position the vector. |
| Direction | [UnitVector](../UnitVector/UnitVector.md) | Input UnitVector that defines direction to find all entities that the vector penetrates. The vector is treated as infinite in both directions from the origin point so all entities that lie in the path of the vector on either side of the origin point will be returned. |
| ObjectTypes | [SelectionFilterEnum](../SelectionFilterEnum.md) | Input array of SelelctionFilterEnum values that indicate the type of objects to find. The values are the enum values from the SelectionFilterEnum and can be combined to specify multiple object types. |
| UseCylinder | Boolean | Input argument that specifies if the vector defines a cylinder or cone when checking to see if an entity is hit by the ray. |
| ProximityTolerance | Variant | Optional input Double that specifies the tolerance value for the search. This value defines the radius of a cylinder if UseCylinder is True or the angle of the cone if False. If not specified, the default internal tolerance is used.   This is an optional argument whose default value is null. |
| VisibleObjectsOnly | Boolean | Optional input Boolean that indicates whether or not invisible objects should be included in the search. Defaults to True indicating that invisible objects will be ignored.   This is an optional argument whose default value is True. |
| LocationPoints | Variant | Optional output that returns a set of Point objects. One Point object is returned for each entity in the FoundEntities list. The point defines the coordinate of the intersection between the vector and the corresponding entity.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2011
