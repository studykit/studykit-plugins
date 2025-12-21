# WeldmentComponentDefinition.FindUsingPoint Method

Parent Object: [WeldmentComponentDefinition](../WeldmentComponentDefinition/WeldmentComponentDefinition.md)

## Description

Method that finds all the entities of the specified type at the specified location.

## Syntax

WeldmentComponentDefinition.**FindUsingPoint**( ***Point*** As [Point](../Point/Point.md), ***ObjectTypes***() As [SelectionFilterEnum](../SelectionFilterEnum.md), [***ProximityTolerance***] As Variant, [***VisibleObjectsOnly***] As Boolean ) As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Point | [Point](../Point/Point.md) | Input Point object that specifies the model space point at which to find the entities. |
| ObjectTypes | [SelectionFilterEnum](../SelectionFilterEnum.md) | Input array of SelelctionFilterEnum values that indicate the type of objects to find. The values are the enum values from the SelectionFilterEnum and can be combined to specify multiple object types. |
| ProximityTolerance | Variant | Input Double that specifies the tolerance value for the search. This value defines the radius of a sphere at the input point. All objects that intersect this sphere will be returned. If not specified, the default internal tolerance is used. |
| VisibleObjectsOnly | Boolean | Optional input Boolean that indicates whether or not invisible objects should be included in the search. Defaults to True indicating that invisible objects will be ignored.   This is an optional argument whose default value is True. |

## Version

Introduced in version 2009
