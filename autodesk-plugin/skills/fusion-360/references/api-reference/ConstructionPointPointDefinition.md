# ConstructionPointPointDefinition Object

Derived from: [ConstructionPointDefinition](ConstructionPointDefinition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPointPointDefinition.h>

## Description

The definition for a parametric construction point created using the SetbyPoint method All non-parametric constructions points will return this type of definition regardless of the method used to initially create them.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConstructionPointPointDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](ConstructionPointPointDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConstructionPointPointDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentConstructionPoint](ConstructionPointPointDefinition_parentConstructionPoint.htm) | Returns the ConstructionPoint object |
| [pointEntity](ConstructionPointPointDefinition_pointEntity.htm) | Gets and sets the position of the point using a construction point, sketch point or vertex. Non-parametric points will always return a Point3D object |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |