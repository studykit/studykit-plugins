# BOMQuantity.SetBaseQuantity Method

Parent Object: [BOMQuantity](../BOMQuantity/BOMQuantity.md)

## Description

Method that sets the base quantity for the component.

## Syntax

BOMQuantity.**SetBaseQuantity**( ***QuantityType*** As [BOMQuantityTypeEnum](../BOMQuantityTypeEnum.md), [***Quantity***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| QuantityType | [BOMQuantityTypeEnum](../BOMQuantityTypeEnum.md) | Input BOMQuantityTypeEnum indicating the quantity type. If kParameterBOMQuantity is set, a Parameter needs to be specified as the second argument. |
| Quantity | Variant | Input Variant specifying the quantity. If QuantityType is kParameterBOMQuantity, this argument expects a Parameter input, else this argument can be left unspecified. Only such parameters whose units resolve to being a linear length, a volume, or a mass are valid. |

## Version

Introduced in version 10
