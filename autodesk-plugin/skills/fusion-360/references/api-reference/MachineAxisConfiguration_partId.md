# MachineAxisConfiguration.partId Property

Parent Object: [MachineAxisConfiguration](MachineAxisConfiguration.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineAxisConfiguration.h>

## Description

ID of the part in the KinematicsMachineElement that this axis configuration modifies.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAxisConfiguration\_var" is a variable referencing a MachineAxisConfiguration object. |

"machineAxisConfiguration\_var" is a variable referencing a MachineAxisConfiguration object. ```` ``` #include <Cam/Machine/MachineAxisConfiguration.h>  // Get the value of the property. string propertyValue = machineAxisConfiguration_var->partId(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |