# MachineAxisInput.axisType Property

Parent Object: [MachineAxisInput](MachineAxisInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineAxisInput.h>

## Description

The type of axis. This axis type determines which parameters of this object are valid to be accessed or modified.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAxisInput\_var" is a variable referencing a MachineAxisInput object. |

"machineAxisInput\_var" is a variable referencing a MachineAxisInput object. ```` ``` #include <Cam/Machine/MachineAxisInput.h>  // Get the value of the property. MachineAxisTypes propertyValue = machineAxisInput_var->axisType(); ``` ```` |

## Property Value

This is a read only property whose value is a [MachineAxisTypes](MachineAxisTypes.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |