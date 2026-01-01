# NurbsCurve2D Object

Derived from: [Curve2D](Curve2D.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/NurbsCurve2D.h>

## Description

Transient 2D NURBS curve. A transient NURBS curve is not displayed or saved in a document. Transient 2D NURBS curves are used as a wrapper to work with raw 2D NURBS curve information. They are created statically using one of the create methods of the NurbsCurve2D class.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](NurbsCurve2D_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copy](NurbsCurve2D_copy.htm) | Creates and returns an independent copy of this NurbsCurve2D object. |
| [createNonRational](NurbsCurve2D_createNonRational.htm) | Creates a transient 2D NURBS non-rational b-spline object. |
| [createRational](NurbsCurve2D_createRational.htm) | Creates a transient 2D NURBS rational b-spline object. |
| [extract](NurbsCurve2D_extract.htm) | Defines a new NURBS curve that is the subset of this NURBS curve in the parameter range of [startParam, endParam] |
| [getData](NurbsCurve2D_getData.htm) | Gets the data that defines a transient 2D NURBS rational b-spline object. |
| [merge](NurbsCurve2D_merge.htm) | Define a new NURBS curve that is the result of combining this NURBS curve with another NURBS curve. The curves are merged with the end point of the current curve merging with the start point of the other curve. The curves are forced to join even if they are not physically touching so you will typically want to make sure the end and start points of the curves are where you expect them to be. |
| [reverse](NurbsCurve2D_reverse.htm) | Reverses the orientation of the curve so the start and end points are swapped. The shape of the curve remains unchanged. This is especially useful to prepare the curves to use with the merge method. |
| [set](NurbsCurve2D_set.htm) | Sets the data that defines a transient 2D NURBS rational b-spline object. |
| [transformBy](NurbsCurve2D_transformBy.htm) | Transforms this curve in 2D space. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [controlPointCount](NurbsCurve2D_controlPointCount.htm) | Gets the number of control points that define the curve |
| [controlPoints](NurbsCurve2D_controlPoints.htm) | Returns an array of Point2D objects that define the control points of the curve. |
| [curveType](NurbsCurve2D_curveType.htm) | Returns the type of geometry this curve represents. |
| [degree](NurbsCurve2D_degree.htm) | Returns the degree of the curve |
| [evaluator](NurbsCurve2D_evaluator.htm) | Returns an evaluator object that lets you perform additional evaluations on the curve. |
| [isClosed](NurbsCurve2D_isClosed.htm) | Returns if the curve is closed |
| [isPeriodic](NurbsCurve2D_isPeriodic.htm) | Returns if the curve is periodic. |
| [isRational](NurbsCurve2D_isRational.htm) | Returns if the curve is rational or non-rational type |
| [isValid](NurbsCurve2D_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [knotCount](NurbsCurve2D_knotCount.htm) | Returns the knot count of the curve |
| [knots](NurbsCurve2D_knots.htm) | Returns an array of numbers that define the Knots of the curve. |
| [objectType](NurbsCurve2D_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Arc2D.asNurbsCurve](Arc2D_asNurbsCurve.htm), [Circle2D.asNurbsCurve](Circle2D_asNurbsCurve.htm), [Ellipse2D.asNurbsCurve](Ellipse2D_asNurbsCurve.htm), [EllipticalArc2D.asNurbsCurve](EllipticalArc2D_asNurbsCurve.htm), [Line2D.asNurbsCurve](Line2D_asNurbsCurve.htm), [NurbsCurve2D.copy](NurbsCurve2D_copy.htm), [NurbsCurve2D.createNonRational](NurbsCurve2D_createNonRational.htm), [NurbsCurve2D.createRational](NurbsCurve2D_createRational.htm), [NurbsCurve2D.extract](NurbsCurve2D_extract.htm), [NurbsCurve2D.merge](NurbsCurve2D_merge.htm), [Polyline2D.asNurbsCurve](Polyline2D_asNurbsCurve.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |