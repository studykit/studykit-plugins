# MachineLibrary.objectType Property

Parent Object: [MachineLibrary](MachineLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineLibrary.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineLibrary\_var" is a variable referencing a MachineLibrary object.  ```` ``` # Get the value of the property. propertyValue = machineLibrary_var.objectType ``` ```` |

"machineLibrary\_var" is a variable referencing a MachineLibrary object. ```` ``` #include <Cam/Machine/MachineLibrary.h>  // Get the value of the property. string propertyValue = machineLibrary_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |