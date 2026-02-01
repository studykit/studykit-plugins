# KinematicsMachineElement.parts Property

Parent Object: [KinematicsMachineElement](KinematicsMachineElement.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/KinematicsMachineElement.h>

## Description

Get the root parts collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"kinematicsMachineElement\_var" is a variable referencing a KinematicsMachineElement object. |

"kinematicsMachineElement\_var" is a variable referencing a KinematicsMachineElement object. ```` ``` #include <Cam/Machine/KinematicsMachineElement.h>  // Get the value of the property. Ptr<MachineParts> propertyValue = kinematicsMachineElement_var->parts(); ``` ```` |

## Property Value

This is a read only property whose value is a [MachineParts](MachineParts.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |