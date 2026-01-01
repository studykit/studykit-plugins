# Workspace.tooltip Property

Parent Object: [Workspace](Workspace.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Workspace.h>

## Description

Gets or sets the tooltip text displayed for the workspace. This is the first line of text shown when the user hovers over the workspace name in the Fusion toolbar drop-down. This is typically the name of the workspace. This is different from the name in the that the name is a short name shown in the drop-down. The tooltip is only shown when the user hovers over the name and box appears providing more information about the workspace. For example, the name of the model workspace is "Model" and the tooltip is "Model Workspace".

## Syntax

* [Python](#Python)
* [C++](#C++)

"workspace\_var" is a variable referencing a Workspace object. |

"workspace\_var" is a variable referencing a Workspace object. ```` ``` #include <Core/UserInterface/Workspace.h>  // Get the value of the property. string propertyValue = workspace_var->tooltip();  // Set the value of the property, where value_var is a string. bool returnValue = workspace_var->tooltip(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |