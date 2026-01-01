# Workspace.isNative Property

Parent Object: [Workspace](Workspace.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Workspace.h>

## Description

Gets if this workspace is native to Fusion or was created via the API.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workspace\_var" is a variable referencing a Workspace object. |

"workspace\_var" is a variable referencing a Workspace object. ```` ``` #include <Core/UserInterface/Workspace.h>  // Get the value of the property. boolean propertyValue = workspace_var->isNative(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |