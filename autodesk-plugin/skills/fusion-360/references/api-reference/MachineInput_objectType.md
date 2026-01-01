# MachineInput.objectType Property

Parent Object: [MachineInput](MachineInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineInput\_var" is a variable referencing a MachineInput object.  ```` ``` # Get the value of the property. propertyValue = machineInput_var.objectType ``` ```` |

"machineInput\_var" is a variable referencing a MachineInput object. ```` ``` #include <Cam/Machine/MachineInput.h>  // Get the value of the property. string propertyValue = machineInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |