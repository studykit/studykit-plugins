# RotaryMachineAxisConfiguration.coordinate Property

Parent Object: [RotaryMachineAxisConfiguration](RotaryMachineAxisConfiguration.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/RotaryMachineAxisConfiguration.h>

## Description

Coordinate to use for post processing.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rotaryMachineAxisConfiguration\_var" is a variable referencing a RotaryMachineAxisConfiguration object. |

"rotaryMachineAxisConfiguration\_var" is a variable referencing a RotaryMachineAxisConfiguration object. ```` ``` #include <Cam/Machine/RotaryMachineAxisConfiguration.h>  // Get the value of the property. MachineAxisCoordinates propertyValue = rotaryMachineAxisConfiguration_var->coordinate();  // Set the value of the property, where value_var is a MachineAxisCoordinates. bool returnValue = rotaryMachineAxisConfiguration_var->coordinate(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MachineAxisCoordinates](MachineAxisCoordinates.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |