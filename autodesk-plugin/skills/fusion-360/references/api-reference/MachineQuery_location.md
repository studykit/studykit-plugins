# MachineQuery.location Property

Parent Object: [MachineQuery](MachineQuery.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineQuery.h>

## Description

The location specifies the location to search in the machine library. Setting the location clears any previous specified URL.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineQuery\_var" is a variable referencing a MachineQuery object. |

"machineQuery\_var" is a variable referencing a MachineQuery object. ```` ``` #include <Cam/Machine/MachineQuery.h>  // Get the value of the property. LibraryLocations propertyValue = machineQuery_var->location();  // Set the value of the property, where value_var is a LibraryLocations. bool returnValue = machineQuery_var->location(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [LibraryLocations](LibraryLocations.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |