# ThreadDataQuery.allDesignations Method

Parent Object: [ThreadDataQuery](ThreadDataQuery.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadDataQuery.h>

## Description

returns an array/list of all the available thread designations for a thread type of a given size. Valid thread types and sizes and be obtained by using the allThreadTypes and allSizes functions.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadDataQuery\_var" is a variable referencing a [ThreadDataQuery](ThreadDataQuery.htm) object.```` ``` returnValue = threadDataQuery_var.allDesignations(threadType, size) ``` ```` |

"threadDataQuery\_var" is a variable referencing a [ThreadDataQuery](ThreadDataQuery.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| string[] | Returns the specified thread designations or empty array/list if an invalid thread type or size was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| threadType | string | The thread type of the designation you want. |
| size | string | The thread size of the designation you want. |

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