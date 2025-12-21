# ThreadFeatures.CreateTaperedThreadInfo Method

Parent Object: [ThreadFeatures](../ThreadFeatures/ThreadFeatures.md)

## Description

Method that creates a new TaperedThreadInfo object that can be used in creating Hole and ThreadFeature objects. See the Thread.xls file that is delivered with Autodesk Inventor for examples of valid input for these arguments. The spreadsheet columns match one for one with these arguments.

## Syntax

ThreadFeatures.**CreateTaperedThreadInfo**( ***Internal*** As Boolean, ***RightHanded*** As Boolean, ***ThreadType*** As String, ***ThreadDesignation*** As String ) As [TaperedThreadInfo](../TaperedThreadInfo/TaperedThreadInfo.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Internal | Boolean | Input Boolean that indicates if the thread is an internal or external thread. A value of True indicates an Internal thread. |
| RightHanded | Boolean | Input Boolean that indicates if the thread is right or left-handed thread. A value of True indicates a right-handed thread. |
| ThreadType | String | Input String that specifies the sheet in the Thread.xls that this thread information should be validated within. Each sheet within the Excel document is typically used for different thread types. The string is the name of the sheet. For example "NPT" or "JIS Taper" are valid for English versions of Autodesk Inventor. |
| ThreadDesignation | String | Input String that contains the thread designation. This is input as the full thread designation that will be used in a drawing for the thread callout. The nominal size information is extracted from the designation. |

## Version

Introduced in version 5
