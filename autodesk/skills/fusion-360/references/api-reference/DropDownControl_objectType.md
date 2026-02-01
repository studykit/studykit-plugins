# DropDownControl.objectType Property

Parent Object: [DropDownControl](DropDownControl.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/DropDownControl.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dropDownControl\_var" is a variable referencing a DropDownControl object.  ```` ``` # Get the value of the property. propertyValue = dropDownControl_var.objectType ``` ```` |

"dropDownControl\_var" is a variable referencing a DropDownControl object. ```` ``` #include <Core/UserInterface/DropDownControl.h>  // Get the value of the property. string propertyValue = dropDownControl_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |