# JointInput.isFlipped Property

Parent Object: [JointInput](JointInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointInput.h>

## Description

Gets and sets if the joint direction is flipped or not. This is effectively specifying if the third axis of the two input geometries is facing (false) or opposed (true).

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointInput\_var" is a variable referencing a JointInput object. |

"jointInput\_var" is a variable referencing a JointInput object. ```` ``` #include <Fusion/Components/JointInput.h>  // Get the value of the property. boolean propertyValue = jointInput_var->isFlipped();  // Set the value of the property, where value_var is a boolean. bool returnValue = jointInput_var->isFlipped(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

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