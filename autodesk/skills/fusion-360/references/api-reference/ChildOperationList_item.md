# ChildOperationList.item Method

Parent Object: [ChildOperationList](ChildOperationList.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/ChildOperationList.h>

## Description

Returns the specified item using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"childOperationList\_var" is a variable referencing a [ChildOperationList](ChildOperationList.htm) object.```` ``` returnValue = childOperationList_var.item(index) ``` ```` |

"childOperationList\_var" is a variable referencing a [ChildOperationList](ChildOperationList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Base](Base.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |