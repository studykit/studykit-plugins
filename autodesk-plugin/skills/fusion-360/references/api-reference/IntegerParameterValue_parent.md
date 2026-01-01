# IntegerParameterValue.parent Property

Parent Object: [IntegerParameterValue](IntegerParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/IntegerParameterValue.h>

## Description

Get the parameter object that the value is associated with.

## Syntax

* [Python](#Python)
* [C++](#C++)

"integerParameterValue\_var" is a variable referencing an IntegerParameterValue object. |

"integerParameterValue\_var" is a variable referencing an IntegerParameterValue object. ```` ``` #include <Cam/Operations/IntegerParameterValue.h>  // Get the value of the property. Ptr<Base> propertyValue = integerParameterValue_var->parent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |