# WorkspaceList.itemById Method

Parent Object: [WorkspaceList](WorkspaceList.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/WorkspaceList.h>

## Description

Returns the Workspace of the specified ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workspaceList\_var" is a variable referencing a [WorkspaceList](WorkspaceList.htm) object.```` ``` returnValue = workspaceList_var.itemById(id) ``` ```` |

"workspaceList\_var" is a variable referencing a [WorkspaceList](WorkspaceList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Workspace](Workspace.htm) | Returns the specified workspace or null in the case where there isn't a workspace with the specified ID. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The ID of the workspace to get. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |