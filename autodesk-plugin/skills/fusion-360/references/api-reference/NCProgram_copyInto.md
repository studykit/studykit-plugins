# NCProgram.copyInto Method

Parent Object: [NCProgram](NCProgram.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/NCProgram/NCProgram.h>

## Description

Creates a duplicate of the operation into the given container. You can only copy into containers, such as setups or folders. Copied operation will be copied at the end of all operations already in the container. Throws an exception if a not allowed copy operation is made for example copying a setup into a setup.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nCProgram\_var" is a variable referencing a [NCProgram](NCProgram.htm) object.```` ``` returnValue = nCProgram_var.copyInto(container) ``` ```` |

"nCProgram\_var" is a variable referencing a [NCProgram](NCProgram.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns if copy command was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| container | [OperationBase](OperationBase.htm) | Container to copy targeted operation into. |

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |