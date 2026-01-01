# RotaryMachineAxis.isValid Property

Parent Object: [RotaryMachineAxis](RotaryMachineAxis.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/RotaryMachineAxis.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rotaryMachineAxis\_var" is a variable referencing a RotaryMachineAxis object. |

"rotaryMachineAxis\_var" is a variable referencing a RotaryMachineAxis object. ```` ``` #include <Cam/Machine/RotaryMachineAxis.h>  // Get the value of the property. boolean propertyValue = rotaryMachineAxis_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |