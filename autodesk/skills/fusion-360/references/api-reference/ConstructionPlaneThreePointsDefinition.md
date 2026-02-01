# ConstructionPlaneThreePointsDefinition Object

Derived from: [ConstructionPlaneDefinition](ConstructionPlaneDefinition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneThreePointsDefinition.h>

## Description

ConstructionPlaneThreePointDefinition defines a ConstructionPlane by 3 point entities (e.g. (sketch points, vertices or construction points) that form a triangle (i.e. no two points the same and they aren't collinear).

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConstructionPlaneThreePointsDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [redefine](ConstructionPlaneThreePointsDefinition_redefine.htm) | Redefines the input geometry of the construction plane. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](ConstructionPlaneThreePointsDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConstructionPlaneThreePointsDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentConstructionPlane](ConstructionPlaneThreePointsDefinition_parentConstructionPlane.htm) | Returns the ConstructionPlane object |
| [pointEntityOne](ConstructionPlaneThreePointsDefinition_pointEntityOne.htm) | Gets the first construction point, sketch point or vertex. |
| [pointEntityThree](ConstructionPlaneThreePointsDefinition_pointEntityThree.htm) | Gets the third construction point, sketch point or vertex. |
| [pointEntityTwo](ConstructionPlaneThreePointsDefinition_pointEntityTwo.htm) | Gets the second construction point, sketch point or vertex. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |