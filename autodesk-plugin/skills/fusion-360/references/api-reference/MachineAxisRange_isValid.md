# MachineAxisRange.isValid Property

Parent Object: [MachineAxisRange](MachineAxisRange.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineAxisRange.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAxisRange\_var" is a variable referencing a MachineAxisRange object. |

"machineAxisRange\_var" is a variable referencing a MachineAxisRange object. ```` ``` #include <Cam/Machine/MachineAxisRange.h>  // Get the value of the property. boolean propertyValue = machineAxisRange_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |