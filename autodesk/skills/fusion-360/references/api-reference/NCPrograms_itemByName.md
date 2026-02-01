# NCPrograms.itemByName Method

Parent Object: [NCPrograms](NCPrograms.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/NCProgram/NCPrograms.h>

## Description

Returns the NC program with the specified name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nCPrograms\_var" is a variable referencing a [NCPrograms](NCPrograms.htm) object.```` ``` returnValue = nCPrograms_var.itemByName(name) ``` ```` |

"nCPrograms\_var" is a variable referencing a [NCPrograms](NCPrograms.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [NCProgram](NCProgram.htm) | Returns the specified NC program or null in the case where there is no NC program with the specified name. If there are multiple NC programs with the same name, the first item in the tree will be returned. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name (as it appears in the browser) of the operation. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |