# LinearMachineAxisConfiguration.isReversed Property

Parent Object: [LinearMachineAxisConfiguration](LinearMachineAxisConfiguration.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/LinearMachineAxisConfiguration.h>

## Description

Does the axis move in the opposite direction to usual. For rotary axes this would mean it uses the left hand rule, and for linear axes is moves in the opposite direction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"linearMachineAxisConfiguration\_var" is a variable referencing a LinearMachineAxisConfiguration object. |

"linearMachineAxisConfiguration\_var" is a variable referencing a LinearMachineAxisConfiguration object. ```` ``` #include <Cam/Machine/LinearMachineAxisConfiguration.h>  // Get the value of the property. boolean propertyValue = linearMachineAxisConfiguration_var->isReversed();  // Set the value of the property, where value_var is a boolean. bool returnValue = linearMachineAxisConfiguration_var->isReversed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |