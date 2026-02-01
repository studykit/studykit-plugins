# CommandInput.isVisible Property

Parent Object: [CommandInput](CommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandInput.h>

## Description

Gets or sets if this input will be visible to the user.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandInput\_var" is a variable referencing a CommandInput object.  ```` ``` # Get the value of the property. propertyValue = commandInput_var.isVisible  # Set the value of the property. commandInput_var.isVisible = propertyValue ``` ```` |

"commandInput\_var" is a variable referencing a CommandInput object. ```` ``` #include <Core/UserInterface/CommandInput.h>  // Get the value of the property. boolean propertyValue = commandInput_var->isVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = commandInput_var->isVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |