# Polyline2D Object

Derived from: [Curve2D](Curve2D.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/Polyline2D.h>

## Description

Represents a single curve composed of a series of connected lines in 2D space.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Polyline2D_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [create](Polyline2D_create.htm) | Creates a transient 2D polyline using an array of Point2D objects that defines the position of the polyline vertices. |
| [createByArray](Polyline2D_createByArray.htm) | Creates a transient 2D polyline using an array of floating point values that specify the X, Y coordinates for each point. |
| [transformBy](Polyline2D_transformBy.htm) | Transforms this curve in 2D space. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [asNurbsCurve](Polyline2D_asNurbsCurve.htm) | Returns a NURBS curve that is geometrically identical to the polyline. |
| [curveType](Polyline2D_curveType.htm) | Returns the type of geometry this curve represents. |
| [evaluator](Polyline2D_evaluator.htm) | Returns an evaluator object that lets you perform additional evaluations on the curve. |
| [isValid](Polyline2D_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Polyline2D_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [pointCount](Polyline2D_pointCount.htm) | Returns the number of points defining the polyline. |
| [points](Polyline2D_points.htm) | Gets and sets the points that define the coordinates of the polyline. |

## Accessed From

[Polyline2D.create](Polyline2D_create.htm), [Polyline2D.createByArray](Polyline2D_createByArray.htm)

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |