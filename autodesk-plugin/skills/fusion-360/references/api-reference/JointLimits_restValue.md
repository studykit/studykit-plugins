# JointLimits.restValue Property

Parent Object: [JointLimits](JointLimits.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointLimits.h>

## Description

The resting state value. This is in either centimeters or radians depending on if the joint value this is associated with defines a distance or an angle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointLimits\_var" is a variable referencing a JointLimits object. |

"jointLimits\_var" is a variable referencing a JointLimits object. ```` ``` #include <Fusion/Components/JointLimits.h>  // Get the value of the property. double propertyValue = jointLimits_var->restValue();  // Set the value of the property, where value_var is a double. bool returnValue = jointLimits_var->restValue(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

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