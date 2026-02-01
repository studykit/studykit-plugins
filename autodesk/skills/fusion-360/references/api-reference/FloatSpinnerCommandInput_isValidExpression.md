# FloatSpinnerCommandInput.isValidExpression Property

Parent Object: [FloatSpinnerCommandInput](FloatSpinnerCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/FloatSpinnerCommandInput.h>

## Description

Returns true if the current expression is valid and can be evaluated. If this is false, the value returned should be ignored because there currently is not a valid value.

## Syntax

* [Python](#Python)
* [C++](#C++)

"floatSpinnerCommandInput\_var" is a variable referencing a FloatSpinnerCommandInput object. |

"floatSpinnerCommandInput\_var" is a variable referencing a FloatSpinnerCommandInput object. ```` ``` #include <Core/UserInterface/FloatSpinnerCommandInput.h>  // Get the value of the property. boolean propertyValue = floatSpinnerCommandInput_var->isValidExpression(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |