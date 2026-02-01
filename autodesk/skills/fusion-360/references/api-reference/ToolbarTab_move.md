# ToolbarTab.move Method

Parent Object: [ToolbarTab](ToolbarTab.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarTab.h>

## Description

Move this tab to a different position in the Toolbar in the user interface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarTab\_var" is a variable referencing a [ToolbarTab](ToolbarTab.htm) object.```` ``` returnValue = toolbarTab_var.move(positionId, isBefore) ``` ```` |

"toolbarTab\_var" is a variable referencing a [ToolbarTab](ToolbarTab.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if it was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| positionId | string | The ID of another ToolbarTab in the same Toolbar that is used to position this tab. This tab will be positioned either directly before or after it. |
| isBefore | boolean | If true, then this tab will be positioned directly before the tab indicated by positionID. If false, then this tab will be positioned after it. |

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |