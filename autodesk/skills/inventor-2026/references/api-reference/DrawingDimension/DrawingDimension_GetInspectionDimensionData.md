# DrawingDimension.GetInspectionDimensionData Method

Parent Object: [DrawingDimension](../DrawingDimension/DrawingDimension.md)

## Description

Method that returns the data associated with an inspection dimension. This method returns an error if the IsInspectionDimension property returns False.

## Remarks

An example of a StyleOverride tag in this context. `<StyleOverride Font='AIGDT'\>m</StyleOverride>` will result in the symbol ![](../images/styleoverride_aigdt_m.png)

## Syntax

DrawingDimension.**GetInspectionDimensionData**( ***Shape*** As [InspectionDimensionShapeEnum](../InspectionDimensionShapeEnum.md), ***Label*** As String, ***Rate*** As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Shape | [InspectionDimensionShapeEnum](../InspectionDimensionShapeEnum.md) | Output InspectionDimensionShapeEnum that indicates the border shape surrounding the inspection dimension text. Valid return values are kNoInspectionBorder, kAngularEndsInspectionBorder and kRoundedEndsInspectionBorder. |
| Label | String | Output string that returns the text placed left of the dimension value. The string can contain symbols specified using the StyleOverride tag. |
| Rate | String | Output string that returns the text (typically a percentage value) placed to the right of the dimension value. The string can contain symbols specified using the StyleOverride tag. |

## Version

Introduced in version 2010
