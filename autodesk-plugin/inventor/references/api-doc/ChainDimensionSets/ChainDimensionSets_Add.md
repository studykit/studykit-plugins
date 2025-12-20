# ChainDimensionSets.Add Method

Parent Object: [ChainDimensionSets](../ChainDimensionSets/ChainDimensionSets.md)

## Description

Method that creates a chain dimension set using the specified geometries. Returns the newly created ChainDimensionSets object.

## Syntax

ChainDimensionSets.**Add**( ***GeometryIntents*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***PlacementPoint*** As [Point2d](../Point2d/Point2d.md), ***DimensionType*** As [DimensionTypeEnum](../DimensionTypeEnum.md), [***DimensionStyle***] As Variant, [***Layer***] As Variant ) As [ChainDimensionSet](../ChainDimensionSet/ChainDimensionSet.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| GeometryIntents | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection containing GeometryIntent objects. The GeometryIntent objects specify the geometries to use for the dimension set. A GeometryIntent object can be created using the Sheet.CreateGeometryIntent method. |
| PlacementPoint | [Point2d](../Point2d/Point2d.md) | Input Point2d object that specifies the placement point of the dimension set on the sheet. |
| DimensionType | [DimensionTypeEnum](../DimensionTypeEnum.md) | Input DimensionTypeEnum that specifies the dimension type. Valid values kHorizontalDimensionType, kVerticalDimensionType and kAlignedDimensionType. The value kAlignedDimensionType can be specified only if the first geometry specified in the input GeometryIntents collection represents a line which is not parallel to the x or y axes of the sheet. If kAlignedDimensionType is specified, the placement point decides the orientation of the dimension set. |
| DimensionStyle | Variant | Optional input DimensionStyle object that specifies the dimension style to use for the dimension. If not specified, the style defined by the active standard is used. |
| Layer | Variant | Optional input Layer object that specifies the layer to use for the dimension. If not specified, the layer defined by the active standard is used.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Chain dimensions sets](../../sample-programs/ChainDimensionSets_Add_Sample.md) | This sample demonstrates the creation of a chain dimension set in a drawing. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |