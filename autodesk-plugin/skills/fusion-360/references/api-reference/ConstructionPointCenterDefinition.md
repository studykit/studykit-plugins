# ConstructionPointCenterDefinition Object

Derived from: [ConstructionPointDefinition](ConstructionPointDefinition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPointCenterDefinition.h>

## Description

The definition for a parametric construction point created using the SetbyCenter method

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConstructionPointCenterDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [circularEntity](ConstructionPointCenterDefinition_circularEntity.htm) | Gets and sets the spherical face (sphere or torus), circular edge or sketch arc/circle whose center defines the location for the construction point. |
| [isValid](ConstructionPointCenterDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConstructionPointCenterDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentConstructionPoint](ConstructionPointCenterDefinition_parentConstructionPoint.htm) | Returns the ConstructionPoint object |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |