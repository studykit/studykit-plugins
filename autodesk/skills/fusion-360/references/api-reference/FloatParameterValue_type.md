# FloatParameterValue.type Property

Parent Object: [FloatParameterValue](FloatParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/FloatParameterValue.h>

## Description

Get the type of the float parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"floatParameterValue\_var" is a variable referencing a FloatParameterValue object. |

"floatParameterValue\_var" is a variable referencing a FloatParameterValue object. ```` ``` #include <Cam/Operations/FloatParameterValue.h>  // Get the value of the property. FloatParameterValueTypes propertyValue = floatParameterValue_var->type(); ``` ```` |

## Property Value

This is a read only property whose value is a [FloatParameterValueTypes](FloatParameterValueTypes.htm).

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |