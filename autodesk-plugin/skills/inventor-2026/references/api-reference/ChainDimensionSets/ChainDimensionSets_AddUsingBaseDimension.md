# ChainDimensionSets.AddUsingBaseDimension Method

Parent Object: [ChainDimensionSets](../ChainDimensionSets/ChainDimensionSets.md)

## Description

Method that creates a chain dimension set based on the specified base dimension and using specified additional geometry. Returns the newly created ChainDimensionSet object.

## Syntax

ChainDimensionSets.**AddUsingBaseDimension**( ***Dimensions*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***GeometryIntents*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), [***DimensionStyle***] As Variant, [***Layer***] As Variant ) As [ChainDimensionSet](../ChainDimensionSet/ChainDimensionSet.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Dimensions | [ObjectCollection](../ObjectCollection/ObjectCollection.md) |  |
| GeometryIntents | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection containing GeometryIntent objects. The GeometryIntent objects specify the geometries to use for the dimension set. A GeometryIntent object can be created using the Sheet.CreateGeometryIntent method. |
| DimensionStyle | Variant | Optional input DimensionStyle object that specifies the dimension style to use for the dimension. If not specified, the style defined by the active standard is used. |
| Layer | Variant | Optional input Layer object that specifies the layer to use for the dimension. If not specified, the layer defined by the active standard is used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2011
