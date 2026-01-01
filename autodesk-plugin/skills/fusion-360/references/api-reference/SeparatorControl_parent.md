# SeparatorControl.parent Property

Parent Object: [SeparatorControl](SeparatorControl.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SeparatorControl.h>

## Description

Gets the Parent object. When associated with a toolbar (right or left QAT or the NavBar) this returns the parent Toolbar object. When associated with a panel it returns the parent ToolbarPanel object. When associated with a control (DropDownControl) it returns the parent control.

## Syntax

* [Python](#Python)
* [C++](#C++)

"separatorControl\_var" is a variable referencing a SeparatorControl object. |

"separatorControl\_var" is a variable referencing a SeparatorControl object. ```` ``` #include <Core/UserInterface/SeparatorControl.h>  // Get the value of the property. Ptr<Base> propertyValue = separatorControl_var->parent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| Â© Copyright 2025 Autodesk, Inc. | Comment on this page. |