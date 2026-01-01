# CAMHoleRecognition.moveAfter Method

Parent Object: [CAMHoleRecognition](CAMHoleRecognition.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMHoleRecognition.h>

## Description

Move operation in tree after the given operation. Throws an exception if a not allowed move is made for example moving a operation out of a setup.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMHoleRecognition\_var" is a variable referencing a [CAMHoleRecognition](CAMHoleRecognition.htm) object.```` ``` returnValue = cAMHoleRecognition_var.moveAfter(operation) ``` ```` |

"cAMHoleRecognition\_var" is a variable referencing a [CAMHoleRecognition](CAMHoleRecognition.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns if move operation was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| operation | [OperationBase](OperationBase.htm) | Operation to move targeted operation after. |

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |