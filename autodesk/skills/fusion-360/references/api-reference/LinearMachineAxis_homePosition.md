# LinearMachineAxis.homePosition Property

Parent Object: [LinearMachineAxis](LinearMachineAxis.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/LinearMachineAxis.h>

## Description

Specifies the value that this axis returns to when the machine is homed. Units are cm for linear axes or radians for rotary axes. Will return NaN if home position isn't set.

## Syntax

* [Python](#Python)
* [C++](#C++)

"linearMachineAxis\_var" is a variable referencing a LinearMachineAxis object. |

"linearMachineAxis\_var" is a variable referencing a LinearMachineAxis object. ```` ``` #include <Cam/Machine/LinearMachineAxis.h>  // Get the value of the property. double propertyValue = linearMachineAxis_var->homePosition();  // Set the value of the property, where value_var is a double. bool returnValue = linearMachineAxis_var->homePosition(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |