# HoleFeatures.CreateTaperedTapInfo Method

Parent Object: [HoleFeatures](../HoleFeatures/HoleFeatures.md)

## Description

Method that creates a new TaperedThreadInfo object that can be used in creating HoleFeature objects. See the Thread.xls file that is delivered with Inventor for examples of valid input for these arguments. The spreadsheet columns match one for one with these arguments.

## Syntax

HoleFeatures.**CreateTaperedTapInfo**( ***RightHanded*** As Boolean, ***ThreadType*** As String, ***ThreadDesignation*** As String ) As [TaperedThreadInfo](../TaperedThreadInfo/TaperedThreadInfo.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| RightHanded | Boolean | Input Boolean that indicates if the thread is right or left-handed thread. A value of True indicates a right-handed thread. |
| ThreadType | String | Input String that specifies the thread type. The thread type is the name of the sheet in the Thread.xls file that is used by the Thread command to define valid thread definitions. |
| ThreadDesignation | String | Input String that contains the thread designation. This is input as the full thread designation that will be used in a drawing for the thread callout. The nominal size information is extracted from the designation. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |