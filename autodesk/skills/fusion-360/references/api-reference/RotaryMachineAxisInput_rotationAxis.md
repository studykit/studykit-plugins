# RotaryMachineAxisInput.rotationAxis Property

Parent Object: [RotaryMachineAxisInput](RotaryMachineAxisInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/RotaryMachineAxisInput.h>

## Description

The infinite line that defines the direction and location of the axis of rotation. This direction is in the machine's coordinate system (e.g. an A axis would typically use (1,0,0) for the direction), and follows the right-hand rule.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rotaryMachineAxisInput\_var" is a variable referencing a RotaryMachineAxisInput object. |

"rotaryMachineAxisInput\_var" is a variable referencing a RotaryMachineAxisInput object. ```` ``` #include <Cam/Machine/RotaryMachineAxisInput.h>  // Get the value of the property. Ptr<InfiniteLine3D> propertyValue = rotaryMachineAxisInput_var->rotationAxis();  // Set the value of the property, where value_var is an InfiniteLine3D. bool returnValue = rotaryMachineAxisInput_var->rotationAxis(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [InfiniteLine3D](InfiniteLine3D.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |