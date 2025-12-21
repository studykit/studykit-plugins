# ModelDatumDefinition.ApplySizeToAllDatumTargets Method

Parent Object: [ModelDatumDefinition](../ModelDatumDefinition/ModelDatumDefinition.md)

## Description

Applies the area size to all datum targets.

## Syntax

ModelDatumDefinition.**ApplySizeToAllDatumTargets**( ***DiameterOrWidth*** As Double, [***Height***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DiameterOrWidth | Double | Input Double value that specifies the datum target area diameter or width. The value indicate the datum target area diameter when the DatumTargetType is kModelDatumTargetTypeCircle, and the datum target area width when the DatumTargetType is kModelDatumTargetTypeRectangle. |
| Height | Variant | Optional input Double value that specifies the datum target area height. This property it is applicable when the DatumTargetType is kModelDatumTargetTypeRectangle. |

## Version

Introduced in version 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |