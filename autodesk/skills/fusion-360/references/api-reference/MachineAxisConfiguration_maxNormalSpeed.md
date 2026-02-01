# MachineAxisConfiguration.maxNormalSpeed Property

Parent Object: [MachineAxisConfiguration](MachineAxisConfiguration.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineAxisConfiguration.h>

## Description

Specifies the maximum normal speed for this axis. This would be called feedrate for a linear axis or rotary speed for a rotary axis. Units are cm/s for linear axes or rad/s for rotary axes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAxisConfiguration\_var" is a variable referencing a MachineAxisConfiguration object. |

"machineAxisConfiguration\_var" is a variable referencing a MachineAxisConfiguration object. ```` ``` #include <Cam/Machine/MachineAxisConfiguration.h>  // Get the value of the property. double propertyValue = machineAxisConfiguration_var->maxNormalSpeed();  // Set the value of the property, where value_var is a double. bool returnValue = machineAxisConfiguration_var->maxNormalSpeed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |