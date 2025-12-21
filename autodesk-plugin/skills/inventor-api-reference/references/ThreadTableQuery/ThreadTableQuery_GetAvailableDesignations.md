# ThreadTableQuery.GetAvailableDesignations Method

Parent Object: [ThreadTableQuery](../ThreadTableQuery/ThreadTableQuery.md)

## Description

Method that returns all the available thread designations for a thread type of a given size.

## Syntax

ThreadTableQuery.**GetAvailableDesignations**( ***Internal*** As Boolean, ***ThreadType*** As String, ***NominalSize*** As String ) As String()

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Internal | Boolean | Input Boolean that indicates if the thread is an internal or external thread. A value of True indicates an Internal thread. |
| ThreadType | String | Thread type identifier string. |
| NominalSize | String | The description of the nominal size. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creating a ThreadInfo object](../../sample-programs/ThreadTableQuery_CreateThreadInfo_Sample.md) | Demonstrates the use of a ThreadInfo object. |

## Version

Introduced in version 11
