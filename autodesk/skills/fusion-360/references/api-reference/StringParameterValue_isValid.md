# StringParameterValue.isValid Property

Parent Object: [StringParameterValue](StringParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/StringParameterValue.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stringParameterValue\_var" is a variable referencing a StringParameterValue object. |

"stringParameterValue\_var" is a variable referencing a StringParameterValue object. ```` ``` #include <Cam/Operations/StringParameterValue.h>  // Get the value of the property. boolean propertyValue = stringParameterValue_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |