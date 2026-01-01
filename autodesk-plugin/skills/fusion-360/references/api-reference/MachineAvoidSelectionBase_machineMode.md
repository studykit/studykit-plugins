# MachineAvoidSelectionBase.machineMode Property

Parent Object: [MachineAvoidSelectionBase](MachineAvoidSelectionBase.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/MachineAvoidSelections/MachineAvoidSelectionBase.h>

## Description

Desired machining mode. The default is Avoid. The current machining mode will determine which value the radial and axial offset functions refer to. When set to Machine, the radial and axial offset methods will read/set the stock to leave parameter. When set to Avoid, the radial and axial offset methods will read/set the clearance value, and the Fixture mode will map to the relative fixture clearance value.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAvoidSelectionBase\_var" is a variable referencing a MachineAvoidSelectionBase object. |

"machineAvoidSelectionBase\_var" is a variable referencing a MachineAvoidSelectionBase object. ```` ``` #include <Cam/MachineAvoidSelections/MachineAvoidSelectionBase.h>  // Get the value of the property. MachiningMode propertyValue = machineAvoidSelectionBase_var->machineMode();  // Set the value of the property, where value_var is a MachiningMode. bool returnValue = machineAvoidSelectionBase_var->machineMode(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MachiningMode](MachiningMode.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |