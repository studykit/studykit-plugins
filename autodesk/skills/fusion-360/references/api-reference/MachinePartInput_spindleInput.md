# MachinePartInput.spindleInput Property

Parent Object: [MachinePartInput](MachinePartInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachinePartInput.h>

## Description

Gets or sets an spindle input object to create a new MachineSpindle with this part. Only valid when partType is not Axis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machinePartInput\_var" is a variable referencing a MachinePartInput object. |

"machinePartInput\_var" is a variable referencing a MachinePartInput object. ```` ``` #include <Cam/Machine/MachinePartInput.h>  // Get the value of the property. Ptr<MachineSpindleInput> propertyValue = machinePartInput_var->spindleInput();  // Set the value of the property, where value_var is a MachineSpindleInput. bool returnValue = machinePartInput_var->spindleInput(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MachineSpindleInput](MachineSpindleInput.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |