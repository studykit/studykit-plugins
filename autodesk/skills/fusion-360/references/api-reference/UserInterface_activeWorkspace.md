# UserInterface.activeWorkspace Property

Parent Object: [UserInterface](UserInterface.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterface.h>

## Description

Gets the active workspace. The active workspace is the one currently active in the user interface. This can be null if there is no active product.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userInterface\_var" is a variable referencing a UserInterface object. |

"userInterface\_var" is a variable referencing a UserInterface object. ```` ``` #include <Core/UserInterface/UserInterface.h>  // Get the value of the property. Ptr<Workspace> propertyValue = userInterface_var->activeWorkspace(); ``` ```` |

## Property Value

This is a read only property whose value is a [Workspace](Workspace.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |