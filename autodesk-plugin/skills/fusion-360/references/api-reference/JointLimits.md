# JointLimits Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointLimits.h>

## Description

Used to define limits for the range of motion of a joint.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](JointLimits_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isMaximumValueEnabled](JointLimits_isMaximumValueEnabled.htm) | Gets and sets whether the maximum joint limit is enabled or not. |
| [isMinimumValueEnabled](JointLimits_isMinimumValueEnabled.htm) | Gets and sets whether the minimum joint limit is enabled or not. |
| [isRestValueEnabled](JointLimits_isRestValueEnabled.htm) | Gets and sets whether the resting joint value is enabled or not. |
| [isValid](JointLimits_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [maximumValue](JointLimits_maximumValue.htm) | The maximum value of the value. This is in either centimeters or radians depending on if the joint value this is associated with defines a distance or an angle. |
| [minimumValue](JointLimits_minimumValue.htm) | The minimum value of the value. This is in either centimeters or radians depending on if the joint value this is associated with defines a distance or an angle. |
| [objectType](JointLimits_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [restValue](JointLimits_restValue.htm) | The resting state value. This is in either centimeters or radians depending on if the joint value this is associated with defines a distance or an angle. |

## Accessed From

[BallJointMotion.pitchLimits](BallJointMotion_pitchLimits.htm), [BallJointMotion.rollLimits](BallJointMotion_rollLimits.htm), [BallJointMotion.yawLimits](BallJointMotion_yawLimits.htm), [CylindricalJointMotion.rotationLimits](CylindricalJointMotion_rotationLimits.htm), [CylindricalJointMotion.slideLimits](CylindricalJointMotion_slideLimits.htm), [PinSlotJointMotion.rotationLimits](PinSlotJointMotion_rotationLimits.htm), [PinSlotJointMotion.slideLimits](PinSlotJointMotion_slideLimits.htm), [PlanarJointMotion.primarySlideLimits](PlanarJointMotion_primarySlideLimits.htm), [PlanarJointMotion.rotationLimits](PlanarJointMotion_rotationLimits.htm), [PlanarJointMotion.secondarySlideLimits](PlanarJointMotion_secondarySlideLimits.htm), [RevoluteJointMotion.rotationLimits](RevoluteJointMotion_rotationLimits.htm), [SliderJointMotion.slideLimits](SliderJointMotion_slideLimits.htm)

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