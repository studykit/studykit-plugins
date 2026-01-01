# FloatSliderCommandInput.spinStep Property

Parent Object: [FloatSliderCommandInput](FloatSliderCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/FloatSliderCommandInput.h>

## Description

Gets and sets the spin step value in the unit type set by the unitType argument. The value should be more than zero. This is the amount the slider will advance when the user clicks the spin button beside the value.

## Syntax

* [Python](#Python)
* [C++](#C++)

"floatSliderCommandInput\_var" is a variable referencing a FloatSliderCommandInput object. |

"floatSliderCommandInput\_var" is a variable referencing a FloatSliderCommandInput object. ```` ``` #include <Core/UserInterface/FloatSliderCommandInput.h>  // Get the value of the property. double propertyValue = floatSliderCommandInput_var->spinStep();  // Set the value of the property, where value_var is a double. bool returnValue = floatSliderCommandInput_var->spinStep(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |