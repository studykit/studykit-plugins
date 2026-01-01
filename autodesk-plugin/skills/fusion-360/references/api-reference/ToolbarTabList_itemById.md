# ToolbarTabList.itemById Method

Parent Object: [ToolbarTabList](ToolbarTabList.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarTabList.h>

## Description

Returns the ToolbarTab of the specified ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarTabList\_var" is a variable referencing a [ToolbarTabList](ToolbarTabList.htm) object.```` ``` returnValue = toolbarTabList_var.itemById(id) ``` ```` |

"toolbarTabList\_var" is a variable referencing a [ToolbarTabList](ToolbarTabList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ToolbarTab](ToolbarTab.htm) | Returns the specified ToolbarTab or null in the case where there isn't a ToolbarTab with the specified ID. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The ID of the ToolbarTab to get. |

## Version

Introduced in version August 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |