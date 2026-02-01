# ToolbarControlList.itemById Method

Parent Object: [ToolbarControlList](ToolbarControlList.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarControlList.h>

## Description

Returns the ToolbarControl at the specified ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarControlList\_var" is a variable referencing a [ToolbarControlList](ToolbarControlList.htm) object.```` ``` returnValue = toolbarControlList_var.itemById(id) ``` ```` |

"toolbarControlList\_var" is a variable referencing a [ToolbarControlList](ToolbarControlList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ToolbarControl](ToolbarControl.htm) | Returns the ToolbarControl with the specified ID or null if no control has this ID. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The ID of the control within the collection to return. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |