# Polyline3D Object

Derived from: [Curve3D](Curve3D.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/Polyline3D.h>

## Description

Represents a single piecewise linear curve. This is a single curve that consists of a series of connected lines in 3D space.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Polyline3D_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [create](Polyline3D_create.htm) | Creates a transient 3D polyline using an array of Point3D objects that defines the position of the polyline vertices. |
| [createByArray](Polyline3D_createByArray.htm) | Creates a transient 3D polyline using an array of floating point values that specify the X, Y, Z coordinates for each point. |
| [transformBy](Polyline3D_transformBy.htm) | Transforms this curve in 3D space. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [asNurbsCurve](Polyline3D_asNurbsCurve.htm) | Returns a NURBS curve that is geometrically identical to the polyline. |
| [curveType](Polyline3D_curveType.htm) | Returns the type of geometry this curve represents. |
| [evaluator](Polyline3D_evaluator.htm) | Returns an evaluator object that lets you perform additional evaluations on the curve. |
| [isValid](Polyline3D_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Polyline3D_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [pointCount](Polyline3D_pointCount.htm) | Returns the number of points defining the polyline. |
| [points](Polyline3D_points.htm) | Gets and sets the points that define the coordinates of the polyline. |

## Accessed From

[Polyline3D.create](Polyline3D_create.htm), [Polyline3D.createByArray](Polyline3D_createByArray.htm)

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |