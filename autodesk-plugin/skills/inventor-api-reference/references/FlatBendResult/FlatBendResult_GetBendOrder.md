# FlatBendResult.GetBendOrder Method

Parent Object: [FlatBendResult](../FlatBendResult/FlatBendResult.md)

## Description

Method that gets the bend order for this bend result.

## Syntax

FlatBendResult.**GetBendOrder**( ***BenderOrder*** As Long, ***BendOrderSourceType*** As [BendOrderSourceTypeEnum](../BendOrderSourceTypeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BenderOrder | Long | Output Long that defines the order of this bend. |
| BendOrderSourceType | [BendOrderSourceTypeEnum](../BendOrderSourceTypeEnum.md) | Output BendOrderSourceTypeEnum value that defines how the bend order value has been defined. Valid values and their meaning is described below.  kDefaultBendOrder - The original bend order as determined by Inventor.  kOverrideBendOrder - The bend order has been assigned by the end-user and has overridden the default value.  kDuplicateOverrideBendOrder - The bend order has been assigned by the end-user and has overridden the default value. It is also has a duplicate value as another bend. |

## Version

Introduced in version 2010
