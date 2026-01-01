# SliderCommandInput.expressionTwo Property

Parent Object: [SliderCommandInput](SliderCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SliderCommandInput.h>

## Description

Uses an expression to set the value in the second input field. This can contain equations and is evaluated using the specified unit type.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sliderCommandInput\_var" is a variable referencing a SliderCommandInput object.  ```` ``` # Get the value of the property. propertyValue = sliderCommandInput_var.expressionTwo  # Set the value of the property. sliderCommandInput_var.expressionTwo = propertyValue ``` ```` |

"sliderCommandInput\_var" is a variable referencing a SliderCommandInput object. ```` ``` #include <Core/UserInterface/SliderCommandInput.h>  // Get the value of the property. string propertyValue = sliderCommandInput_var->expressionTwo();  // Set the value of the property, where value_var is a string. bool returnValue = sliderCommandInput_var->expressionTwo(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |