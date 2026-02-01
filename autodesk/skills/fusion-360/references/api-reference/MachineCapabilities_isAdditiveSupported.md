# MachineCapabilities.isAdditiveSupported Property

Parent Object: [MachineCapabilities](MachineCapabilities.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineCapabilities.h>

## Description

Gets and sets if the machine is capable of additive operations.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineCapabilities\_var" is a variable referencing a MachineCapabilities object. |

"machineCapabilities\_var" is a variable referencing a MachineCapabilities object. ```` ``` #include <Cam/Machine/MachineCapabilities.h>  // Get the value of the property. boolean propertyValue = machineCapabilities_var->isAdditiveSupported();  // Set the value of the property, where value_var is a boolean. bool returnValue = machineCapabilities_var->isAdditiveSupported(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |