# RotaryMachineAxis.homePosition Property

Parent Object: [RotaryMachineAxis](RotaryMachineAxis.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/RotaryMachineAxis.h>

## Description

Specifies the value that this axis returns to when the machine is homed. Units are cm for linear axes or radians for rotary axes. Will return NaN if home position isn't set.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rotaryMachineAxis\_var" is a variable referencing a RotaryMachineAxis object. |

"rotaryMachineAxis\_var" is a variable referencing a RotaryMachineAxis object. ```` ``` #include <Cam/Machine/RotaryMachineAxis.h>  // Get the value of the property. double propertyValue = rotaryMachineAxis_var->homePosition();  // Set the value of the property, where value_var is a double. bool returnValue = rotaryMachineAxis_var->homePosition(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |