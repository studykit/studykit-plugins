# SliderJointMotion Object

Derived from: [JointMotion](JointMotion.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/SliderJointMotion.h>

## Description

Represents the set of information specific to a slider joint.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](SliderJointMotion_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [customSlideDirectionEntity](SliderJointMotion_customSlideDirectionEntity.htm) | This property can be set using various types of entities that can infer a direction. For example, a linear edge, sketch line, planar face, and cylindrical face. This property is only valid in the case where the slideDirection property returns CustomJointDirection. Setting this property will automatically set the slideDirection property to CustomJointDirection. |
| [isValid](SliderJointMotion_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [jointType](SliderJointMotion_jointType.htm) | Returns an enum value indicating the type of joint this joint represents. |
| [objectType](SliderJointMotion_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [slideDirection](SliderJointMotion_slideDirection.htm) | Gets and sets the direction of the slide. This can be set to XAxisJointDirection, YAxisJointDirection, or ZAxisJointDirection. It can return those three directions and CustomJointDirection. If this returns CustomJointDirection then the customSlideDirectionEntity will return an entity that defines the direction. If there is a custom direction defined and this property is set to one of the three standard axes, the custom direction will be removed and customSlideDirectionEntity will return null. |
| [slideDirectionVector](SliderJointMotion_slideDirectionVector.htm) | Returns the direction of the slide. This property will return null in the case where the SliderJointMotion object was obtained from a JointInput object. |
| [slideLimits](SliderJointMotion_slideLimits.htm) | Returns a JointLimits object that defines the slide limits for this joint. Use the functionality of the returned JointLimits object to get, set, and modify the joint limits. |
| [slideValue](SliderJointMotion_slideValue.htm) | Gets and sets the slide value. This is in centimeters. Setting this value is the equivalent of using the Drive Joints command. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SliderJointMotion API Sample](SliderJointMotionSample_Sample.htm) | Demonstrates creating a joint with slider joint motion. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |