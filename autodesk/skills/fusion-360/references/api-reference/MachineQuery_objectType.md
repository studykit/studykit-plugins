# MachineQuery.objectType Property

Parent Object: [MachineQuery](MachineQuery.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineQuery.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineQuery\_var" is a variable referencing a MachineQuery object.  ```` ``` # Get the value of the property. propertyValue = machineQuery_var.objectType ``` ```` |

"machineQuery\_var" is a variable referencing a MachineQuery object. ```` ``` #include <Cam/Machine/MachineQuery.h>  // Get the value of the property. string propertyValue = machineQuery_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |