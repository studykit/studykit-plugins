# Workspace.toolClipFilename Property

Parent Object: [Workspace](Workspace.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Workspace.h>

## Description

Gets or sets the full filename of the image file (PNG) used for the tool clip. the tool clip is the image shown when the user hovers the mouse over the workspace name in the workspace drop-down.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workspace\_var" is a variable referencing a Workspace object. |

"workspace\_var" is a variable referencing a Workspace object. ```` ``` #include <Core/UserInterface/Workspace.h>  // Get the value of the property. string propertyValue = workspace_var->toolClipFilename();  // Set the value of the property, where value_var is a string. bool returnValue = workspace_var->toolClipFilename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |