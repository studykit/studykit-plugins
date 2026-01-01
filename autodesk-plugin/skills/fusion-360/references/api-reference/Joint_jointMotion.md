# Joint.jointMotion Property

Parent Object: [Joint](Joint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Joint.h>

## Description

Returns a JointMotion object that defines the motion relationship between the two geometries.

## Syntax

* [Python](#Python)
* [C++](#C++)

"joint\_var" is a variable referencing a Joint object.  ```` ``` # Get the value of the property. propertyValue = joint_var.jointMotion ``` ```` |

"joint\_var" is a variable referencing a Joint object. ```` ``` #include <Fusion/Components/Joint.h>  // Get the value of the property. Ptr<JointMotion> propertyValue = joint_var->jointMotion(); ``` ```` |

## Property Value

This is a read only property whose value is a [JointMotion](JointMotion.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [BallJointMotion API Sample](BallJointMotionSample_Sample.htm) | Demonstrates creating a joint with ball joint motion |
| [CylindricalJointMotion API Sample](CylindricalJointMotionSample_Sample.htm) | Demonstrates creating a joint with cylindrical joint motion. |
| [Pin Slot Joint Motion API Sample](PinSlotJointMotionSample_Sample.htm) | Demonstrates creating a joint with pin slot joint motion |
| [Planar Joint Motion API Sample](PlanarJointMotionSample_Sample.htm) | Demonstrates creating a joint with planar joint motion |
| [RevoluteJointMotion API Sample](RevoluteJointMotionSample_Sample.htm) | Demonstrates creating a joint with revolute joint motion. |
| [SliderJointMotion API Sample](SliderJointMotionSample_Sample.htm) | Demonstrates creating a joint with slider joint motion. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |