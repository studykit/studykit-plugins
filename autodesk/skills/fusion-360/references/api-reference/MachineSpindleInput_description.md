# MachineSpindleInput.description Property

Parent Object: [MachineSpindleInput](MachineSpindleInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineSpindleInput.h>

## Description

The description of this spindle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineSpindleInput\_var" is a variable referencing a MachineSpindleInput object. |

"machineSpindleInput\_var" is a variable referencing a MachineSpindleInput object. ```` ``` #include <Cam/Machine/MachineSpindleInput.h>  // Get the value of the property. string propertyValue = machineSpindleInput_var->description();  // Set the value of the property, where value_var is a string. bool returnValue = machineSpindleInput_var->description(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |