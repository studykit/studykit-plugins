# RotaryMachineAxis.objectType Property

Parent Object: [RotaryMachineAxis](RotaryMachineAxis.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/RotaryMachineAxis.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rotaryMachineAxis\_var" is a variable referencing a RotaryMachineAxis object.  ```` ``` # Get the value of the property. propertyValue = rotaryMachineAxis_var.objectType ``` ```` |

"rotaryMachineAxis\_var" is a variable referencing a RotaryMachineAxis object. ```` ``` #include <Cam/Machine/RotaryMachineAxis.h>  // Get the value of the property. string propertyValue = rotaryMachineAxis_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |