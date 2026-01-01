# UserInterface.activeToolbarTab Property

Parent Object: [UserInterface](UserInterface.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterface.h>

## Description

Retrieve the active ToolbarTab being displayed in the user interface. This may be null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userInterface\_var" is a variable referencing a UserInterface object. |

"userInterface\_var" is a variable referencing a UserInterface object. ```` ``` #include <Core/UserInterface/UserInterface.h>  // Get the value of the property. Ptr<ToolbarTab> propertyValue = userInterface_var->activeToolbarTab(); ``` ```` |

## Property Value

This is a read only property whose value is a [ToolbarTab](ToolbarTab.htm).

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |