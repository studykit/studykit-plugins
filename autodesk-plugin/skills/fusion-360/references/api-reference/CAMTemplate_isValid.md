# CAMTemplate.isValid Property

Parent Object: [CAMTemplate](CAMTemplate.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAMTemplate/CAMTemplate.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMTemplate\_var" is a variable referencing a CAMTemplate object. |

"cAMTemplate\_var" is a variable referencing a CAMTemplate object. ```` ``` #include <Cam/CAMTemplate/CAMTemplate.h>  // Get the value of the property. boolean propertyValue = cAMTemplate_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |