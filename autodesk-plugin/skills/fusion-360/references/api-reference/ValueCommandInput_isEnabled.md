# ValueCommandInput.isEnabled Property

Parent Object: [ValueCommandInput](ValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ValueCommandInput.h>

## Description

Gets or sets if this input is currently enabled or disabled for user interaction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"valueCommandInput\_var" is a variable referencing a ValueCommandInput object.  ```` ``` # Get the value of the property. propertyValue = valueCommandInput_var.isEnabled  # Set the value of the property. valueCommandInput_var.isEnabled = propertyValue ``` ```` |

"valueCommandInput\_var" is a variable referencing a ValueCommandInput object. ```` ``` #include <Core/UserInterface/ValueCommandInput.h>  // Get the value of the property. boolean propertyValue = valueCommandInput_var->isEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = valueCommandInput_var->isEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |