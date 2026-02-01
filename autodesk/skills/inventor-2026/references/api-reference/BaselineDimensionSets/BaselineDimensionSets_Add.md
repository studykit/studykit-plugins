# BaselineDimensionSets.Add Method

Parent Object: [BaselineDimensionSets](../BaselineDimensionSets/BaselineDimensionSets.md)

## Description

Method that creates a baseline dimension set and returns the newly created BaselineDimensionSet object.

## Remarks

The value kAlignedDimensionType for the DimensionType parameter can be specified only if the first geometry specified in the input GeometryIntents collection represents a line which is not parallel to the x or y axes of the sheet. If kAlignedDimensionType is specified, the placement point decides the orientation of the dimension set as demonstrated in the pictures below.

![](../Images/kAlignedDimensionType1.png)

Aligned dimension set: Placement point along the direction of the first geometry with a tolerance of 0.25 cm on either side of the line.

![](../Images/kAlignedDimensionType2.png)

Aligned dimension set: Placement point not along the direction of the first geometry

## Syntax

BaselineDimensionSets.**Add**( ***GeometryIntents*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***PlacementPoint*** As [Point2d](../Point2d/Point2d.md), ***DimensionType*** As [DimensionTypeEnum](../DimensionTypeEnum.md), [***DimensionStyle***] As Variant, [***Layer***] As Variant ) As [BaselineDimensionSet](../BaselineDimensionSet/BaselineDimensionSet.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| GeometryIntents | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection containing GeometryIntent objects. The GeometryIntent objects specify the geometries to use for the dimension. The first geometry in the collection is assumed to be the origin. |
| PlacementPoint | [Point2d](../Point2d/Point2d.md) | Input Point2d object that specifies the placement point of the dimension set on the sheet. |
| DimensionType | [DimensionTypeEnum](../DimensionTypeEnum.md) | ' Input DimensionTypeEnum that specifies the dimension type. Valid values kHorizontalDimensionType, kVerticalDimensionType and kAlignedDimensionType. See Remarks. |
| DimensionStyle | Variant | Optional input DimensionStyle object that specifies the dimension style to use for the dimension. If not specified, the style defined by the active standard is used. |
| Layer | Variant | Optional input Layer object that specifies the layer to use for the dimension. If not specified, the layer defined by the active standard is used.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Baseline dimension sets](../../sample-programs/BaselineDimensionSets_Add_Sample.md) | This sample demonstrates the creation of a baseline set dimension in a drawing. |

## Version

Introduced in version 2010
