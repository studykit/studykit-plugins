# BOMQuantity.GetBaseQuantity Method

Parent Object: [BOMQuantity](../BOMQuantity/BOMQuantity.md)

## Description

Method that retrieves the base quantity for the component.

## Syntax

BOMQuantity.**GetBaseQuantity**( ***QuantityType*** As [BOMQuantityTypeEnum](../BOMQuantityTypeEnum.md), [***Quantity***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| QuantityType | [BOMQuantityTypeEnum](../BOMQuantityTypeEnum.md) | Output BOMQuantityTypeEnum indicating the quantity type. If kParameterBOMQuantity is returned, the Quantity argument returns the corresponding parameter object. |
| Quantity | Variant | Output Variant returning the quantity. This argument returns a Parameter object if the QuantityType returned is kParameterBOMQuantity. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |