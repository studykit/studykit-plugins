# StringParameterValue.parent Property

Parent Object: [StringParameterValue](StringParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/StringParameterValue.h>

## Description

Get the parameter object that the value is associated with.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stringParameterValue\_var" is a variable referencing a StringParameterValue object. |

"stringParameterValue\_var" is a variable referencing a StringParameterValue object. ```` ``` #include <Cam/Operations/StringParameterValue.h>  // Get the value of the property. Ptr<Base> propertyValue = stringParameterValue_var->parent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |