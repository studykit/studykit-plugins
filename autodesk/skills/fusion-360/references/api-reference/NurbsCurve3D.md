# NurbsCurve3D Object

Derived from: [Curve3D](Curve3D.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/NurbsCurve3D.h>

## Description

Transient 3D NURBS curve. A transient NURBS curve is not displayed or saved in a document. Transient 3D NURBS curves are used as a wrapper to work with raw 3D NURBS curve information. They are created statically using one of the create methods of the NurbsCurve3D class.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](NurbsCurve3D_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copy](NurbsCurve3D_copy.htm) | Creates and returns an independent copy of this NurbsCurve3D object. |
| [createNonRational](NurbsCurve3D_createNonRational.htm) | Creates a transient 3D NURBS non-rational b-spline object. |
| [createRational](NurbsCurve3D_createRational.htm) | Creates a transient 3D NURBS rational b-spline object. |
| [extract](NurbsCurve3D_extract.htm) | Defines a new NURBS curve that is the subset of this NURBS curve in the parameter range of [startParam, endParam] |
| [getData](NurbsCurve3D_getData.htm) | Gets the data that defines a transient 3D NURBS rational b-spline object. |
| [merge](NurbsCurve3D_merge.htm) | Define a new NURBS curve that is the result of combining this NURBS curve with another NURBS curve. |
| [reverse](NurbsCurve3D_reverse.htm) | Reverses the orientation of the curve so the start and end points are swapped. The shape of the curve remains unchanged. This is especially useful to prepare the curves to use with the merge method. |
| [set](NurbsCurve3D_set.htm) | Sets the data that defines a transient 3D NURBS rational b-spline object. |
| [transformBy](NurbsCurve3D_transformBy.htm) | Transforms this curve in 3D space. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [controlPointCount](NurbsCurve3D_controlPointCount.htm) | Gets the number of control points that define the curve. |
| [controlPoints](NurbsCurve3D_controlPoints.htm) | Returns an array of Point3D objects that define the control points of the curve. |
| [curveType](NurbsCurve3D_curveType.htm) | Returns the type of geometry this curve represents. |
| [degree](NurbsCurve3D_degree.htm) | Returns the degree of the curve. |
| [evaluator](NurbsCurve3D_evaluator.htm) | Returns an evaluator object that lets you perform additional evaluations on the curve. |
| [isClosed](NurbsCurve3D_isClosed.htm) | Gets if the curve is closed. |
| [isPeriodic](NurbsCurve3D_isPeriodic.htm) | Gets if the curve is periodic. |
| [isRational](NurbsCurve3D_isRational.htm) | Gets if the curve is rational or non-rational type. |
| [isValid](NurbsCurve3D_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [knotCount](NurbsCurve3D_knotCount.htm) | Returns the knot count of the curve. |
| [knots](NurbsCurve3D_knots.htm) | Returns an array of numbers that define the knot vector of the curve. |
| [objectType](NurbsCurve3D_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Arc3D.asNurbsCurve](Arc3D_asNurbsCurve.htm), [Circle3D.asNurbsCurve](Circle3D_asNurbsCurve.htm), [Ellipse3D.asNurbsCurve](Ellipse3D_asNurbsCurve.htm), [EllipticalArc3D.asNurbsCurve](EllipticalArc3D_asNurbsCurve.htm), [Line3D.asNurbsCurve](Line3D_asNurbsCurve.htm), [NurbsCurve3D.copy](NurbsCurve3D_copy.htm), [NurbsCurve3D.createNonRational](NurbsCurve3D_createNonRational.htm), [NurbsCurve3D.createRational](NurbsCurve3D_createRational.htm), [NurbsCurve3D.extract](NurbsCurve3D_extract.htm), [NurbsCurve3D.merge](NurbsCurve3D_merge.htm), [Polyline3D.asNurbsCurve](Polyline3D_asNurbsCurve.htm), [SketchConicCurve.geometry](SketchConicCurve_geometry.htm), [SketchConicCurve.worldGeometry](SketchConicCurve_worldGeometry.htm), [SketchControlPointSpline.geometry](SketchControlPointSpline_geometry.htm), [SketchControlPointSpline.worldGeometry](SketchControlPointSpline_worldGeometry.htm), [SketchFittedSpline.geometry](SketchFittedSpline_geometry.htm), [SketchFittedSpline.worldGeometry](SketchFittedSpline_worldGeometry.htm), [SketchFixedSpline.geometry](SketchFixedSpline_geometry.htm), [SketchFixedSpline.worldGeometry](SketchFixedSpline_worldGeometry.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |