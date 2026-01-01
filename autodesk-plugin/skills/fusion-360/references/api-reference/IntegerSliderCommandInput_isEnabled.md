# IntegerSliderCommandInput.isEnabled Property

Parent Object: [IntegerSliderCommandInput](IntegerSliderCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/IntegerSliderCommandInput.h>

## Description

Gets or sets if this input is currently enabled or disabled for user interaction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"integerSliderCommandInput\_var" is a variable referencing an IntegerSliderCommandInput object.  ```` ``` # Get the value of the property. propertyValue = integerSliderCommandInput_var.isEnabled  # Set the value of the property. integerSliderCommandInput_var.isEnabled = propertyValue ``` ```` |

"integerSliderCommandInput\_var" is a variable referencing an IntegerSliderCommandInput object. ```` ``` #include <Core/UserInterface/IntegerSliderCommandInput.h>  // Get the value of the property. boolean propertyValue = integerSliderCommandInput_var->isEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = integerSliderCommandInput_var->isEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |