# ThreadDataQuery.threadTypeUnit Method

Parent Object: [ThreadDataQuery](ThreadDataQuery.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadDataQuery.h>

## Description

Method that returns the unit for a given thread type.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadDataQuery\_var" is a variable referencing a [ThreadDataQuery](ThreadDataQuery.htm) object.```` ``` returnValue = threadDataQuery_var.threadTypeUnit(threadType) ``` ```` |

"threadDataQuery\_var" is a variable referencing a [ThreadDataQuery](ThreadDataQuery.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| string | Returns the specified unit or empty string if an invalid thread type was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| threadType | string | The thread type you want to get the thread unit type for. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |