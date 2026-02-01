# RotaryMachineAxisConfiguration.wrapAroundAtRange Property

Parent Object: [RotaryMachineAxisConfiguration](RotaryMachineAxisConfiguration.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/RotaryMachineAxisConfiguration.h>

## Description

Specify the range that the axis value wraps around for unlimited axes. If there are no wrap around limits then wrapAroundAtRange is infinite. Units are radians.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rotaryMachineAxisConfiguration\_var" is a variable referencing a RotaryMachineAxisConfiguration object. |

"rotaryMachineAxisConfiguration\_var" is a variable referencing a RotaryMachineAxisConfiguration object. ```` ``` #include <Cam/Machine/RotaryMachineAxisConfiguration.h>  // Get the value of the property. Ptr<MachineAxisRange> propertyValue = rotaryMachineAxisConfiguration_var->wrapAroundAtRange();  // Set the value of the property, where value_var is a MachineAxisRange. bool returnValue = rotaryMachineAxisConfiguration_var->wrapAroundAtRange(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MachineAxisRange](MachineAxisRange.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |