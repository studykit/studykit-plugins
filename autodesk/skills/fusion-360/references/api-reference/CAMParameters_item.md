# CAMParameters.item Method

Parent Object: [CAMParameters](CAMParameters.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/CAMParameters.h>

## Description

Function that returns the specified parameter using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMParameters\_var" is a variable referencing a [CAMParameters](CAMParameters.htm) object.```` ``` returnValue = cAMParameters_var.item(index) ``` ```` |

"cAMParameters\_var" is a variable referencing a [CAMParameters](CAMParameters.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CAMParameter](CAMParameter.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |