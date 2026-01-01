# MachineAvoidDefaultSelection.inputGeometry Property

Parent Object: [MachineAvoidDefaultSelection](MachineAvoidDefaultSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/MachineAvoidSelections/MachineAvoidDefaultSelection.h>

## Description

Get the value of the input geometry.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAvoidDefaultSelection\_var" is a variable referencing a MachineAvoidDefaultSelection object. |

"machineAvoidDefaultSelection\_var" is a variable referencing a MachineAvoidDefaultSelection object. ```` ``` #include <Cam/MachineAvoidSelections/MachineAvoidDefaultSelection.h>  // Get the value of the property. std::vector<Ptr<Base>> propertyValue = machineAvoidDefaultSelection_var->inputGeometry(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [Base](Base.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |