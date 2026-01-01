# TableCommandInput.isVisible Property

Parent Object: [TableCommandInput](TableCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TableCommandInput.h>

## Description

Gets or sets if this input will be visible to the user.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tableCommandInput\_var" is a variable referencing a TableCommandInput object.  ```` ``` # Get the value of the property. propertyValue = tableCommandInput_var.isVisible  # Set the value of the property. tableCommandInput_var.isVisible = propertyValue ``` ```` |

"tableCommandInput\_var" is a variable referencing a TableCommandInput object. ```` ``` #include <Core/UserInterface/TableCommandInput.h>  // Get the value of the property. boolean propertyValue = tableCommandInput_var->isVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = tableCommandInput_var->isVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |