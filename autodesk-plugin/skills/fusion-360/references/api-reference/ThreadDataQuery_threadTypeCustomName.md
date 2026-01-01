# ThreadDataQuery.threadTypeCustomName Method

Parent Object: [ThreadDataQuery](ThreadDataQuery.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadDataQuery.h>

## Description

Method that returns the custom name for a given thread type. The custom name is the localized name of the thread type using the current language specified for Fusion.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadDataQuery\_var" is a variable referencing a [ThreadDataQuery](ThreadDataQuery.htm) object.```` ``` returnValue = threadDataQuery_var.threadTypeCustomName(threadType) ``` ```` |

"threadDataQuery\_var" is a variable referencing a [ThreadDataQuery](ThreadDataQuery.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| string | Returns the specified custom name or an empty string if an invalid thread type was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| threadType | string | The thread type you want to get the custom name for. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |