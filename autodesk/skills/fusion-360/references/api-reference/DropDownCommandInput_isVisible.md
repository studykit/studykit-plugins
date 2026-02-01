# DropDownCommandInput.isVisible Property

Parent Object: [DropDownCommandInput](DropDownCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/DropDownCommandInput.h>

## Description

Gets or sets if this input will be visible to the user.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dropDownCommandInput\_var" is a variable referencing a DropDownCommandInput object.  ```` ``` # Get the value of the property. propertyValue = dropDownCommandInput_var.isVisible  # Set the value of the property. dropDownCommandInput_var.isVisible = propertyValue ``` ```` |

"dropDownCommandInput\_var" is a variable referencing a DropDownCommandInput object. ```` ``` #include <Core/UserInterface/DropDownCommandInput.h>  // Get the value of the property. boolean propertyValue = dropDownCommandInput_var->isVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = dropDownCommandInput_var->isVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |