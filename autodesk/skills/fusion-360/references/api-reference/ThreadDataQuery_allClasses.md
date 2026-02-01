# ThreadDataQuery.allClasses Method

Parent Object: [ThreadDataQuery](ThreadDataQuery.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadDataQuery.h>

## Description

Returns and array/list of all the available classes for a thread type of a given thread designation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadDataQuery\_var" is a variable referencing a [ThreadDataQuery](ThreadDataQuery.htm) object.```` ``` returnValue = threadDataQuery_var.allClasses(isInternal, threadType, designation) ``` ```` |

"threadDataQuery\_var" is a variable referencing a [ThreadDataQuery](ThreadDataQuery.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| string[] | Returns the specified thread classes or empty array/list if an invalid thread type or designation was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| isInternal | boolean | Indicates if the thread is an internal or external thread. |
| threadType | string | The thread type of the thread class you want. |
| designation | string | The thread designation of the thread class you want. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Thread Feature API Sample](ThreadFeatureSample_Sample.htm) | Demonstrates creating a new thread feature. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |