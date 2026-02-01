# FloatSliderCommandInput.isVisible Property

Parent Object: [FloatSliderCommandInput](FloatSliderCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/FloatSliderCommandInput.h>

## Description

Gets or sets if this input will be visible to the user.

## Syntax

* [Python](#Python)
* [C++](#C++)

"floatSliderCommandInput\_var" is a variable referencing a FloatSliderCommandInput object.  ```` ``` # Get the value of the property. propertyValue = floatSliderCommandInput_var.isVisible  # Set the value of the property. floatSliderCommandInput_var.isVisible = propertyValue ``` ```` |

"floatSliderCommandInput\_var" is a variable referencing a FloatSliderCommandInput object. ```` ``` #include <Core/UserInterface/FloatSliderCommandInput.h>  // Get the value of the property. boolean propertyValue = floatSliderCommandInput_var->isVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = floatSliderCommandInput_var->isVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |