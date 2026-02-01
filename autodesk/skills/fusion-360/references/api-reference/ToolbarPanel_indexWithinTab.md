# ToolbarPanel.indexWithinTab Method

Parent Object: [ToolbarPanel](ToolbarPanel.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarPanel.h>

## Description

Gets the position this panel is in within the toolbar tab. The first panel in the tab is at position 0.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarPanel\_var" is a variable referencing a [ToolbarPanel](ToolbarPanel.htm) object.```` ``` returnValue = toolbarPanel_var.indexWithinTab(tabId) ``` ```` |

"toolbarPanel\_var" is a variable referencing a [ToolbarPanel](ToolbarPanel.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| uinteger | Returns the index value of the panel within the tab. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| tabId | string |  |

## Version

Introduced in version August 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |