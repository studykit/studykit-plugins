# DropDownControl.name Property

Parent Object: [DropDownControl](DropDownControl.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/DropDownControl.h>

## Description

Gets or sets the Name displayed for this drop down. This isn't used when the drop-down is in a toolbar because an icon is used in that case.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dropDownControl\_var" is a variable referencing a DropDownControl object. |

"dropDownControl\_var" is a variable referencing a DropDownControl object. ```` ``` #include <Core/UserInterface/DropDownControl.h>  // Get the value of the property. string propertyValue = dropDownControl_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = dropDownControl_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |