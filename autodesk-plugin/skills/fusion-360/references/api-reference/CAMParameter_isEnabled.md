# CAMParameter.isEnabled Property

Parent Object: [CAMParameter](CAMParameter.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/CAMParameter.h>

## Description

Gets if this parameter is enabled. Some parameters are enabled/disabled depending on the values set for other parameters.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMParameter\_var" is a variable referencing a CAMParameter object. |

"cAMParameter\_var" is a variable referencing a CAMParameter object. ```` ``` #include <Cam/Operations/CAMParameter.h>  // Get the value of the property. boolean propertyValue = cAMParameter_var->isEnabled(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |