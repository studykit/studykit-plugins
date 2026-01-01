# Operations.itemByOperationId Method

Parent Object: [Operations](Operations.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/Operations.h>

## Description

Returns the operation with the specified operation id.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operations\_var" is a variable referencing an [Operations](Operations.htm) object.```` ``` returnValue = operations_var.itemByOperationId(id) ``` ```` |

"operations\_var" is a variable referencing an [Operations](Operations.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Operation](Operation.htm) | Returns the specified operation or null in the case where there is no operation with the specified operation id. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | integer | The id of the operation. |

## Version

Introduced in version May 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |