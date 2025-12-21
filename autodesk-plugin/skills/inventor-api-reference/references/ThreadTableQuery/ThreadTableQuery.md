# ThreadTableQuery Object

## Description

The ThreadTableQuery object has methods to query the thread table data contained in the Thread.xls spreadsheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CreateThreadInfo](../ThreadTableQuery/ThreadTableQuery_CreateThreadInfo.md) | Method that creates a new ThreadInfo object that can be used in creating thread features. The object returned is a StandardThreadInfo for parallel threads and TaperedThreadInfo for tapered threads. See the Thread.xls file that is delivered with Autodesk Inventor for examples of valid input for these arguments. |
| [GetAvailableClasses](../ThreadTableQuery/ThreadTableQuery_GetAvailableClasses.md) | Method that returns all the available classes for a thread type of a given thread designation. |
| [GetAvailableDesignations](../ThreadTableQuery/ThreadTableQuery_GetAvailableDesignations.md) | Method that returns all the available thread designations for a thread type of a given size. |
| [GetAvailableThreadSizes](../ThreadTableQuery/ThreadTableQuery_GetAvailableThreadSizes.md) | Method that returns all the available thread sizes for a given thread type. |
| [GetAvailableThreadTypes](../ThreadTableQuery/ThreadTableQuery_GetAvailableThreadTypes.md) | Method that returns all the available thread types (families). |
| [GetThreadTypeIdentifier](../ThreadTableQuery/ThreadTableQuery_GetThreadTypeIdentifier.md) | Method that returns the non-localized thread type identifier given the localized thread type name |
| [GetThreadTypeName](../ThreadTableQuery/ThreadTableQuery_GetThreadTypeName.md) | Method that returns the localized thread type name given the non-localized thread type identifier |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ThreadTableQuery/ThreadTableQuery_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Type](../ThreadTableQuery/ThreadTableQuery_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GeneralOptions.ThreadTableQuery](../GeneralOptions/GeneralOptions_ThreadTableQuery.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creating a ThreadInfo object](../../sample-programs/ThreadTableQuery_CreateThreadInfo_Sample.md) | Demonstrates the use of a ThreadInfo object. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |