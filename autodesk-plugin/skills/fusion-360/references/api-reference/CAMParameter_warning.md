# CAMParameter.warning Property

Parent Object: [CAMParameter](CAMParameter.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/CAMParameter.h>

## Description

Returns a message corresponding to any active warning associated with the value of this parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMParameter\_var" is a variable referencing a CAMParameter object. |

"cAMParameter\_var" is a variable referencing a CAMParameter object. ```` ``` #include <Cam/Operations/CAMParameter.h>  // Get the value of the property. string propertyValue = cAMParameter_var->warning(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |