# IntegerParameterValue.isValid Property

Parent Object: [IntegerParameterValue](IntegerParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/IntegerParameterValue.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"integerParameterValue\_var" is a variable referencing an IntegerParameterValue object. |

"integerParameterValue\_var" is a variable referencing an IntegerParameterValue object. ```` ``` #include <Cam/Operations/IntegerParameterValue.h>  // Get the value of the property. boolean propertyValue = integerParameterValue_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |