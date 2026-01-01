# RotaryMachineAxisInput.name Property

Parent Object: [RotaryMachineAxisInput](RotaryMachineAxisInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/RotaryMachineAxisInput.h>

## Description

The user facing name of this axis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rotaryMachineAxisInput\_var" is a variable referencing a RotaryMachineAxisInput object. |

"rotaryMachineAxisInput\_var" is a variable referencing a RotaryMachineAxisInput object. ```` ``` #include <Cam/Machine/RotaryMachineAxisInput.h>  // Get the value of the property. string propertyValue = rotaryMachineAxisInput_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = rotaryMachineAxisInput_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |