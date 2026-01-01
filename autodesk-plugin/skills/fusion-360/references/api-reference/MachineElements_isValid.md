# MachineElements.isValid Property

Parent Object: [MachineElements](MachineElements.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineElements.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineElements\_var" is a variable referencing a MachineElements object. |

"machineElements\_var" is a variable referencing a MachineElements object. ```` ``` #include <Cam/Machine/MachineElements.h>  // Get the value of the property. boolean propertyValue = machineElements_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |