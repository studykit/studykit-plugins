# Workspace.productType Property

Parent Object: [Workspace](Workspace.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Workspace.h>

## Description

Returns the name of the product this workspace is associated with.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workspace\_var" is a variable referencing a Workspace object. |

"workspace\_var" is a variable referencing a Workspace object. ```` ``` #include <Core/UserInterface/Workspace.h>  // Get the value of the property. string propertyValue = workspace_var->productType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |