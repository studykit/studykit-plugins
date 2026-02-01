# MachinePartInput.id Property

Parent Object: [MachinePartInput](MachinePartInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachinePartInput.h>

## Description

Gets or sets the internal ID of the part, used to reference this part for other operations. This ID can be any string. This must be unique with respect to other MachineParts in the Machine.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machinePartInput\_var" is a variable referencing a MachinePartInput object. |

"machinePartInput\_var" is a variable referencing a MachinePartInput object. ```` ``` #include <Cam/Machine/MachinePartInput.h>  // Get the value of the property. string propertyValue = machinePartInput_var->id();  // Set the value of the property, where value_var is a string. bool returnValue = machinePartInput_var->id(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |