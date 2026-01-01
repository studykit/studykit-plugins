# SliderCommandInput.unitType Property

Parent Object: [SliderCommandInput](SliderCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SliderCommandInput.h>

## Description

Gets and sets the unit type that is used when evaluating the user's input.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sliderCommandInput\_var" is a variable referencing a SliderCommandInput object. |

"sliderCommandInput\_var" is a variable referencing a SliderCommandInput object. ```` ``` #include <Core/UserInterface/SliderCommandInput.h>  // Get the value of the property. string propertyValue = sliderCommandInput_var->unitType();  // Set the value of the property, where value_var is a string. bool returnValue = sliderCommandInput_var->unitType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |