# NCPrograms.isValid Property

Parent Object: [NCPrograms](NCPrograms.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/NCProgram/NCPrograms.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nCPrograms\_var" is a variable referencing a NCPrograms object. |

"nCPrograms\_var" is a variable referencing a NCPrograms object. ```` ``` #include <Cam/NCProgram/NCPrograms.h>  // Get the value of the property. boolean propertyValue = nCPrograms_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |