# HoleClearanceInfo.SetClearanceInfo Method

Parent Object: [HoleClearanceInfo](../HoleClearanceInfo/HoleClearanceInfo.md)

## Description

Method that set HoleClearanceInfo data.

## Syntax

HoleClearanceInfo.**SetClearanceInfo**( ***FastenerStandard*** As String, ***FastenerType*** As String, ***FastenerSize*** As String, [***FastenerFitType***] As Variant )

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

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |