# RotaryMachineAxis.name Property

Parent Object: [RotaryMachineAxis](RotaryMachineAxis.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/RotaryMachineAxis.h>

## Description

The name of this axis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rotaryMachineAxis\_var" is a variable referencing a RotaryMachineAxis object. |

"rotaryMachineAxis\_var" is a variable referencing a RotaryMachineAxis object. ```` ``` #include <Cam/Machine/RotaryMachineAxis.h>  // Get the value of the property. string propertyValue = rotaryMachineAxis_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = rotaryMachineAxis_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |