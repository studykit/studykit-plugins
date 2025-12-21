# OrdinateDimensionSets.Add Method

Parent Object: [OrdinateDimensionSets](../OrdinateDimensionSets/OrdinateDimensionSets.md)

## Description

Method that creates an ordinate dimension set and returns the newly created OrdinateDimensionSet object.

## Remarks

The value kAlignedDimensionType of the DimensionType parameter can be specified only if the first geometry specified in the input GeometryIntents collection represents a line which is not parallel to the x or y axes of the sheet. If kAlignedDimensionType is specified, the placement point decides the orientation of the dimension set as demonstrated in the picture below.

![](../images/OrdinateDimensionSets_Add.png)

## Syntax

OrdinateDimensionSets.**Add**( ***GeometryIntents*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***PlacementPoint*** As [Point2d](../Point2d/Point2d.md), ***DimensionType*** As [DimensionTypeEnum](../DimensionTypeEnum.md), [***DimensionStyle***] As Variant, [***Layer***] As Variant ) As [OrdinateDimensionSet](../OrdinateDimensionSet/OrdinateDimensionSet.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| GeometryIntents | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection containing GeometryIntent objects. The GeometryIntent objects specify the geometries to use for the dimension. The first geometry in the collection is assumed to be the origin.  A GeometryIntent object can be created using the Sheet.CreateGeometryIntent method. |
| PlacementPoint | [Point2d](../Point2d/Point2d.md) | Input Point2d object that specifies the placement point of the dimension set on the sheet. |
| DimensionType | [DimensionTypeEnum](../DimensionTypeEnum.md) | ' Input DimensionTypeEnum that specifies the dimension type. Valid values kHorizontalDimensionType, kVerticalDimensionType and kAlignedDimensionType. See Remarks. |
| DimensionStyle | Variant | Optional input DimensionStyle object that specifies the dimension style to use for the dimension. If not specified, the style defined by the active standard is used. |
| Layer | Variant | Optional input Layer object that specifies the layer to use for the dimension. If not specified, the layer defined by the active standard is used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2010
