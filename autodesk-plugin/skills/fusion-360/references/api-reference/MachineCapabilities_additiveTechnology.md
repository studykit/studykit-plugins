# MachineCapabilities.additiveTechnology Property

Parent Object: [MachineCapabilities](MachineCapabilities.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineCapabilities.h>

## Description

Gets which additive technology the machine supports. Return "NA" if the machine does not support Additive

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineCapabilities\_var" is a variable referencing a MachineCapabilities object. |

"machineCapabilities\_var" is a variable referencing a MachineCapabilities object. ```` ``` #include <Cam/Machine/MachineCapabilities.h>  // Get the value of the property. AdditiveTechnologies propertyValue = machineCapabilities_var->additiveTechnology(); ``` ```` |

## Property Value

This is a read only property whose value is an [AdditiveTechnologies](AdditiveTechnologies.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |