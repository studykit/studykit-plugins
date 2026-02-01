# NCPrograms.item Method

Parent Object: [NCPrograms](NCPrograms.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/NCProgram/NCPrograms.h>

## Description

Function that returns the specified NC program using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nCPrograms\_var" is a variable referencing a [NCPrograms](NCPrograms.htm) object.```` ``` returnValue = nCPrograms_var.item(index) ``` ```` |

"nCPrograms\_var" is a variable referencing a [NCPrograms](NCPrograms.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [NCProgram](NCProgram.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |