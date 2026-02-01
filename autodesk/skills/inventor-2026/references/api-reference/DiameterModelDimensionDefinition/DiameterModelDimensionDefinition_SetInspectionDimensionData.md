# DiameterModelDimensionDefinition.SetInspectionDimensionData Method

Parent Object: [DiameterModelDimensionDefinition](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition.md)

## Description

Method that sets the data associated with an inspection dimension. This method automatically sets the IsInspectionDimension property to True, if it isn’t already.

## Syntax

DiameterModelDimensionDefinition.**SetInspectionDimensionData**( [***Shape***] As [InspectionDimensionShapeEnum](../InspectionDimensionShapeEnum.md), [***Label***] As String, [***Rate***] As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Shape | [InspectionDimensionShapeEnum](../InspectionDimensionShapeEnum.md) | Optional input InspectionDimensionShapeEnum that specifies the border shape surrounding the inspection dimension text. Valid values are kNoInspectionBorder, kAngularEndsInspectionBorder and kRoundedEndsInspectionBorder. If not specified, kNoInspectionBorder is used. |
| Label | String | Optional input string that specifies the text placed left of the dimension value. The string can contain symbols specified using the StyleOverride tag. For instance, it can contain “<StyleOverride Font='AIGDT'>m</StyleOverride>” to specify ![](../images/CircleM.png).   This is an optional argument whose default value is "". |
| Rate | String | Optional input string that specifies the text (typically a percentage value) placed to the right of the dimension value. The string can contain symbols specified using the StyleOverride tag. For instance, it can contain “<StyleOverride Font='AIGDT'>m</StyleOverride>” to specify ![](../images/CircleM.png).   This is an optional argument whose default value is "". |

## Version

Introduced in version 2018
