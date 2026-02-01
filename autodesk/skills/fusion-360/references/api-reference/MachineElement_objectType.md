# MachineElement.objectType Property

Parent Object: [MachineElement](MachineElement.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineElement.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineElement\_var" is a variable referencing a MachineElement object.  ```` ``` # Get the value of the property. propertyValue = machineElement_var.objectType ``` ```` |

"machineElement\_var" is a variable referencing a MachineElement object. ```` ``` #include <Cam/Machine/MachineElement.h>  // Get the value of the property. string propertyValue = machineElement_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |