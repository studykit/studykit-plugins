# FloatSliderCommandInput.valueList Property

Parent Object: [FloatSliderCommandInput](FloatSliderCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/FloatSliderCommandInput.h>

## Description

Gets the value list of the slider. This property is valid when this input represents a list type of slider command input. Otherwise an empty list will be returned.

## Syntax

* [Python](#Python)
* [C++](#C++)

"floatSliderCommandInput\_var" is a variable referencing a FloatSliderCommandInput object. |

"floatSliderCommandInput\_var" is a variable referencing a FloatSliderCommandInput object. ```` ``` #include <Core/UserInterface/FloatSliderCommandInput.h>  // Get the value of the property. std::vector<double> propertyValue = floatSliderCommandInput_var->valueList(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type double.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |