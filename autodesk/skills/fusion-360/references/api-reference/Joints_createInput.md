# Joints.createInput Method

Parent Object: [Joints](Joints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Joints.h>

## Description

Creates a JointInput object, which is the API equivalent to the Joint command dialog. You you use methods and properties on the returned class to set the desired options, similar to providing input and setting options in the Joint command dialog. Once the settings are defined you call the Joints.add method passing in the JointInput object to create the actual joint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"joints\_var" is a variable referencing a [Joints](Joints.htm) object.```` ``` returnValue = joints_var.createInput(geometryOrOriginOne, geometryOrOriginTwo) ``` ```` |

"joints\_var" is a variable referencing a [Joints](Joints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [JointInput](JointInput.htm) | Returns the JointInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| geometryOrOriginOne | [Base](Base.htm) | A JointGeometry or JointOrigin object that defines the first set of geometry of the joint. JointGeometry objects are created by using the various static methods on the JointGeometry class and JointOrigin objects are created through the JointOrigins object. |
| geometryOrOriginTwo | [Base](Base.htm) | A JointGeometry or JointOrigin object that defines the second set of geometry of the joint. JointGeometry objects are created by using the various static methods on the JointGeometry class and JointOrigin objects are created through the JointOrigins object. |

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