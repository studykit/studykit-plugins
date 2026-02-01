# MachineAxisConfiguration.coordinate Property

Parent Object: [MachineAxisConfiguration](MachineAxisConfiguration.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineAxisConfiguration.h>

## Description

Coordinate to use for post processing.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAxisConfiguration\_var" is a variable referencing a MachineAxisConfiguration object. |

"machineAxisConfiguration\_var" is a variable referencing a MachineAxisConfiguration object. ```` ``` #include <Cam/Machine/MachineAxisConfiguration.h>  // Get the value of the property. MachineAxisCoordinates propertyValue = machineAxisConfiguration_var->coordinate();  // Set the value of the property, where value_var is a MachineAxisCoordinates. bool returnValue = machineAxisConfiguration_var->coordinate(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MachineAxisCoordinates](MachineAxisCoordinates.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |