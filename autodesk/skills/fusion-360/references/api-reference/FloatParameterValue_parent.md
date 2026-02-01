# FloatParameterValue.parent Property

Parent Object: [FloatParameterValue](FloatParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/FloatParameterValue.h>

## Description

Get the parameter object that the value is associated with.

## Syntax

* [Python](#Python)
* [C++](#C++)

"floatParameterValue\_var" is a variable referencing a FloatParameterValue object. |

"floatParameterValue\_var" is a variable referencing a FloatParameterValue object. ```` ``` #include <Cam/Operations/FloatParameterValue.h>  // Get the value of the property. Ptr<Base> propertyValue = floatParameterValue_var->parent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |