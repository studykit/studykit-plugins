# MachineAxisInput.physicalRange Property

Parent Object: [MachineAxisInput](MachineAxisInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineAxisInput.h>

## Description

Range of possible values for this axis. Units are cm for linear axes or radians for rotary axes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAxisInput\_var" is a variable referencing a MachineAxisInput object. |

"machineAxisInput\_var" is a variable referencing a MachineAxisInput object. ```` ``` #include <Cam/Machine/MachineAxisInput.h>  // Get the value of the property. Ptr<MachineAxisRange> propertyValue = machineAxisInput_var->physicalRange();  // Set the value of the property, where value_var is a MachineAxisRange. bool returnValue = machineAxisInput_var->physicalRange(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MachineAxisRange](MachineAxisRange.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |