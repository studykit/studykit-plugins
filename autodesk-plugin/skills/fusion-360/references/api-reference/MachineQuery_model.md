# MachineQuery.model Property

Parent Object: [MachineQuery](MachineQuery.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineQuery.h>

## Description

The case-insensitive model specifies the model of the machine. The default empty model applies to all machines.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineQuery\_var" is a variable referencing a MachineQuery object. |

"machineQuery\_var" is a variable referencing a MachineQuery object. ```` ``` #include <Cam/Machine/MachineQuery.h>  // Get the value of the property. string propertyValue = machineQuery_var->model();  // Set the value of the property, where value_var is a string. bool returnValue = machineQuery_var->model(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |