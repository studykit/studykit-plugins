# Operations.itemByName Method

Parent Object: [Operations](Operations.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/Operations.h>

## Description

Returns the operation with the specified name (as appears in the browser).

## Syntax

* [Python](#Python)
* [C++](#C++)

"operations\_var" is a variable referencing an [Operations](Operations.htm) object.```` ``` returnValue = operations_var.itemByName(name) ``` ```` |

"operations\_var" is a variable referencing an [Operations](Operations.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Operation](Operation.htm) | Returns the specified operation or null in the case where there is no operation with the specified name. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name (as it appears in the browser) of the operation. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |