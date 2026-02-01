# AsBuiltJointInput Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AsBuiltJointInput.h>

## Description

Defines all of the information needed to create an as-built joint.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](AsBuiltJointInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [setAsBallJointMotion](AsBuiltJointInput_setAsBallJointMotion.htm) | Defines the relationship between the two joint geometries as a ball joint. |
| [setAsCylindricalJointMotion](AsBuiltJointInput_setAsCylindricalJointMotion.htm) | Defines the relationship between the two joint geometries as a cylindrical joint. |
| [setAsPinSlotJointMotion](AsBuiltJointInput_setAsPinSlotJointMotion.htm) | Defines the relationship between the two joint geometries as a pin-slot joint. |
| [setAsPlanarJointMotion](AsBuiltJointInput_setAsPlanarJointMotion.htm) | Defines the relationship between the two joint geometries as a planar joint. |
| [setAsRevoluteJointMotion](AsBuiltJointInput_setAsRevoluteJointMotion.htm) | Defines the relationship between the two joint geometries as a revolute joint. |
| [setAsRigidJointMotion](AsBuiltJointInput_setAsRigidJointMotion.htm) | Defines the relationship between the two joint geometries as a rigid joint. |
| [setAsSliderJointMotion](AsBuiltJointInput_setAsSliderJointMotion.htm) | Defines the relationship between the two joint geometries as a slider joint. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [geometry](AsBuiltJointInput_geometry.htm) | Specifies the position of the joint. |
| [isValid](AsBuiltJointInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [jointMotion](AsBuiltJointInput_jointMotion.htm) | Returns one of the objects derived from JointMotion that defines how the motion between the two joint geometries is defined. Can be null if the motion hasn't yet been defined. |
| [objectType](AsBuiltJointInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [occurrenceOne](AsBuiltJointInput_occurrenceOne.htm) | Specifies the first of two occurrences the joint is between. |
| [occurrenceTwo](AsBuiltJointInput_occurrenceTwo.htm) | Specifies the second of two occurrences the joint is between. |

## Accessed From

[AsBuiltJoints.createInput](AsBuiltJoints_createInput.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [As-Built Joint Sample](AsBuiltJointSample_Sample.htm) | Demonstrates creating a new As-Built Joint. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |