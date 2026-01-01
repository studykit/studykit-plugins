# MachineAvoidDirectSelection.combinedOffset Property

Parent Object: [MachineAvoidDirectSelection](MachineAvoidDirectSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/MachineAvoidSelections/MachineAvoidDirectSelection.h>

## Description

Combined offset - clearance and stock to leave based on the machine mode This only applies to strategies that use a single offset value (Advanced Swarf, Multi-Axis Clearing, Multi-Axis Finishing, Deburr and Geodesic)

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAvoidDirectSelection\_var" is a variable referencing a MachineAvoidDirectSelection object. |

"machineAvoidDirectSelection\_var" is a variable referencing a MachineAvoidDirectSelection object. ```` ``` #include <Cam/MachineAvoidSelections/MachineAvoidDirectSelection.h>  // Get the value of the property. double propertyValue = machineAvoidDirectSelection_var->combinedOffset();  // Set the value of the property, where value_var is a double. bool returnValue = machineAvoidDirectSelection_var->combinedOffset(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |