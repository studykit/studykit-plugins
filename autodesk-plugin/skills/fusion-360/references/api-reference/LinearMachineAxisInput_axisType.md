# LinearMachineAxisInput.axisType Property

Parent Object: [LinearMachineAxisInput](LinearMachineAxisInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/LinearMachineAxisInput.h>

## Description

The type of axis. This axis type determines which parameters of this object are valid to be accessed or modified.

## Syntax

* [Python](#Python)
* [C++](#C++)

"linearMachineAxisInput\_var" is a variable referencing a LinearMachineAxisInput object. |

"linearMachineAxisInput\_var" is a variable referencing a LinearMachineAxisInput object. ```` ``` #include <Cam/Machine/LinearMachineAxisInput.h>  // Get the value of the property. MachineAxisTypes propertyValue = linearMachineAxisInput_var->axisType(); ``` ```` |

## Property Value

This is a read only property whose value is a [MachineAxisTypes](MachineAxisTypes.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |