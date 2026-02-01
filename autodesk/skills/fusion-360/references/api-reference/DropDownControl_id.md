# DropDownControl.id Property

Parent Object: [DropDownControl](DropDownControl.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/DropDownControl.h>

## Description

Gets the unique ID of this control. The ID is unique with respect to the other controls within the same panel, toolbar, or drop-down control.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dropDownControl\_var" is a variable referencing a DropDownControl object. |

"dropDownControl\_var" is a variable referencing a DropDownControl object. ```` ``` #include <Core/UserInterface/DropDownControl.h>  // Get the value of the property. string propertyValue = dropDownControl_var->id(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |