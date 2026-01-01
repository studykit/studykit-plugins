# JointInput.angle Property

Parent Object: [JointInput](JointInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointInput.h>

## Description

Specifies the angle between two input geometries. This is effectively the angle between the two primary axes of the input geometries. When a new JointInput object is created, this value defaults to zero. When the joint is created this will become the value of the parameter that controls the joint angle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointInput\_var" is a variable referencing a JointInput object.  ```` ``` # Get the value of the property. propertyValue = jointInput_var.angle  # Set the value of the property. jointInput_var.angle = propertyValue ``` ```` |

"jointInput\_var" is a variable referencing a JointInput object. ```` ``` #include <Fusion/Components/JointInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = jointInput_var->angle();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = jointInput_var->angle(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Joint API Sample](JointSample_Sample.htm) | Demonstrates creating a new joint. |
| [RevoluteJointMotion API Sample](RevoluteJointMotionSample_Sample.htm) | Demonstrates creating a joint with revolute joint motion. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |