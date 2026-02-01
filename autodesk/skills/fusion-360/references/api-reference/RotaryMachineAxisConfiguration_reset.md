# RotaryMachineAxisConfiguration.reset Property

Parent Object: [RotaryMachineAxisConfiguration](RotaryMachineAxisConfiguration.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/RotaryMachineAxisConfiguration.h>

## Description

Specify when to reset the initial axis position.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rotaryMachineAxisConfiguration\_var" is a variable referencing a RotaryMachineAxisConfiguration object. |

"rotaryMachineAxisConfiguration\_var" is a variable referencing a RotaryMachineAxisConfiguration object. ```` ``` #include <Cam/Machine/RotaryMachineAxisConfiguration.h>  // Get the value of the property. MachineResetOptions propertyValue = rotaryMachineAxisConfiguration_var->reset();  // Set the value of the property, where value_var is a MachineResetOptions. bool returnValue = rotaryMachineAxisConfiguration_var->reset(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MachineResetOptions](MachineResetOptions.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |