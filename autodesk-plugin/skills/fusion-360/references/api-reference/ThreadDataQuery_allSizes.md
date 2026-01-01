# ThreadDataQuery.allSizes Method

Parent Object: [ThreadDataQuery](ThreadDataQuery.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadDataQuery.h>

## Description

Returns an array/list of all the available thread sizes for a given thread type. You can use the allThreadTypes property to get the available thread types.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadDataQuery\_var" is a variable referencing a [ThreadDataQuery](ThreadDataQuery.htm) object.```` ``` returnValue = threadDataQuery_var.allSizes(threadType) ``` ```` |

"threadDataQuery\_var" is a variable referencing a [ThreadDataQuery](ThreadDataQuery.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| string[] | Returns the specified thread sizes or an empty array/list if an invalid thread type was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| threadType | string | Specify the thread type. |

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