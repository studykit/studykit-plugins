# MachinePartInput.createAxisInput Method

Parent Object: [MachinePartInput](MachinePartInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachinePartInput.h>

## Description

Creates a new MachineAxisInput object to be used to create a new MachineAxis. Set this object on to an axis type MachinePartInput to create a new MachineAxis with that part.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machinePartInput\_var" is a variable referencing a [MachinePartInput](MachinePartInput.htm) object.```` ``` returnValue = machinePartInput_var.createAxisInput(axisType) ``` ```` |

"machinePartInput\_var" is a variable referencing a [MachinePartInput](MachinePartInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MachineAxisInput](MachineAxisInput.htm) | Returns a LinearMachineAxisInput or RotaryMachineAxisInput, or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| axisType | [MachineAxisTypes](MachineAxisTypes.htm) | The type of MachineAxisInput to create. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |