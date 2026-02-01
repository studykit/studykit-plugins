# MachineSpindle.maxSpeed Property

Parent Object: [MachineSpindle](MachineSpindle.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineSpindle.h>

## Description

Specifies the maximum speed (rpm) for this spindle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineSpindle\_var" is a variable referencing a MachineSpindle object. |

"machineSpindle\_var" is a variable referencing a MachineSpindle object. ```` ``` #include <Cam/Machine/MachineSpindle.h>  // Get the value of the property. double propertyValue = machineSpindle_var->maxSpeed();  // Set the value of the property, where value_var is a double. bool returnValue = machineSpindle_var->maxSpeed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |