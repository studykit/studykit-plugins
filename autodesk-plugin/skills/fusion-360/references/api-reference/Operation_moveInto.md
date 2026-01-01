# Operation.moveInto Method

Parent Object: [Operation](Operation.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/Operation.h>

## Description

Move operation in tree into the given container. This only works with setups, patterns and folders. Moved operation will be moved at the end of all operations already in the container. Throws an exception if a not allowed move is made for example moving a setup into a setup.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operation\_var" is a variable referencing an [Operation](Operation.htm) object.```` ``` returnValue = operation_var.moveInto(container) ``` ```` |

"operation\_var" is a variable referencing an [Operation](Operation.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns if move operation was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| container | [OperationBase](OperationBase.htm) | Container to move targeted operation into. |

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |