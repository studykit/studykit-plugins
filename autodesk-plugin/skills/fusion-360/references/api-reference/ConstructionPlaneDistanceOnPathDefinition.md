# ConstructionPlaneDistanceOnPathDefinition Object

Derived from: [ConstructionPlaneDefinition](ConstructionPlaneDefinition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneDistanceOnPathDefinition.h>

## Description

ConstructionDistanceOnPathDefinition defines a ConstructionPlane normal to an edge or sketch profile at a specified position along the path defined by the edge or sketch profile.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConstructionPlaneDistanceOnPathDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [redefine](ConstructionPlaneDistanceOnPathDefinition_redefine.htm) | Redefines the input defining the construction plane. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [distance](ConstructionPlaneDistanceOnPathDefinition_distance.htm) | Gets the distance along the path. |
| [isValid](ConstructionPlaneDistanceOnPathDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConstructionPlaneDistanceOnPathDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentConstructionPlane](ConstructionPlaneDistanceOnPathDefinition_parentConstructionPlane.htm) | Returns the ConstructionPlane object |
| [pathEntity](ConstructionPlaneDistanceOnPathDefinition_pathEntity.htm) | Gets the sketch curve, edge, or a profile object. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |