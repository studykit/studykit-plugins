# Workspace.tooltipDescription Property

Parent Object: [Workspace](Workspace.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Workspace.h>

## Description

Gets or sets the tooltip description displayed for the workspace. The tooltip description is a longer description of the workspace and is only displayed when the user hovers over the workspace name in the Fusion toolbar drop-down. The pop-up dialog that appears contains the tooltip, the tooltip description, and the tool clip which is a picture.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workspace\_var" is a variable referencing a Workspace object. |

"workspace\_var" is a variable referencing a Workspace object. ```` ``` #include <Core/UserInterface/Workspace.h>  // Get the value of the property. string propertyValue = workspace_var->tooltipDescription();  // Set the value of the property, where value_var is a string. bool returnValue = workspace_var->tooltipDescription(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |