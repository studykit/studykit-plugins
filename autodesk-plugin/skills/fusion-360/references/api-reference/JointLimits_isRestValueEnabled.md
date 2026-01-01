# JointLimits.isRestValueEnabled Property

Parent Object: [JointLimits](JointLimits.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointLimits.h>

## Description

Gets and sets whether the resting joint value is enabled or not.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointLimits\_var" is a variable referencing a JointLimits object. |

"jointLimits\_var" is a variable referencing a JointLimits object. ```` ``` #include <Fusion/Components/JointLimits.h>  // Get the value of the property. boolean propertyValue = jointLimits_var->isRestValueEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = jointLimits_var->isRestValueEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [BallJointMotion API Sample](BallJointMotionSample_Sample.htm) | Demonstrates creating a joint with ball joint motion |
| [CylindricalJointMotion API Sample](CylindricalJointMotionSample_Sample.htm) | Demonstrates creating a joint with cylindrical joint motion. |
| [Pin Slot Joint Motion API Sample](PinSlotJointMotionSample_Sample.htm) | Demonstrates creating a joint with pin slot joint motion |
| [Planar Joint Motion API Sample](PlanarJointMotionSample_Sample.htm) | Demonstrates creating a joint with planar joint motion |
| [SliderJointMotion API Sample](SliderJointMotionSample_Sample.htm) | Demonstrates creating a joint with slider joint motion. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |