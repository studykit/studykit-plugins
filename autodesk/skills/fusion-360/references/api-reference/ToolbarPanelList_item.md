# ToolbarPanelList.item Method

Parent Object: [ToolbarPanelList](ToolbarPanelList.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarPanelList.h>

## Description

Returns the specified work space using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarPanelList\_var" is a variable referencing a [ToolbarPanelList](ToolbarPanelList.htm) object.```` ``` returnValue = toolbarPanelList_var.item(index) ``` ```` |

"toolbarPanelList\_var" is a variable referencing a [ToolbarPanelList](ToolbarPanelList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ToolbarPanel](ToolbarPanel.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |