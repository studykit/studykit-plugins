# Centerlines.AddCenteredPattern Method

Parent Object: [Centerlines](../Centerlines/Centerlines.md)

## Description

Method that creates a new centerline pattern. The centerline created with this method is kCenteredPatternCenterline type.

## Syntax

Centerlines.**AddCenteredPattern**( ***PatternCenter*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), ***CenterEntities*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), [***CentermarkStyle***] As Variant, [***Layer***] As Variant, [***Closed***] As Boolean ) As [Centerline](../Centerline/Centerline.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PatternCenter | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Input GeometryIntent that defines the a circular or elliptical drawing curve that defines the center of the pattern. |
| CenterEntities | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection object that contains the set of entities that define the points the centerline passes through. Valid objects for input are GeometryIntent objects that reference circular or elliptical drawing curves, and center marks. |
| CentermarkStyle | Variant | Object that specifies the center mark style to use for the centerline. If not specified, the style defined by the active standard is used. |
| Layer | Variant | Object that specifies the layer to use for the centerline. If not specified, the layer defined by the active standard is used.   This is an optional argument whose default value is null. |
| Closed | Boolean | Input Boolean that indicates if the centerline should be closed or not.   This is an optional argument whose default value is False. |

## Version

Introduced in version 2010
