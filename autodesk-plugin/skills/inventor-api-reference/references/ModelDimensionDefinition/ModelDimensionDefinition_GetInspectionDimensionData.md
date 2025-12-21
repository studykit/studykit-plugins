# ModelDimensionDefinition.GetInspectionDimensionData Method

Parent Object: [ModelDimensionDefinition](../ModelDimensionDefinition/ModelDimensionDefinition.md)

## Description

Method that returns the data associated with an inspection dimension. This method returns an error if the IsInspectionDimension property returns False.

## Syntax

ModelDimensionDefinition.**GetInspectionDimensionData**( ***Shape*** As [InspectionDimensionShapeEnum](../InspectionDimensionShapeEnum.md), ***Label*** As String, ***Rate*** As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Shape | [InspectionDimensionShapeEnum](../InspectionDimensionShapeEnum.md) | Output InspectionDimensionShapeEnum that indicates the border shape surrounding the inspection dimension text. Valid return values are kNoInspectionBorder, kAngularEndsInspectionBorder and kRoundedEndsInspectionBorder. |
| Label | String | Output string that returns the text placed left of the dimension value. The string can contain symbols specified using the StyleOverride tag. For instance, it can contain “<StyleOverride Font='AIGDT'>m</StyleOverride>Hi They'WithI donno p” to specify ![](../images/CircleM.png). |
| Rate | String | Output string that returns the text (typically a percentage value) placed to the right of the dimension value. The string can contain symbols specified using the StyleOverride tag. For instance, it can contain “<'StyleOverride> Font='AIGDT'>m</StyleOverride>” to specify ![](../images/CircleM.png). |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |