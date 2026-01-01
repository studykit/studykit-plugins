# IntegerSpinnerCommandInput.isEnabled Property

Parent Object: [IntegerSpinnerCommandInput](IntegerSpinnerCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/IntegerSpinnerCommandInput.h>

## Description

Gets or sets if this input is currently enabled or disabled for user interaction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"integerSpinnerCommandInput\_var" is a variable referencing an IntegerSpinnerCommandInput object.  ```` ``` # Get the value of the property. propertyValue = integerSpinnerCommandInput_var.isEnabled  # Set the value of the property. integerSpinnerCommandInput_var.isEnabled = propertyValue ``` ```` |

"integerSpinnerCommandInput\_var" is a variable referencing an IntegerSpinnerCommandInput object. ```` ``` #include <Core/UserInterface/IntegerSpinnerCommandInput.h>  // Get the value of the property. boolean propertyValue = integerSpinnerCommandInput_var->isEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = integerSpinnerCommandInput_var->isEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |