# MachineParts.createPartInput Method

Parent Object: [MachineParts](MachineParts.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineParts.h>

## Description

Create a new MachinePartInput.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineParts\_var" is a variable referencing a [MachineParts](MachineParts.htm) object.```` ``` returnValue = machineParts_var.createPartInput(partType) ``` ```` |

"machineParts\_var" is a variable referencing a [MachineParts](MachineParts.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MachinePartInput](MachinePartInput.htm) | Returns the new MachinePartInput or null if creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| partType | [MachinePartTypes](MachinePartTypes.htm) | The type of part to create. When this parameter is Axis, you must set a value for axisInput. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |