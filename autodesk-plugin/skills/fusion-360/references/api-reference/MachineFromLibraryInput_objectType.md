# MachineFromLibraryInput.objectType Property

Parent Object: [MachineFromLibraryInput](MachineFromLibraryInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineFromLibraryInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineFromLibraryInput\_var" is a variable referencing a MachineFromLibraryInput object.  ```` ``` # Get the value of the property. propertyValue = machineFromLibraryInput_var.objectType ``` ```` |

"machineFromLibraryInput\_var" is a variable referencing a MachineFromLibraryInput object. ```` ``` #include <Cam/Machine/MachineFromLibraryInput.h>  // Get the value of the property. string propertyValue = machineFromLibraryInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |