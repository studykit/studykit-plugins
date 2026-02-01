# MachineAvoidSelectionBase.axialOffset Property

Parent Object: [MachineAvoidSelectionBase](MachineAvoidSelectionBase.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/MachineAvoidSelections/MachineAvoidSelectionBase.h>

## Description

Axial offset - sets the corresponding axial offset value based on the machine mode

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAvoidSelectionBase\_var" is a variable referencing a MachineAvoidSelectionBase object. |

"machineAvoidSelectionBase\_var" is a variable referencing a MachineAvoidSelectionBase object. ```` ``` #include <Cam/MachineAvoidSelections/MachineAvoidSelectionBase.h>  // Get the value of the property. double propertyValue = machineAvoidSelectionBase_var->axialOffset();  // Set the value of the property, where value_var is a double. bool returnValue = machineAvoidSelectionBase_var->axialOffset(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |