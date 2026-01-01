# ConstructionPlaneTwoEdgesDefinition Object

Derived from: [ConstructionPlaneDefinition](ConstructionPlaneDefinition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneTwoEdgesDefinition.h>

## Description

ConstructionPlaneTwoEdgesDefinition defines a ConstructionPlane by two co-planar linear entities like edges, sketch lines or construction axis.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConstructionPlaneTwoEdgesDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [redefine](ConstructionPlaneTwoEdgesDefinition_redefine.htm) | Redefines the input geometry of the construction plane. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](ConstructionPlaneTwoEdgesDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [linearEntityOne](ConstructionPlaneTwoEdgesDefinition_linearEntityOne.htm) | Gets the first linear edge, construction line, or sketch line that defines the construction plane. |
| [linearEntityTwo](ConstructionPlaneTwoEdgesDefinition_linearEntityTwo.htm) | Gets the second linear edge, construction line, or sketch line that defines the construction plane. |
| [objectType](ConstructionPlaneTwoEdgesDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentConstructionPlane](ConstructionPlaneTwoEdgesDefinition_parentConstructionPlane.htm) | Returns the ConstructionPlane object |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |