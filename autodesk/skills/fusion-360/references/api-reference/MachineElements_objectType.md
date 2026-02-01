# MachineElements.objectType Property

Parent Object: [MachineElements](MachineElements.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineElements.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineElements\_var" is a variable referencing a MachineElements object.  ```` ``` # Get the value of the property. propertyValue = machineElements_var.objectType ``` ```` |

"machineElements\_var" is a variable referencing a MachineElements object. ```` ``` #include <Cam/Machine/MachineElements.h>  // Get the value of the property. string propertyValue = machineElements_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |