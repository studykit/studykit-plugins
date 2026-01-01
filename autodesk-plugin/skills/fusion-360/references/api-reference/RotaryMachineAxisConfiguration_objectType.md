# RotaryMachineAxisConfiguration.objectType Property

Parent Object: [RotaryMachineAxisConfiguration](RotaryMachineAxisConfiguration.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/RotaryMachineAxisConfiguration.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rotaryMachineAxisConfiguration\_var" is a variable referencing a RotaryMachineAxisConfiguration object.  ```` ``` # Get the value of the property. propertyValue = rotaryMachineAxisConfiguration_var.objectType ``` ```` |

"rotaryMachineAxisConfiguration\_var" is a variable referencing a RotaryMachineAxisConfiguration object. ```` ``` #include <Cam/Machine/RotaryMachineAxisConfiguration.h>  // Get the value of the property. string propertyValue = rotaryMachineAxisConfiguration_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |