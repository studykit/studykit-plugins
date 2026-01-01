# ChildOperationList.itemByOperationId Method

Parent Object: [ChildOperationList](ChildOperationList.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/ChildOperationList.h>

## Description

Returns the operation, folder or pattern with the specified operation id.

## Syntax

* [Python](#Python)
* [C++](#C++)

"childOperationList\_var" is a variable referencing a [ChildOperationList](ChildOperationList.htm) object.```` ``` returnValue = childOperationList_var.itemByOperationId(id) ``` ```` |

"childOperationList\_var" is a variable referencing a [ChildOperationList](ChildOperationList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Base](Base.htm) | Returns the specified item or null in the case where there is no item with the specified operation id. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | integer | The id of the operation, folder or pattern. |

## Version

Introduced in version May 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |