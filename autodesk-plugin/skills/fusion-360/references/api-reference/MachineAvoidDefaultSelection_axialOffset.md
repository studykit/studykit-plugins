# MachineAvoidDefaultSelection.axialOffset Property

Parent Object: [MachineAvoidDefaultSelection](MachineAvoidDefaultSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/MachineAvoidSelections/MachineAvoidDefaultSelection.h>

## Description

Axial offset - sets the corresponding axial offset value based on the machine mode

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAvoidDefaultSelection\_var" is a variable referencing a MachineAvoidDefaultSelection object. |

"machineAvoidDefaultSelection\_var" is a variable referencing a MachineAvoidDefaultSelection object. ```` ``` #include <Cam/MachineAvoidSelections/MachineAvoidDefaultSelection.h>  // Get the value of the property. double propertyValue = machineAvoidDefaultSelection_var->axialOffset();  // Set the value of the property, where value_var is a double. bool returnValue = machineAvoidDefaultSelection_var->axialOffset(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |