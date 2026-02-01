# ThreadTableQuery.GetAvailableClasses Method

Parent Object: [ThreadTableQuery](../ThreadTableQuery/ThreadTableQuery.md)

## Description

Method that returns all the available classes for a thread type of a given thread designation.

## Syntax

ThreadTableQuery.**GetAvailableClasses**( ***Internal*** As Boolean, ***ThreadType*** As String, ***ThreadDesignation*** As String ) As String()

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Internal | Boolean | Input Boolean that indicates if the thread is an internal or external thread. A value of True indicates an Internal thread. |
| ThreadType | String | Thread type identifier string. |
| ThreadDesignation | String | A string that contains the thread designation. This is the full thread designation that is used in a drawing for the thread callout. |

## Version

Introduced in version 11
