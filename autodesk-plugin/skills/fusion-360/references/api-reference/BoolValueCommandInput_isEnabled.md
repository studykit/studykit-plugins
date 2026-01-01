# BoolValueCommandInput.isEnabled Property

Parent Object: [BoolValueCommandInput](BoolValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/BoolValueCommandInput.h>

## Description

Gets or sets if this input is currently enabled or disabled for user interaction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boolValueCommandInput\_var" is a variable referencing a BoolValueCommandInput object.  ```` ``` # Get the value of the property. propertyValue = boolValueCommandInput_var.isEnabled  # Set the value of the property. boolValueCommandInput_var.isEnabled = propertyValue ``` ```` |

"boolValueCommandInput\_var" is a variable referencing a BoolValueCommandInput object. ```` ``` #include <Core/UserInterface/BoolValueCommandInput.h>  // Get the value of the property. boolean propertyValue = boolValueCommandInput_var->isEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = boolValueCommandInput_var->isEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |