# ConstructionPlaneAtAngleDefinition Object

Derived from: [ConstructionPlaneDefinition](ConstructionPlaneDefinition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneAtAngleDefinition.h>

## Description

ConstructionPlaneAtAngleDefinition defines a ConstructionPlane by an angle around a linear entity.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConstructionPlaneAtAngleDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [redefine](ConstructionPlaneAtAngleDefinition_redefine.htm) | Redefines the input geometry of the construction plane. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [angle](ConstructionPlaneAtAngleDefinition_angle.htm) | Returns a Parameter object that controls the value of the angle. You can use properties of the returned Parameter object to modify the angle. |
| [isValid](ConstructionPlaneAtAngleDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [linearEntity](ConstructionPlaneAtAngleDefinition_linearEntity.htm) | Gets the linear edge, construction line, or sketch line that defines the axis of rotation for the construction plane. |
| [objectType](ConstructionPlaneAtAngleDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentConstructionPlane](ConstructionPlaneAtAngleDefinition_parentConstructionPlane.htm) | Returns the ConstructionPlane object |
| [planarEntity](ConstructionPlaneAtAngleDefinition_planarEntity.htm) | Gets the planar face or construction plane the angle for this construction plane is measured from and is parametrically dependent on.   This property is only valid for construction planes that were created using the API. When an angle construction plane is created using the user interface the plane is not defined by the user and a plane is automatically inferred by Fusion. In this case, this property will return null. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |