# MachineAxisInput.name Property

Parent Object: [MachineAxisInput](MachineAxisInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineAxisInput.h>

## Description

The user facing name of this axis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAxisInput\_var" is a variable referencing a MachineAxisInput object. |

"machineAxisInput\_var" is a variable referencing a MachineAxisInput object. ```` ``` #include <Cam/Machine/MachineAxisInput.h>  // Get the value of the property. string propertyValue = machineAxisInput_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = machineAxisInput_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |