# Joints.add Method

Parent Object: [Joints](Joints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Joints.h>

## Description

Creates a new joint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"joints\_var" is a variable referencing a [Joints](Joints.htm) object.```` ``` returnValue = joints_var.add(input) ``` ```` |

"joints\_var" is a variable referencing a [Joints](Joints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Joint](Joint.htm) | Returns the newly created Joint or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [JointInput](JointInput.htm) | The JointInput object that defines the geometry and various inputs that fully define a joint. A JointInput object is created using the Joints.createInput method. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [BallJointMotion API Sample](BallJointMotionSample_Sample.htm) | Demonstrates creating a joint with ball joint motion |
| [CylindricalJointMotion API Sample](CylindricalJointMotionSample_Sample.htm) | Demonstrates creating a joint with cylindrical joint motion. |
| [Joint API Sample](JointSample_Sample.htm) | Demonstrates creating a new joint. |
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