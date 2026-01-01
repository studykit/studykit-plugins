# CAMParameter.isValid Property

Parent Object: [CAMParameter](CAMParameter.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/CAMParameter.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMParameter\_var" is a variable referencing a CAMParameter object. |

"cAMParameter\_var" is a variable referencing a CAMParameter object. ```` ``` #include <Cam/Operations/CAMParameter.h>  // Get the value of the property. boolean propertyValue = cAMParameter_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |