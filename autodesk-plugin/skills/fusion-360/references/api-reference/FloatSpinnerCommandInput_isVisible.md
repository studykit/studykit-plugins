# FloatSpinnerCommandInput.isVisible Property

Parent Object: [FloatSpinnerCommandInput](FloatSpinnerCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/FloatSpinnerCommandInput.h>

## Description

Gets or sets if this input will be visible to the user.

## Syntax

* [Python](#Python)
* [C++](#C++)

"floatSpinnerCommandInput\_var" is a variable referencing a FloatSpinnerCommandInput object.  ```` ``` # Get the value of the property. propertyValue = floatSpinnerCommandInput_var.isVisible  # Set the value of the property. floatSpinnerCommandInput_var.isVisible = propertyValue ``` ```` |

"floatSpinnerCommandInput\_var" is a variable referencing a FloatSpinnerCommandInput object. ```` ``` #include <Core/UserInterface/FloatSpinnerCommandInput.h>  // Get the value of the property. boolean propertyValue = floatSpinnerCommandInput_var->isVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = floatSpinnerCommandInput_var->isVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |