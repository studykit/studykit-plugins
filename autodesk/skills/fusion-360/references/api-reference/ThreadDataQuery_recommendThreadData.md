# ThreadDataQuery.recommendThreadData Method

Parent Object: [ThreadDataQuery](ThreadDataQuery.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadDataQuery.h>

## Description

Method that gets the recommended thread data for a given cylinder diameter. This method is only valid for straight threads and will fail for tapered threads.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadDataQuery\_var" is a variable referencing a [ThreadDataQuery](ThreadDataQuery.htm) object. |

```` ```  #include <Fusion/Features/ThreadDataQuery.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| modelDiameter | double | The diameter of the cylinder the thread will be placed on. The units are centimeters. |
| isInternal | boolean | Indicates if the thread is an internal or external thread. |
| threadType | string | Specifies the thread type to query the thread data. |
| designation | string | The output thread designation. |
| threadClass | string | The output thread class. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |