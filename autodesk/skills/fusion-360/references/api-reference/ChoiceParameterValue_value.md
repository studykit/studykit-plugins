# ChoiceParameterValue.value Property

Parent Object: [ChoiceParameterValue](ChoiceParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/ChoiceParameterValue.h>

## Description

Get or set the value of the parameter. This value will correspond to one of the available values of the parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"choiceParameterValue\_var" is a variable referencing a ChoiceParameterValue object. |

"choiceParameterValue\_var" is a variable referencing a ChoiceParameterValue object. ```` ``` #include <Cam/Operations/ChoiceParameterValue.h>  // Get the value of the property. string propertyValue = choiceParameterValue_var->value();  // Set the value of the property, where value_var is a string. bool returnValue = choiceParameterValue_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |