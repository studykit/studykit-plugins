# MachinePartInput.partType Property

Parent Object: [MachinePartInput](MachinePartInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachinePartInput.h>

## Description

Get the type of part this input will create.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machinePartInput\_var" is a variable referencing a MachinePartInput object. |

"machinePartInput\_var" is a variable referencing a MachinePartInput object. ```` ``` #include <Cam/Machine/MachinePartInput.h>  // Get the value of the property. MachinePartTypes propertyValue = machinePartInput_var->partType(); ``` ```` |

## Property Value

This is a read only property whose value is a [MachinePartTypes](MachinePartTypes.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |