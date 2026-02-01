# Workspace.toolbarPanels Property

Parent Object: [Workspace](Workspace.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Workspace.h>

## Description

Gets the collection containing the panels associated with this workspace. It's through this collection that you can add new toolbar panels.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workspace\_var" is a variable referencing a Workspace object. |

"workspace\_var" is a variable referencing a Workspace object. ```` ``` #include <Core/UserInterface/Workspace.h>  // Get the value of the property. Ptr<ToolbarPanels> propertyValue = workspace_var->toolbarPanels(); ``` ```` |

## Property Value

This is a read only property whose value is a [ToolbarPanels](ToolbarPanels.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |