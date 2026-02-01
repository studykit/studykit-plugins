# Centerlines.Add Method

Parent Object: [Centerlines](../Centerlines/Centerlines.md)

## Description

Method that creates a new centerline. The centerline created with this method is kRegularCenterline type.

## Syntax

Centerlines.**Add**( ***CenterEntities*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), [***CentermarkStyle***] As Variant, [***Layer***] As Variant, [***Closed***] As Boolean ) As [Centerline](../Centerline/Centerline.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CenterEntities | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection object that contains the set of entities that define the points the centerline passes through. Valid objects for input are GeometryIntent objects that reference circular or elliptical drawing curves, GeometryIntent objects that reference the end or midpoint of linear drawing curves, and center marks. Providing two points will result in a linear centerline. Providing three points will result in a circular centerline. Providing more than three points will result in a linear or a circular centerline depending on whether all of the input points lie on a circle. |
| CentermarkStyle | Variant | Object that specifies the center mark style to use for the centerline. If not specified, the style defined by the active standard is used. |
| Layer | Variant | Object that specifies the layer to use for the centerline. If not specified, the layer defined by the active standard is used.   This is an optional argument whose default value is null. |
| Closed | Boolean | Input Boolean that is only used in the case of a circular centerline. This indicates if it should be closed or not.   This is an optional argument whose default value is False. |

## Version

Introduced in version 2009
