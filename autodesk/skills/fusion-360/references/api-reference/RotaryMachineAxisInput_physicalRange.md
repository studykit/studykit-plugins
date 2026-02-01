# RotaryMachineAxisInput.physicalRange Property

Parent Object: [RotaryMachineAxisInput](RotaryMachineAxisInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/RotaryMachineAxisInput.h>

## Description

Range of possible values for this axis. Units are cm for linear axes or radians for rotary axes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rotaryMachineAxisInput\_var" is a variable referencing a RotaryMachineAxisInput object. |

"rotaryMachineAxisInput\_var" is a variable referencing a RotaryMachineAxisInput object. ```` ``` #include <Cam/Machine/RotaryMachineAxisInput.h>  // Get the value of the property. Ptr<MachineAxisRange> propertyValue = rotaryMachineAxisInput_var->physicalRange();  // Set the value of the property, where value_var is a MachineAxisRange. bool returnValue = rotaryMachineAxisInput_var->physicalRange(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MachineAxisRange](MachineAxisRange.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |