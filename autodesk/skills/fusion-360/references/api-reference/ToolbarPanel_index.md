# ToolbarPanel.index Property

Parent Object: [ToolbarPanel](ToolbarPanel.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarPanel.h>

## Description

Gets the position this panel is in within the toolbar. The first panel is at position 0. This value is with respect to the complete list of panels so this value could be outside of the expected range if you have a collection of panels associated with a workspace, which is a subset of the entire list of panels.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarPanel\_var" is a variable referencing a ToolbarPanel object. |

"toolbarPanel\_var" is a variable referencing a ToolbarPanel object. ```` ``` #include <Core/UserInterface/ToolbarPanel.h>  // Get the value of the property. uinteger propertyValue = toolbarPanel_var->index(); ``` ```` |

## Property Value

This is a read only property whose value is a uinteger.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |