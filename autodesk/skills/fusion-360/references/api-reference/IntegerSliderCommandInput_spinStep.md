# IntegerSliderCommandInput.spinStep Property

Parent Object: [IntegerSliderCommandInput](IntegerSliderCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/IntegerSliderCommandInput.h>

## Description

Gets and sets the spin step. This defines the amount the slider moves when the user clicks the spin button beside the value. The spin step should be more than zero.

## Syntax

* [Python](#Python)
* [C++](#C++)

"integerSliderCommandInput\_var" is a variable referencing an IntegerSliderCommandInput object. |

"integerSliderCommandInput\_var" is a variable referencing an IntegerSliderCommandInput object. ```` ``` #include <Core/UserInterface/IntegerSliderCommandInput.h>  // Get the value of the property. uinteger propertyValue = integerSliderCommandInput_var->spinStep();  // Set the value of the property, where value_var is a uinteger. bool returnValue = integerSliderCommandInput_var->spinStep(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a uinteger.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |