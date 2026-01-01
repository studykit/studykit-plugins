# MachineAxisConfigurations.addLinear Method

Parent Object: [MachineAxisConfigurations](MachineAxisConfigurations.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineAxisConfigurations.h>

## Description

Add a new linear axis configuration for a kinematics part.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAxisConfigurations\_var" is a variable referencing a [MachineAxisConfigurations](MachineAxisConfigurations.htm) object.```` ``` returnValue = machineAxisConfigurations_var.addLinear(partId) ``` ```` |

"machineAxisConfigurations\_var" is a variable referencing a [MachineAxisConfigurations](MachineAxisConfigurations.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [LinearMachineAxisConfiguration](LinearMachineAxisConfiguration.htm) | Returns the newly created LinearMachineAxisConfiguration or null if creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| partId | string | ID used to label this axis configuration and link to a part in the kinematics tree. partID must match a part of type AxisMachinePartType in the kinematics tree and the part must be a linear axis. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |