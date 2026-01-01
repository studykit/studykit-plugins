# FloatSliderCommandInput.minimumValue Property

Parent Object: [FloatSliderCommandInput](FloatSliderCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/FloatSliderCommandInput.h>

## Description

Gets and sets minimum value of the slider in database units. Gets a failure when set if the value of this command input was added by value list.

## Syntax

* [Python](#Python)
* [C++](#C++)

"floatSliderCommandInput\_var" is a variable referencing a FloatSliderCommandInput object. |

"floatSliderCommandInput\_var" is a variable referencing a FloatSliderCommandInput object. ```` ``` #include <Core/UserInterface/FloatSliderCommandInput.h>  // Get the value of the property. double propertyValue = floatSliderCommandInput_var->minimumValue();  // Set the value of the property, where value_var is a double. bool returnValue = floatSliderCommandInput_var->minimumValue(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |