# ToolbarControlList.item Method

Parent Object: [ToolbarControlList](ToolbarControlList.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarControlList.h>

## Description

Returns the ToolbarControl at the specified index. When iterating by index, the controls are returned in the same order as they are shown in the user interface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarControlList\_var" is a variable referencing a [ToolbarControlList](ToolbarControlList.htm) object.```` ``` returnValue = toolbarControlList_var.item(index) ``` ```` |

"toolbarControlList\_var" is a variable referencing a [ToolbarControlList](ToolbarControlList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ToolbarControl](ToolbarControl.htm) | Returns the ToolbarControl at the specified index or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the control within the collection to return. The first item in the collection has in index of 0. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |