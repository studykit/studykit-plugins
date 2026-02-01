# MachineCapabilities.objectType Property

Parent Object: [MachineCapabilities](MachineCapabilities.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineCapabilities.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineCapabilities\_var" is a variable referencing a MachineCapabilities object.  ```` ``` # Get the value of the property. propertyValue = machineCapabilities_var.objectType ``` ```` |

"machineCapabilities\_var" is a variable referencing a MachineCapabilities object. ```` ``` #include <Cam/Machine/MachineCapabilities.h>  // Get the value of the property. string propertyValue = machineCapabilities_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |