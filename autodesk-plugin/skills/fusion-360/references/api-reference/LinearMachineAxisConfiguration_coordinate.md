# LinearMachineAxisConfiguration.coordinate Property

Parent Object: [LinearMachineAxisConfiguration](LinearMachineAxisConfiguration.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/LinearMachineAxisConfiguration.h>

## Description

Coordinate to use for post processing.

## Syntax

* [Python](#Python)
* [C++](#C++)

"linearMachineAxisConfiguration\_var" is a variable referencing a LinearMachineAxisConfiguration object. |

"linearMachineAxisConfiguration\_var" is a variable referencing a LinearMachineAxisConfiguration object. ```` ``` #include <Cam/Machine/LinearMachineAxisConfiguration.h>  // Get the value of the property. MachineAxisCoordinates propertyValue = linearMachineAxisConfiguration_var->coordinate();  // Set the value of the property, where value_var is a MachineAxisCoordinates. bool returnValue = linearMachineAxisConfiguration_var->coordinate(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MachineAxisCoordinates](MachineAxisCoordinates.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |