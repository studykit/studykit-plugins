# ConstructionPointEdgePlaneDefinition Object

Derived from: [ConstructionPointDefinition](ConstructionPointDefinition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPointEdgePlaneDefinition.h>

## Description

The definition for a parametric construction point created using the SetbyEdgePlane method

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConstructionPointEdgePlaneDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [redefine](ConstructionPointEdgePlaneDefinition_redefine.htm) | Redefines the input geometry of the construction point. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [edge](ConstructionPointEdgePlaneDefinition_edge.htm) | A linear B-Rep edge, construction axis or sketch line. |
| [isValid](ConstructionPointEdgePlaneDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConstructionPointEdgePlaneDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentConstructionPoint](ConstructionPointEdgePlaneDefinition_parentConstructionPoint.htm) | Returns the ConstructionPoint object |
| [plane](ConstructionPointEdgePlaneDefinition_plane.htm) | A plane, planar B-Rep face or construction plane. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |