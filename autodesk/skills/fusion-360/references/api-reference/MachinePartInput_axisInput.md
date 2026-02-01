# MachinePartInput.axisInput Property

Parent Object: [MachinePartInput](MachinePartInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachinePartInput.h>

## Description

Gets or sets an axis input object to create a new MachineAxis with this part. Only valid when partType is Axis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machinePartInput\_var" is a variable referencing a MachinePartInput object. |

"machinePartInput\_var" is a variable referencing a MachinePartInput object. ```` ``` #include <Cam/Machine/MachinePartInput.h>  // Get the value of the property. Ptr<MachineAxisInput> propertyValue = machinePartInput_var->axisInput();  // Set the value of the property, where value_var is a MachineAxisInput. bool returnValue = machinePartInput_var->axisInput(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MachineAxisInput](MachineAxisInput.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |