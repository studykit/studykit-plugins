# CAMPatterns.isValid Property

Parent Object: [CAMPatterns](CAMPatterns.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMPatterns.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMPatterns\_var" is a variable referencing a CAMPatterns object. |

"cAMPatterns\_var" is a variable referencing a CAMPatterns object. ```` ``` #include <Cam/CAM/CAMPatterns.h>  // Get the value of the property. boolean propertyValue = cAMPatterns_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |