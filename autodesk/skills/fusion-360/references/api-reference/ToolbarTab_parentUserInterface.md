# ToolbarTab.parentUserInterface Property

Parent Object: [ToolbarTab](ToolbarTab.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarTab.h>

## Description

Gets the parent UserInterface object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarTab\_var" is a variable referencing a ToolbarTab object. |

"toolbarTab\_var" is a variable referencing a ToolbarTab object. ```` ``` #include <Core/UserInterface/ToolbarTab.h>  // Get the value of the property. Ptr<UserInterface> propertyValue = toolbarTab_var->parentUserInterface(); ``` ```` |

## Property Value

This is a read only property whose value is a [UserInterface](UserInterface.htm).

## Version

Introduced in version August 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |