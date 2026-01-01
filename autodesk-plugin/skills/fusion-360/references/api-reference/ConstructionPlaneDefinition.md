# ConstructionPlaneDefinition Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneDefinition.h>

## Description

A Base class to return the information, possibly parametric, used to define the ConstructionPlane.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConstructionPlaneDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](ConstructionPlaneDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConstructionPlaneDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentConstructionPlane](ConstructionPlaneDefinition_parentConstructionPlane.htm) | Returns the ConstructionPlane object |

## Accessed From

[ConstructionPlane.definition](ConstructionPlane_definition.htm)

## Derived Classes

[ConstructionPlaneAtAngleDefinition](ConstructionPlaneAtAngleDefinition.htm), [ConstructionPlaneByPlaneDefinition](ConstructionPlaneByPlaneDefinition.htm), [ConstructionPlaneDistanceOnPathDefinition](ConstructionPlaneDistanceOnPathDefinition.htm), [ConstructionPlaneMidplaneDefinition](ConstructionPlaneMidplaneDefinition.htm), [ConstructionPlaneOffsetDefinition](ConstructionPlaneOffsetDefinition.htm), [ConstructionPlaneOffsetThroughPointDefinition](ConstructionPlaneOffsetThroughPointDefinition.htm), [ConstructionPlaneTangentAtPointDefinition](ConstructionPlaneTangentAtPointDefinition.htm), [ConstructionPlaneTangentDefinition](ConstructionPlaneTangentDefinition.htm), [ConstructionPlaneThreePointsDefinition](ConstructionPlaneThreePointsDefinition.htm), [ConstructionPlaneTwoEdgesDefinition](ConstructionPlaneTwoEdgesDefinition.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |