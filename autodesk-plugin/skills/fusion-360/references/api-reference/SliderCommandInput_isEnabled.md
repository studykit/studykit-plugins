# SliderCommandInput.isEnabled Property

Parent Object: [SliderCommandInput](SliderCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SliderCommandInput.h>

## Description

Gets or sets if this input is currently enabled or disabled for user interaction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sliderCommandInput\_var" is a variable referencing a SliderCommandInput object.  ```` ``` # Get the value of the property. propertyValue = sliderCommandInput_var.isEnabled  # Set the value of the property. sliderCommandInput_var.isEnabled = propertyValue ``` ```` |

"sliderCommandInput\_var" is a variable referencing a SliderCommandInput object. ```` ``` #include <Core/UserInterface/SliderCommandInput.h>  // Get the value of the property. boolean propertyValue = sliderCommandInput_var->isEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = sliderCommandInput_var->isEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |