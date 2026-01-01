# NCPrograms.itemByOperationId Method

Parent Object: [NCPrograms](NCPrograms.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/NCProgram/NCPrograms.h>

## Description

Returns the NC program with the specified operation id.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nCPrograms\_var" is a variable referencing a [NCPrograms](NCPrograms.htm) object.```` ``` returnValue = nCPrograms_var.itemByOperationId(id) ``` ```` |

"nCPrograms\_var" is a variable referencing a [NCPrograms](NCPrograms.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [NCProgram](NCProgram.htm) | Returns the specified NC program or null in the case where there is no NC program with the specified operation id. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | integer | The id of the NC program. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |