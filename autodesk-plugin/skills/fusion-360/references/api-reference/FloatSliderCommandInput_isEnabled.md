# FloatSliderCommandInput.isEnabled Property

Parent Object: [FloatSliderCommandInput](FloatSliderCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/FloatSliderCommandInput.h>

## Description

Gets or sets if this input is currently enabled or disabled for user interaction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"floatSliderCommandInput\_var" is a variable referencing a FloatSliderCommandInput object.  ```` ``` # Get the value of the property. propertyValue = floatSliderCommandInput_var.isEnabled  # Set the value of the property. floatSliderCommandInput_var.isEnabled = propertyValue ``` ```` |

"floatSliderCommandInput\_var" is a variable referencing a FloatSliderCommandInput object. ```` ``` #include <Core/UserInterface/FloatSliderCommandInput.h>  // Get the value of the property. boolean propertyValue = floatSliderCommandInput_var->isEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = floatSliderCommandInput_var->isEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |