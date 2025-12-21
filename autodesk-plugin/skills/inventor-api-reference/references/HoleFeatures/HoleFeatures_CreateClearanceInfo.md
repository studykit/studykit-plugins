# HoleFeatures.CreateClearanceInfo Method

Parent Object: [HoleFeatures](../HoleFeatures/HoleFeatures.md)

## Description

Creates a new ClearanceInfo object.

## Syntax

HoleFeatures.**CreateClearanceInfo**( ***FastenerStandard*** As String, ***FastenerType*** As String, ***FastenerSize*** As String, [***FastenerFitType***] As Variant ) As [HoleClearanceInfo](../HoleClearanceInfo/HoleClearanceInfo.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FastenerStandard | String | Input String value that specifies the fastener standard. The standard is the name of the sheet in the Clearance.xls file that is used to define the clearance info. |
| FastenerType | String | Input String value that specifies the fastener type. |
| FastenerSize | String | Input String value that specifies the fastener size. |
| FastenerFitType | Variant | Optinal input FastenerFitTypeEnum value that specifies the fastener fit type. If not provided the default kNormalFitType will be used. |

## Version

Introduced in version 2021
