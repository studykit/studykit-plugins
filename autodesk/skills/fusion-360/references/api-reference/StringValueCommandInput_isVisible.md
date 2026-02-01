# StringValueCommandInput.isVisible Property

Parent Object: [StringValueCommandInput](StringValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/StringValueCommandInput.h>

## Description

Gets or sets if this input will be visible to the user.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stringValueCommandInput\_var" is a variable referencing a StringValueCommandInput object.  ```` ``` # Get the value of the property. propertyValue = stringValueCommandInput_var.isVisible  # Set the value of the property. stringValueCommandInput_var.isVisible = propertyValue ``` ```` |

"stringValueCommandInput\_var" is a variable referencing a StringValueCommandInput object. ```` ``` #include <Core/UserInterface/StringValueCommandInput.h>  // Get the value of the property. boolean propertyValue = stringValueCommandInput_var->isVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = stringValueCommandInput_var->isVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |