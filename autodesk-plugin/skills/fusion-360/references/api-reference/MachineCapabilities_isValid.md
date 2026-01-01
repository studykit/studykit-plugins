# MachineCapabilities.isValid Property

Parent Object: [MachineCapabilities](MachineCapabilities.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineCapabilities.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineCapabilities\_var" is a variable referencing a MachineCapabilities object. |

"machineCapabilities\_var" is a variable referencing a MachineCapabilities object. ```` ``` #include <Cam/Machine/MachineCapabilities.h>  // Get the value of the property. boolean propertyValue = machineCapabilities_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |