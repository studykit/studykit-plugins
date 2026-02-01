# ThreadTableQuery.CreateThreadInfo Method

Parent Object: [ThreadTableQuery](../ThreadTableQuery/ThreadTableQuery.md)

## Description

Method that creates a new ThreadInfo object that can be used in creating thread features. The object returned is a StandardThreadInfo for parallel threads and TaperedThreadInfo for tapered threads. See the Thread.xls file that is delivered with Autodesk Inventor for examples of valid input for these arguments.

## Syntax

ThreadTableQuery.**CreateThreadInfo**( ***Internal*** As Boolean, ***RightHanded*** As Boolean, ***ThreadType*** As String, ***ThreadDesignation*** As String, [***Class***] As String ) As [ThreadInfo](../ThreadInfo/ThreadInfo.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Internal | Boolean | Input Boolean that indicates if the thread is an internal or external thread. A value of True indicates an Internal thread. |
| RightHanded | Boolean | Input Boolean that indicates if the thread is right or left\-handed thread. A value of True indicates a right\-handed thread. |
| ThreadType | String | Input String that specifies the thread type. The thread type is the name of the sheet in the Thread.xls file that is used by the Thread command to define valid thread definitions. |
| ThreadDesignation | String | Input String that contains the thread designation. This is input as the full thread designation that will be used in a drawing for the thread callout. The nominal size and pitch information are extracted from the designation. For \example valid inch thread designations are '10\-24 UNC' and '7/16\-20 UNF'. Examples of valid metric designations are 'M16x1.5' and 'M55x1.5'. |
| Class | String | Optional input String that defines the thread class. For example a valid class for an inch internal thread is '2B'. A valid class for a metric external thread is '6g'. Null strings are valid for some thread types. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creating a ThreadInfo object](../../sample-programs/ThreadTableQuery_CreateThreadInfo_Sample.md) | Demonstrates the use of a ThreadInfo object. |

## Version

Introduced in version 2008
