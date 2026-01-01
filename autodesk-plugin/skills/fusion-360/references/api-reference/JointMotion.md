# JointMotion Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointMotion.h>

## Description

The base class for the classes that represent all of the various joint types.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](JointMotion_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](JointMotion_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [jointType](JointMotion_jointType.htm) | Returns an enum value indicating the type of joint this joint represents. |
| [objectType](JointMotion_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[AsBuiltJoint.jointMotion](AsBuiltJoint_jointMotion.htm), [AsBuiltJointInput.jointMotion](AsBuiltJointInput_jointMotion.htm), [Joint.jointMotion](Joint_jointMotion.htm), [JointInput.jointMotion](JointInput_jointMotion.htm)

## Derived Classes

[BallJointMotion](BallJointMotion.htm), [CylindricalJointMotion](CylindricalJointMotion.htm), [PinSlotJointMotion](PinSlotJointMotion.htm), [PlanarJointMotion](PlanarJointMotion.htm), [RevoluteJointMotion](RevoluteJointMotion.htm), [RigidJointMotion](RigidJointMotion.htm), [SliderJointMotion](SliderJointMotion.htm)

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |