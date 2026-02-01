# HoleFeatures.CreateTapInfo Method

Parent Object: [HoleFeatures](../HoleFeatures/HoleFeatures.md)

## Description

Method that creates a new HoleTapInfo object that can be used in creating threads for Hole features. See the Thread.xls file that is delivered with Autodesk Inventor for examples of valid input for these arguments.

## Syntax

HoleFeatures.**CreateTapInfo**( ***RightHanded*** As Boolean, ***ThreadType*** As String, ***ThreadDesignation*** As String, ***Class*** As String, ***FullTapDepth*** As Boolean, [***ThreadDepth***] As Variant ) As [HoleTapInfo](../HoleTapInfo/HoleTapInfo.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| RightHanded | Boolean | Input Boolean that indicates if the thread is right or left-handed thread. A value of True indicates a right-handed thread. |
| ThreadType | String | Input String that specifies the sheet in the Thread.xls that this thread information should be validated within. Each sheet within the Excel document is typically used for different thread types. The string is the name of the sheet. For example "ANSI Unified Screw Threads" or "ANSI Metric M Profile" are valid for English versions of Autodesk Inventor. |
| ThreadDesignation | String | Input String that contains the thread designation. This is input as the full thread designation that will be used in a drawing for the thread callout. The nominal size and pitch information are extracted from the designation. For example valid inch thread designations are '10-24 UNC' and '7/16-20 UNF'. Examples of valid metric designations are 'M16x1.5' and 'M55x1.5'. |
| Class | String | Input String that defines the thread class. For example a valid class for an inch internal thread is 2B. A valid class for a metric external thread is 6g. |
| FullTapDepth | Boolean | Input Boolean that indicates if the thread extends the full length of the hole or not. A value of True indicates the thread goes the full extent of the hole. |
| ThreadDepth | Variant | Optional input Variant that defines the thread depth. This is only applicable when the FullDepth argument is False, otherwise this argument is ignored. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Hole Feature - Through holes (RegularAndTapped)](../../sample-programs/HoleFeature_Sample.md) | This sample demonstrates the creation of through holes, both regular and tapped. |

## Version

Introduced in version 5
