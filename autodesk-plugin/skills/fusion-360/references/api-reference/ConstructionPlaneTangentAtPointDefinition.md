# ConstructionPlaneTangentAtPointDefinition Object

Derived from: [ConstructionPlaneDefinition](ConstructionPlaneDefinition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneTangentAtPointDefinition.h>

## Description

ConstructionPlaneTangentAtPointDefinition defines a ConstructionPlane tangent to a face and aligned to a point.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConstructionPlaneTangentAtPointDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [redefine](ConstructionPlaneTangentAtPointDefinition_redefine.htm) | Redefines the input geometry of the construction plane. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](ConstructionPlaneTangentAtPointDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConstructionPlaneTangentAtPointDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentConstructionPlane](ConstructionPlaneTangentAtPointDefinition_parentConstructionPlane.htm) | Returns the ConstructionPlane object |
| [pointEntity](ConstructionPlaneTangentAtPointDefinition_pointEntity.htm) | Gets the point (sketch point, vertex, construction point) used to align the plane. |
| [tangentFace](ConstructionPlaneTangentAtPointDefinition_tangentFace.htm) | Gets the tangent face. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |