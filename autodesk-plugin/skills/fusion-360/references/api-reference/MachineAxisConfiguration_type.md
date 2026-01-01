# MachineAxisConfiguration.type Property

Parent Object: [MachineAxisConfiguration](MachineAxisConfiguration.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineAxisConfiguration.h>

## Description

The type of this axis configuration. Use this to inform a cast to the derived types.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAxisConfiguration\_var" is a variable referencing a MachineAxisConfiguration object. |

"machineAxisConfiguration\_var" is a variable referencing a MachineAxisConfiguration object. ```` ``` #include <Cam/Machine/MachineAxisConfiguration.h>  // Get the value of the property. MachineAxisTypes propertyValue = machineAxisConfiguration_var->type(); ``` ```` |

## Property Value

This is a read only property whose value is a [MachineAxisTypes](MachineAxisTypes.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |