# RigidGroupList.item Method

Parent Object: [RigidGroupList](RigidGroupList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/RigidGroupList.h>

## Description

Function that returns the specified rigid group using an index into the list.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rigidGroupList\_var" is a variable referencing a [RigidGroupList](RigidGroupList.htm) object.```` ``` returnValue = rigidGroupList_var.item(index) ``` ```` |

"rigidGroupList\_var" is a variable referencing a [RigidGroupList](RigidGroupList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RigidGroup](RigidGroup.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the list to return. The first item in the list has an index of 0. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |