# IntegerAssetValue.GetLimits Method

Parent Object: [IntegerAssetValue](../IntegerAssetValue/IntegerAssetValue.md)

## Description

Method that returns the limits for this value.

## Syntax

IntegerAssetValue.**GetLimits**( ***HasLowLimit*** As Boolean, ***LowLimit*** As Long, ***HasHighLimit*** As Boolean, ***HighLimit*** As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| HasLowLimit | Boolean | Output Boolean that indicates if there is a lower limit. If False then the value of the LowLimit argument should be ignored. |
| LowLimit | Long | Output Long that is the lowest valid value. |
| HasHighLimit | Boolean | Output Boolean that indicates if there is an upper limit. If False then the value of the HighLimit argument should be ignored. |
| HighLimit | Long | Output Long that is the upper valid value. |

## Version

Introduced in version 2014
