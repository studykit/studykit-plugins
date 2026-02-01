# MachineFromFileInput.isValid Property

Parent Object: [MachineFromFileInput](MachineFromFileInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineFromFileInput.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineFromFileInput\_var" is a variable referencing a MachineFromFileInput object. |

"machineFromFileInput\_var" is a variable referencing a MachineFromFileInput object. ```` ``` #include <Cam/Machine/MachineFromFileInput.h>  // Get the value of the property. boolean propertyValue = machineFromFileInput_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |