# CommandControl.parent Property

Parent Object: [CommandControl](CommandControl.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandControl.h>

## Description

Gets the Parent object. When associated with a toolbar (right or left QAT or the NavBar) this returns the parent Toolbar object. When associated with a panel it returns the parent ToolbarPanel object. When associated with a control (DropDownControl) it returns the parent control.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandControl\_var" is a variable referencing a CommandControl object. |

"commandControl\_var" is a variable referencing a CommandControl object. ```` ``` #include <Core/UserInterface/CommandControl.h>  // Get the value of the property. Ptr<Base> propertyValue = commandControl_var->parent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |