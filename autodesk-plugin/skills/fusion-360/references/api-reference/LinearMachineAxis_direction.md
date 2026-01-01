# LinearMachineAxis.direction Property

Parent Object: [LinearMachineAxis](LinearMachineAxis.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/LinearMachineAxis.h>

## Description

The unit vector that represents the direction along which the axis will move.

## Syntax

* [Python](#Python)
* [C++](#C++)

"linearMachineAxis\_var" is a variable referencing a LinearMachineAxis object. |

"linearMachineAxis\_var" is a variable referencing a LinearMachineAxis object. ```` ``` #include <Cam/Machine/LinearMachineAxis.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = linearMachineAxis_var->direction();  // Set the value of the property, where value_var is a Vector3D. bool returnValue = linearMachineAxis_var->direction(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |