# MachineQuery.isValid Property

Parent Object: [MachineQuery](MachineQuery.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineQuery.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineQuery\_var" is a variable referencing a MachineQuery object. |

"machineQuery\_var" is a variable referencing a MachineQuery object. ```` ``` #include <Cam/Machine/MachineQuery.h>  // Get the value of the property. boolean propertyValue = machineQuery_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |