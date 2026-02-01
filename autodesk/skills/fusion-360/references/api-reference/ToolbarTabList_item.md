# ToolbarTabList.item Method

Parent Object: [ToolbarTabList](ToolbarTabList.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarTabList.h>

## Description

Returns the specified tab using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarTabList\_var" is a variable referencing a [ToolbarTabList](ToolbarTabList.htm) object.```` ``` returnValue = toolbarTabList_var.item(index) ``` ```` |

"toolbarTabList\_var" is a variable referencing a [ToolbarTabList](ToolbarTabList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ToolbarTab](ToolbarTab.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version August 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |