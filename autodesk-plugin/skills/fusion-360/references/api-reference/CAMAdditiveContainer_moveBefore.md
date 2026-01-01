# CAMAdditiveContainer.moveBefore Method

Parent Object: [CAMAdditiveContainer](CAMAdditiveContainer.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMAdditiveContainer.h>

## Description

Move operation in tree before the given operation. Throws an exception if a not allowed move is made for example moving a operation out of a setup.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMAdditiveContainer\_var" is a variable referencing a [CAMAdditiveContainer](CAMAdditiveContainer.htm) object.```` ``` returnValue = cAMAdditiveContainer_var.moveBefore(operation) ``` ```` |

"cAMAdditiveContainer\_var" is a variable referencing a [CAMAdditiveContainer](CAMAdditiveContainer.htm) object. |

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

Introduced in version July 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |