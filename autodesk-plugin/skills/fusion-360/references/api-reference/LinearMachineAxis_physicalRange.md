# LinearMachineAxis.physicalRange Property

Parent Object: [LinearMachineAxis](LinearMachineAxis.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/LinearMachineAxis.h>

## Description

Range of possible values for this axis. Units are cm for linear axes or radians for rotary axes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"linearMachineAxis\_var" is a variable referencing a LinearMachineAxis object. |

"linearMachineAxis\_var" is a variable referencing a LinearMachineAxis object. ```` ``` #include <Cam/Machine/LinearMachineAxis.h>  // Get the value of the property. Ptr<MachineAxisRange> propertyValue = linearMachineAxis_var->physicalRange();  // Set the value of the property, where value_var is a MachineAxisRange. bool returnValue = linearMachineAxis_var->physicalRange(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MachineAxisRange](MachineAxisRange.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |