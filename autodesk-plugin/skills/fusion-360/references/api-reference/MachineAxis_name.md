# MachineAxis.name Property

Parent Object: [MachineAxis](MachineAxis.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineAxis.h>

## Description

The name of this axis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAxis\_var" is a variable referencing a MachineAxis object. |

"machineAxis\_var" is a variable referencing a MachineAxis object. ```` ``` #include <Cam/Machine/MachineAxis.h>  // Get the value of the property. string propertyValue = machineAxis_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = machineAxis_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |