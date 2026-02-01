# MachineAxisInput.objectType Property

Parent Object: [MachineAxisInput](MachineAxisInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineAxisInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAxisInput\_var" is a variable referencing a MachineAxisInput object.  ```` ``` # Get the value of the property. propertyValue = machineAxisInput_var.objectType ``` ```` |

"machineAxisInput\_var" is a variable referencing a MachineAxisInput object. ```` ``` #include <Cam/Machine/MachineAxisInput.h>  // Get the value of the property. string propertyValue = machineAxisInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |