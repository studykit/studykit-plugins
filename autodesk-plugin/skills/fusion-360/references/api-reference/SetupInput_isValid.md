# SetupInput.isValid Property

Parent Object: [SetupInput](SetupInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/SetupInput.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setupInput\_var" is a variable referencing a SetupInput object. |

"setupInput\_var" is a variable referencing a SetupInput object. ```` ``` #include <Cam/CAM/SetupInput.h>  // Get the value of the property. boolean propertyValue = setupInput_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |