# WorkspaceList.item Method

Parent Object: [WorkspaceList](WorkspaceList.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/WorkspaceList.h>

## Description

Returns the specified work space using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workspaceList\_var" is a variable referencing a [WorkspaceList](WorkspaceList.htm) object.```` ``` returnValue = workspaceList_var.item(index) ``` ```` |

"workspaceList\_var" is a variable referencing a [WorkspaceList](WorkspaceList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Workspace](Workspace.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |