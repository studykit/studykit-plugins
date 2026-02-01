# RigidJointMotion Object

Derived from: [JointMotion](JointMotion.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/RigidJointMotion.h>

## Description

Represents the set of information specific to a rigid joint. A rigid joint doesn't support any additional information beyond getting the joint type which it derives from JointMotion.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](RigidJointMotion_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](RigidJointMotion_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [jointType](RigidJointMotion_jointType.htm) | Returns an enum value indicating the type of joint this joint represents. |
| [objectType](RigidJointMotion_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |