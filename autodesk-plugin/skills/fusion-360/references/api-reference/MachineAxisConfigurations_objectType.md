# MachineAxisConfigurations.objectType Property

Parent Object: [MachineAxisConfigurations](MachineAxisConfigurations.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineAxisConfigurations.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAxisConfigurations\_var" is a variable referencing a MachineAxisConfigurations object.  ```` ``` # Get the value of the property. propertyValue = machineAxisConfigurations_var.objectType ``` ```` |

"machineAxisConfigurations\_var" is a variable referencing a MachineAxisConfigurations object. ```` ``` #include <Cam/Machine/MachineAxisConfigurations.h>  // Get the value of the property. string propertyValue = machineAxisConfigurations_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |