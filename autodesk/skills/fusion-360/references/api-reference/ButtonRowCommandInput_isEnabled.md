# ButtonRowCommandInput.isEnabled Property

Parent Object: [ButtonRowCommandInput](ButtonRowCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ButtonRowCommandInput.h>

## Description

Gets or sets if this input is currently enabled or disabled for user interaction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"buttonRowCommandInput\_var" is a variable referencing a ButtonRowCommandInput object.  ```` ``` # Get the value of the property. propertyValue = buttonRowCommandInput_var.isEnabled  # Set the value of the property. buttonRowCommandInput_var.isEnabled = propertyValue ``` ```` |

"buttonRowCommandInput\_var" is a variable referencing a ButtonRowCommandInput object. ```` ``` #include <Core/UserInterface/ButtonRowCommandInput.h>  // Get the value of the property. boolean propertyValue = buttonRowCommandInput_var->isEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = buttonRowCommandInput_var->isEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |