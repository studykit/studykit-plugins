# MachineSpindle.description Property

Parent Object: [MachineSpindle](MachineSpindle.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineSpindle.h>

## Description

The description of this spindle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineSpindle\_var" is a variable referencing a MachineSpindle object. |

"machineSpindle\_var" is a variable referencing a MachineSpindle object. ```` ``` #include <Cam/Machine/MachineSpindle.h>  // Get the value of the property. string propertyValue = machineSpindle_var->description();  // Set the value of the property, where value_var is a string. bool returnValue = machineSpindle_var->description(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |