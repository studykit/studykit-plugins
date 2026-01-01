# MachineAxis.physicalRange Property

Parent Object: [MachineAxis](MachineAxis.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineAxis.h>

## Description

Range of possible values for this axis. Units are cm for linear axes or radians for rotary axes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAxis\_var" is a variable referencing a MachineAxis object. |

"machineAxis\_var" is a variable referencing a MachineAxis object. ```` ``` #include <Cam/Machine/MachineAxis.h>  // Get the value of the property. Ptr<MachineAxisRange> propertyValue = machineAxis_var->physicalRange();  // Set the value of the property, where value_var is a MachineAxisRange. bool returnValue = machineAxis_var->physicalRange(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MachineAxisRange](MachineAxisRange.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |