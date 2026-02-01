# FloatSliderCommandInput.expressionTwo Property

Parent Object: [FloatSliderCommandInput](FloatSliderCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/FloatSliderCommandInput.h>

## Description

Uses an expression to set the value in the second input field. This can contain equations and is evaluated using the specified unit type.

## Syntax

* [Python](#Python)
* [C++](#C++)

"floatSliderCommandInput\_var" is a variable referencing a FloatSliderCommandInput object.  ```` ``` # Get the value of the property. propertyValue = floatSliderCommandInput_var.expressionTwo  # Set the value of the property. floatSliderCommandInput_var.expressionTwo = propertyValue ``` ```` |

"floatSliderCommandInput\_var" is a variable referencing a FloatSliderCommandInput object. ```` ``` #include <Core/UserInterface/FloatSliderCommandInput.h>  // Get the value of the property. string propertyValue = floatSliderCommandInput_var->expressionTwo();  // Set the value of the property, where value_var is a string. bool returnValue = floatSliderCommandInput_var->expressionTwo(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |