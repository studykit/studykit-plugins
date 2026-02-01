# MachinePart.axis Property

Parent Object: [MachinePart](MachinePart.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachinePart.h>

## Description

Get the axis object for this part used to reference this part for other operations. Only valid when partType is Axis, otherwise returns null

## Syntax

* [Python](#Python)
* [C++](#C++)

"machinePart\_var" is a variable referencing a MachinePart object. |

"machinePart\_var" is a variable referencing a MachinePart object. ```` ``` #include <Cam/Machine/MachinePart.h>  // Get the value of the property. Ptr<MachineAxis> propertyValue = machinePart_var->axis(); ``` ```` |

## Property Value

This is a read only property whose value is a [MachineAxis](MachineAxis.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |