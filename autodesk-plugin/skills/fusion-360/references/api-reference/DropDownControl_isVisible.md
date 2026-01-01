# DropDownControl.isVisible Property

Parent Object: [DropDownControl](DropDownControl.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/DropDownControl.h>

## Description

Gets or sets if this control is currently visible.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dropDownControl\_var" is a variable referencing a DropDownControl object. |

"dropDownControl\_var" is a variable referencing a DropDownControl object. ```` ``` #include <Core/UserInterface/DropDownControl.h>  // Get the value of the property. boolean propertyValue = dropDownControl_var->isVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = dropDownControl_var->isVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |