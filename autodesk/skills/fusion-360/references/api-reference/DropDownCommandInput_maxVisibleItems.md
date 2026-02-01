# DropDownCommandInput.maxVisibleItems Property

Parent Object: [DropDownCommandInput](DropDownCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/DropDownCommandInput.h>

## Description

Gets or sets the maximum allowed size on screen of the drop down list, measured in items.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dropDownCommandInput\_var" is a variable referencing a DropDownCommandInput object. |

"dropDownCommandInput\_var" is a variable referencing a DropDownCommandInput object. ```` ``` #include <Core/UserInterface/DropDownCommandInput.h>  // Get the value of the property. integer propertyValue = dropDownCommandInput_var->maxVisibleItems();  // Set the value of the property, where value_var is an integer. bool returnValue = dropDownCommandInput_var->maxVisibleItems(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |