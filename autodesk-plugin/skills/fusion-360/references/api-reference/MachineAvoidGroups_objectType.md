# MachineAvoidGroups.objectType Property

Parent Object: [MachineAvoidGroups](MachineAvoidGroups.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/MachineAvoidSelections/MachineAvoidGroups.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAvoidGroups\_var" is a variable referencing a MachineAvoidGroups object.  ```` ``` # Get the value of the property. propertyValue = machineAvoidGroups_var.objectType ``` ```` |

"machineAvoidGroups\_var" is a variable referencing a MachineAvoidGroups object. ```` ``` #include <Cam/MachineAvoidSelections/MachineAvoidGroups.h>  // Get the value of the property. string propertyValue = machineAvoidGroups_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |