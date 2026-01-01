# IntegerSpinnerCommandInput.spinStep Property

Parent Object: [IntegerSpinnerCommandInput](IntegerSpinnerCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/IntegerSpinnerCommandInput.h>

## Description

Gets the spin step. The value should be more than zero. This is the amount the spinner will advance when the user clicks the spin button beside the value.

## Syntax

* [Python](#Python)
* [C++](#C++)

"integerSpinnerCommandInput\_var" is a variable referencing an IntegerSpinnerCommandInput object. |

"integerSpinnerCommandInput\_var" is a variable referencing an IntegerSpinnerCommandInput object. ```` ``` #include <Core/UserInterface/IntegerSpinnerCommandInput.h>  // Get the value of the property. uinteger propertyValue = integerSpinnerCommandInput_var->spinStep(); ``` ```` |

## Property Value

This is a read only property whose value is a uinteger.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |