# MachineAxisRange.max Property

Parent Object: [MachineAxisRange](MachineAxisRange.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineAxisRange.h>

## Description

Maximum value of range Type depends on where this range is being used. Centimeters are used for distances and radians for angles. Returns infinity if this range is infinite.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAxisRange\_var" is a variable referencing a MachineAxisRange object. |

"machineAxisRange\_var" is a variable referencing a MachineAxisRange object. ```` ``` #include <Cam/Machine/MachineAxisRange.h>  // Get the value of the property. double propertyValue = machineAxisRange_var->max(); ``` ```` |

## Property Value

This is a read only property whose value is a double.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |