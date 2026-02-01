# BooleanParameterValue.isValid Property

Parent Object: [BooleanParameterValue](BooleanParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/BooleanParameterValue.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"booleanParameterValue\_var" is a variable referencing a BooleanParameterValue object. |

"booleanParameterValue\_var" is a variable referencing a BooleanParameterValue object. ```` ``` #include <Cam/Operations/BooleanParameterValue.h>  // Get the value of the property. boolean propertyValue = booleanParameterValue_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |