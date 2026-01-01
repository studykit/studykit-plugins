# IntegerSliderCommandInput.expressionTwo Property

Parent Object: [IntegerSliderCommandInput](IntegerSliderCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/IntegerSliderCommandInput.h>

## Description

Uses an expression to set the value in the second input field. This can contain equations and is evaluated using the specified unit type.

## Syntax

* [Python](#Python)
* [C++](#C++)

"integerSliderCommandInput\_var" is a variable referencing an IntegerSliderCommandInput object.  ```` ``` # Get the value of the property. propertyValue = integerSliderCommandInput_var.expressionTwo  # Set the value of the property. integerSliderCommandInput_var.expressionTwo = propertyValue ``` ```` |

"integerSliderCommandInput\_var" is a variable referencing an IntegerSliderCommandInput object. ```` ``` #include <Core/UserInterface/IntegerSliderCommandInput.h>  // Get the value of the property. string propertyValue = integerSliderCommandInput_var->expressionTwo();  // Set the value of the property, where value_var is a string. bool returnValue = integerSliderCommandInput_var->expressionTwo(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |