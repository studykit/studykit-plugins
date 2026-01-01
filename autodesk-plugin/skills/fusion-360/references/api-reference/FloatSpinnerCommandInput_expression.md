# FloatSpinnerCommandInput.expression Property

Parent Object: [FloatSpinnerCommandInput](FloatSpinnerCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/FloatSpinnerCommandInput.h>

## Description

Gets or sets the expression displayed in the input field. This can contain equations and references to parameters. It is evaluated using the specified unit type.

## Syntax

* [Python](#Python)
* [C++](#C++)

"floatSpinnerCommandInput\_var" is a variable referencing a FloatSpinnerCommandInput object. |

"floatSpinnerCommandInput\_var" is a variable referencing a FloatSpinnerCommandInput object. ```` ``` #include <Core/UserInterface/FloatSpinnerCommandInput.h>  // Get the value of the property. string propertyValue = floatSpinnerCommandInput_var->expression();  // Set the value of the property, where value_var is a string. bool returnValue = floatSpinnerCommandInput_var->expression(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |