# IntegerParameterValue.value Property

Parent Object: [IntegerParameterValue](IntegerParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/IntegerParameterValue.h>

## Description

Get or set the value of the parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"integerParameterValue\_var" is a variable referencing an IntegerParameterValue object. |

"integerParameterValue\_var" is a variable referencing an IntegerParameterValue object. ```` ``` #include <Cam/Operations/IntegerParameterValue.h>  // Get the value of the property. integer propertyValue = integerParameterValue_var->value();  // Set the value of the property, where value_var is an integer. bool returnValue = integerParameterValue_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |