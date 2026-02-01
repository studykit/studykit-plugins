# ConstructionAxisPerpendicularAtPointDefinition Object

Derived from: [ConstructionAxisDefinition](ConstructionAxisDefinition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxisPerpendicularAtPointDefinition.h>

## Description

The definition for a parametric construction axis created using the SetByPerpendicularAtPoint method

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConstructionAxisPerpendicularAtPointDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [redefine](ConstructionAxisPerpendicularAtPointDefinition_redefine.htm) | Redefines the input geometry of the construction axis. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [face](ConstructionAxisPerpendicularAtPointDefinition_face.htm) | Returns the face the construction axis is perpendicular to. |
| [isValid](ConstructionAxisPerpendicularAtPointDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConstructionAxisPerpendicularAtPointDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentConstructionAxis](ConstructionAxisPerpendicularAtPointDefinition_parentConstructionAxis.htm) | Returns the ConstructionAxis object |
| [point](ConstructionAxisPerpendicularAtPointDefinition_point.htm) | Returns the point (construction or sketch point) that positions the axis. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |