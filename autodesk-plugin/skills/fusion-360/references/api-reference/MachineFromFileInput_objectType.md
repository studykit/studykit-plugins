# MachineFromFileInput.objectType Property

Parent Object: [MachineFromFileInput](MachineFromFileInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineFromFileInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineFromFileInput\_var" is a variable referencing a MachineFromFileInput object.  ```` ``` # Get the value of the property. propertyValue = machineFromFileInput_var.objectType ``` ```` |

"machineFromFileInput\_var" is a variable referencing a MachineFromFileInput object. ```` ``` #include <Cam/Machine/MachineFromFileInput.h>  // Get the value of the property. string propertyValue = machineFromFileInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |