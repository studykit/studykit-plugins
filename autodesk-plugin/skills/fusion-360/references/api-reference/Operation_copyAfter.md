# Operation.copyAfter Method

Parent Object: [Operation](Operation.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/Operation.h>

## Description

Creates a duplicate of the operation in the tree after the given operation. Throws an exception if a not allowed copy operation is made for example copying a operation out of a setup.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operation\_var" is a variable referencing an [Operation](Operation.htm) object.```` ``` returnValue = operation_var.copyAfter(operation) ``` ```` |

"operation\_var" is a variable referencing an [Operation](Operation.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns if copy command was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| operation | [OperationBase](OperationBase.htm) | Operation to copy targeted operation after. |

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |