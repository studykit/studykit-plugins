# CAMManager.isValid Property

Parent Object: [CAMManager](CAMManager.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Global/CAMManager.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMManager\_var" is a variable referencing a CAMManager object. |

"cAMManager\_var" is a variable referencing a CAMManager object. ```` ``` #include <Cam/Global/CAMManager.h>  // Get the value of the property. boolean propertyValue = cAMManager_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |