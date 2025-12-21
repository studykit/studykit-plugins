# BOMQuantity.GetEvaluatedBaseQuantity Method

Parent Object: [BOMQuantity](../BOMQuantity/BOMQuantity.md)

## Description

Method that retrieves the stored base quantity for the component.

## Syntax

BOMQuantity.**GetEvaluatedBaseQuantity**( ***QuantityType*** As [BOMQuantityTypeEnum](../BOMQuantityTypeEnum.md) ) As Double

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| QuantityType | [BOMQuantityTypeEnum](../BOMQuantityTypeEnum.md) | BOMQuantityTypeEnum indicating the stored quantity type. This can currently return either kEachBOMQuantity or kParameterBOMQuantity. If kParameterBOMQuantity is returned, the Quantity argument returns the evaluated string indicating the base quantity. |

## Version

Introduced in version 11
