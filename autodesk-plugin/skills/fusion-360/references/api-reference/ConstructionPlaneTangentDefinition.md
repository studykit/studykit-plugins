# ConstructionPlaneTangentDefinition Object

Derived from: [ConstructionPlaneDefinition](ConstructionPlaneDefinition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneTangentDefinition.h>

## Description

ConstructionPlaneTangentDefinition defines a ConstructionPlane tangent to a cylindrical or conical face at a point.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConstructionPlaneTangentDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [redefine](ConstructionPlaneTangentDefinition_redefine.htm) | Redefines the input geometry of the construction plane. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [angle](ConstructionPlaneTangentDefinition_angle.htm) | Returns a Value object that for a transient definition provides the current assigned value. For a definition associated with a construction plane, it provides access to the associated parameter controlling the angle. |
| [isValid](ConstructionPlaneTangentDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConstructionPlaneTangentDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentConstructionPlane](ConstructionPlaneTangentDefinition_parentConstructionPlane.htm) | Returns the ConstructionPlane object |
| [planarEntity](ConstructionPlaneTangentDefinition_planarEntity.htm) | Gets the planar face or construction plane the angle for this construction plane is measured from and is parametrically dependent on. |
| [tangentFace](ConstructionPlaneTangentDefinition_tangentFace.htm) | Gets the cylindrical or conical face that the construction plane is tangent to. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |