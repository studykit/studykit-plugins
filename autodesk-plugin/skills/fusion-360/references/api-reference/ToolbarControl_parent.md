# ToolbarControl.parent Property

Parent Object: [ToolbarControl](ToolbarControl.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarControl.h>

## Description

Gets the Parent object. When associated with a toolbar (right or left QAT or the NavBar) this returns the parent Toolbar object. When associated with a panel it returns the parent ToolbarPanel object. When associated with a control (DropDownControl) it returns the parent control.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarControl\_var" is a variable referencing a ToolbarControl object. |

"toolbarControl\_var" is a variable referencing a ToolbarControl object. ```` ``` #include <Core/UserInterface/ToolbarControl.h>  // Get the value of the property. Ptr<Base> propertyValue = toolbarControl_var->parent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |