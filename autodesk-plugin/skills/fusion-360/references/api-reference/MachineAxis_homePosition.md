# MachineAxis.homePosition Property

Parent Object: [MachineAxis](MachineAxis.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineAxis.h>

## Description

Specifies the value that this axis returns to when the machine is homed. Units are cm for linear axes or radians for rotary axes. Will return NaN if home position isn't set.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAxis\_var" is a variable referencing a MachineAxis object. |

"machineAxis\_var" is a variable referencing a MachineAxis object. ```` ``` #include <Cam/Machine/MachineAxis.h>  // Get the value of the property. double propertyValue = machineAxis_var->homePosition();  // Set the value of the property, where value_var is a double. bool returnValue = machineAxis_var->homePosition(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |