# MachineAvoidDirectSelection.objectType Property

Parent Object: [MachineAvoidDirectSelection](MachineAvoidDirectSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/MachineAvoidSelections/MachineAvoidDirectSelection.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAvoidDirectSelection\_var" is a variable referencing a MachineAvoidDirectSelection object.  ```` ``` # Get the value of the property. propertyValue = machineAvoidDirectSelection_var.objectType ``` ```` |

"machineAvoidDirectSelection\_var" is a variable referencing a MachineAvoidDirectSelection object. ```` ``` #include <Cam/MachineAvoidSelections/MachineAvoidDirectSelection.h>  // Get the value of the property. string propertyValue = machineAvoidDirectSelection_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |