# Machine.capabilities Property

Parent Object: [Machine](Machine.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/Machine.h>

## Description

Gets the capabilities of the machine.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machine\_var" is a variable referencing a Machine object. |

"machine\_var" is a variable referencing a Machine object. ```` ``` #include <Cam/Machine/Machine.h>  // Get the value of the property. Ptr<MachineCapabilities> propertyValue = machine_var->capabilities(); ``` ```` |

## Property Value

This is a read only property whose value is a [MachineCapabilities](MachineCapabilities.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |