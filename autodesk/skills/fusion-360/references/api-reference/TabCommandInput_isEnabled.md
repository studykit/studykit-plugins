# TabCommandInput.isEnabled Property

Parent Object: [TabCommandInput](TabCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TabCommandInput.h>

## Description

Gets or sets if this input is currently enabled or disabled for user interaction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tabCommandInput\_var" is a variable referencing a TabCommandInput object.  ```` ``` # Get the value of the property. propertyValue = tabCommandInput_var.isEnabled  # Set the value of the property. tabCommandInput_var.isEnabled = propertyValue ``` ```` |

"tabCommandInput\_var" is a variable referencing a TabCommandInput object. ```` ``` #include <Core/UserInterface/TabCommandInput.h>  // Get the value of the property. boolean propertyValue = tabCommandInput_var->isEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = tabCommandInput_var->isEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |