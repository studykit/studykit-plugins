# RotaryMachineAxis.rotationAxis Property

Parent Object: [RotaryMachineAxis](RotaryMachineAxis.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/RotaryMachineAxis.h>

## Description

The infinite line that defines the direction and location of the axis of rotation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rotaryMachineAxis\_var" is a variable referencing a RotaryMachineAxis object. |

"rotaryMachineAxis\_var" is a variable referencing a RotaryMachineAxis object. ```` ``` #include <Cam/Machine/RotaryMachineAxis.h>  // Get the value of the property. Ptr<InfiniteLine3D> propertyValue = rotaryMachineAxis_var->rotationAxis();  // Set the value of the property, where value_var is an InfiniteLine3D. bool returnValue = rotaryMachineAxis_var->rotationAxis(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [InfiniteLine3D](InfiniteLine3D.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |