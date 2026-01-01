# ToolbarPanelList.itemById Method

Parent Object: [ToolbarPanelList](ToolbarPanelList.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarPanelList.h>

## Description

Returns the ToolbarPanel of the specified ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarPanelList\_var" is a variable referencing a [ToolbarPanelList](ToolbarPanelList.htm) object.```` ``` returnValue = toolbarPanelList_var.itemById(id) ``` ```` |

"toolbarPanelList\_var" is a variable referencing a [ToolbarPanelList](ToolbarPanelList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ToolbarPanel](ToolbarPanel.htm) | Returns the specified ToolbarPanel or null in the case where there isn't a ToolbarPanel with the specified ID. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The ID of the ToolbarPanel to get. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |