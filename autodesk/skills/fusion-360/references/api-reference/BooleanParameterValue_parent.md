# BooleanParameterValue.parent Property

Parent Object: [BooleanParameterValue](BooleanParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/BooleanParameterValue.h>

## Description

Get the parameter object that the value is associated with.

## Syntax

* [Python](#Python)
* [C++](#C++)

"booleanParameterValue\_var" is a variable referencing a BooleanParameterValue object. |

"booleanParameterValue\_var" is a variable referencing a BooleanParameterValue object. ```` ``` #include <Cam/Operations/BooleanParameterValue.h>  // Get the value of the property. Ptr<Base> propertyValue = booleanParameterValue_var->parent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |