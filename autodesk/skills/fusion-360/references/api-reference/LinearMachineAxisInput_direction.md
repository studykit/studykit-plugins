# LinearMachineAxisInput.direction Property

Parent Object: [LinearMachineAxisInput](LinearMachineAxisInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/LinearMachineAxisInput.h>

## Description

The unit vector that represents the direction along which the linear axis will move. This vector is in the machine's coordinate system (e.g. the X axis is always (1,0,0)).

## Syntax

* [Python](#Python)
* [C++](#C++)

"linearMachineAxisInput\_var" is a variable referencing a LinearMachineAxisInput object. |

"linearMachineAxisInput\_var" is a variable referencing a LinearMachineAxisInput object. ```` ``` #include <Cam/Machine/LinearMachineAxisInput.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = linearMachineAxisInput_var->direction();  // Set the value of the property, where value_var is a Vector3D. bool returnValue = linearMachineAxisInput_var->direction(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |