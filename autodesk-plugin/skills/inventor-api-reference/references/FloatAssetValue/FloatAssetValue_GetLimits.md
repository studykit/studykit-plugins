# FloatAssetValue.GetLimits Method

Parent Object: [FloatAssetValue](../FloatAssetValue/FloatAssetValue.md)

## Description

Method that returns the limits for this value.

## Syntax

FloatAssetValue.**GetLimits**( ***HasLowLimit*** As Boolean, ***LowLimit*** As Double, ***HasHighLimit*** As Boolean, ***HighLimit*** As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| HasLowLimit | Boolean | Output Boolean that indicates if there is a lower limit. If False then the value of the LowLimit argument should be ignored. |
| LowLimit | Double | Output Double that is the lowest valid value. The value of this argument should be ignored if HasLowLimit is false. |
| HasHighLimit | Boolean | Output Boolean that indicates if there is an upper limit. If False then the value of the HighLimit argument should be ignored. |
| HighLimit | Double | Output Double that is the upper valid value. The value of this argument should be ignored if HasHighLimit is false. |

## Version

Introduced in version 2014
