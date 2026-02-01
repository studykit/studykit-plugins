# ToolbarTab.index Property

Parent Object: [ToolbarTab](ToolbarTab.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarTab.h>

## Description

Gets the position this tab is in within the toolbar. The first tab is at position 0. This value is with respect to the complete list of tabs so this value could be outside of the expected range if you have a collection of tabs associated with a workspace, which is a subset of the entire list of tabs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarTab\_var" is a variable referencing a ToolbarTab object. |

"toolbarTab\_var" is a variable referencing a ToolbarTab object. ```` ``` #include <Core/UserInterface/ToolbarTab.h>  // Get the value of the property. uinteger propertyValue = toolbarTab_var->index(); ``` ```` |

## Property Value

This is a read only property whose value is a uinteger.

## Version

Introduced in version August 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |