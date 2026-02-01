# ChildOperationList.itemByName Method

Parent Object: [ChildOperationList](ChildOperationList.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/ChildOperationList.h>

## Description

Returns the operation, folder or pattern with the specified name (the name seen in the browser).

## Syntax

* [Python](#Python)
* [C++](#C++)

"childOperationList\_var" is a variable referencing a [ChildOperationList](ChildOperationList.htm) object.```` ``` returnValue = childOperationList_var.itemByName(name) ``` ```` |

"childOperationList\_var" is a variable referencing a [ChildOperationList](ChildOperationList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Base](Base.htm) | Returns the specified item or null in the case where there is no item with the specified name. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the operation, folder or pattern as seen in the browser. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |