# RotaryMachineAxisConfiguration.rotaryPreference Property

Parent Object: [RotaryMachineAxisConfiguration](RotaryMachineAxisConfiguration.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/RotaryMachineAxisConfiguration.h>

## Description

Specify the preferred angle direction at the beginning of an operation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rotaryMachineAxisConfiguration\_var" is a variable referencing a RotaryMachineAxisConfiguration object. |

"rotaryMachineAxisConfiguration\_var" is a variable referencing a RotaryMachineAxisConfiguration object. ```` ``` #include <Cam/Machine/RotaryMachineAxisConfiguration.h>  // Get the value of the property. MachineAnglePreferences propertyValue = rotaryMachineAxisConfiguration_var->rotaryPreference();  // Set the value of the property, where value_var is a MachineAnglePreferences. bool returnValue = rotaryMachineAxisConfiguration_var->rotaryPreference(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MachineAnglePreferences](MachineAnglePreferences.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |