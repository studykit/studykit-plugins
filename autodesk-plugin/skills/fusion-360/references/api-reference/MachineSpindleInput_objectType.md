# MachineSpindleInput.objectType Property

Parent Object: [MachineSpindleInput](MachineSpindleInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineSpindleInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineSpindleInput\_var" is a variable referencing a MachineSpindleInput object.  ```` ``` # Get the value of the property. propertyValue = machineSpindleInput_var.objectType ``` ```` |

"machineSpindleInput\_var" is a variable referencing a MachineSpindleInput object. ```` ``` #include <Cam/Machine/MachineSpindleInput.h>  // Get the value of the property. string propertyValue = machineSpindleInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |