# MachineElement.elementId Property

Parent Object: [MachineElement](MachineElement.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineElement.h>

## Description

Identifier for this element. Unique within an element type.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineElement\_var" is a variable referencing a MachineElement object. |

"machineElement\_var" is a variable referencing a MachineElement object. ```` ``` #include <Cam/Machine/MachineElement.h>  // Get the value of the property. string propertyValue = machineElement_var->elementId(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |