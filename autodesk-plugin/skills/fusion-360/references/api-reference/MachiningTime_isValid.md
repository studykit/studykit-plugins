# MachiningTime.isValid Property

Parent Object: [MachiningTime](MachiningTime.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/MachiningTime.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machiningTime\_var" is a variable referencing a MachiningTime object. |

"machiningTime\_var" is a variable referencing a MachiningTime object. ```` ``` #include <Cam/CAM/MachiningTime.h>  // Get the value of the property. boolean propertyValue = machiningTime_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |