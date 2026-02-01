# PathEntity Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathEntity.h>

## Description

The PathEntity object represents a curve within a path

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](PathEntity_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](PathEntity_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](PathEntity_assemblyContext.htm) | This property is not supported for a PathEntity object. |
| [curve](PathEntity_curve.htm) | Property that returns the geometry of the entity. This is different from the original path curve if the true start point is not the same as the start point of the original path curve. |
| [curveType](PathEntity_curveType.htm) | Property that returns the type of the curve referenced by the path entity. This property allows you to determine what type of object will be returned by the Curve property. |
| [entity](PathEntity_entity.htm) | Property that gets the sketch curve or edge this entity was derived from. |
| [isOpposedToEntity](PathEntity_isOpposedToEntity.htm) | Indicates if the orientation of this PathEntity is in the same direction or opposed to the natural direction of the SketchCurve or BRepEdge object it is derived from. |
| [isValid](PathEntity_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [nativeObject](PathEntity_nativeObject.htm) | This property is not supported for a PathEntity object. |
| [objectType](PathEntity_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentPath](PathEntity_parentPath.htm) | Property that returns the parent Path of the entity. |

## Accessed From

[Path.item](Path_item.htm), [PathEntity.createForAssemblyContext](PathEntity_createForAssemblyContext.htm), [PathEntity.nativeObject](PathEntity_nativeObject.htm)

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |