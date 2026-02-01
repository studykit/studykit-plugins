# ThreadFeatures.CreateStandardThreadInfo Method

Parent Object: [ThreadFeatures](../ThreadFeatures/ThreadFeatures.md)

## Description

Method that creates a new HoleTapInfo object that can be used in creating threads for Hole features. See the Thread.xls \file that is delivered with Autodesk Inventor for examples of valid input for these arguments. Internal \Input Boolean that indicates if the thread is an internal or external thread. A value of True indicates an Internal thread. RightHanded : Input Boolean that indicates if the thread is right or left-handed thread. A value of True indicates a right-handed thread. ThreadType : Input String that specifies the sheet in the Thread.xls that this thread information should be validated within. Each sheet within the Excel document is typically used for different thread types. The string is the name of the sheet. For example "ANSI Unified Screw Threads" or "ANSI Metric M Profile" are valid for English versions of Autodesk Inventor. ThreadDesignation : Input String that contains the thread designation. This is input as the full thread designation that will be used in a drawing for the thread callout. The nominal size and pitch information are extracted from the designation. For example valid inch thread designations are '10-24 UNC' and '7/16-20 UNF'. Examples of valid metric designations are 'M16x1.5' and 'M55x1.5'. Class : Input String that defines the thread class. For \example a valid class for an inch internal thread is 2B. A valid class for a metric external thread is 6g.

## Syntax

ThreadFeatures.**CreateStandardThreadInfo**( ***Internal*** As Boolean, ***RightHanded*** As Boolean, ***ThreadType*** As String, ***ThreadDesignation*** As String, ***Class*** As String ) As [StandardThreadInfo](../StandardThreadInfo/StandardThreadInfo.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Internal | Boolean |  |
| RightHanded | Boolean |  |
| ThreadType | String |  |
| ThreadDesignation | String |  |
| Class | String |  |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Thread Feature Create](../../sample-programs/ThreadFeature_Sample.md) | This sample demonstrates the creation of a thread feature. It creates a cylinder in a new part document and creates a thread feature on the cylinder. |
| [Edit thread features](../../sample-programs/ThreadFeatures_CreateStandardThreadInfo_Sample.md) | The following example demonstrates how to edit an existing thread feature. |

## Version

Introduced in version 5
