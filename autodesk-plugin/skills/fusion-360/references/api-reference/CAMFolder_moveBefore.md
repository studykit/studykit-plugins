# CAMFolder.moveBefore Method

Parent Object: [CAMFolder](CAMFolder.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMFolder.h>

## Description

Move operation in tree before the given operation. Throws an exception if a not allowed move is made for example moving a operation out of a setup.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMFolder\_var" is a variable referencing a [CAMFolder](CAMFolder.htm) object.```` ``` returnValue = cAMFolder_var.moveBefore(operation) ``` ```` |

"cAMFolder\_var" is a variable referencing a [CAMFolder](CAMFolder.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns if move operation was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| operation | [OperationBase](OperationBase.htm) | Operation to move targeted operation before. |

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |