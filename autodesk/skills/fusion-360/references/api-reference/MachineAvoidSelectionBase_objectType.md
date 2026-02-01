# MachineAvoidSelectionBase.objectType Property

Parent Object: [MachineAvoidSelectionBase](MachineAvoidSelectionBase.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/MachineAvoidSelections/MachineAvoidSelectionBase.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAvoidSelectionBase\_var" is a variable referencing a MachineAvoidSelectionBase object.  ```` ``` # Get the value of the property. propertyValue = machineAvoidSelectionBase_var.objectType ``` ```` |

"machineAvoidSelectionBase\_var" is a variable referencing a MachineAvoidSelectionBase object. ```` ``` #include <Cam/MachineAvoidSelections/MachineAvoidSelectionBase.h>  // Get the value of the property. string propertyValue = machineAvoidSelectionBase_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |