# CAMLibrary.isValid Property

Parent Object: [CAMLibrary](CAMLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Global/CAMLibrary.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMLibrary\_var" is a variable referencing a CAMLibrary object. |

"cAMLibrary\_var" is a variable referencing a CAMLibrary object. ```` ``` #include <Cam/Global/CAMLibrary.h>  // Get the value of the property. boolean propertyValue = cAMLibrary_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |