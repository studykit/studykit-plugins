# LinearMachineAxisConfiguration.maxRapidSpeed Property

Parent Object: [LinearMachineAxisConfiguration](LinearMachineAxisConfiguration.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/LinearMachineAxisConfiguration.h>

## Description

Specifies the maximum rapid speed for this axis. This would be called feedrate for a linear axis or rotary speed for a rotary axis. Units are cm/s for linear axes or rad/s for rotary axes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"linearMachineAxisConfiguration\_var" is a variable referencing a LinearMachineAxisConfiguration object. |

"linearMachineAxisConfiguration\_var" is a variable referencing a LinearMachineAxisConfiguration object. ```` ``` #include <Cam/Machine/LinearMachineAxisConfiguration.h>  // Get the value of the property. double propertyValue = linearMachineAxisConfiguration_var->maxRapidSpeed();  // Set the value of the property, where value_var is a double. bool returnValue = linearMachineAxisConfiguration_var->maxRapidSpeed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |